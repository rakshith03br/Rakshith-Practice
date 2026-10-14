import time
import difflib
import inspect
import logging
import traceback
from SSH_session import SSH_session

log = logging.getLogger()
logging.basicConfig(level=logging.INFO, format='%(asctime)s %(lineno)d %(levelname)s: %(message)s', datefmt='%d-%m-%Y %H:%M:%S')

deviceProperties = {}


def _cli_get_device_information(_cli_session):
    try:
        global deviceProperties
        swversion = "Software version "
        regulatoryDomain = "Regulatory domain "
        buildDate = "Build date "
        deviceAgentVersion = "Device-Agent version "
        serialNumber = "Serial number "
        uptime = "System is up "
        macAddr = "Device MAC address is "
        output = _cli_session.send_cmd("show version").split("\n\r")
        for line in output:
            if swversion in line:
                deviceProperties[swversion] = line[len(swversion):]
            if regulatoryDomain in line:
                deviceProperties[regulatoryDomain] = line[len(regulatoryDomain):]
            if buildDate in line:
                deviceProperties[buildDate] = line[len(buildDate):]
            if deviceAgentVersion in line:
                deviceProperties[deviceAgentVersion] = line[len(deviceAgentVersion):]
            if serialNumber in line:
                deviceProperties[serialNumber] = line[len(serialNumber):]
            if uptime in line:
                deviceProperties[uptime] = line[len(uptime):]
            if macAddr in line:
                deviceProperties[macAddr] = line[len(macAddr):]
        log.info(deviceProperties)
    except Exception as e:
        log.critical(f"An exception of type {type(e).__name__} occurred")
        log.critical(traceback.format_exc())
        raise


def _cli_get_firmware_version(_cli_session):
    try:
        swversion = "Software version "
        _cli_get_device_information(_cli_session)
        return deviceProperties[swversion]
    except Exception as e:
        log.critical(f"An exception of type {type(e).__name__} occurred")
        log.critical(traceback.format_exc())
        raise


def _cli_upgrade_device(_cli_session, ftppath):
    try:
        log.debug(inspect.currentframe().f_code.co_name)
        cmd = "upgrade tftp://" + ftppath
        log.info("Execute command: %s" % cmd)
        res = _cli_session.send_cmd(cmd)
        log.info(res.rstrip())
        time.sleep(1)
        res = _cli_session.send_cmd("show upgrade-status")
        log.info(res.rstrip())
        while "Firmware file ready, now updating device" in res or "Downloading firmware file" in res:
            time.sleep(10)
            res = _cli_session.send_cmd("show upgrade-status")
            log.info(res.rstrip())
        if 'Upgrade status not available' in res:
            log.warning("Session disconnected and doesn't retain upgrade status")
            return False
        if 'Upgraded successfully' in res:
            return True
        return False
    except Exception as e:
        log.critical(f"An exception of type {type(e).__name__} occurred")
        log.critical(traceback.format_exc())
        raise


def _cli_reload_device(_cli_session, rebootTime=300):
    try:
        cmd = "reload"
        stdin, stdout, stderr = _cli_session.ssh.exec_command(cmd)
        stdin.write('y')
        stdin.write('\n')
        stdin.flush()
        time.sleep(30)
        count = 1
        start = time.time()
        device_accessible = False
        while time.time() - start < rebootTime:
            log.info("*" * count)
            if _cli_session.is_host_active():
                device_accessible = True
                break
            time.sleep(10)
            count += 1
        if not device_accessible:
            log.info("********* Device not reachable ***********")
            return False
        # the old channel is now destroyed at reboot, so clean the object
        _cli_session.log_out()
        return True
    except Exception as e:
        log.warning("Unable to reload device")
        log.error(str(e))
        raise


def test_upgrade_downgrade(device_ip, tftp_server, iterations):
    cli_session = None
    try:
        cli_session = SSH_session(hostname=device_ip, password="admin", username="admin", os="e400")
        for i in range(iterations):

            log.info(f"{'=' * 80}")
            log.info("Iteration - %s" % i)
            log.info(f"{'=' * 80}")

            cmd = "show wireless wlan"
            out = cli_session.send_cmd(cmd)
            log.info(out)
            log.info(f"{'*' * 80}")

            show_ver = "show version"
            out = cli_session.send_cmd(show_ver)
            log.info(out)
            log.info(f"{'=' * 80}")

            show_power = "show power"
            out = cli_session.send_cmd(show_power)
            log.info(out)
            log.info(f"{'=' * 80}")

            show_lldp = "show lldp neighbors"
            out = cli_session.send_cmd(show_lldp)
            log.info(out)
            log.info(f"{'=' * 80}")

            show_ipif = "show ip interface brief"
            out = cli_session.send_cmd(show_ipif)
            log.info(out)
            log.info(f"{'=' * 80}")

            show_ifdt = "show interface details"
            out = cli_session.send_cmd(show_ifdt)
            log.info(out)
            log.info(f"{'=' * 80}")

            show_ser_sh_ifcon = "service show ifconfig"
            out = cli_session.send_cmd(show_ser_sh_ifcon)
            log.info(out)
            log.info(f"{'=' * 80}")

            show_ser_sh_eth = "service show ethtool"
            out = cli_session.send_cmd(show_ser_sh_eth)
            log.info(out)
            log.info(f"{'=' * 80}")

            config_before_reboot = cli_session.send_cmd("show wireless wlans")
            log.info("show wireless wlans output before upgrade/downgrade reboot")
            log.info(config_before_reboot)

            current_build = _cli_get_firmware_version(cli_session)
            log.info(f"{'=' * 20} Current Build: {current_build} {'=' * 20}")

            if current_build in image_a:
                upgrade_build = image_b
            else:
                upgrade_build = image_a

            log.info(f"Updating from {current_build} to {upgrade_build}")
            ftppath = "/".join([tftp_server, upgrade_build])

            log.info(f"Upgrading to {upgrade_build} from {current_build}")
            assert _cli_upgrade_device(cli_session, ftppath), f"Upgrading to {upgrade_build} failed, Iteration: {i}"

            log.info("Rebooting AP after upgrade")
            assert _cli_reload_device(cli_session), f"Failed to reload device after upgrade, Iteration: {i}"

            build_after_boot = _cli_get_firmware_version(cli_session)
            log.info(f"{'=' * 15} Build after upgrade: {build_after_boot} {'=' * 15}")
            log.info(f"Expected Build: {current_build}")

            assert build_after_boot != current_build, f"Upgrade to {upgrade_build} is not successful, Iteration: {i}"
            log.info(f"Upgrade to {upgrade_build} is successful")

            config_after_reboot = cli_session.send_cmd("show wireless wlans")
            log.info("show wireless wlans output after upgrade/downgrade reboot")
            log.info(config_after_reboot)

            # Compare difference before and after upgrade/downgrade reboot
            diff = difflib.ndiff(config_before_reboot.split(), config_after_reboot.split())
            diff_removed, diff_added = [], []
            for item in diff:
                if item.startswith('-'):
                    diff_removed.append(item[2:])
                elif item.startswith('+'):
                    diff_added.append(item[2:])
            log.info(diff_added)
            log.info(diff_removed)

            if diff_added:
                assert False, f"There is difference added in config after upgrade/downgrade, {diff_added}"
            if diff_removed:
                assert False, f"There is difference removed in config after upgrade/downgrade, {diff_removed}"

            log.info(f"{'~' * 30} PASS {'~' * 30}")

    except Exception as e:
        log.critical(f"An exception of type {type(e).__name__} occurred")
        log.critical(traceback.format_exc())
        raise
    finally:
        cli_session.log_out()


if __name__ == '__main__':
    server_hostname = "10.110.153.207"
    server_username = "sitindia"
    server_password = "sitindia123"
    server_os = "linux"
    # directory path where generate-passwd.py script is present
    rootdir = "/home/sitindia/"

    # make sure these builds are in tftp directory
    image_a = "xv222h_xv221x_xv223t_xv220h-7.0.0.1-r8.cimg"
    image_b = "xv222h_xv221x_xv223t_xv220h-7.0.0.1-r9.cimg"

    # device ip address
    device_ip = "10.110.153.12"

    # tftp server ip address
    tftp_server = "10.110.153.207"
    iterations = 1

    test_upgrade_downgrade(device_ip=device_ip, tftp_server=tftp_server, iterations=iterations)
