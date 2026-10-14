import time
import paramiko
import logging
import traceback
from SSH_session import SSH_session

log = logging.getLogger()
logging.basicConfig(level=logging.INFO, format='%(asctime)s %(lineno)d %(levelname)s: %(message)s', datefmt='%d-%m-%Y %H:%M:%S')


# def cli_reload_device(_cli_session, rebootTime=300):
#     try:
#         cmd = "reload"
#         stdin, stdout, stderr = _cli_session.ssh.exec_command(cmd)
#         stdin.write('y')
#         stdin.write('\n')
#         stdin.flush()
#         time.sleep(30)
#         count = 1
#         start = time.time()
#         device_accessible = False
#         while time.time() - start < rebootTime:
#             log.info("*" * count)
#             if _cli_session.is_host_active():
#                 device_accessible = True
#                 break
#             time.sleep(10)
#             count += 1
#         if not device_accessible:
#             log.info("********* Device not reachable ***********")
#             return False
#         # the old channel is now destroyed at reboot, so clean the object
#         _cli_session.log_out()
#         return True
#     except Exception as e:
#         log.warning("Unable to reload device")
#         log.error(str(e))
#         raise


def test_factory_reset(device_ip, iterations, new_password):
    cli_session = None
    new_cli_session = None
    admin_flag, new_password_flag = False, False
    for i in range(iterations):
        log.info(f"###################### Iteration:- {i} ######################")
        try:
            ## create SSH session to AP
            log.info("Create SSH session to AP")
            ssh_client = paramiko.SSHClient()
            ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            try:
                ssh_client.connect(hostname=device_ip, username="admin", password="admin", timeout=30)
                cli_session = ssh_client.invoke_shell()
                log.info("Logged in to AP using username: admin and password: admin")
                admin_flag = True
            except paramiko.ssh_exception.AuthenticationException:
                ssh_client.connect(hostname=device_ip, username="admin", password=new_password, timeout=30)
                cli_session = ssh_client.invoke_shell()
                log.info(f"Logged in to AP using username: admin and password: {new_password}")
                new_password_flag = True
            except paramiko.ssh_exception.SSHException as e:
                log.error(f"Exception occurred during SSH Login: {e}")
                raise

            if admin_flag:
                cli_session = SSH_session(device_ip, "admin", "admin")
            if new_password_flag:
                cli_session = SSH_session(device_ip, "admin", new_password)

            ## factory reset AP
            log.info("Executing command: delete config")
            stdin, stdout, stderr = cli_session.ssh.exec_command("delete config", timeout=10)
            stdin.write('y')
            stdin.write('\n')
            stdin.flush()

            time.sleep(30)
            log.info("Wait for AP to come UP after factory reset")
            ## waiting for AP to come UP
            start_time = time.time()
            while time.time() - start_time < 300:
                if cli_session.is_host_active():
                    log.info("AP came UP after factory reset")
                    time.sleep(2)
                    break
                time.sleep(20)
            else:
                log.error(f"AP: {device_ip} did not come UP within 300 seconds after factory reset")
                assert False, f"AP: {device_ip} did not come UP within 300 seconds after factory reset"

            ## create SSH session to AP after factory reset
            log.info("Create SSH session to AP after factory reset")
            ssh_client = paramiko.SSHClient()
            ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh_client.connect(hostname=device_ip, username="admin", password="admin", timeout=30)
            shell = ssh_client.invoke_shell()
            time.sleep(1)
            output = b''
            while shell.recv_ready():
                output += shell.recv(2048)
            if 'New password:' in output.decode():
                log.info("Setting new password")
                shell.send(new_password + '\r')
                time.sleep(1)
                while shell.recv_ready():
                    output += shell.recv(2048)
                if 'Confirm the new password:' in output.decode():
                    log.info("Confirming new password")
                    shell.send(new_password + '\r')
                    time.sleep(1)
                    shell.close()
                    ssh_client.close()
                    log.info("PASS: Setting new password is successful")
                    log.info(f'Creating SSH session for the device: {device_ip} with new password: {new_password}')
                    new_cli_session = SSH_session(device_ip, "admin", new_password)
                    log.info("PASS: Setting new password is successful")
            else:
                log.error(f"AP: {device_ip} is not asking for new password after factory reset")
                assert False, f"AP: {device_ip} is not asking for new password after factory reset"

            ## print last reboot reason
            log.info(new_cli_session.send_cmd("service show last-reboot-reason"))

            # ## check show wireless wlans output after factory reset
            # result = new_cli_session.send_cmd("show wireless wlan")
            # log.info(f"'show wireless wlan' output:\n {result}")
            # if wlan_name in result:
            #     assert False, "WLAN is still present in AP even after factory reset"
            # else:
            #     log.info("AP is successfully factory rested")
            #
            # ## push config to AP from cli
            # new_cli_session.send_cmd(f"import config tftp://{tftp_server}/config.txt")
            # time.sleep(5)
            #
            # ## reboot AP after config import
            # assert cli_reload_device(new_cli_session)
            #
            # ## check show wireless wlans output after config push
            # result = new_cli_session.send_cmd("show wireless wlan")
            # log.info(f"'show wireless wlan' output:\n {result}")
            # if wlan_name not in result:
            #     assert False, "WLAN not persent in AP after config push"
            # else:
            #     log.info("Config push successfully done from AP CLI")
            log.info("###################### PASS ######################")
        except Exception as e:
            log.critical(f"An exception of type {type(e).__name__} occurred")
            log.critical(traceback.format_exc())
            raise


if __name__ == '__main__':

    device_ip = "10.110.153.10"
    iterations = 1
    new_password = 'sitindia123'

    test_factory_reset(device_ip=device_ip, iterations=iterations, new_password=new_password)
