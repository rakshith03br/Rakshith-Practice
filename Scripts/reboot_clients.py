"""
Re-start clients scripts
"""

import time
import paramiko


def reboot_client(host, username, password, port=22):
    try:
        print(f"Connecting to {host}...")

        # Create SSH client
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())  # accept unknown keys

        # Connect
        client.connect(hostname=host, port=port, username=username, password=password, timeout=10)
        print(f"Connected to {host}")

        if host == '172.30.1.150':
            # Execute reboot command
            client.exec_command("shutdown /r /t 0")
        else:
            # Execute reboot command
            client.exec_command("init 6")

        print(f"Reboot command sent to {host}")

        time.sleep(2)
        client.close()
        print(f"Disconnected from {host}")

    except Exception as e:
        print(f"Error connecting to {host}: {e}")


if __name__ == "__main__":

    clients = [
        {"host": "192.168.60.25", "username": "root", "password": "sitindia123"},
        {"host": "192.168.100.25", "username": "root", "password": "sitindia123"},
        {"host": "172.30.1.200", "username": "root", "password": "sitindia123"},
        {"host": "172.30.1.250", "username": "root", "password": "sitindia123"},
        {"host": "172.30.1.251", "username": "root", "password": "sitindia123"},
        {"host": "172.30.1.120", "username": "root", "password": "sitindia123"},
        {"host": "172.30.1.130", "username": "root", "password": "sitindia123"}]

    for c in clients:
        reboot_client(c["host"], c["username"], c["password"])
