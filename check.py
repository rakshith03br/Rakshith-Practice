# # set:
#
# # creating empty set
# s = set()
# print(type(s))  # Output: <class 'set'>
#
# # Creating a set with curly braces
# my_set = {1, 2, 3, 4, 4, 5}
# print(my_set)   # {1, 2, 3, 4, 5}  -> duplicate 4 removed
#
# # Adding and Removing Elements
# my_set = {10, 20, 30}
# my_set.add(40)         # Add a single element
# print(my_set)          # {40, 10, 20, 30}
#
# my_set.update([50, 60])  # Add multiple elements
# print(my_set)            # {40, 10, 50, 20, 60, 30}
#
# my_set.remove(20)      # Removes 20, raises error if not present
# print(my_set)
#
# my_set.discard(100)    # No error if element doesn’t exist
# print(my_set)
#
# my_set.discard(60)    # {40, 10, 50, 30}
# print(my_set)
#
# popped = my_set.pop()  # Removes and returns a random element
# print("Popped:", popped, "Remaining:", my_set)
#
# # Set Operations
# # Python sets support mathematical operations like union, intersection, difference, symmetric difference.
#
# A = {1, 2, 3, 4}
# B = {3, 4, 5, 6}
#
# print("Union:", A | B)         # {1, 2, 3, 4, 5, 6} -combination of both sets
# print("Intersection:", A & B)  # {3, 4} -common in both sets
# print("Difference:", A - B)    # {1, 2} -remaining elements of set A
# print("Symmetric Difference:", A ^ B)  # {1, 2, 5, 6} -remaining elements of A and B
#
# # Membership Test
# A = {10, 20, 30}
# print(10 in A)   # True
# print(50 in A)   # False
#
# # Use Case Example: Removing duplicates from a list
# nums = [1, 2, 2, 3, 4, 4, 5]
# unique_nums = list(set(nums))
# print(unique_nums)   # [1, 2, 3, 4, 5]
#
# ##########################################################################################
# ## frozenset
# """
#     -key: frozenset()
#     -A frozenset is just like a set, but immutable:
#     -Once created, you cannot add or remove elements.
#     -It still ensures unique elements.
#     -It supports set operations (union, intersection, etc.).
#     -It can be used as a key in dictionaries or an element of another set (since it’s hashable).
# """
# # Empty frozenset
# empty_fs = frozenset()
# print(empty_fs)        # frozenset()
# print(type(empty_fs))  # <class 'frozenset'>
#
#
# fs = frozenset([1, 2, 3])
# print(type(fs))  # Output: <class 'frozenset'>
#
# # From a list
# fs = frozenset([1, 2, 3, 2, 4])
# print(fs)       # frozenset({1, 2, 3, 4})
#
# # From a string
# fs2 = frozenset("hello")
# print(fs2)      # frozenset({'o', 'l', 'e', 'h'}) → unordered & unique
#
# # Operations on frozenset
# A = frozenset([1, 2, 3, 4])
# B = frozenset([3, 4, 5, 6])
# print("Union:", A | B)         # frozenset({1, 2, 3, 4, 5, 6})
# print("Intersection:", A & B)  # frozenset({3, 4})
# print("Difference:", A - B)    # frozenset({1, 2})
# print("Symmetric Diff:", A ^ B)     # frozenset({1, 2, 5, 6})
#
# # Not Allowed with frozenset
# fs = frozenset([10, 20, 30])
# # These will cause an error:
# # fs.add(40)    # AttributeError: 'frozenset' object has no attribute 'add'
# # fs.remove(20)   # AttributeError: 'frozenset' object has no attribute 'remove'
#
# # Use Case Example
# # Suppose you want a set of sets (normally not possible because sets are mutable and unhashable):
# A = frozenset([1, 2])
# B = frozenset([3, 4])
#
# set_of_sets = {A, B}
# print(set_of_sets)   # {frozenset({1, 2}), frozenset({3, 4})}
#
# '''
# In short:
#     set = mutable, cannot be used as dict keys.
#     frozenset = immutable, can be used as dict keys or inside sets.
# '''
#
#
# import os, re
# import requests
# import subprocess as sp
#
# password = 'sitindia123'
# modules = {'SSH':['PASS'], 'Libs':['PASS'], 'Python3':['PASS'], 'Pip':['PASS'], 'PythonPackages':['PASS'],
#            'Pycharm':['PASS'], 'Chrome':['PASS'], 'ChromeAutoUpdate':['PASS'], 'ChromeDriver':['PASS'], 'NetworkManager':['PASS'],
#            'DHCP':['PASS'], 'TeamViewer':['PASS'], 'Webmin':['PASS'], 'Firewall':['PASS'], 'Apache':['PASS'],
#            'Static IP':['PASS'], 'Zeroconf':['PASS'], 'Vlan Interface':['PASS'], 'NAT':['PASS'], 'Git-Notes':['PASS'],
#            'AutoLogin':['PASS'], 'Generate_Passwd_Script':['PASS'], 'TFTPServer':['PASS'], 'TFTPClient':['PASS'],
#            'FTP':['PASS'], 'FILES':['PASS'], 'ARPScan': ['PASS'], 'NPING': ['PASS'], 'IGMPv2':['PASS']}
#
# def get_requests(url):
#     global status
#     try:
#         req = requests.get(url, stream=True)
#     except requests.exceptions.RequestException:
#         print(f"FAILED to download Selenium Chrome driver due to Invalid URL: {url}")
#         modules['ChromeDriver'][0] = "FAIL"
#         modules['ChromeDriver'].append(f"FAILED to download Selenium Chrome driver due to Invalid URL: {url}")
#         status = False
#     except ConnectionError:
#         print("FAILED to download Selenium Chrome driver due to Connection refused by the server")
#         modules['ChromeDriver'][0] = "FAIL"
#         modules['ChromeDriver'].append("FAILED to download Selenium Chrome driver due to Connection refused by the server")
#         status = False
#     except Exception as e:
#         print(f"FAILED to download Selenium Chrome driver due to Exception: {e}")
#         modules['ChromeDriver'][0] = "FAIL"
#         modules['ChromeDriver'].append(f"FAILED to download Selenium Chrome driver due to Exception: {e}")
#         status = False
#     else:
#         return req
#
# # Install Google Chrome
# chrome_ver = sp.getoutput(f"echo {password}|sudo -S google-chrome -version")
# if "command not found" in chrome_ver:
#     print("Installing Google Chrome")
#     url = 'https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb'
#     os.system(f"echo {password}|sudo -S wget {url}")
#     os.system(f"echo {password}|sudo -S apt install -y ./google-chrome-stable_current_amd64.deb")
#     # Get Google Chrome version
#     chrome_ver = sp.getoutput(f"echo {password}|sudo -S google-chrome -version")
#     if "command not found" in chrome_ver:
#         print("FAILED to install Google Chrome")
#         modules['Chrome'][0] = "FAIL"
#         modules['Chrome'].append("FAILED to install Google Chrome")
#         modules['ChromeDriver'][0] = "FAIL"
#         modules['ChromeDriver'].append("FAILED to install Google Chrome")
#         status = False
#     else:
#         print("Installed Google Chrome successfully")
#         print("Disabling Google Chrome auto-update")
#         if os.path.exists("/etc/apt/sources.list.d/google-chrome.list"):
#             with open("/etc/apt/sources.list.d/google-chrome.list") as fname:
#                 data = fname.readlines()
#             for index, line in enumerate(data):
#                 if line.startswith('deb'):
#                     line = '#' + line
#                     data[index] = line
#                     break
#             with open("/etc/apt/sources.list.d/google-chrome.list", mode='w', encoding='utf-8') as fname:
#                 fname.writelines(data)
#             # Verify the changes
#             auto_update_disabled = sp.getoutput(
#                 f"echo {password}|sudo -S cat /etc/apt/sources.list.d/google-chrome.list")
#             if not "#deb" in auto_update_disabled:
#                 print("FAILED to disable Google Chrome Auto-Update")
#                 modules['ChromeAutoUpdate'][0] = "FAIL"
#                 modules['ChromeAutoUpdate'].append("FAILED to disable Google Chrome Auto-Update")
#                 status = False
#         else:
#             print(
#                 "FAILED to disable Google Chrome Auto-Update since the file /etc/apt/sources.list.d/google-chrome.list "
#                 "doesn't exists")
#             modules['ChromeAutoUpdate'][0] = "FAIL"
#             modules['ChromeAutoUpdate'].append("FAILED to disable Google Chrome Auto-Update since the file "
#                                                "/etc/apt/sources.list.d/google-chrome.list doesn't exists")
#             status = False
#
# # Download chrome driver for selenium
# if modules['Chrome'][0] == 'PASS':
#     # Get Google Chrome version
#     chrome_ver = sp.getoutput(f"echo {password}|sudo -S google-chrome -version")
#     url = "https://chromedriver.chromium.org/downloads"
#     req = get_requests(url)
#     if req.status_code == 200:
#         match = re.search(r'\d+.0', chrome_ver)
#         if match:
#             chrome_ver = match.group()
#             if int(chrome_ver[:-2]) < 115:
#                 print("Chrome version lesser than 115")
#                 match = re.search('ChromeDriver ' + chrome_ver + '(.\d+.\d+)', req.text)
#                 if match:
#                     url = "https://chromedriver.storage.googleapis.com/" + chrome_ver + match.group(1) + \
#                           "/chromedriver_linux64.zip"
#                     req = get_requests(url)
#                     if req.status_code == 200:
#                         print(f"Downloading Chrome driver chromedriver_linux64.zip from {url}")
#                         file = "chromedriver_linux64.zip"
#                         with open(file, "wb") as fname:
#                             for content in req.iter_content(chunk_size=1024):
#                                 if content:
#                                     fname.write(content)
#                         if 'chromedriver_linux64.zip' in os.listdir():
#                             os.system(f"echo {password}|sudo -S unzip chromedriver_linux64.zip")
#                             os.system(f"echo {password}|sudo -S mv chromedriver /usr/bin/")
#                             os.system(f"echo {password}|sudo -S chmod +x /usr/bin/chromedriver")
#                             if not 'chromedriver' in os.listdir('/usr/bin/'):
#                                 print("FAILED to copy Selenium Chrome driver into /usr/bin after downloading")
#                                 modules['ChromeDriver'][0] = "FAIL"
#                                 modules['ChromeDriver'].append("FAILED to download Selenium Chrome driver")
#                                 status = False
#                         else:
#                             print("FAILED to download Selenium Chrome driver")
#                             modules['ChromeDriver'][0] = "FAIL"
#                             modules['ChromeDriver'].append("FAILED to download Selenium Chrome driver")
#                             status = False
#                     else:
#                         print("FAILED to download Selenium Chrome driver")
#                         modules['ChromeDriver'][0] = "FAIL"
#                         modules['ChromeDriver'].append("FAILED to download Selenium Chrome driver")
#                         status = False
#                 else:
#                     print("FAILED to download Selenium Chrome driver")
#                     modules['ChromeDriver'][0] = "FAIL"
#                     modules['ChromeDriver'].append("FAILED to download Selenium Chrome driver")
#                     status = False
#             else:
#                 print("Chrome version greater than 115")
#                 url = "https://googlechromelabs.github.io/chrome-for-testing/known-good-versions.json"
#                 req = get_requests(url)
#                 if req.status_code == 200:
#                     match = re.findall(r'\{"version":"' + chrome_ver + '(.\d+.\d+)"', req.text)
#                     if match:
#                         url = "https://storage.googleapis.com/chrome-for-testing-public/" + chrome_ver + match[
#                             -1] + "/linux64/chromedriver-linux64.zip"
#                         req = get_requests(url)
#                         if req.status_code == 200:
#                             print(f"Downloading Chrome driver chromedriver_linux64.zip from {url}")
#                             file = "chromedriver_linux64.zip"
#                             with open(file, "wb") as fname:
#                                 for content in req.iter_content(chunk_size=1024):
#                                     if content:
#                                         fname.write(content)
#                             if 'chromedriver_linux64.zip' in os.listdir():
#                                 os.system(f"echo {password}|sudo -S unzip chromedriver_linux64.zip")
#                                 os.system(f"echo {password}|sudo -S cp ./chromedriver-linux64/chromedriver /usr/bin/")
#                                 os.system(f"echo {password}|sudo -S chmod +x /usr/bin/chromedriver")
#                                 if not 'chromedriver' in os.listdir('/usr/bin/'):
#                                     print("FAILED to copy Selenium Chrome driver into /usr/bin after downloading")
#                                     modules['ChromeDriver'][0] = "FAIL"
#                                     modules['ChromeDriver'].append("FAILED to download Selenium Chrome driver")
#                                     status = False
#                             else:
#                                 print("FAILED to download Selenium Chrome driver")
#                                 modules['ChromeDriver'][0] = "FAIL"
#                                 modules['ChromeDriver'].append("FAILED to download Selenium Chrome driver")
#                                 status = False
#                         else:
#                             print("FAILED to download Selenium Chrome driver")
#                             modules['ChromeDriver'][0] = "FAIL"
#                             modules['ChromeDriver'].append("FAILED to download Selenium Chrome driver")
#                             status = False
#                     else:
#                         print("FAILED to get last known release version for chrome driver")
#                         modules['ChromeDriver'][0] = "FAIL"
#                         modules['ChromeDriver'].append("FAILED to get last known release version for chrome driver")
#                         status = False
#                 else:
#                     print("FAILED to get all release versions for chrome driver")
#                     modules['ChromeDriver'][0] = "FAIL"
#                     modules['ChromeDriver'].append("FAILED to get all release versions for chrome driver")
#                     status = False
#         else:
#             print("FAILED to download Selenium Chrome driver")
#             modules['ChromeDriver'][0] = "FAIL"
#             modules['ChromeDriver'].append("FAILED to download Selenium Chrome driver")
#             status = False
#
##################################################################################################################
# ## factory reset AP
# import paramiko
# import time
# device_ip_list = ["10.110.219.87", "10.110.219.88", "10.110.219.89", "10.110.219.90",
#                   "10.110.219.91", "10.110.219.92", "10.110.219.93", "10.110.219.94",
#                   "10.110.219.95", "10.110.219.96", "10.110.219.139", "10.110.219.137",
#                   "10.110.219.114", "10.110.219.215", "10.110.219.241"]
#
# for device_ip in device_ip_list:
#     ssh_client = paramiko.SSHClient()
#     ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#     try:
#         ssh_client.connect(hostname=device_ip, username="admin", password="admin")
#         print("Executing command: delete config")
#         stdin, stdout, stderr = ssh_client.exec_command("delete config")
#         stdin.write('y')
#         stdin.write('\n')
#         print(f"PASS--Factory reset done for AP: {device_ip}")
#         time.sleep(2)
#     except Exception as e:
#         ssh_client.connect(hostname=device_ip, username="admin", password="sitindia123")
#         print("Executing command: delete config")
#         stdin, stdout, stderr = ssh_client.exec_command("delete config")
#         stdin.write('y')
#         stdin.write('\n')
#         print(f"PASS--Factory reset done for AP: {device_ip}")
#         time.sleep(2)
#     except:
#         print(f"FAIL--Factory reset failed for AP: {device_ip}")
##################################################################################################################
import copy

from selenium.common import NoSuchElementException
# text = """
# vlc        2016 sitindia   22u  IPv4  42374      0t0  UDP 192.168.82.1:35752->226.0.0.5:5004
# vlc        2016 sitindia   26u  IPv4  42377      0t0  UDP 192.168.82.1:35753->226.0.0.5:5005
# vlc       40057 sitindia    6u  IPv4 561118      0t0  UDP 192.168.82.1:47066->226.0.0.20:5020
# vlc       40057 sitindia    7u  IPv4 561121      0t0  UDP 192.168.82.1:47067->226.0.0.20:5021
# """
#
# text = """
# vlc       6529 sitindia    6u  IPv4  53671      0t0  UDP 226.0.0.20:5020
# """
#
# sender = False
# def parse_lsof_lines(text):
#     results = []
#     lines = text.strip().splitlines()
#
#     for line in lines:
#         parts = line.split()
#
#         if sender:
#             process, pid, user, fd, net_type, inode, size, proto = parts[:8]
#             connection = parts[8]
#             src, dst = connection.split("->")
#             src_ip, src_port = src.split(":")
#             dst_ip, dst_port = dst.split(":")
#
#             entry = {"process": process, "pid": pid, "user": user, "fd": fd, "type": net_type, "inode": inode,
#                      "size": size, "protocol": proto, "src_ip": src_ip, "src_port": src_port, "dst_ip": dst_ip,
#                      "dst_port": dst_port}
#         else:
#             process, pid, user, fd, net_type, inode, size, proto = parts[:8]
#             connection = parts[8]
#             src_ip, src_port = connection.split(":")
#
#             entry = {"process": process, "pid": pid, "user": user, "fd": fd, "type": net_type, "inode": inode,
#                      "size": size, "protocol": proto, "src_ip": src_ip, "src_port": src_port}
#
#         results.append(entry)
#     return results
#
#
# parsed = parse_lsof_lines(text)
# print(parsed)
#########################################################################################################

# youtube traffic test script
# import sys
# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.common.exceptions import WebDriverException, TimeoutException
#
#
# def check_url_accessible(url: str, timeout: int = 15) -> bool:
#     try:
#         # Setup Chrome options (headless optional)
#         options = webdriver.ChromeOptions()
#         options.add_argument("--start-maximized")
#         # options.add_argument("--headless")  # uncomment for headless mode
#
#         # Launch browser
#         driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
#         driver.set_page_load_timeout(timeout)
#
#         try:
#             driver.get(url)
#             driver.implicitly_wait(10)
#             print(driver.current_url)
#
#             # If page loads and title exists, assume it's accessible
#             if driver.title:
#                 print(f"[SUCCESS] URL '{url}' is accessible. Page title: {driver.title}")
#                 # return True
#             else:
#                 print(driver.name)
#                 print(f"[WARNING] URL '{url}' loaded but has no title.")
#                 # return True
#
#             driver.find_element(By.XPATH, "//a[@aria-label='Home']//yt-icon//span").click()
#             time.sleep(5)
#
#             search_box = driver.find_element(By.XPATH, "//input[@name='search_query']")
#             search_box.clear()
#             time.sleep(2)
#             search_box.send_keys("tv9 kannada live")
#             time.sleep(2)
#             search_box.send_keys(Keys.ENTER)
#             time.sleep(5)
#
#             driver.find_element(By.XPATH, "//a[@id='video-title' and contains(@title,'TV9 KANNADA NEWS')]").click()
#             time.sleep(120)
#
#         except TimeoutException:
#             print(f"[ERROR] URL '{url}' timed out after {timeout} seconds.")
#             return False
#         finally:
#             driver.quit()
#
#     except WebDriverException as e:
#         print(f"[ERROR] Could not launch Chrome or access URL: {e}")
#         return False
#
#
# if __name__ == "__main__":
#     test_url = "https://www.youtube.com"  # change to your URL
#     result = check_url_accessible(test_url)
#     sys.exit(0 if result else 1)
############################################################################################################
# data = {
#     '2.4 GHz Band': {
#         'Enabled': 'True',
#         'Transmit Power': 'Auto',
#         'Auto-RF': 'True',
#         'Dynamic Channel': 'True',
#         'Auto-RF Disable': 'True',
#         'DCS Trigger': 'False',
#         'Packet Error Rate Disable': 'False',
#         'Channel Utilization Disable': 'False',
#         'Noise Disable': 'False',
#         'Dynamic Power': 'False',
#         'Maximum Transmit Power': '19',
#         'Minimum Transmit Power': '9',
#         'Cellsize Overlap Threshold': '70'
#     },
#     '5 GHz Band': {
#         'Enabled': 'True',
#         'Transmit Power': 'Auto',
#         'Auto-RF': 'True',
#         'Dynamic Channel': 'True',
#         'Auto-RF Disable': 'True',
#         'DCS Trigger': 'False',
#         'Packet Error Rate Disable': 'False',
#         'Channel Utilization Disable': 'False',
#         'Noise Disable': 'False',
#         'Dynamic Power': 'False',
#         'Maximum Transmit Power': '25',
#         'Minimum Transmit Power': '15',
#         'Cellsize Overlap Threshold': '50'
#     },
#     '6 GHz Band': {
#         'Enabled': 'True',
#         'Transmit Power': 'Auto',
#         'Auto-RF': 'True',
#         'Dynamic Channel': 'True',
#         'Auto-RF Disable': 'True',
#         'DCS Trigger': 'False',
#         'Packet Error Rate Disable': 'False',
#         'Channel Utilization Disable': 'False',
#         'Noise Disable': 'False',
#         'Dynamic Power': 'False',
#         'Maximum Transmit Power': '25',
#         'Minimum Transmit Power': '15',
#         'Cellsize Overlap Threshold': '70'
#     }
# }
#
# # Target updates
# updates = {
#     '2.4 GHz Band': {
#         'Transmit Power': '10',
#         'DCS Trigger': 'True',
#         'Packet Error Rate Disable': 'True',
#         'Channel Utilization Disable': 'True',
#         'Noise Disable': 'True',
#         'Dynamic Power': 'True',
#         'Maximum Transmit Power': '30',
#         'Minimum Transmit Power': '8',
#         'Cellsize Overlap Threshold': '50'
#     },
#     '5 GHz Band': {
#         'Transmit Power': '18',
#         'DCS Trigger': 'True',
#         'Packet Error Rate Disable': 'True',
#         'Channel Utilization Disable': 'True',
#         'Noise Disable': 'True',
#         'Dynamic Power': 'True',
#         'Maximum Transmit Power': '30',
#         'Minimum Transmit Power': '8'
#     },
#     '6 GHz Band': {
#         'DCS Trigger': 'True',
#         'Packet Error Rate Disable': 'True',
#         'Channel Utilization Disable': 'True',
#         'Noise Disable': 'True',
#         'Dynamic Power': 'True',
#         'Maximum Transmit Power': '30',
#         'Minimum Transmit Power': '8',
#         'Cellsize Overlap Threshold': '50'
#     }
# }
#
# # Apply updates
# for band, values in updates.items():
#     data[band].update(values)
#
# print(data)
#
############################################################################################################
# import re
#
# output = """
# IP Multicast Routing Table
# --------------------------
# Route Flags S: SPT Bit W: Wild Card Bit R: RPT Bit
# IIF State P: Pruned F: Forwarding A: Graft Ack Pending
# Timers: Uptime/Expires
# Interface State: Interface, State/Mode
#
# PIM Multicast Routing Table For Component 1
#
# Total number of Multicast Routes is 3
#
# (192.168.82.1,226.0.0.20) ,00:11:37/17:36:44
#   Incoming Interface : vlan852 ,RPF nbr : NULL ,Route Flags : S
#   Outgoing InterfaceList :
#     vlan854, Forwarding/Sparse ,00:10:17/---
#
# (*, 226.0.0.20) ,00:10:17/--- ,RP : 192.168.82.150
#   Incoming Interface : vlan852 ,RPF nbr : NULL ,Route Flags : WR
#   Outgoing InterfaceList :
#     vlan854, Forwarding/Sparse ,00:10:17/---
#
# (*, 226.0.0.6) ,08:20:05/--- ,RP : 192.168.82.150
#   Incoming Interface : vlan852 ,RPF nbr : NULL ,Route Flags : WR
#   Outgoing InterfaceList :
#     vlan854, Forwarding/Sparse ,08:20:05/---
#
# (192.168.83.1,227.0.0.7) ,08:20:07/02:37:18
#   Incoming Interface : vlan853 ,RPF nbr : NULL ,Route Flags : S
#   Outgoing InterfaceList :
#     vlan855, Forwarding/Sparse ,08:20:05/---
#
# (*, 227.0.0.7) ,08:20:05/--- ,RP : 192.168.83.150
#   Incoming Interface : vlan853 ,RPF nbr : NULL ,Route Flags : WR
#   Outgoing InterfaceList :
#     vlan855, Forwarding/Sparse ,08:20:05/---
#     """
#
# entries = []
# lines = output.splitlines()
#
# current = {}
#
# for line in lines:
#     line = line.strip()
#
#     # Match multicast entry like (192.168.82.1,226.0.0.20)
#     m = re.match(r"\(([^)]+)\)", line)
#     if m:
#         # Save previous entry
#         if current:
#             entries.append(current)
#             current = {}
#
#         current['multicase-ip'] = f"({m.group(1)})"
#
#         # Extract RP if present
#         rp_match = re.search(r"RP\s*:\s*([\d\.]+)", line)
#         if rp_match:
#             current['RP'] = rp_match.group(1)
#
#     # Match Outgoing InterfaceList
#     if "Outgoing InterfaceList" in line:
#         continue
#
#     iface_match = re.match(r"(vlan\d+)", line)
#     if iface_match and 'Outgoing InterfaceList' not in current:
#         current['Outgoing InterfaceList'] = iface_match.group(1)
#
# # append last entry
# if current:
#     entries.append(current)
#
# print(entries)
# print()
# # for e in entries:
# #     print(e)
# # values to validate
# validate_values = [
#     {'multicase-ip': '(192.168.82.1,226.0.0.20)', 'Outgoing InterfaceList': 'vlan854'},
#     {'multicase-ip': '(*, 226.0.0.20)', 'RP': '192.168.82.150', 'Outgoing InterfaceList': 'vlan854'}
# ]
#
# for check in validate_values:
#     found = any(all(item.get(k) == v for k, v in check.items()) for item in entries)
#
#     if found:
#         print(f"{check} -> VALIDATED")
#     else:
#         print(f"{check} -> NOT FOUND")
#####################################################################################
#
# import re
# output = """
# IGMP is globally enabled
#
# I - Include Mode,  E - Exclude Mode
# S - Static Mbr,    D - Dynamic Mbr
#
# GroupAddress    Flg Iface        UpTime           ExpiryTime       LastReporter
# --------------- --- ------------ ---------------- ---------------- ---------------
# 226.0.0.6       D   vlan854      [0d 07:03:19.24] [0d 00:03:34.42] 192.168.84.47
# 226.0.0.20      D   vlan854      [0d 00:01:21.07] [0d 00:03:05.84] 192.168.84.23
# 239.255.255.250 D   vlan854      [0d 06:50:42.39] [0d 00:03:33.11] 192.168.84.47
# 227.0.0.7       D   vlan855      [0d 07:02:55.45] [0d 00:03:30.58] 192.168.85.42
# 239.255.102.18  D   vlan855      [0d 07:02:48.45] [0d 00:03:28.59] 192.168.85.42
# """
#
# entries = []
# for line in output.splitlines():
#     line = line.strip()
#     # Match data rows starting with IP
#     if re.match(r"\d+\.\d+\.\d+\.\d+", line):
#         parts = line.split()
#         entry = {
#             "GroupAddress": parts[0],
#             "Flg": parts[1],
#             "Iface": parts[2],
#             "UpTime": parts[3] + " " + parts[4],
#             "ExpiryTime": parts[5] + " " + parts[6],
#             "LastReporter": parts[7]
#         }
#         entries.append(entry)
# print(entries)
# wired_854 = '192.168.84.50'
# for check in entries:
#     if check['LastReporter'] == wired_854:
#         print("Pass")
#         break
# else:
#     print("Fail")

#########################################################################################################
# import re
#
# output = """
# IGMP is globally enabled
#
# I - Include Mode,  E - Exclude Mode
# S - Static Mbr,    D - Dynamic Mbr
#
# GroupAddress    Flg Iface        UpTime           ExpiryTime       LastReporter
#
# --------------- --- ------------ ---------------- ---------------- -------------
# --
# 226.0.0.20      D   vlan854      [0d 00:04:10.16] [0d 00:04:08.90] 192.168.84.23
#
# 239.255.255.250 D   vlan854      [12d 22:02:43.35][0d 00:04:04.94] 192.168.84.16
#
# 227.0.0.7       D   vlan855      [12d 19:12:33.73][0d 00:02:42.68] 192.168.85.4
# 2
# 239.255.102.18  D   vlan855      [12d 20:03:52.21][0d 00:02:47.66] 192.168.85.42
#
# """
#
# entries = []
#
# pattern = re.compile(
#     r"(\d+\.\d+\.\d+\.\d+)\s+"      # GroupAddress
#     r"(\w)\s+"                     # Flg
#     r"(\w+)\s+"                    # Iface
#     r"\[([^\]]+)\]\s*"             # UpTime
#     r"\[([^\]]+)\]\s+"             # ExpiryTime
#     r"(\d+\.\d+\.\d+\.\d+)"        # LastReporter
# )
#
# for line in output.splitlines():
#     line = line.strip()
#     match = pattern.match(line)
#     if match:
#         entry = {
#             "GroupAddress": match.group(1),
#             "Flg": match.group(2),
#             "Iface": match.group(3),
#             "UpTime": match.group(4),
#             "ExpiryTime": match.group(5),
#             "LastReporter": match.group(6),
#         }
#         entries.append(entry)
#
# print(entries)
#
# wired_854 = '192.168.84.23'
# for check in entries:
#     print(check)
#     if check['LastReporter'] == wired_854:
#         print("Pass")
#         break
# else:
#     print("Fail")
##################################################################################################
# output = """
# eth0: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
#         inet 192.168.50.5  netmask 255.255.255.0  broadcast 192.168.50.255
#         inet6 fe80::68d7:f152:2484:8bc5  prefixlen 64  scopeid 0x20<link>
#         ether d8:3a:dd:bb:df:cb  txqueuelen 1000  (Ethernet)
#         RX packets 341660  bytes 15951854 (15.2 MiB)
#         RX errors 0  dropped 63  overruns 0  frame 0
#         TX packets 12169  bytes 1454385 (1.3 MiB)
#         TX errors 0  dropped 161 overruns 0  carrier 0  collisions 0
#         device interrupt 106
#
# eth1: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
#         inet 172.30.1.130  netmask 255.255.255.0  broadcast 172.30.1.255
#         inet6 fe80::e478:2752:753c:c442  prefixlen 64  scopeid 0x20<link>
#         ether 00:e0:4c:88:86:bc  txqueuelen 1000  (Ethernet)
#         RX packets 945065  bytes 89109385 (84.9 MiB)
#         RX errors 0  dropped 0  overruns 0  frame 0
#         TX packets 5479  bytes 812903 (793.8 KiB)
#         TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0
#
# lo: flags=73<UP,LOOPBACK,RUNNING>  mtu 65536
#         inet 127.0.0.1  netmask 255.0.0.0
#         inet6 ::1  prefixlen 128  scopeid 0x10<host>
#         loop  txqueuelen 1000  (Local Loopback)
#         RX packets 3884  bytes 402805 (393.3 KiB)
#         RX errors 0  dropped 0  overruns 0  frame 0
#         TX packets 3884  bytes 402805 (393.3 KiB)
#         TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0
#
# """
# import re
#
# blocks = re.split(r'\n(?=\S)', output.strip())
#
# for block in blocks:
#     iface = block.splitlines()[0].split(':')[0]
#     inet_match = re.search(r'\binet\s+(\d+\.\d+\.\d+\.\d+)', block)
#     ip = inet_match.group(1) if inet_match else None
#
#     if ip not in ["127.0.0.1"] and (ip is None or not ip.startswith("172.30.")):
#         print(iface)
#     else:
#         print("No interface found")
###########################################################################################
# sta_information = """
# Name                   : Wi-Fi
# Description            : Intel(R) Wi-Fi 6E AX211 160MHz
# GUID                   : 70bd2cc8-e8fa-4f77-89b8-54c1417068bb
# Physical address       : a0:80:69:e1:40:ec
# State                  : connected
# SSID                   : Test_sanity_wpa2_psk
# BSSID               : fc:11:65:dd:99:c6
# Network type           : Infrastructure
# Radio type             : 802.11ax
# Authentication         : WPA2-Personal
# Cipher                 : CCMP
# Connection mode        : Profile
# Channel                : 161
# Receive rate (Mbps)    : 287
# Transmit rate (Mbps)   : 287
# Signal                 : 99%
# Profile                : Test_sanity_wpa2_psk
# Hosted network status  : Not available
# """
#
# wifi_info = {}
# for line in sta_information.splitlines():
#     if ":" not in line:
#         continue
#     try:
#         key, value = line.split(":", 1)
#         if "BSSID" in key.strip():
#             bssid_key = key.strip()
#             wifi_info[bssid_key] = value.strip()
#         else:
#             wifi_info[key.strip()] = value.strip()
#     except Exception:
#         continue  # Never crash on bad formatting
#
# # Extract AP BSSID safely
# ap_bssid = wifi_info.get(bssid_key)
# print(ap_bssid)
#
#################################################################
# import re
# import time
# import traceback
#
# def _cli_show_application_stats():
#     try:
#         out = """
#             Applications Count = 26
#             Application Statistics for All Applications
#             ================================================================================
#             Protocol or             TX           TX         RX            RX
#             Application           Packets       Bytes     Packets        Bytes
#             -------------------------------------------------------------------------------------
#              Other                     144535        199407348     14492         4182752
#              Bing.com (formerly        124           130850        52            8708
#              Dynamic Host Config       354           116225        282           92958
#              Domain Name Service       43            4903          69            15449
#              EndPoint Mapper           107           12892         123           10796
#              File Transfer Proto       154           13922         153           13231
#              Google Generic            115           23115         0             0
#         """
#         time.sleep(1)
#         print(out)
#         output = out.strip().split("\n")
#         print(output)
#         app_stats = []
#         # 7.2 removed Productivity Index and Risk columns
#         if any("Productivity" in line for line in output[:6]):
#             header_line = (
#                 "Protocol", "Productivity Index", "Risk", "Tx Packets", "Tx Bytes", "Rx Packets", "Rx Bytes")
#         else:
#             header_line = ("Protocol", "Tx Packets", "Tx Bytes", "Rx Packets", "Rx Bytes")
#         for i in range(6, len(output)):
#             temp_dict = {}
#             line_out = re.split(r'\s{2,}', output[i].strip())
#             for header, value in (zip(header_line, line_out)):
#                 if value != None or value != '' and header != None:
#                     temp_dict[str(header)] = str(value)
#             app_stats.append(temp_dict)
#         print("The value to be returned is %s " % app_stats)
#         length_of_app_stats_element = len(app_stats[0])
#         print("App stats each dictionary length %s " % length_of_app_stats_element)
#         # This will filter out any value which is less than length of 6
#         result = list(filter(lambda x: len(x) == length_of_app_stats_element, app_stats))
#         print("App stats output %s " % result)
#         return result
#     except Exception as e:
#         print(f"An exception of type {type(e).__name__} occurred")
#         print(traceback.format_exc())
#         raise
#
# print(_cli_show_application_stats())
#####################################################################################
# client_dict = {'MAC': None, 'VENDOR': None, 'AGE': None, 'MODE': None, 'STREAM': None, 'SLEEP': None,
#                            'RADIO': None, 'WLAN': None,
#                            'VLAN': None, '802.11-AUTH': None, 'NAME': None, 'SSID': None, 'IPv4': None,
#                            'CAPABILITY': None}
# clients = [{'HostName': 'IN01-CJK3D44', 'User': '', 'MACAddress': 'A0:D3:65:E4:51:5B', 'IPv4Address': '192.168.100.116', 'IPv6Address': 'N/A', 'VLAN-ID': '100', 'SSID': 'Test_Layer3_Filter_WPA3PSK', 'LastDuration': '< 1m', 'RSSI': '-52 dBm', 'SNR': '43 dB', 'Band': '6 GHz', 'Capability': 'axa', '6GHzCapable': 'Yes', 'Streams': '2', 'GuestAccessType': '-', 'AuthenticationType': '', 'AuthStatus': 'false', 'SessionExpiry': '0d 0h 0m', 'UploadQuota': '0', 'UploadQuotaBalance': '0', 'DownloadQuota': '0', 'DownloadQuotaBalance': '0', 'TotalQuota': '0', 'TotalQuotaBalance': '0', 'RadioID': '3', 'RadioMode': 'axa', 'Manufacturer': 'Intel Corporate', 'OS': 'Linux', 'ClientType': 'Client', 'Upload': '5.6 KB', 'Download': '19.4 KB', 'LastSeen': '28 Jul 2026, 03:42 PM'}]
#
# clientMac = 'A0:D3:65:E4:51:5B'
# for client in clients:
#     if clientMac in (client.get('MACAddress'), client.get('MAC')):
#         mac = client.get('MACAddress') or client.get('MAC')
#         client_dict['MAC'] = mac.replace(':', '-')
#         client_dict['VENDOR'] = client['Manufacturer']
#         client_dict['AGE'] = client['LastDuration']
#         client_dict['MODE'] = client['RadioMode']
#         client_dict['STREAM'] = client['Streams']
#         client_dict['RADIO'] = client['RadioID']
#         client_dict['VLAN'] = client['VLAN-ID']
#         client_dict['AUTHTYPE'] = client['AuthenticationType']
#         client_dict['NAME'] = client['HostName']
#         client_dict['SSID'] = client['SSID']
#         client_dict['IPv4'] = client['IPv4Address']
#         client_dict['IPv6'] = client['IPv6Address']
#         client_dict['CAPABILITY'] = client['Capability']
#         client_dict['BAND'] = client['Band']
#         client_dict['OS'] = client['OS']
#         client_dict['RSSI'] = client['RSSI']
#         client_dict['SNR'] = client['SNR']
#         client_dict['6GHz'] = client['6GHzCapable']
#         print("Connected client info:")
#         print(client_dict)
# else:
#     print(f"Expected client: {clientMac} data not found in cnMaestro clients page")
###########################################################################################################
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.facebook.com/")
driver.implicitly_wait(5)
assert driver.find_element(By.XPATH, "//span[text()='Log in to Facebook']").text == "Log in to Facebook"
