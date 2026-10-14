import time
import logging
import traceback
from SSH_session import SSH_session

log = logging.getLogger()
logging.basicConfig(filename='million_reboots_with_config-check.log', level="INFO")


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
            log.error("********* Device not reachable after reboot ***********")
            return False
        # the old channel is now destroyed at reboot, so clean the object
        _cli_session.log_out()
        return True
    except Exception as e:
        log.warning("Unable to reload device")
        log.error(str(e))
        raise


def test_reboot_with_config(device_ip, reboot_count, clients_mac):
    _cli_session = None
    try:
        _cli_session = SSH_session(hostname=device_ip, username="admin", password="admin")
        _cli_session.init_shell()
        for i in range(1, reboot_count + 1):
            log.info(log.info(f" *************************** Reboot count: {i} *************************** "))
            assert _cli_reload_device(_cli_session), f"Failed to reboot device, reboot count: {i}"

            # All process to restart and radios to come UP and mesh clients to reconnect
            log.info(f"Sleep for 300 seconds for all process to restart and radios to come UP and mesh clients to reconnect")
            time.sleep(300)

            log.info(f"{'#'* 80}")
            output = _cli_session.send_cmd("show version")
            log.info(output)
            time.sleep(2)

            macAddr = "Device MAC address is "
            for line in output.split("\n"):
                if macAddr in line:
                    mac = line[len(macAddr):]
                    log.info(f"AP MAC address in show version output: {mac}")

            log.info(f"{'#' * 80}")
            device_output = _cli_session.send_cmd("show interface brief")
            log.info(device_output)
            time.sleep(2)

            lines = device_output.strip().splitlines()
            headers = lines[0].split()
            data_list = []
            for line in lines[1:]:
                values = line.split(maxsplit=len(headers) - 1)
                row_dict = {}
                for i, header in enumerate(headers):
                    row_dict[header] = values[i].strip() if i < len(values) else ""
                # Check if any value in row_dict is non-empty
                if any(value != '' for value in row_dict.values()):
                    data_list.append(row_dict)
            # print(data_list)
            for d in data_list:
                if d["STATUS"] == "UP" and d["MAC"] == mac:
                    log.info("PASS: Show interface brief eth MAC and show version MAC address is matching")
                    break
            else:
                log.error(f"FAIL: Show interface brief eth MAC and show version MAC address is matching, reboot count: {i}")

            log.info(f"{'#' * 80}")
            output = _cli_session.send_cmd("show power")
            log.info(output)
            time.sleep(2)

            log.info(f"{'#' * 80}")
            output = _cli_session.send_cmd("show lldp neighbors")
            log.info(output)
            time.sleep(2)

            log.info(f"{'#' * 80}")
            output = _cli_session.send_cmd("show interface details")
            log.info(output)
            time.sleep(2)

            log.info(f"{'#' * 80}")
            output = _cli_session.send_cmd("show wireless wlan")
            log.info(output)
            time.sleep(2)

            log.info(f"{'#' * 80}")
            output = _cli_session.send_cmd("show wireless wlan interface")
            log.info(output)
            time.sleep(2)

            log.info(f"{'#' * 80}")
            output = _cli_session.send_cmd("service show ifconfig")
            log.info(output)
            time.sleep(2)

            log.info(f"{'#' * 80}")
            output = _cli_session.send_cmd("service show ethtool")
            log.info(output)
            time.sleep(2)

            log.info(f"{'#' * 80}")
            output = _cli_session.send_cmd("service show bridge")
            log.info(output)
            time.sleep(2)

            log.info(f"{'#' * 80}")
            output = _cli_session.send_cmd("show wireless radios")
            log.info(output)
            time.sleep(2)

            log.info(f"{'#' * 80}")
            output = _cli_session.send_cmd("show wireless mesh")
            log.info(output)
            time.sleep(2)

            for cli_mac in clients_mac:
                if cli_mac in output:
                    log.info(f"PASS: Found client mac: {cli_mac} in output")
                else:
                    log.error(f"FAIL: Did not found client mac: {cli_mac} in output, reboot count: {i}")

    except Exception as e:
        log.critical(f"An exception of type {type(e).__name__} occurred")
        log.critical(traceback.format_exc())
        raise
    finally:
        if _cli_session:
            _cli_session.log_out()


if __name__ == '__main__':
    device_ip = "192.168.0.10"
    reboot_count = 2
    clients_mac = ["30-CB-C7-54-12-50", "BC-E6-7C-4A-20-B0"]
    test_reboot_with_config(device_ip, reboot_count, clients_mac)

