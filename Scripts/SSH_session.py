import traceback
import paramiko
import time
import socket
import inspect
import re
import platform
import os
import logging
import pexpect
import subprocess
import json

log = logging.getLogger(__name__)

# Change this value when testing over internet to an appropriate value
TIME_BW_RETRIES = 0.3


class SSH_session():

    def __init__(self,
                 hostname="127.0.0.1",
                 username="admin",
                 password="admin",
                 os="access_point",
                 keyfile=None,
                 configfile=None,
                 friendly_name=None,
                 aws=None,
                 appliance=None,
                 retriesAllowed=25,
                 shell_timeout=30,
                 port=22):
        log.debug(inspect.currentframe().f_code.co_name)
        logging.getLogger("paramiko").setLevel(logging.INFO)
        self.hostname = hostname
        self.username = username
        self.password = password
        self.os = os
        self.keyfile = keyfile
        self.config_file = configfile
        self.friendly_name = friendly_name
        self.aws = aws
        self.shell = None
        self.ssh = None
        self.appliance = appliance  # determines if cnMaestro runs as appliance
        self.shell_timeout = shell_timeout  # Timeout fo shell commands
        self.retriesAllowed = retriesAllowed
        self.retryCount = 1
        self.port = port
        try:
            self.init_shell()
        except Exception as e:
            if not self.retry_connect(timeBetweenRetries=TIME_BW_RETRIES):
                raise

    def init_shell(self):
        """
        Initializes shell and ssh client to execute command
        ssh - to send and recv from channel directly
        shell - to send exec_cmd
        :return: None
        """
        log.debug(inspect.currentframe().f_code.co_name)
        try:
            log.info("Creating SSH_session ip: %s, username: %s, password: %s, operating system: %s" % (self.hostname, self.username, self.password, self.os))
            time.sleep(1)
            self.ssh = paramiko.SSHClient()
            self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

            if self.keyfile and self.config_file:
                self.ssh._policy = paramiko.WarningPolicy()
                # loading the ssh config file
                ssh_config = paramiko.SSHConfig()
                if os.path.exists(self.config_file):
                    with open(self.config_file) as f:
                        ssh_config.parse(f)
                parameters = {
                    "hostname": self.hostname,
                    "username": self.username,
                    "port": 22,
                }
                # looking for the given host from the loaded ssh config.
                user_config = ssh_config.lookup(self.friendly_name)
                for k in ('hostname', 'username', 'port'):
                    if k in user_config:
                        parameters[k] = user_config[k]

                # if any proxy available for the server asked
                if 'proxycommand' in user_config:
                    parameters['sock'] = paramiko.ProxyCommand(user_config['proxycommand'])

                # override the private key from the ssh config if any.
                parameters['key_filename'] = self.keyfile
                parameters['timeout'] = 10
                self.ssh.connect(**parameters)

            elif self.keyfile:
                log.info(self.keyfile, self.aws)
                keypath = '~/.ssh/' + self.keyfile
                key_filename = os.path.expanduser(keypath)
                # password = keyring.get_password("SSH",key_filename)
                self.ssh.connect(
                    self.hostname,
                    username=self.username,
                    key_filename=os.path.expanduser(keypath),
                    timeout=10)
            else:
                self.ssh.connect(
                    self.hostname,
                    username=self.username,
                    password=self.password,
                    port=self.port,
                    timeout=10)
            if self.appliance:
                # logic to perform bifold ssh inorder to get cnMaestro shell
                ssh_transport = self.ssh.get_transport()
                # cnMaestro Private IP which is hardened in case of appliance
                cnmaestro_addr = ('192.168.100.253', 22)
                appliance_addr = (self.hostname, self.port)
                app_channel = ssh_transport.open_channel(
                    "direct-tcpip", cnmaestro_addr, appliance_addr)
                jump_host = paramiko.SSHClient()
                jump_host.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                jump_host.connect(
                    '192.168.100.253',
                    username='cambium',
                    password='cnmaestro',
                    sock=app_channel,
                    timeout=10)
                self.ssh = jump_host  # shallow copy the object

            self.shell = self.ssh.invoke_shell()
            self.shell.settimeout(self.shell_timeout)
            time.sleep(3)
            self.shell.send("\r\n")
            start_time = time.time()
            timeout = 10
            while True:
                if self.shell.recv_ready():
                    resp = self.shell.recv(99999)
                    log.debug(resp)
                    break
                else:
                    if time.time() - start_time > timeout:
                        log.error("Timed Out waiting for data after establishing SSH session")
                        break
            self.retryCount = 1
        except paramiko.AuthenticationException:
            # in case of authentication exception report and stop
            log.error("Paramiko authentication exception!")
            shell = None
            raise paramiko.AuthenticationException("SSH Authentication Exception")
        except paramiko.ssh_exception.NoValidConnectionsError:
            # log.error("NOTICE ME")
            log.error("Multiple connection attempts were made and no families succeeded")
            raise
        except (socket.error, EOFError, paramiko.SSHException, paramiko.ssh_exception.NoValidConnectionsError) as e:
            if e is EOFError:
                log.error("EOFError")
            elif e is socket.error:
                log.error(e.strerror)
                log.error("Unable to establish socket")
            elif e is paramiko.SSHException:
                log.error(e.strerror)
                log.error("Unable to Establish SSH Session to device")
            elif e is paramiko.ssh_exception.NoValidConnectionsError:
                log.error(e.strerror)
                log.error("Multiple connection attempts were made and no families succeeded")
            else:
                log.error(str(e))
            raise

    def flush_buffer(self):
        if self.shell and self.shell.recv_ready():
            log.debug(self.shell.recv(9999))

    def is_host_active(self):
        log.debug(inspect.currentframe().f_code.co_name)
        """
        Check if the given hostname is active and pingable
        :param hostname: hostname can be a local dns assigned, ip, web address etc
        :return: True/False
        """
        if "posix" in os.name:
            output = subprocess.Popen(["ping", "-c1", self.hostname], stdout=subprocess.PIPE).communicate()[0]
            pattern = "\d+ bytes from .*\(?((25[0-4]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(2[0-4][0-9]|[01]?[0-9][0-9]?[0-9]?)\)?: icmp_seq=\d+ ttl=\d+ time=\d+.\d* ms"
        else:
            output = subprocess.Popen(["ping", "-n", "1", self.hostname], stdout=subprocess.PIPE,
                                      shell=True).communicate()[0]
            # handle 250 series ips
            pattern = "Reply from ((2[0-5][0-9]|[01]?[0-9][0-9]?)\.){3}(2[0-4][0-9]|[01]?[0-9][0-9]?): bytes=\d{2} time[<|=]\d+ms TTL=\d+"

        output = output.decode('utf-8')
        log.debug("Ping result\n %s"% str(output))

        if 'unreachable' in output:
            log.warning("Offline:\t%s"% self.hostname)
            log.warning("Unable to ping device:\t%s"% self.hostname)
            return False
        if "Request timed out." in output:
            log.warning("Request timed out:\t%s"% self.hostname)
            log.warning("Unable to ping device:\t%s"% self.hostname)
            return False
        if re.search(pattern, output):
            log.debug("Reachable:\t%s"% self.hostname)
            return True
        log.warning("Unable to ping device:\t%s" % self.hostname)
        return False

    def is_session_alive(self):
        log.debug(inspect.currentframe().f_code.co_name)
        """
        Check if the session shell is still active
        :return: True/False
        """
        try:
            if self.shell.closed:
                raise paramiko.SSHException('SSH interactive shell Channel is not open')
            elif self.shell.eof_received or self.shell.eof_sent or not self.shell.active:
                self.shell.close()
                raise paramiko.SSHException('SSH interactive shell Channel is not open')
            else:
                # stdin, stdout, stderr = self.ssh.exec_command("show version", bufsize=99999)
                return True
        except Exception as e:
            log.error("Exeption occurred while checking for active SSH interactive shell channel")
            log.error(e)
            # self.log_out()
            return False

    def is_ssh(self):
        '''
        Check if the ssh session is still active
        :return: True/False
        '''
        try:
            if self.ssh.get_transport().is_active():
                return True
            else:
                log.warning("SSH Session not active")
                return False
        except Exception:
            log.warning("SSH Session not active")
            return False

    def retry_connect(self, timeBetweenRetries=TIME_BW_RETRIES):
        log.debug(inspect.currentframe().f_code.co_name)
        """
        Attempt to reconnect ssh session
            a given prefixed number of times
        :param timeBetweenRetries: time to wait between retries
        :return: None
        """
        log.debug("In retry logic")

        while self.retryCount <= self.retriesAllowed:
            log.debug("No of retries(%s)/Retries Allowed(%s)" % (self.retryCount, self.retriesAllowed))
            log.debug("Sleep %s seconds before retry" % timeBetweenRetries)
            time.sleep(timeBetweenRetries)
            self.retryCount += 1
            if self.is_host_active():
                try:
                    self.init_shell()
                except Exception as e:
                    if self.retryCount > self.retriesAllowed:
                        raise
                    else:
                        continue
                return True
        return False

    def send_cmd(self, cmd="ls", timeout=60):
        log.debug(inspect.currentframe().f_code.co_name)
        """
        Sends a command to ssh_session
            returns the result of the command
        :param cmd: command to be executed
        :return: result of cmd
        """
        try:
            # if self.is_session_alive():
            if self.is_ssh():
                log.debug("The command going to execute : %s" % cmd)
                try:
                    stdin, stdout, stderr = self.ssh.exec_command(cmd, bufsize=99999, timeout=timeout)
                except Exception as e:
                    log.error(f"Following exception occurred while executing the command: {cmd}")
                    log.error(str(e))
                    log.info("Closing SSH session & initiating new SSH session")
                    self.ssh.close()
                    time.sleep(30)
                    try:
                        self.init_shell()
                    except Exception as e:
                        log.error("exception occurred while doing ssh init shell %s" % e)
                        log.info("sleeping for 2 min before retrying the init shell")
                        time.sleep(120)
                        self.init_shell()
                    time.sleep(10)
                    log.info(f"Retrying executing the command: {cmd}")
                    stdin, stdout, stderr = self.ssh.exec_command(cmd, bufsize=99999, timeout=timeout)
                stdin.flush()
                stdin.close()
                time.sleep(1)
                endtime = time.time() + timeout
                while not stdout.channel.eof_received:
                    time.sleep(1)
                    if time.time() > endtime:
                        stdout.channel.close()
                        stderr.channel.close()
                        break
                output = stdout.read()
                output = output.decode('utf-8').strip()
                if output:
                    log.debug("result : %s " % output)
                    stdout.channel.close()
                    stderr.channel.close()
                    return output
                else:
                    error = stderr.read()
                    error = error.decode('utf-8').strip()
                    if not error:
                        log.debug("result : %s " % output)
                        stdout.channel.close()
                        stderr.channel.close()
                        return output
                    log.error("Error : %s " % error)
                    stdout.channel.close()
                    stderr.channel.close()
                    return error
            elif self.is_host_active():
                self.retry_connect(timeBetweenRetries=TIME_BW_RETRIES)
                log.debug("The command going to execute : %s" % cmd)
                try:
                    stdin, stdout, stderr = self.ssh.exec_command(cmd, bufsize=99999, timeout=timeout)
                except Exception as e:
                    log.error(f"Following exception occurred while executing the command: {cmd}")
                    log.error(str(e))
                    log.info("Closing SSH session & initiating new SSH session")
                    self.ssh.close()
                    time.sleep(5)
                    try:
                        self.init_shell()
                    except Exception as e:
                        log.error("exception occured while doing ssh init shell %s" % e)
                        log.info("sleeping for 2 min before retrying the init shell")
                        time.sleep(120)
                        self.init_shell()
                    time.sleep(5)
                    log.info(f"Retrying executing the command: {cmd}")
                    stdin, stdout, stderr = self.ssh.exec_command(cmd, bufsize=99999, timeout=timeout)
                stdin.flush()
                stdin.close()
                time.sleep(1)
                endtime = time.time() + timeout
                while not stdout.channel.eof_received:
                    time.sleep(1)
                    if time.time() > endtime:
                        stdout.channel.close()
                        break
                output = stdout.read()
                output = output.decode('utf-8').strip()
                if output:
                    log.debug("result : %s " % output)
                    stdout.channel.close()
                    stderr.channel.close()
                    return output
                else:
                    error = stderr.read()
                    error = error.decode('utf-8')
                    if not error:
                        log.debug("result : %s " % output)
                        stdout.channel.close()
                        stderr.channel.close()
                        return output
                    log.error("Error : %s " % error)
                    stdout.channel.close()
                    stderr.channel.close()
                    return error
            else:
                raise paramiko.SSHException("SSH Exception")
        except paramiko.SSHException as e:
            log.error("paramiko command execution failed as %s" % str(e))
            raise
        except Exception as e:
            log.error(str(e))
            raise

    def safe_send_cmd(self, cmd, timeout=60, ignore_error=False):
        """
        Safe wrapper for send_cmd().

        - Logs output and warnings if potential command error is detected.
        - Suppresses exceptions if ignore_error=True.

        Args:
            cmd (str): Command to execute via SSH.
            timeout (int): Timeout in seconds.
            ignore_error (bool): If True, exceptions are suppressed and "" returned.

        Returns:
            str: Output of the command, or "" if suppressed error.
        """
        try:
            output = self.send_cmd(cmd, timeout=timeout)
            if output is not None and any(x in output.lower() for x in ["error", "fail", "not found"]):
                log.warning(
                    f"[{self.hostname}] ⚠️ Potential command failure:\n  ➤ Command: {cmd}\n  ➤ Output: {output.strip()}")
            return output.strip() if output else ""
        except Exception as e:
            log.error(f"[{self.hostname}] ❌ Command failed:\n  ➤ Command: {cmd}\n  ➤ Exception: {e}")
            if ignore_error:
                log.warning(f"[{self.hostname}] 🚧 Continuing despite error (ignore_error=True)")
                return ""
            raise

    def log_out(self):
        log.debug(inspect.currentframe().f_code.co_name)
        """
        logout and cleanup the SSH Session
        :return: None
        """
        try:
            self.ssh.close()
        except paramiko.SSHException as e:
            log.error("paramiko exit failed...")
            log.error(str(e))
            raise


    def close(self):
        log.debug(inspect.currentframe().f_code.co_name)
        """
        logout and cleanup the SSH Session
        :return: None
        """
        try:
            self.ssh.close()
        except paramiko.SSHException as e:
            log.error("paramiko exit failed...")
            log.error(str(e))
            raise

    # def __del__(self):
    #     """
    #     Class destructor
    #     :return: None
    #     """
    #     log.info("Destroying SSHSession object")
    #     self.log_out()

    def send_shell(self, cmd, expectedPrompt='CTRL-EVENT-SCAN-STARTED', counter=5, line_sep='\r\n'):
        """
        Sends a series of shell commands
        :param cmd: command to be executed
        :param expectedPrompt: prompt expected, if its going to change
        :return: result of cmd
        """
        try:
            cmd += line_sep
            retry = 1
            while retry <= counter:
                if self.is_session_alive():
                    # Wait for maximum 2 minutes for the channel to be ready to send
                    start_time = time.time()
                    while time.time() - start_time <= 120:
                        if not self.shell.send_ready():
                            log.debug("Waiting for channel to get ready to send data")
                            time.sleep(10)
                        else:
                            break
                    else:
                        log.error("Channel did not become ready to send data within 2 minutes. "
                                  "Retrying sending command")
                        retry += 1
                        continue
                    try:
                        # Send the command
                        log.info(f"Executing command:{cmd}")
                        self.shell.send(cmd)
                    except socket.timeout:
                        log.error("Socket timeout occurred while sending data. Retrying...")
                        retry += 1
                        time.sleep(2)
                        continue

                    # Receive data
                    # Wait for a brief moment to receive the output
                    time.sleep(5)
                    # Waiting for max 2 minutes to receive the data
                    start_time = time.time()
                    while time.time() - start_time <= 120:
                        if not self.shell.recv_ready():
                            log.debug("Waiting for channel to get ready to receive data")
                            time.sleep(10)
                        else:
                            break
                    else:
                        log.error("Channel did not become ready to receive the data within 2 minutes. "
                                  "Retrying sending command")
                        retry += 1
                        continue
                    resp = self.shell.recv(99999)
                    resp = resp.decode('utf8')
                    log.debug("Command output:")
                    log.debug(resp)
                    log.debug(f"Expected prompt: {expectedPrompt}")
                    if 'Error processing cli command' in resp:
                        log.error("Failed to execute the command")
                        # Sending exit command to come out of current prompt
                        self.shell.send("exit")
                        time.sleep(2)
                        if self.shell.recv_ready():
                            self.shell.recv(99999)
                        return "%Error processing cli command"
                    elif expectedPrompt in resp:
                        log.debug("Found expected prompt")
                        return resp
                    else:
                        log.error("Expected prompt not returned but returned:")
                        log.error(resp)
                        log.info("Retrying")
                        retry += 1
                        time.sleep(2)
                else:
                    log.error("SSH Interactive Shell Channel is not open")
                    log.info("Opening SSH Interactive Shell Channel.............")
                    try:
                        self.shell = self.ssh.invoke_shell()
                        time.sleep(2)
                        if self.shell.recv_ready():
                            self.shell.recv(99999)
                        return "%Error processing cli command"
                    except paramiko.SSHException:
                        msg = traceback.format_exc()
                        log.error(msg)
                        log.error("Exception occurred while Opening SSH Interactive Shell Channel")
                        log.info("Opening new SSH session after waiting for 1 minutes")
                        time.sleep(60)
                        self.init_shell()
                        time.sleep(2)
                        if self.shell.recv_ready():
                            self.shell.recv(99999)
                        return "%Error processing cli command"
            else:
                log.error(f"Could not execute command {cmd} after {counter} retries")
                return "%Error processing cli command"
        except Exception:
            msg = traceback.format_exc()
            log.error("Exception occurred")
            log.error(msg)
            raise

    def remote_shell_cmd(self, cmd, line_sep='\n'):
        """
        Execute a command in the background on remote shell & captures standard output & error
        :param cmd: command to be executed
        :return: standard output and standard error
        """
        try:
            if not self.is_session_alive():
                self.init_shell()
            cmd += line_sep
            while self.shell.recv_ready():
                self.shell.recv(99999)
            while self.shell.recv_stderr_ready():
                self.shell.recv_stderr(99999)
            output = ""
            error = ""
            log.info(f"Executing command: {cmd}")
            self.shell.send(cmd)
            time.sleep(1)
            while self.shell.recv_ready():
                output += self.shell.recv(99999).decode('utf8').strip()
            while self.shell.recv_stderr_ready():
                error += self.shell.recv_stderr(99999).decode('utf8').strip()
            if not error:
                return output
            else:
                return error
        except paramiko.SSHException as e:
            log.error(f"paramiko command execution failed: {e}")
        except Exception as e:
            log.error("Exception Occurred: {e}")

    def sudo_exec(cmdline, passwd):
        osname = platform.system()  # 1
        if osname == 'Linux':
            prompt = r'\[sudo\] password for %s: ' % os.environ['USER']
        elif osname == 'Darwin':
            prompt = 'Password:'
        else:
            assert False, osname

        child = pexpect.spawn(cmdline)
        idx = child.expect([prompt, pexpect.EOF], 3)  # 2
        if idx == 0:  # if prompted for the sudo password
            log.debug('sudo password was asked.')
            child.sendline(passwd)
            child.expect(pexpect.EOF)
        return child.before

    def send_shell_cmd(self, cmd, expectedPrompt=None, regex=False, interactive_mode=False):
        """
        Sends a command to interactive shell and returns it response
        :param cmd: command to be executed
        :param expectedPrompt: prompt expected
        :param regex: True if the expected prompt is regular expression, False otherwise and default.
        :param interactive_mode: if True keep the session in interactive mode and user can give input in next command
        :return: tuple (result, resp), result will be True if expectedPrompt is matched in the response.
        """
        self.flush_buffer()
        # Wait for shell to be ready to receive inputs
        while not self.shell.send_ready():
            pass
        if isinstance(cmd, bytes):
            cmd += b'\r\n'
        elif isinstance(cmd, str):
            if interactive_mode:
                cmd += '\r'
            else:
                cmd += '\r\n'

        self.shell.send(cmd)

        # Wait for shell to be ready to read inputs
        start_time = time.time()
        while time.time() < start_time + 300:
            if self.shell.recv_ready():
                break
        else:
            raise AssertionError("Device shell is not ready")

        if expectedPrompt is None:
            regex = re.compile(r"(#|\$|\>)$")
        elif regex:
            regex = re.compile(expectedPrompt)
        else:
            regex = re.compile(re.escape(expectedPrompt))

        resp = ""
        try:
            time.sleep(3)
            resp = self.shell.recv(9999)
            resp = str(resp, 'utf-8')
            log.debug(resp)
            if not re.search(regex, resp.strip()):
                start_time = time.time()
                while time.time() < start_time + 300:
                    if self.shell.recv_ready():
                        resp += str(self.shell.recv(9999), 'utf-8')
                        log.debug(resp)
                        if not re.search(regex, resp.strip()):
                            log.debug("Expected prompt not found in the response")
                            result = False
                            break
                        else:
                            result = True
                        break
                    else:
                        log.debug("Expected prompt not found in the response")
                        result = False
                        break
            else:
                result = True
        except socket.timeout:
            result = False
        log.info(resp)
        log.info("removing ansi escape sequences")
        ansi_escape = re.compile(r'(\x9B|\x1B\[)[0-?]*[ -\/]*[@-~]')
        resp = ansi_escape.sub('', resp)

        return result, resp

    def send_shell_send_recv(self, cmd, regex=None):
        """
         Sends a command to interactive shell and returns it response without validation
        :param cmd: command to be executed
        :return: tuple (result, resp) , result will be False on exception
        """

        self.flush_buffer()
        # Wait for shell to be ready to receive inputs
        while not self.shell.send_ready():
            pass

        if isinstance(cmd, bytes):
            cmd += b'\r\n'
        elif isinstance(cmd, str):
            cmd += '\r\n'
        self.shell.sendall(cmd)

        if not regex:
            eod_regex = r"(\#|\$|\>)$"
        else:
            eod_regex = regex

        time.sleep(3)
        # Wait for shell to be ready to read inputs
        # If shell is not recv_ready in 60 mins then timeout
        start_time = time.time()
        while time.time() < start_time + 120:
            if self.shell.recv_ready():
                break
        else:
            raise AssertionError("Device shell is not ready")
        try:
            read_buffer_size = 99999
            output = self.shell.recv(read_buffer_size)
            resp = str(output, 'utf-8')

            # Read till end of data or till no data in the channel
            while not re.search(eod_regex, resp.strip()):
                time.sleep(0.5)
                output = self.shell.recv(read_buffer_size)
                if output:
                    resp = resp + str(output, 'utf-8')
                else:
                    break
            result = True

        except socket.timeout as e:
            log.debug(
                "Exception while send and recv of shell command : %s" %
                str(e))
            result = False

        log.debug(resp)
        return result, resp

    def depricated_send_shell_cmd(
            self,
            cmd,
            expectedPrompt=None,
            regex=False,
            eod_resp=True):
        """
        Sends a command to interactive shell through send_shell_send_recv command and returns it response after
         validation
        :param cmd: command to be executed
        :param expectedPrompt: prompt expected
        :param regex: True if the expected prompt is regular expression, False otherwise and default.
        :param eod_resp: True if the expected prompt is end of the response, False otherwise.
        :return: tuple (result, resp) , result will be True if expectedPrompt is matched in the response.
        """
        if expectedPrompt:
            if regex:
                regex = expectedPrompt
            else:
                regex = re.escape(expectedPrompt)
            if eod_resp:
                regex = "(%s)$" % regex

        result, resp = self.send_shell_send_recv(cmd, regex)

        # Validate response if expected Prompt is given
        if expectedPrompt:
            if re.search(regex, resp.strip()):
                result = True
            else:
                result = False

        log.debug("removing ansi escape sequences")
        ansi_escape = re.compile(r'(\x9B|\x1B\[)[0-?]*[ -\/]*[@-~]')
        resp = ansi_escape.sub('', resp)
        return result, resp

    def send_command_shell_once(self, cmd, expectedPrompt='CTRL-EVENT-SCAN-STARTED', counter=10,waitTime=10):
        """
        Sends a series of shell commands
        :param cmd: command to be executed
        :param expectedPrompt: prompt expected, if its going to change
        :return: result of cmd
        """
        try:
            cmd += '\r\n'
            self.shell.send(cmd)
            time.sleep(waitTime)
            resp = ""
            while (not expectedPrompt in resp) and counter > 0:
                counter = counter - 1
                time.sleep(1)
                if self.shell.recv_ready():
                    resp = self.shell.recv(99999)
                log.debug("result : %s " % resp)
            return resp
        except paramiko.SSHException as e:
            log.error("paramiko command execution failed...")
            log.error(str(e))

    # # not used
    def send_sudo(self, cmd='ls'):
        """
        Sends a sudo command to ssh_session
        returns the result of the command
        :param cmd: command to execute
        :return: result of cmd
        """
        if self.aws:
            return self.send_cmd(cmd=cmd)
        try:
            log.debug("The command going to execute : %s" % cmd)
            stdin, stdout, stderr = self.ssh.exec_command(cmd)
            epwd = self.password + '\n'
            stdin.write(epwd)
            stdin.flush()
            stdin.close()
            line = stdout.read()
            log.debug("result : %s " % line)
            stdout.channel.close()
            stderr.channel.close()
            return line
        except paramiko.SSHException as e:
            log.error(stderr.read())
            stdout.channel.close()
            stderr.channel.close()
            log.error("paramiko command execution failed...")
            log.error(str(e))

    #
    # # not used
    # def sftp_put(self, source='mongodb.list', dest='/home/ubuntu/mongodb.list'):
    #     """
    #     SFTP a file from host to destination
    #     :param source: source file path
    #     :param dest: destination file path
    #     :return: None
    #     """
    #     try:
    #         sftp = self.ssh.open_sftp()
    #         log.debug(sftp, source, dest)
    #         sftp.put(source, dest)
    #         sftp.close()
    #         log.info("copied successfully!")
    #     except paramiko.SSHException, e:
    #         log.error("paramiko exit failed...")
    #         log.error(str(e))
    # # not used
    # def sshpass_send_cmd(self, ip='192.168.10.12', user='root', password='password', cmd='ls'):
    #     """
    #     NOT USED : FUTURE
    #     :param ip:
    #     :param user:
    #     :param password:
    #     :param cmd:
    #     :return:
    #     """
    #     self.ssh
    #     comd = 'sshpass -p ' + password + ' ssh -o StrictHostKeyChecking=no ' + \
    #         user + '@' + ip + " \'" + cmd + "\'"
    #
    #     line = self.send_cmd(comd)
    #     if line:
    #         return line
    #     else:
    #         log.error("sshpass command \'%s\' failed.." % comd)

    def issue_command(self, command="ls", pause=2):
        # chan = self.shell.transport
        self.shell.send(command)

        buff_size = 1024
        stdout = ""
        stderr = ""

        while not self.shell.exit_status_ready():
            time.sleep(pause)
            if self.shell.recv_ready():
                stdout += self.shell.recv(buff_size).decode('utf-8')

            if self.shell.recv_stderr_ready():
                stderr += self.shell.recv_stderr(buff_size).decode('utf-8')

        exit_status = self.shell.recv_exit_status()
        # Need to gobble up any remaining output after program terminates...
        while self.shell.recv_ready():
            stdout += self.shell.recv(buff_size).decode('utf-8')

        while self.shell.recv_stderr_ready():
            stderr += self.shell.recv_stderr(buff_size).decode('utf-8')

        return exit_status, stdout, stderr

    def perform_exec_command(self, command="sudo -i", passwd=None):
        """
        command is executed along with the password.
        :param command: command to be executed
        :param passwd: password to successfully execute the command
        :return: objects representing stdin, stdout, and stderr.
        """
        stdin, stdout, stderr = self.ssh.exec_command(command, get_pty=True)
        if passwd:
            stdin.write(passwd)
            stdin.write('\n')
        return stdin, stdout, stderr

    def send_recv(self, command, timeout=30):
        """
        will issue and receive the output
        :param command: command to be issued
        :param timeout: timeout for the command channel
        :return: response received for the command
        """
        stdout = self.ssh.exec_command(command, timeout=timeout)[1]
        resp = stdout.read()
        log.debug("\n")
        log.debug("*" * 120)
        log.debug("COMMAND: %s" % command)
        log.debug("\n")
        log.debug("OUTPUT:")
        log.debug(resp)
        log.debug("*" * 120)
        return resp.decode('utf-8').strip()

    def copy_data_to_file_in_remote_server(self, data, file, create_new_session=True):
        """
        will copy the requested data to a file specified in the remote machine.
        :param data: data to be copied to a file
        :param file: name of the file. Provide absolute path for file in which the data to be copied to
        :param create_new_session: Whether to create a new SSH connection or reuse an existing one.
        :return:
        """
        if create_new_session:
            transport = paramiko.Transport((self.hostname, 22))
            transport.connect(username=self.username, password=self.password)
            sftp = paramiko.SFTPClient.from_transport(transport)
        else:
            sftp = paramiko.SFTPClient.from_transport(self.ssh.get_transport())
        f = sftp.open(file, "a+")
        f.write(data)
        f.close()

    def upload_file(self, uploadlocalfilepath, uploadremotefilepath):
        "This method uploads the file to remote server from the local host"
        result_flag = True
        try:
            ftp_client = self.ssh.open_sftp()
            ftp_client.put(uploadlocalfilepath, uploadremotefilepath)
            ftp_client.close()
        except Exception as e:
            log.error(f'Unable to upload the file {uploadlocalfilepath} to the remote server due to Exception')
            log.error(f'PYTHON SAYS: {e}')
            result_flag = False
            ftp_client.close()

        return result_flag


    def download_file(self, downloadremotefilepath, downloadlocalfilepath):
        "This method downloads the file from remote server to the local host."
        result_flag = True
        try:
            ftp_client = self.ssh.open_sftp()
            ftp_client.get(downloadremotefilepath, downloadlocalfilepath)
            ftp_client.close()
        except Exception as e:
            log.error(f'Unable to download the file {downloadremotefilepath} from the remote server due to Exception')
            log.error(e)
            result_flag = False
            ftp_client.close()

        return result_flag

    def read_data_file_from_remote_server(self, file):
        """
        will copy the requested data to a file specified in the remote machine.

        :param file: name of the file. Provide absoluate path for file in which the data to be copied to
        :return:
        """

        sftp = self.ssh.open_sftp()
        with sftp.open(file, 'r') as f:
            json_data = json.load(f)
        sftp.close()
        return json_data

    def write_data_to_file_in_remote_server(self, data, filename, append=True):
        """
        Will write the data to existing file in remote server or create a new file
        """
        try:
            sftp = self.ssh.open_sftp()

            # Open the remote file for writing
            with sftp.open(filename, 'w') as remote_file:
                # Write the data to the file
                remote_file.write(data)

            # Close the SFTP session
            sftp.close()
        except Exception as e:
            log.error(f'Not able to write data to file due to {e}')

    def wait_for_expected_resp(self, expected_resp, timeout=500):
        """
        api to receive the output from shell untill expected response is present or timeout happens
        :param expected_resp: response in string
        :param timeout: timeout to wait for the response
        :return: True, "success" if expected response is found else False, error_message
        """
        tstart = time.time()
        output = ""
        while tstart + timeout > time.time():
            try:
                resp = str(self.shell.recv(9999), 'utf-8')
                output = output + resp
                if expected_resp in output:
                    status = True
                    msg = "success"
                    break
                else:
                    time.sleep(5)
                    continue
            except Exception as e:
                msg = "Error: %s, resp: %s" % (str(e), output)
                status = False
        else:
            return False, "Expected response is not found, resp: %s" % output
        return True, "success"

    def check_file_availability(self, path, pattern):
        """
        check for given file availability in cnMaestro server
        :param path: location in which file presence has to be looked for
        :param pattern: pattern of file to be looked for
        :return:
        """
        ls_cmd = f"ls {path}"
        log.info(f"list of content from {ls_cmd} is %s")
        status, result = self.send_shell_cmd(
            ls_cmd, expectedPrompt=':~$')
        matches = re.findall(
            pattern.split('*')[0],
            result,
            re.DOTALL | re.MULTILINE)
        if len(matches) >= 1:
            log.info(
                "File pattern %s is available and the result is %s" %
                (pattern, result))
            return True
        else:
            log.error("File pattern %s not found" % pattern)
            return False

    def delete_files_by_pattern(self, path, pattern):
        """
        Deletes files matching the given pattern in the specified path on a remote server.

        :param path: Directory where the files are located.
        :param pattern: Regex pattern to match file names.
        :return: List of deleted files.
        """
        try:
            # List files in the given path
            ls_cmd = f"ls {path}"
            status, result = self.send_shell_cmd(ls_cmd, expectedPrompt=':~$')

            if not status:
                log.error(f"Failed to list files in {path}")
                return []

            # Find files matching the pattern
            matched_files = [file for file in result.split("\n") if re.match(pattern, file)]

            if not matched_files:
                log.info(f"No files matching pattern '{pattern}' found in {path}")
                return []

            # Delete matching files
            deleted_files = []
            for file in matched_files:
                rm_cmd = f"sudo rm -f {path}/{file}"
                status, _ = self.send_shell_cmd(rm_cmd, expectedPrompt=':~$')
                if status:
                    deleted_files.append(file)
                    log.info(f"Deleted: {file}")
                else:
                    log.error(f"Failed to delete: {file}")

            return deleted_files

        except Exception as e:
            log.error(f"Error deleting files: {str(e)}")
            return []


class SFTPConnection(object):
    """
    SSH Connection class enabling SFTP get and put.
    """

    def __init__(self, host, username, password, port=22):
        """Initialize and setup connection"""
        self.sftp = None
        self.sftp_open = False

        # open SSH Transport stream
        self.transport = paramiko.Transport((host, port))

        self.transport.connect(username=username, password=password)

    def _openSFTPConnection(self):
        """
        Opens an SFTP connection if not already open
        """
        if not self.sftp_open:
            self.sftp = paramiko.SFTPClient.from_transport(self.transport)
            self.sftp_open = True

    def get(self, remote_path, local_path=None):
        """
        Copies a file from the remote host to the local host.
        """
        self._openSFTPConnection()
        self.sftp.get(remote_path, local_path)

    def put(self, local_path, remote_path, filename):
        """
        Copies a file from the local host to the remote host
        """
        self._openSFTPConnection()
        self.sftp_mkdir_path(remote_path)
        self.sftp.put(local_path, remote_path + filename)

    def close(self):
        """
        Close SFTP connection and ssh connection
        """
        if self.sftp_open:
            self.sftp.close()
            self.sftp_open = False
        self.transport.close()

    def sftp_mkdir_path(self, remote_directory):
        """
        Recursively creates directory on the remote server
        :param remote_directory: Path (Directory structure) to be created
        """
        dirs_exist = remote_directory.split('/')
        dirs_make = []
        # find level where dir doesn't exist
        while len(dirs_exist) > 0:
            try:
                self.sftp.listdir('/'.join(dirs_exist))
                break
            except IOError:
                value = dirs_exist.pop()
                if value == '':
                    continue
                dirs_make.append(value)
            else:
                return False
        # ...and create dirs starting from that level
        for mdir in dirs_make[::-1]:
            dirs_exist.append(mdir)
            self.sftp.mkdir('/'.join(dirs_exist))


if __name__ == "__main__":
    # config_file = get_file_path('ami_config')
    # key_file = get_file_path('ami_id_rsa')
    # ssh_ses = SSH_session(hostname='35.175.95.202', username='ubuntu',
    # keyfile=key_file,config_file = config_file, server_friendly_name='facebook')
    # # ssh_ses.init_shell()
    # print(ssh_ses.send_shell_cmd(cmd='dpkg -s cnmaestro-server'))
    #
    # # Start tunnel
    # tunnel = ssh_ses.create_ssh_tunnel(jumphost_ip='52.66.57.251',user='pavan',identityfile='id_rsa')
    # try:
    #     db_server = '127.0.0.1'
    #     db_port = 3210
    #     client = pymongo.MongoClient('mongodb://{}:{}'.format(db_server, db_port))
    #     db = client['stats']
    #     res = db['b88abc17511aa2990c8644bf3a7471bc.inventory']
    #     for data in res.find({}):
    #         print data
    # finally:
    #     ssh_ses.close_ssh_tunnel([tunnel])
    sftp = SFTPConnection(host='10.110.192.203', username='', password='')
    sftp.get(r"/home/watermelon/testdata/device_builds/gambit/E400_E50X-4.0-r4.img",
             "C:/Users/pmi001/project/ctaf/cnssauto/temp/E400_E50X-4.0-r4.img")
