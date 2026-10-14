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


def test_ap_reboot(device_ip, reboot_count):
    _cli_session = None
    try:
        _cli_session = SSH_session(hostname=device_ip, username="admin", password="admin")
        _cli_session.init_shell()
        for i in range(1, reboot_count + 1):
            log.info(log.info(f" ******************** Reboot count: {i} ******************** "))
            assert _cli_reload_device(_cli_session), f"Failed to reboot device, reboot count: {i}"

            log.info(f"Sleep for 60 seconds for all process to restart and radios to come UP")
            time.sleep(60)

            log.info(f"{'#'* 80}")
            output = _cli_session.send_cmd("show version")
            log.info(output)
            time.sleep(3)

            log.info(f"{'#' * 80}")
            output = _cli_session.send_cmd("show wireless radios")
            log.info(output)
            time.sleep(3)
    except Exception as e:
        log.critical(f"An exception of type {type(e).__name__} occurred")
        log.critical(traceback.format_exc())
        raise
    finally:
        if _cli_session:
            _cli_session.log_out()


if __name__ == '__main__':
    test_ap_reboot("192.168.0.10", 100)

