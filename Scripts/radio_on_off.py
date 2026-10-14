import os
import sys
import time
import logging
import traceback
from SSH_session import SSH_session

filename = 'Radio_on_off.txt'
if not os.path.exists(filename):
    with open(filename, "w") as file:
        file.write("Radio ON OFF test\n")

log = logging.getLogger()
logging.basicConfig(filename=filename, level="INFO", force=True)

expected_prompt = "config-radio"
TIME_BW_RETRIES = 0.1


def enable_radio(shell, radio):
    try:
        shell.send_shell(cmd=f"wireless radio {radio}", expectedPrompt=expected_prompt)
        time.sleep(1)
        shell.send_shell(cmd="no shutdown", expectedPrompt=expected_prompt)
        time.sleep(1)
        shell.send_shell(cmd="save", expectedPrompt=expected_prompt)
        time.sleep(1)
        shell.send_shell(cmd="exit", expectedPrompt="(config)#")
    except Exception:
        msg = traceback.format_exc()
        log.error("Exception occurred")
        log.error(msg)
        raise


def disable_radio(shell, radio):
    try:
        shell.send_shell(cmd=f"wireless radio {radio}", expectedPrompt=expected_prompt)
        time.sleep(1)
        shell.send_shell(cmd="shutdown", expectedPrompt=expected_prompt)
        time.sleep(1)
        shell.send_shell(cmd="save", expectedPrompt=expected_prompt)
        time.sleep(1)
        shell.send_shell(cmd="exit", expectedPrompt="(config)#")
    except Exception:
        msg = traceback.format_exc()
        log.error("Exception occurred")
        log.error(msg)
        raise


def test_radio_on_off_radios_2(hostname, radio_list, iterations):
    ap_ssh = None
    try:
        ap_ssh = SSH_session(hostname=hostname, username="admin", password="admin")
        ap_ssh.init_shell()
        radio_1 = radio_list[0]
        radio_2 = radio_list[1]
        out = ap_ssh.send_cmd(cmd="show version")
        log.info(out)
        out = ap_ssh.send_cmd(cmd="show wireless radios")
        log.info(out)
        out = ap_ssh.send_cmd(cmd="show wireless wlans interface")
        log.info(out)
        out = ap_ssh.send_cmd(cmd="show wireless clients")
        log.info(out)
        for iteration in range(1, iterations + 1):
            log.info(f" *************************** Iteration: {iteration} *************************** ")
            # radio 1 on
            enable_radio(ap_ssh, radio_1)
            # radio 2 off
            disable_radio(ap_ssh, radio_2)
            log.info("Sleep 150 seconds for radios to come UP and clients to reconnect")
            time.sleep(150)
            out = ap_ssh.send_cmd(cmd="show wireless radios")
            log.info(out)
            out = ap_ssh.send_cmd(cmd="show wireless wlans interface")
            log.info(out)
            out = ap_ssh.send_cmd(cmd="show wireless clients")
            log.info(out)
            if not out:
                log.error("FAIL: No clients data found")

            # radio 1 off
            disable_radio(ap_ssh, radio_1)
            # radio 2 on
            enable_radio(ap_ssh, radio_2)
            log.info("Sleep 150 seconds for radios to come UP and clients to reconnect")
            time.sleep(150)
            out = ap_ssh.send_cmd(cmd="show wireless radios")
            log.info(out)
            out = ap_ssh.send_cmd(cmd="show wireless wlans interface")
            log.info(out)
            out = ap_ssh.send_cmd(cmd="show wireless clients")
            log.info(out)
            if not out:
                log.error("FAIL: No clients data found")
        else:
            # Turn on all radios
            for radio in radio_list:
                enable_radio(ap_ssh, radio)
    except Exception:
        msg = traceback.format_exc()
        log.error("Exception occurred")
        log.error(msg)
        raise
    finally:
        if ap_ssh:
            ap_ssh.close()


def test_radio_on_off_radios_3(hostname, radio_list, iterations):
    ap_ssh = None
    try:
        ap_ssh = SSH_session(hostname=hostname, username="admin", password="admin")
        ap_ssh.init_shell()
        radio_1 = radio_list[0]
        radio_2 = radio_list[1]
        radio_3 = radio_list[2]
        out = ap_ssh.send_cmd(cmd="show version")
        log.info(out)
        out = ap_ssh.send_cmd(cmd="show wireless radios")
        log.info(out)
        out = ap_ssh.send_cmd(cmd="show wireless wlans interface")
        log.info(out)
        out = ap_ssh.send_cmd(cmd="show wireless clients")
        log.info(out)
        for iteration in range(1, iterations + 1):
            log.info(f" *************************** Iteration: {iteration} *************************** ")
            # radio 1 on
            enable_radio(ap_ssh, radio_1)
            # radio 2 off
            disable_radio(ap_ssh, radio_2)
            # radio 3 off
            disable_radio(ap_ssh, radio_3)
            log.info("Sleep 150 seconds for radios to come UP and clients to reconnect")
            time.sleep(150)
            out = ap_ssh.send_cmd(cmd="show wireless radios")
            log.info(out)
            out = ap_ssh.send_cmd(cmd="show wireless wlans interface")
            log.info(out)
            out = ap_ssh.send_cmd(cmd="show wireless clients")
            log.info(out)
            if not out:
                log.error("FAIL: No clients data found")

            # radio 1 off
            disable_radio(ap_ssh, radio_1)
            # radio 2 on
            enable_radio(ap_ssh, radio_2)
            # radio 3 off
            disable_radio(ap_ssh, radio_3)
            log.info("Sleep 150 seconds for radios to come UP and clients to reconnect")
            time.sleep(150)
            out = ap_ssh.send_cmd(cmd="show wireless radios")
            log.info(out)
            out = ap_ssh.send_cmd(cmd="show wireless wlans interface")
            log.info(out)
            out = ap_ssh.send_cmd(cmd="show wireless clients")
            log.info(out)
            if not out:
                log.error("FAIL: No clients data found")

            # radio 1 off
            disable_radio(ap_ssh, radio_1)
            # radio 2 off
            disable_radio(ap_ssh, radio_2)
            # radio 3 on
            enable_radio(ap_ssh, radio_3)
            log.info("Sleep 150 seconds for radios to come UP and clients to reconnect")
            time.sleep(150)
            out = ap_ssh.send_cmd(cmd="show wireless radios")
            log.info(out)
            out = ap_ssh.send_cmd(cmd="show wireless wlans interface")
            log.info(out)
            out = ap_ssh.send_cmd(cmd="show wireless clients")
            log.info(out)
            if not out:
                log.error("FAIL: No clients data found")
        else:
            # Turn on all radios
            for radio in radio_list:
                enable_radio(ap_ssh, radio)
    except Exception:
        msg = traceback.format_exc()
        log.error("Exception occurred")
        log.error(msg)
        raise
    finally:
        if ap_ssh:
            ap_ssh.close()


if __name__ == "__main__":

    if len(sys.argv) == 4:
        if int(sys.argv[2]) == 2:
            radio_list = [1, 2]
            test_radio_on_off_radios_2(sys.argv[1], radio_list, int(sys.argv[3]))
            logging.shutdown()
        if int(sys.argv[2]) == 3:
            radio_list = [1, 2, 3]
            test_radio_on_off_radios_3(sys.argv[1], radio_list, int(sys.argv[3]))
            logging.shutdown()
        else:
            log.error("Number of radios should be 2/3")
    else:
        log.error("Usage: python radio_on_off.py <AP_IP> <Number of radios> <Iterations>")
        log.error("Example: python radio_on_off.py 10.110.214.10 2 100")
