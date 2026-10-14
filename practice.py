# ap_group = [{'mcid': '', 'name': 'Automation_Feature_SSH_Keys', 'description': None,
#              'types': ['Falcon', 'Gambit', 'Sage', 'Lila', 'Thor', 'Jaguar', 'Puma', 'Lion', 'Cheetah'], 'src': {
#         'radio': {'XV3': {'overrides': {'POWER_1': '${XV3_POWER_1=auto}', 'POWER_2': '${XV3_POWER_2=auto}',
#                                         'POWER_3': '${XV3_POWER_3=auto}', 'CHANNEL_1': '${XV3_CHANNEL_1=auto}',
#                                         'CHANNEL_2': '${XV3_CHANNEL_2=auto}', 'CHANNEL_3': '${XV3_CHANNEL_3=auto}',
#                                         'SHUTDOWN_1': '${XV3_SHUTDOWN_1=false}',
#                                         'SHUTDOWN_2': '${XV3_SHUTDOWN_2=false}',
#                                         'SHUTDOWN_3': '${XV3_SHUTDOWN_3=false}',
#                                         'CHANNEL_WIDTH_1': '${XV3_CHANNEL_WIDTH_1=20}',
#                                         'CHANNEL_WIDTH_2': '${XV3_CHANNEL_WIDTH_2=40}',
#                                         'CHANNEL_WIDTH_3': '${XV3_CHANNEL_WIDTH_3=40}'}, 'XV3_radio1_band': '2.4GHz',
#                           'XV3_radio2_band': '${XV3_BAND_2=5GHz}'}, 'XE34': {
#             'overrides': {'POWER_1': '${XE34_POWER_1=auto}', 'POWER_2': '${XE34_POWER_2=auto}',
#                           'POWER_3': '${XE34_POWER_3=auto}', 'CHANNEL_1': '${XE34_CHANNEL_1=auto}',
#                           'CHANNEL_2': '${XE34_CHANNEL_2=auto}', 'CHANNEL_3': '${XE34_CHANNEL_3=auto}',
#                           'SHUTDOWN_1': '${XE34_SHUTDOWN_1=false}', 'SHUTDOWN_2': '${XE34_SHUTDOWN_2=false}',
#                           'SHUTDOWN_3': '${XE34_SHUTDOWN_3=false}', 'CHANNEL_WIDTH_1': '${XE34_CHANNEL_WIDTH_1=20}',
#                           'CHANNEL_WIDTH_2': '${XE34_CHANNEL_WIDTH_2=40}',
#                           'CHANNEL_WIDTH_3': '${XE34_CHANNEL_WIDTH_3=80}'}, 'XE34_radio1_band': '2.4GHz',
#             'XE34_radio2_band': '5GHz', 'XE34_radio3_band': '${XE34_BAND_3=6GHz}'}, 'XE58': {
#             'overrides': {'POWER_1': '${XE58_POWER_1=auto}', 'POWER_2': '${XE58_POWER_2=auto}',
#                           'POWER_3': '${XE58_POWER_3=auto}', 'POWER_4': '${XE58_POWER_4=auto}',
#                           'POWER_5': '${XE58_POWER_5=auto}', 'CHANNEL_1': '${XE58_CHANNEL_1=auto}',
#                           'CHANNEL_2': '${XE58_CHANNEL_2=auto}', 'CHANNEL_3': '${XE58_CHANNEL_3=auto}',
#                           'CHANNEL_4': '${XE58_CHANNEL_4=auto}', 'CHANNEL_5': '${XE58_CHANNEL_5=auto}',
#                           'SHUTDOWN_1': '${XE58_SHUTDOWN_1=false}', 'SHUTDOWN_2': '${XE58_SHUTDOWN_2=false}',
#                           'SHUTDOWN_3': '${XE58_SHUTDOWN_3=false}', 'SHUTDOWN_4': '${XE58_SHUTDOWN_4=false}',
#                           'SHUTDOWN_5': '${XE58_SHUTDOWN_5=false}', 'CHANNEL_WIDTH_1': '${XE58_CHANNEL_WIDTH_1=20}',
#                           'CHANNEL_WIDTH_2': '${XE58_CHANNEL_WIDTH_2=40}',
#                           'CHANNEL_WIDTH_3': '${XE58_CHANNEL_WIDTH_3=80}',
#                           'CHANNEL_WIDTH_4': '${XE58_CHANNEL_WIDTH_4=40}',
#                           'CHANNEL_WIDTH_5': '${XE58_CHANNEL_WIDTH_5=40}'}, 'XE58_radio1_band': '2.4GHz',
#             'XE58_radio2_band': '${XE58_BAND_2=5GHz}', 'XE58_radio3_band': '${XE58_BAND_3=6GHz}',
#             'XE58_radio4_band': '${XE58_BAND_4=lion_sbs_mode}', 'XE58_radio5_band': '5GHz'}, 'radio': [
#             {'id': 1, 'atf': False, 'cbs': True, 'drf': True, 'ocs': False, 'mode': 'default',
#              'power': '${POWER_1=auto}', 'cbs_csa': False, 'channel': '${CHANNEL_1=auto}', 'shortgi': True,
#              'shutdown': '${SHUTDOWN_1=false}', 'autoRFMode': 'channel', 'drf_samples': 3, 'cbs_resttime': 6,
#              'cbs_waittime': 2, 'channel_list': 'all-channels', 'drf_interval': 0, 'cbs_dwellrest': 100,
#              'channel_width': '${CHANNEL_WIDTH_1=20}', 'drf_cs_method': 'interference', 'cbs_dwellsplit': 25,
#              'drf_dwell_time': 50, 'beacon_interval': 100, 'eroam_threshold': 15, 'drf_cu_threshold': 25,
#              'non_unicast_rate': 'highest-basic', 'acs_poll_interval': '06:00', 'drf_chan_holdtime': 1440,
#              'drf_dynamic_power': False, 'drf_snr_weightage': 60,
#              'unicast_rate_list': '1b 2b 5.5b 11b 6 9 12 18 24 36 48 54', 'drf_noise_threshold': '-70',
#              'drf_num_per_samples': '40', 'drf_chload_weightage': 40, 'drf_num_noise_samples': '40',
#              'drf_dynamic_power_mode': 'by-channel', 'drf_per_channel_switch': 'off', 'drf_effciency_weightage': 60,
#              'drf_congestion_threshold': '70', 'drf_noise_channel_switch': 'off', 'drf_dynamic_power_min_nbrs': 2,
#              'drf_num_congestion_samples': '100', 'drf_acceptance_per_threshold': '30',
#              'drf_dynamic_power_min_tx_pow': 10, 'drf_congestion_channel_switch': 'off',
#              'drf_dynamic_power_cellsize_overlap_threshold': 50},
#             {'id': 2, 'atf': False, 'cbs': True, 'drf': True, 'ocs': False, 'mode': 'default',
#              'power': '${POWER_2=auto}', 'cbs_csa': False, 'channel': '${CHANNEL_2=auto}', 'shortgi': True,
#              'shutdown': '${SHUTDOWN_2=false}', 'autoRFMode': 'channel', 'drf_samples': 3, 'cbs_resttime': 6,
#              'cbs_waittime': 2, 'channel_list': 'all-channels', 'drf_interval': 0, 'cbs_dwellrest': 100,
#              'channel_width': '${CHANNEL_WIDTH_2=40}', 'drf_cs_method': 'interference', 'cbs_dwellsplit': 25,
#              'drf_dwell_time': 50, 'beacon_interval': 100, 'eroam_threshold': 15, 'drf_cu_threshold': 25,
#              'non_unicast_rate': 'lowest-basic', 'acs_poll_interval': '06:00', 'drf_chan_holdtime': 1440,
#              'drf_dynamic_power': False, 'drf_snr_weightage': 60, 'unicast_rate_list': '6b 9 12b 18 24b 36 48 54',
#              'drf_noise_threshold': '-70', 'drf_num_per_samples': '40', 'drf_chload_weightage': 40,
#              'drf_num_noise_samples': '40', 'drf_dynamic_power_mode': 'by-channel', 'drf_per_channel_switch': 'off',
#              'drf_effciency_weightage': 60, 'drf_congestion_threshold': '70', 'drf_noise_channel_switch': 'off',
#              'drf_dynamic_power_min_nbrs': 2, 'drf_num_congestion_samples': '100', 'drf_acceptance_per_threshold': '30',
#              'drf_dynamic_power_min_tx_pow': 10, 'drf_congestion_channel_switch': 'off',
#              'drf_dynamic_power_cellsize_overlap_threshold': 50},
#             {'id': 3, 'atf': False, 'cbs': True, 'drf': True, 'ocs': False, 'mode': 'default',
#              'power': '${POWER_3=auto}', 'cbs_csa': False, 'channel': '${CHANNEL_3=auto}', 'shortgi': True,
#              'shutdown': '${SHUTDOWN_3=false}', 'autoRFMode': 'channel', 'drf_samples': 3, 'cbs_resttime': 6,
#              'cbs_waittime': 2, 'channel_list': 'all-channels', 'drf_interval': 0, 'cbs_dwellrest': 100,
#              'channel_width': '${CHANNEL_WIDTH_3=80}', 'drf_cs_method': 'interference', 'cbs_dwellsplit': 25,
#              'drf_dwell_time': 50, 'beacon_interval': 100, 'eroam_threshold': 15, 'drf_cu_threshold': 25,
#              'non_unicast_rate': 'lowest-basic', 'acs_poll_interval': '06:00', 'drf_chan_holdtime': 1440,
#              'drf_dynamic_power': False, 'drf_snr_weightage': 60, 'unicast_rate_list': '6b 9 12b 18 24b 36 48 54',
#              'drf_noise_threshold': '-70', 'drf_num_per_samples': '40', 'drf_chload_weightage': 40,
#              'drf_num_noise_samples': '40', 'drf_dynamic_power_mode': 'by-channel', 'drf_per_channel_switch': 'off',
#              'drf_effciency_weightage': 60, 'drf_congestion_threshold': '70', 'drf_noise_channel_switch': 'off',
#              'drf_dynamic_power_min_nbrs': 2, 'drf_num_congestion_samples': '100', 'drf_acceptance_per_threshold': '30',
#              'drf_dynamic_power_min_tx_pow': 10, 'drf_congestion_channel_switch': 'off',
#              'drf_dynamic_power_cellsize_overlap_threshold': 50}]},
#         'basic': {'led': True, 'lldp': True, 'poe_out': '0', 'placement': '${PLACEMENT=indoor}', 'country_code': 'US',
#                   'radio_sbs_mode': '${RADIO_SBS_MODE=true}', 'system_location': '${LOCATION=}',
#                   'channels_distribution': True},
#         'l2tpTunnel': {'tunnel_l2gre_mtu': 1460, 'tunnel_l2tp_auth': 'admin:admin', 'tunnel_l2gre_dscp': 0,
#                        'tunnel_l2gre_in_udp': False, 'tunnel_l2tp_created': False, 'tunnel_l2tp_tcp_mss': 1400,
#                        'tunnel_encapsulation': 'off', 'tunnel_l2gre_cambium': False, 'tunnel_l2gre_created': False,
#                        'tunnel_l2gre_tcp_mss': 1410, 'tunnel_l2tp_pmtudisc': True, 'tunnel_l2gre_pmtudisc': True,
#                        'tunnel_l2tp_auth_type': '', 'tunnel_l2tp_mss_clamp': True, 'tunnel_l2gre_mss_clamp': True,
#                        'tunnel_l2tp_remote_host': '0.0.0.0', 'tunnel_l2gre_remote_host': '0.0.0.0'},
#         'pppoe': {'pppoe_server_created': True}}, 'adv': None, 'policies': {'wlan': ['Test_SSH_Keys']},
#              'auto_sync': False, 'shared': False, 'policies_details': {'wlan': [{'name': 'Test_SSH_Keys', 'mcid': '',
#                                                                                  'vars_obj': {'SSID': 'Test_SSH_Keys',
#                                                                                               'SHUTDOWN': 'false',
#                                                                                               'PASSPHRASE': 'sitindia123'},
#                                                                                  'ssid': 'Test_SSH_Keys',
#                                                                                  'mesh_mode': ''}]}, 'deviceCount': 1,
#              'unmanagedCount': 0, 'offlineCount': 0, 'unmanagedOfflineCount': 0, 'outOfSyncCount': 1,
#              'macs': ['B4:A2:5C:E5:36:B7'], 'onlineMacs': ['B4:A2:5C:E5:36:B7'], 'dlTPutR1': 0, 'dlTPutR2': 2.23,
#              'dlTPutR3': 0, 'ulTPutR1': 0, 'ulTPutR2': 0.18, 'ulTPutR3': 0, 'musR1': 0, 'musR2': 2, 'musR3': 0,
#              'rCountR1': 1, 'rCountR2': 1, 'rCountR3': 0}]
# data = {}
# # ssh_key = "ABCD"
# # for profile in ap_group:
# #     if profile.get("name") == "Automation_Feature_SSH_Keys":
# #         data.update({"src": {"management": {"admin_key": ssh_key}}})
# #         break
# # print(data)
#
#
# # adding radius credentials from cnMaestro
# radius_check_box = "true"
# radius_secret = "password"
# radius_server_ip = "10.110.214.176"
# for profile in ap_group:
#     if profile.get("name") == "Automation_Feature_SSH_Keys":
#         data.update({"src": {"management": {"admin_radius": radius_check_box,
#                                             "admin_radius_secret": radius_secret,
#                                             "admin_radius_server": radius_server_ip}}})
# print(data)
############################################################################################
# import pexpect
#
#
# def ssh_login(username, password, ip, valid):
#     ssh_command = f"ssh -o StrictHostKeyChecking=no radius@{ip}"
#
#     # Spawn a child process for the ssh command
#     ssh_session = pexpect.spawn(ssh_command)
#
#     try:
#         # Expect the 'Are you sure you want to continue connecting' prompt and send 'yes'
#         ssh_session.expect("Are you sure you want to continue connecting (yes/no/[fingerprint])? ")
#         ssh_session.sendline("yes")
#
#         # Expect the 'username:' prompt and send the username
#         ssh_session.expect("username:")
#         ssh_session.sendline(username)
#
#         # Expect the 'password:' prompt and send the password
#         ssh_session.expect("password:")
#         ssh_session.sendline(password)
#
#         if valid:
#             # Optional: You may add additional commands to execute after successful login
#             # For example, you can send 'ls' command to list files in the remote directory.
#             ssh_session.expect("(config)#")
#             ssh_session.sendline("show version")
#
#         # Wait for the process to finish (timeout is set to 10 seconds)
#         ssh_session.expect(pexpect.EOF, timeout=10)
#
#         # Print the output of the command (optional)
#         output = ssh_session.before.decode()
#         return True, output
#     except pexpect.exceptions.TIMEOUT:
#         log.error("Timeout occurred while waiting for the command to complete")
#         return False, "Timeout occurred while waiting for the command to complete"
#     except pexpect.exceptions.EOF:
#         log.error("SSH session closed unexpectedly")
#         return False, "SSH session closed unexpectedly"
#     finally:
#         ssh_session.close()
#
# ##############################################################
# def ssh_login(username, password, ip, valid):
#     ssh_command = f"ssh -o StrictHostKeyChecking=no radius@{ip}"
#     # Spawn a child process for the ssh command
#     ssh_session = pexpect.spawn(ssh_command)
#     try:
#         # Expect the 'Are you sure you want to continue connecting' prompt and send 'yes'
#         ssh_session.expect("Are you sure you want to continue connecting (yes/no/[fingerprint])? ", timeout=60)
#         ssh_session.sendline("yes")
#         # Expect the 'username:' prompt and send the username
#         ssh_session.expect("username:", timeout=60)
#         ssh_session.sendline(username)
#         # Expect the 'password:' prompt and send the password
#         ssh_session.expect("password:", timeout=60)
#         ssh_session.sendline(password)
#         if valid:
#             # Optional: You may add additional commands to execute after successful login
#             # For example, you can send 'ls' command to list files in the remote directory.
#             ssh_session.expect("(config)#", timeout=60)
#             ssh_session.sendline("show version")
#         # Wait for the process to finish (timeout is set to 10 seconds)
#         ssh_session.expect(pexpect.EOF, timeout=10)
#         # Print the output of the command (optional)
#         output = ssh_session.before.decode()
#         return True, output
#     except pexpect.exceptions.TIMEOUT:
#         log.error("Timeout occurred while waiting for the command to complete")
#         return False, "Timeout occurred while waiting for the command to complete"
#     except pexpect.exceptions.EOF:
#         log.error("SSH session closed unexpectedly")
#         return False, "SSH session closed unexpectedly"
#     finally:
#         ssh_session.close()
#
# app_list = ['zoom', 'bbc', 'flipkart', 'viber', 'google', 'spotify', 'snapchat', 'twitter', 'ndtv', 'quora', 'yahoo', 'skype', 'paytm', 'wikipedi', 'telegram']
# output_app_list = [{'Protocol': 'bbc.co.uk', 'Productivity Index': '2', 'Risk': '1', 'Tx Packets': '48', 'Tx Bytes': '56686', 'Rx Packets': '21', 'Rx Bytes': '1837'}, {'Protocol': 'Bonjour', 'Productivity Index': '4', 'Risk': '1', 'Tx Packets': '1', 'Tx Bytes': '146', 'Rx Packets': '0', 'Rx Bytes': '0'}, {'Protocol': 'Flipkart', 'Productivity Index': '1', 'Risk': '4', 'Tx Packets': '40', 'Tx Bytes': '47107', 'Rx Packets': '28', 'Rx Bytes': '2226'}, {'Protocol': 'Google', 'Productivity Index': '3', 'Risk': '1', 'Tx Packets': '19', 'Tx Bytes': '16334', 'Rx Packets': '12', 'Rx Bytes': '1408'}, {'Protocol': 'NDTV', 'Productivity Index': '1', 'Risk': '2', 'Tx Packets': '60', 'Tx Bytes': '74003', 'Rx Packets': '26', 'Rx Bytes': '2098'}, {'Protocol': 'Paytm', 'Productivity Index': '2', 'Risk': '3', 'Tx Packets': '52', 'Tx Bytes': '62844', 'Rx Packets': '18', 'Rx Bytes': '1703'}, {'Protocol': 'Quora', 'Productivity Index': '3', 'Risk': '2', 'Tx Packets': '61', 'Tx Bytes': '51004', 'Rx Packets': '24', 'Rx Bytes': '2019'}, {'Protocol': 'Skype', 'Productivity Index': '3', 'Risk': '1', 'Tx Packets': '29', 'Tx Bytes': '28748', 'Rx Packets': '13', 'Rx Bytes': '1390'}, {'Protocol': 'Snapchat', 'Productivity Index': '1', 'Risk': '4', 'Tx Packets': '23', 'Tx Bytes': '26103', 'Rx Packets': '15', 'Rx Bytes': '1554'}, {'Protocol': 'Spotify', 'Productivity Index': '1', 'Risk': '1', 'Tx Packets': '31', 'Tx Bytes': '19498', 'Rx Packets': '24', 'Rx Bytes': '3165'}, {'Protocol': 'SSL', 'Productivity Index': '3', 'Risk': '3', 'Tx Packets': '8', 'Tx Bytes': '320', 'Rx Packets': '8', 'Rx Bytes': '320'}, {'Protocol': 'TeamViewer', 'Productivity Index': '4', 'Risk': '2', 'Tx Packets': '5', 'Tx Bytes': '308', 'Rx Packets': '5', 'Rx Bytes': '332'}, {'Protocol': 'Telegram', 'Productivity Index': '3', 'Risk': '2', 'Tx Packets': '17', 'Tx Bytes': '13543', 'Rx Packets': '13', 'Rx Bytes': '1470'}, {'Protocol': 'Twitter', 'Productivity Index': '3', 'Risk': '4', 'Tx Packets': '46', 'Tx Bytes': '51129', 'Rx Packets': '20', 'Rx Bytes': '2123'}, {'Protocol': 'Viber', 'Productivity Index': '2', 'Risk': '4', 'Tx Packets': '24', 'Tx Bytes': '19280', 'Rx Packets': '15', 'Rx Bytes': '1721'}, {'Protocol': 'Wikipedia', 'Productivity Index': '3', 'Risk': '3', 'Tx Packets': '33', 'Tx Bytes': '31111', 'Rx Packets': '29', 'Rx Bytes': '3034'}, {'Protocol': 'Yahoo', 'Productivity Index': '3', 'Risk': '3', 'Tx Packets': '183', 'Tx Bytes': '243174', 'Rx Packets': '38', 'Rx Bytes': '2731'}, {'Protocol': 'Zoom', 'Productivity Index': '3', 'Risk': '2', 'Tx Packets': '73', 'Tx Bytes': '85908', 'Rx Packets': '37', 'Rx Bytes': '2693'}]
#
# tx_list = []
# for dictionary in output_app_list:
#     for app in app_list:
#         if app in dictionary["Protocol"] or app.capitalize() in dictionary["Protocol"] or app.upper() in dictionary["Protocol"]:
#             tx_list.append(dictionary['Tx Packets'])
# print(tx_list)
# print(len(tx_list))
# ======set filter 1 in wlan 1 level======
# result = device_inst._cli_application_control_wlan_level_filter(action="deny",
#                                                                             command="category-control",
#                                                                             application_list=app_cat_list_deny,
#                                                                             precedence=cat_precedence_deny,
#                                                                             filter=1)
# assert result, "Failed to configure category control filter deny in AP for filter 1"
# log.info("Successfully configured category control filter deny in AP for filter 1")
# result = device_inst._cli_application_control_wlan_level_filter(action="permit",
#                                                                 command="category-control",
#                                                                 application_list=app_cat_list_permit,
#                                                                 precedence=cat_precedence_permit,
#                                                                 filter=1)
# assert result, "Failed to configure category control filter permit in AP for filter 1"
# log.info("Successfully configured category control filter permit in AP for filter 1")
# # ======set filter 2 in wlan 2 level======
# result = device_inst._cli_application_control_wlan_level_filter(action="deny",
#                                                                             command="category-control",
#                                                                             application_list=app_cat_list_deny,
#                                                                             precedence=cat_precedence_deny,
#                                                                             filter=2)
# assert result, "Failed to configure category control filter deny in AP for filter 2"
# log.info("Successfully configured category control filter deny in AP for filter 2")
# result = device_inst._cli_application_control_wlan_level_filter(action="permit",
#                                                                 command="category-control",
#                                                                 application_list=app_cat_list_permit,
#                                                                 precedence=cat_precedence_permit,
#                                                                 filter=2)
# assert result, "Failed to configure category control filter permit in AP for filter 2"
# log.info("Successfully configured category control filter permit in AP for filter 2")
#
#
# log.info(f"Copy {ftp_file_name} to client under /home/testAutomation")
# client_shell_1.send_cmd(f"rm -rf /home/testAutomation/{ftp_file_name}")
# client_shell_1.upload_file(uploadlocalfilepath=ftp_file_path,
#                            uploadremotefilepath=f'/home/testAutomation/{ftp_file_name}')
# # # running ftp download which is blocked on global category
# ftp_command = f'python /home/testAutomation/ftp_download.py {ftp_file_name} {ftp_server_ip}'
# ftp_output = client_shell_1.send_cmd(ftp_command)
# log.debug(ftp_output)
# assert "timed out" in ftp_output and "226 Transfer complete." not in ftp_output, \
#     "Ftp file transfer was successful so failing"
# log.info("Ftp file transfer failed as expected")
#
#
# cmd = f'python /home/testAutomation/https_request_arg.py "{url_cat_list_deny}"'
# log.info("Executing command in Linux client: %s " % cmd)
# category_http_output = client_shell_1.send_cmd(cmd, timeout=600)
# log.info(f"Wireless client output after sending http packets\n{category_http_output}")
# http_script_output = eval(category_http_output)
# log.info(f"Http script output of client \n{http_script_output}")
# value = http_script_output.values()
# # This will check every element matches Fail, It means connection failed
# res = all(ele == "Fail" for ele in value)
# assert res, "1 or more applications accessed in client"
#
# # # sending http packets for ssid 1 in client 1 for category
# cmd = f'python /home/testAutomation/https_request_arg.py "{url_cat_list}"'
# log.info("Executing command in Linux client: %s " % cmd)
# category_http_output = client_shell_2.send_cmd(cmd, timeout=600)
# log.info(f"Wireless client output after sending http packets\n{category_http_output}")
# http_script_output = eval(application_http_output)
# log.info(f"Http script output of client \n{http_script_output}")
# value = http_script_output.values()
# # This will check every element matches Fail, It means connection failed
# res = all(ele == "Fail" for ele in value)
# assert res, "1 or more applications accessed in client"
# log.info("Accessing applications failed in client as expected")
#
# output_app_list = [{'Protocol': 'bbc.co.uk', 'Productivity Index': '2', 'Risk': '1', 'Tx Packets': '49', 'Tx Bytes': '57808', 'Rx Packets': '25', 'Rx Bytes': '2045'}, {'Protocol': 'Bonjour', 'Productivity Index': '4', 'Risk': '1', 'Tx Packets': '1', 'Tx Bytes': '73', 'Rx Packets': '1', 'Rx Bytes': '73'}, {'Protocol': 'Facebook', 'Productivity Index': '2', 'Risk': '1', 'Tx Packets': '33', 'Tx Bytes': '33111', 'Rx Packets': '23', 'Rx Bytes': '2236'}, {'Protocol': 'Flipkart', 'Productivity Index': '1', 'Risk': '4', 'Tx Packets': '39', 'Tx Bytes': '45795', 'Rx Packets': '34', 'Rx Bytes': '2538'}, {'Protocol': 'Google', 'Productivity Index': '3', 'Risk': '1', 'Tx Packets': '20', 'Tx Bytes': '16294', 'Rx Packets': '14', 'Rx Bytes': '1500'}, {'Protocol': 'Hushmail.com', 'Productivity Index': '3', 'Risk': '2', 'Tx Packets': '85', 'Tx Bytes': '96307', 'Rx Packets': '23', 'Rx Bytes': '1982'}, {'Protocol': 'IGMP', 'Productivity Index': '3', 'Risk': '1', 'Tx Packets': '0', 'Tx Bytes': '0', 'Rx Packets': '4', 'Rx Bytes': '128'}, {'Protocol': 'NDTV', 'Productivity Index': '1', 'Risk': '2', 'Tx Packets': '61', 'Tx Bytes': '75032', 'Rx Packets': '25', 'Rx Bytes': '2046'}, {'Protocol': 'Paytm', 'Productivity Index': '2', 'Risk': '3', 'Tx Packets': '52', 'Tx Bytes': '62873', 'Rx Packets': '17', 'Rx Bytes': '1651'}, {'Protocol': 'Quora', 'Productivity Index': '3', 'Risk': '2', 'Tx Packets': '58', 'Tx Bytes': '50831', 'Rx Packets': '29', 'Rx Bytes': '2279'}, {'Protocol': 'Skype', 'Productivity Index': '3', 'Risk': '1', 'Tx Packets': '29', 'Tx Bytes': '28488', 'Rx Packets': '14', 'Rx Bytes': '1430'}, {'Protocol': 'Snapchat', 'Productivity Index': '1', 'Risk': '4', 'Tx Packets': '24', 'Tx Bytes': '26589', 'Rx Packets': '17', 'Rx Bytes': '1658'}, {'Protocol': 'Spotify', 'Productivity Index': '1', 'Risk': '1', 'Tx Packets': '30', 'Tx Bytes': '19758', 'Rx Packets': '22', 'Rx Bytes': '3061'}, {'Protocol': 'SSL', 'Productivity Index': '3', 'Risk': '3', 'Tx Packets': '36', 'Tx Bytes': '12178', 'Rx Packets': '36', 'Rx Bytes': '2491'}, {'Protocol': 'TeamViewer', 'Productivity Index': '4', 'Risk': '2', 'Tx Packets': '9', 'Tx Bytes': '540', 'Rx Packets': '9', 'Rx Bytes': '612'}, {'Protocol': 'Telegram', 'Productivity Index': '3', 'Risk': '2', 'Tx Packets': '17', 'Tx Bytes': '13543', 'Rx Packets': '13', 'Rx Bytes': '1446'}, {'Protocol': 'Twitter', 'Productivity Index': '3', 'Risk': '4', 'Tx Packets': '49', 'Tx Bytes': '56443', 'Rx Packets': '29', 'Rx Bytes': '2591'}, {'Protocol': 'Viber', 'Productivity Index': '2', 'Risk': '4', 'Tx Packets': '23', 'Tx Bytes': '19222', 'Rx Packets': '15', 'Rx Bytes': '1721'}, {'Protocol': 'Waze', 'Productivity Index': '3', 'Risk': '2', 'Tx Packets': '27', 'Tx Bytes': '29636', 'Rx Packets': '17', 'Rx Bytes': '1829'}, {'Protocol': 'WhatsApp', 'Productivity Index': '2', 'Risk': '2', 'Tx Packets': '54', 'Tx Bytes': '66969', 'Rx Packets': '36', 'Rx Bytes': '2750'}, {'Protocol': 'Wikipedia', 'Productivity Index': '3', 'Risk': '3', 'Tx Packets': '34', 'Tx Bytes': '31162', 'Rx Packets': '29', 'Rx Bytes': '3034'}, {'Protocol': 'Yahoo', 'Productivity Index': '3', 'Risk': '3', 'Tx Packets': '194', 'Tx Bytes': '251505', 'Rx Packets': '42', 'Rx Bytes': '2939'}, {'Protocol': 'YouTube', 'Productivity Index': '1', 'Risk': '4', 'Tx Packets': '135', 'Tx Bytes': '165852', 'Rx Packets': '61', 'Rx Bytes': '3969'}, {'Protocol': 'Zoom', 'Productivity Index': '3', 'Risk': '2', 'Tx Packets': '68', 'Tx Bytes': '85624', 'Rx Packets': '32', 'Rx Bytes': '2433'}]
# app_list = ['zoom', 'bbc', 'flipkart', 'viber', 'google', 'spotify', 'snapchat', 'twitter', 'ndtv', 'quora', 'yahoo', 'skype', 'paytm', 'wikipedi', 'telegram', 'facebook', 'whatsapp', 'youtube', 'hushmail', 'waze']
import re
import random

# Tx_packets = []
# apps = []
# for dictionary in output_app_list:
#     for app in app_list:
#         if app in dictionary["Protocol"] or app.capitalize() in dictionary["Protocol"] or app.upper() in \
#                 dictionary["Protocol"]:
#             Tx_packets.append(dictionary['Tx Packets'])
#             apps.append(app)
# print("Tx_Packets Status %s" % Tx_packets)
# print(apps)
# print(len(Tx_packets))
##########################################################################

# json_output = {'application_control_deny': {'zoom': ['Zoom', 'https://www.zoom.us'], 'bbc': ['bbc.co.uk', 'https://www.bbc.com'], 'flipkart': ['Flipkart', 'https://www.flipkart.com/'], 'viber': ['Viber', 'https://www.viber.com'], 'google': ['Google', 'https://www.google.com'], 'spotify': ['Spotify', 'https://www.spotify.com'], 'snapchat': ['Snapchat', 'https://www.snapchat.com'], 'twitter': ['Twitter', 'https://twitter.com'], 'ndtv': ['NDTV', 'https://www.ndtv.com'], 'quora': ['Quora', 'https://www.quora.com'], 'yahoo': ['yahoo', 'https://www.yahoo.com'], 'skype': ['Skype', 'https://www.skype.com/en'], 'paytm': ['Paytm', 'https://paytm.com'], 'wikipedi': ['Wikipedia', 'https://www.wikipedia.com'], 'telegram': ['Telegram', 'https://telegram.org']}, 'application_control_permit': {'facebook': ['Facebook', 'https://www.facebook.com'], 'whatsapp': ['WhatsApp', 'https://www.whatsapp.com'], 'youtube': ['Youtube', 'https://www.youtube.com'], 'hushmail': ['Hushmail.com', 'https://www.hushmail.com/'], 'waze': ['Waze', 'https://www.waze.com']}, 'category_control_deny': {'filexfer': 'File-Transfer', 'message': 'Messaging', 'social': 'Social-Networking', 'stream': 'Streaming-Media', 'collab': 'Collaboration'}, 'category_control_permit': {'games': 'Games', 'mail': 'Mail', 'monitor': 'Network-Monitoring', 'network': 'Networking', 'remote': 'Remote-Access', 'web_srvc': 'Web-Services'}, 'category_control_url_deny': ['https://www.whatsapp.com', 'https://www.facebook.com', 'https://www.youtube.com', 'https://www.webex.com/'], 'category_control_url_permit': ['https://www.nintendo.com', 'https://www.hushmail.com/', 'https://www.fatmen.com', 'https://anydesk.com/en', 'https://www.wikipedia.com']}

# "application_control_deny" : {"zoom" : ["Zoom", "https://www.zoom.us"],

# print(list(json_output["application_control_deny"].keys()))
# print(list(json_output["category_control_url_deny"]))
# facebook = json_output["application_control_permit"]['facebook'][0].split(" ")
# print(facebook)

# print([url[1] for url in list(json_output["application_control_deny"].values())])
# print([app[0] for app in list(json_output["application_control_deny"].values())])
###################################################################################
# import requests
# import time
# import sys
#
# #
# # def check_application_status(url):
# #     for i in range(3):
# #         try:
# #             response = requests.get(url, timeout=30)
# #             if response.status_code == 200 or response.status_code == 500:
# #                 return "Success"
# #         except requests.exceptions.RequestException:
# #             pass
# #         except Exception as e:
# #             # print(f"Error: {e}")
# #             pass
# #         time.sleep(1)
# #     return "Fail"
# #
# #
#
# def http_check_urls(urls):
#     results = {}
#     for url in urls:
#         time.sleep(5)
#         try:
#             session = requests.Session()
#             response = session.get("url")
#             if response.status_code == 200:
#                 results[url] = "Success"
#             session.cookies.clear()
#             session.close()
#         except Exception as e:
#             print(f"Error message: {e}")
#             results[url] = "Success"
#
#     return results
#
#
# if __name__ == "__main__":
#
#     argument_list = sys.argv
#     urls_list = argument_list[1]
#     urls_to_check = eval(urls_list)
#
#     output = http_check_urls(urls_to_check)
#     print(output)
# import requests
# import sys
# import time
#
#
# def http_client_script(app_urls):
#     result = {}
#     header = {"Cache-Control": "no-cache",
#               "Pragma": "no-cache",
#               "Cookie": ""}
#     for url in app_urls:
#         try:
#             try:
#                 try:
#                     time.sleep(5)
#                     response = requests.get(url, timeout=30, headers=header)
#                     if response.status_code == 200:
#                         result[url] = "Success"
#                         # print(response.status_code)
#                         # print(response.url)
#                 except:
#                     time.sleep(5)
#                     response = requests.get(url, timeout=30, headers=header)
#                     if response.status_code == 200:
#                         result[url] = "Success"
#                         # print(response.status_code)
#                         # print(response.url)
#             except:
#                 time.sleep(5)
#                 response = requests.get(url, timeout=30, headers=header)
#                 if response.status_code == 200:
#                     result[url] = "Success"
#                     # print(response.status_code)
#                     # print(response.url)
#         except Exception as e:
#             # print(f"Other error occurred:{e}")
#             result[url] = "Fail"
#     return result
#
#
# if __name__ == "__main__":
#     argument_list = sys.argv
#     urls_list = argument_list[1]
#     urls = eval(urls_list)
#     # urls = ['https://www.facebook.com']
#     out = http_client_script(urls)
#     print(out)
#
# data = {'Latency': '2.0ms', 'Jitter': '0.8ms', 'Download': '877.35Mbps', 'Upload': '913.79Mbps'}
# pattern = "(\d+\.\d+)"
# speed_test_output = {}
# for key in data:
#     match = re.search(pattern, data[key])
#     if match:
#         speed_test_output[key] = match.group(0)
# # print(speed_test_output)
# # if match:
#     # print(match.group(0))
#
# # print(float("500.100") > 500)
# iwconfig_output = "Mode:Managed  Frequency:5.0 GHz  Access Point: BC:A9:93:E1:43:B0"
# pattern = "Frequency:(\d+\.\d+) GHz"
# match = re.search(pattern, iwconfig_output)
# if match:
#     res = match.group(1)
#     print(float(res))
#     assert float(res) >= 5, "Fail"

# radios_out = [{'PROFILE-ID': '1', 'MAC': 'BC-A9-93-E1-49-A0', 'BAND': '2.4GHz', 'CHANNEL': '11', 'CHANNEL-WIDTH': '20', 'CHANNEL-SELECTION': 'auto', 'POWER': '26', 'CLIENTS': '0', 'WLANS': '1', 'STATE': 'ON', 'RADARS-DETECTED': '0', 'MESH': 'OFF', 'PRIMARY+BONDS': '11'}, {'PROFILE-ID': '2', 'MAC': 'BC-A9-93-F3-17-00', 'BAND': '6GHz', 'CHANNEL': '33', 'CHANNEL-WIDTH': '160', 'CHANNEL-SELECTION': 'auto', 'POWER': '24', 'CLIENTS': '0', 'WLANS': '1', 'STATE': 'ON', 'RADARS-DETECTED': '0', 'MESH': 'OFF', 'PRIMARY+BONDS': '33+37'}, {'PROFILE-ID': '3', 'MAC': 'BC-A9-93-F3-10-D0', 'BAND': '6GHz', 'CHANNEL': '161', 'CHANNEL-WIDTH': '160', 'CHANNEL-SELECTION': 'auto', 'POWER': '24', 'CLIENTS': '0', 'WLANS': '1', 'STATE': 'ON', 'RADARS-DETECTED': '0', 'MESH': 'OFF', 'PRIMARY+BONDS': '161+165'}, {'PROFILE-ID': '4', 'MAC': 'BC-A9-93-E1-43-B0', 'BAND': '5GHz', 'CHANNEL': '44', 'CHANNEL-WIDTH': '80', 'CHANNEL-SELECTION': 'auto', 'POWER': '25', 'CLIENTS': '0', 'WLANS': '1', 'STATE': 'ON', 'RADARS-DETECTED': '0', 'MESH': 'OFF', 'PRIMARY+BONDS': '36+40'}]
# supported_channels_output = {'radio1': [{'CHANNEL': '1', 'FREQUENCY(MHz)': '2412', 'MAX-POWER': '26', 'EIRP': '36'}, {'CHANNEL': '2', 'FREQUENCY(MHz)': '2417', 'MAX-POWER': '26', 'EIRP': '36'}, {'CHANNEL': '3', 'FREQUENCY(MHz)': '2422', 'MAX-POWER': '26', 'EIRP': '36'}, {'CHANNEL': '4', 'FREQUENCY(MHz)': '2427', 'MAX-POWER': '26', 'EIRP': '36'}, {'CHANNEL': '5', 'FREQUENCY(MHz)': '2432', 'MAX-POWER': '26', 'EIRP': '36'}, {'CHANNEL': '6', 'FREQUENCY(MHz)': '2437', 'MAX-POWER': '26', 'EIRP': '36'}, {'CHANNEL': '7', 'FREQUENCY(MHz)': '2442', 'MAX-POWER': '26', 'EIRP': '36'}, {'CHANNEL': '8', 'FREQUENCY(MHz)': '2447', 'MAX-POWER': '26', 'EIRP': '36'}, {'CHANNEL': '9', 'FREQUENCY(MHz)': '2452', 'MAX-POWER': '26', 'EIRP': '36'}, {'CHANNEL': '10', 'FREQUENCY(MHz)': '2457', 'MAX-POWER': '26', 'EIRP': '36'}, {'CHANNEL': '11', 'FREQUENCY(MHz)': '2462', 'MAX-POWER': '26', 'EIRP': '36'}], 'radio2': [{'CHANNEL': '1', 'FREQUENCY(MHz)': '5955', 'MAX-POWER': '24', 'EIRP': '30'}, {'CHANNEL': '5', 'FREQUENCY(MHz)': '5975', 'MAX-POWER': '24', 'EIRP': '30'}, {'CHANNEL': '9', 'FREQUENCY(MHz)': '5995', 'MAX-POWER': '24', 'EIRP': '30'}, {'CHANNEL': '13', 'FREQUENCY(MHz)': '6015', 'MAX-POWER': '24', 'EIRP': '30'}, {'CHANNEL': '17', 'FREQUENCY(MHz)': '6035', 'MAX-POWER': '24', 'EIRP': '30'}, {'CHANNEL': '21', 'FREQUENCY(MHz)': '6055', 'MAX-POWER': '24', 'EIRP': '30'}, {'CHANNEL': '25', 'FREQUENCY(MHz)': '6075', 'MAX-POWER': '24', 'EIRP': '30'}, {'CHANNEL': '29', 'FREQUENCY(MHz)': '6095', 'MAX-POWER': '24', 'EIRP': '30'}, {'CHANNEL': '33', 'FREQUENCY(MHz)': '6115', 'MAX-POWER': '24', 'EIRP': '30'}, {'CHANNEL': '37', 'FREQUENCY(MHz)': '6135', 'MAX-POWER': '24', 'EIRP': '30'}, {'CHANNEL': '41', 'FREQUENCY(MHz)': '6155', 'MAX-POWER': '24', 'EIRP': '30'}, {'CHANNEL': '45', 'FREQUENCY(MHz)': '6175', 'MAX-POWER': '24', 'EIRP': '30'}, {'CHANNEL': '49', 'FREQUENCY(MHz)': '6195', 'MAX-POWER': '24', 'EIRP': '30'}, {'CHANNEL': '53', 'FREQUENCY(MHz)': '6215', 'MAX-POWER': '24', 'EIRP': '30'}, {'CHANNEL': '57', 'FREQUENCY(MHz)': '6235', 'MAX-POWER': '24', 'EIRP': '30'}, {'CHANNEL': '61', 'FREQUENCY(MHz)': '6255', 'MAX-POWER': '24', 'EIRP': '30'}, {'CHANNEL': '65', 'FREQUENCY(MHz)': '6275', 'MAX-POWER': '24', 'EIRP': '30'}, {'CHANNEL': '69', 'FREQUENCY(MHz)': '6295', 'MAX-POWER': '24', 'EIRP': '30'}, {'CHANNEL': '73', 'FREQUENCY(MHz)': '6315', 'MAX-POWER': '24', 'EIRP': '30'}, {'CHANNEL': '77', 'FREQUENCY(MHz)': '6335', 'MAX-POWER': '24', 'EIRP': '30'}, {'CHANNEL': '81', 'FREQUENCY(MHz)': '6355', 'MAX-POWER': '24', 'EIRP': '30'}, {'CHANNEL': '85', 'FREQUENCY(MHz)': '6375', 'MAX-POWER': '24', 'EIRP': '30'}, {'CHANNEL': '89', 'FREQUENCY(MHz)': '6395', 'MAX-POWER': '24', 'EIRP': '30'}, {'CHANNEL': '93', 'FREQUENCY(MHz)': '6415', 'MAX-POWER': '24', 'EIRP': '30'}], 'radio3': [{'CHANNEL': '129', 'FREQUENCY(MHz)': '6595', 'MAX-POWER': '24', 'EIRP': '30'}, {'CHANNEL': '133', 'FREQUENCY(MHz)': '6615', 'MAX-POWER': '24', 'EIRP': '30'}, {'CHANNEL': '137', 'FREQUENCY(MHz)': '6635', 'MAX-POWER': '24', 'EIRP': '30'}, {'CHANNEL': '141', 'FREQUENCY(MHz)': '6655', 'MAX-POWER': '24', 'EIRP': '30'}, {'CHANNEL': '145', 'FREQUENCY(MHz)': '6675', 'MAX-POWER': '24', 'EIRP': '30'}, {'CHANNEL': '149', 'FREQUENCY(MHz)': '6695', 'MAX-POWER': '24', 'EIRP': '30'}, {'CHANNEL': '153', 'FREQUENCY(MHz)': '6715', 'MAX-POWER': '24', 'EIRP': '30'}, {'CHANNEL': '157', 'FREQUENCY(MHz)': '6735', 'MAX-POWER': '24', 'EIRP': '30'}, {'CHANNEL': '161', 'FREQUENCY(MHz)': '6755', 'MAX-POWER': '24', 'EIRP': '30'}, {'CHANNEL': '165', 'FREQUENCY(MHz)': '6775', 'MAX-POWER': '24', 'EIRP': '30'}, {'CHANNEL': '169', 'FREQUENCY(MHz)': '6795', 'MAX-POWER': '24', 'EIRP': '30'}, {'CHANNEL': '173', 'FREQUENCY(MHz)': '6815', 'MAX-POWER': '24', 'EIRP': '30'}, {'CHANNEL': '177', 'FREQUENCY(MHz)': '6835', 'MAX-POWER': '24', 'EIRP': '30'}, {'CHANNEL': '181', 'FREQUENCY(MHz)': '6855', 'MAX-POWER': '24', 'EIRP': '30'}, {'CHANNEL': '185', 'FREQUENCY(MHz)': '6875', 'MAX-POWER': '24', 'EIRP': '30'}, {'CHANNEL': '189', 'FREQUENCY(MHz)': '6895', 'MAX-POWER': '24', 'EIRP': '30'}, {'CHANNEL': '193', 'FREQUENCY(MHz)': '6915', 'MAX-POWER': '24', 'EIRP': '30'}, {'CHANNEL': '197', 'FREQUENCY(MHz)': '6935', 'MAX-POWER': '24', 'EIRP': '30'}, {'CHANNEL': '201', 'FREQUENCY(MHz)': '6955', 'MAX-POWER': '24', 'EIRP': '30'}, {'CHANNEL': '205', 'FREQUENCY(MHz)': '6975', 'MAX-POWER': '24', 'EIRP': '30'}, {'CHANNEL': '209', 'FREQUENCY(MHz)': '6995', 'MAX-POWER': '24', 'EIRP': '30'}, {'CHANNEL': '213', 'FREQUENCY(MHz)': '7015', 'MAX-POWER': '24', 'EIRP': '30'}, {'CHANNEL': '217', 'FREQUENCY(MHz)': '7035', 'MAX-POWER': '24', 'EIRP': '30'}, {'CHANNEL': '221', 'FREQUENCY(MHz)': '7055', 'MAX-POWER': '24', 'EIRP': '30'}, {'CHANNEL': '225', 'FREQUENCY(MHz)': '7075', 'MAX-POWER': '24', 'EIRP': '30'}, {'CHANNEL': '229', 'FREQUENCY(MHz)': '7095', 'MAX-POWER': '24', 'EIRP': '30'}, {'CHANNEL': '233', 'FREQUENCY(MHz)': '7115', 'MAX-POWER': '24', 'EIRP': '30'}], 'radio4': [{'CHANNEL': '36', 'FREQUENCY(MHz)': '5180', 'MAX-POWER': '25', 'EIRP': '30'}, {'CHANNEL': '40', 'FREQUENCY(MHz)': '5200', 'MAX-POWER': '25', 'EIRP': '30'}, {'CHANNEL': '44', 'FREQUENCY(MHz)': '5220', 'MAX-POWER': '25', 'EIRP': '30'}, {'CHANNEL': '48', 'FREQUENCY(MHz)': '5240', 'MAX-POWER': '25', 'EIRP': '30'}, {'CHANNEL': '52', 'FREQUENCY(MHz)': '5260', 'MAX-POWER': '25', 'EIRP': '30'}, {'CHANNEL': '56', 'FREQUENCY(MHz)': '5280', 'MAX-POWER': '25', 'EIRP': '30'}, {'CHANNEL': '60', 'FREQUENCY(MHz)': '5300', 'MAX-POWER': '25', 'EIRP': '30'}, {'CHANNEL': '64', 'FREQUENCY(MHz)': '5320', 'MAX-POWER': '25', 'EIRP': '30'}, {'CHANNEL': '100', 'FREQUENCY(MHz)': '5500', 'MAX-POWER': '25', 'EIRP': '30'}, {'CHANNEL': '104', 'FREQUENCY(MHz)': '5520', 'MAX-POWER': '25', 'EIRP': '30'}, {'CHANNEL': '108', 'FREQUENCY(MHz)': '5540', 'MAX-POWER': '25', 'EIRP': '30'}, {'CHANNEL': '112', 'FREQUENCY(MHz)': '5560', 'MAX-POWER': '25', 'EIRP': '30'}, {'CHANNEL': '116', 'FREQUENCY(MHz)': '5580', 'MAX-POWER': '25', 'EIRP': '30'}, {'CHANNEL': '120', 'FREQUENCY(MHz)': '5600', 'MAX-POWER': '25', 'EIRP': '30'}, {'CHANNEL': '124', 'FREQUENCY(MHz)': '5620', 'MAX-POWER': '25', 'EIRP': '30'}, {'CHANNEL': '128', 'FREQUENCY(MHz)': '5640', 'MAX-POWER': '25', 'EIRP': '30'}, {'CHANNEL': '132', 'FREQUENCY(MHz)': '5660', 'MAX-POWER': '25', 'EIRP': '30'}, {'CHANNEL': '136', 'FREQUENCY(MHz)': '5680', 'MAX-POWER': '25', 'EIRP': '30'}, {'CHANNEL': '140', 'FREQUENCY(MHz)': '5700', 'MAX-POWER': '25', 'EIRP': '30'}, {'CHANNEL': '144', 'FREQUENCY(MHz)': '5720', 'MAX-POWER': '25', 'EIRP': '30'}, {'CHANNEL': '149', 'FREQUENCY(MHz)': '5745', 'MAX-POWER': '25', 'EIRP': '36'}, {'CHANNEL': '153', 'FREQUENCY(MHz)': '5765', 'MAX-POWER': '25', 'EIRP': '36'}, {'CHANNEL': '157', 'FREQUENCY(MHz)': '5785', 'MAX-POWER': '25', 'EIRP': '36'}, {'CHANNEL': '161', 'FREQUENCY(MHz)': '5805', 'MAX-POWER': '25', 'EIRP': '36'}, {'CHANNEL': '165', 'FREQUENCY(MHz)': '5825', 'MAX-POWER': '25', 'EIRP': '36'}, {'CHANNEL': '169', 'FREQUENCY(MHz)': '5845', 'MAX-POWER': '25', 'EIRP': '36'}, {'CHANNEL': '173', 'FREQUENCY(MHz)': '5865', 'MAX-POWER': '25', 'EIRP': '36'}, {'CHANNEL': '177', 'FREQUENCY(MHz)': '5885', 'MAX-POWER': '25', 'EIRP': '36'}]}
#
# radio_list, ch_freq = [], []
# for dict in radios_out:
#     radio_list.append(f"radio{dict['PROFILE-ID']}")
# # print(f"List of radios in AP: {radio_list}")
#
# for radio in radio_list:
#     channel_list = [a_dict['FREQUENCY(MHz)'] for a_dict in supported_channels_output.get(radio)]
#     channel = random.choice(channel_list)
#     ch_freq.append(int(channel))
# import random
# dictionary = {'Zoom': ['Web-Services', 'https://www.zoom.us'], 'YouTube': ['Streaming-Media', 'https://www.yoytube.com'], 'Flipkart': ['Web-Services', 'https://www.flipkart.com/'], 'Viber': ['Messaging', 'https://www.viber.com'], 'Games': ['Games', 'https://www.nintendo.com/'], 'Spotify': ['Streaming-Media', 'https://www.spotify.com'], 'Snapchat': ['Messaging', 'https://www.snapchat.com'], 'Twitter': ['Social-Networking', 'https://twitter.com'], 'NDTV': ['Streaming-Media', 'https://www.ndtv.com'], 'Quora': ['Social-Networking', 'https://www.quora.com'], 'Hushmail.com': ['Mail', 'https://www.hushmail.com/'], 'Skype': ['Messaging', 'https://www.skype.com/en'], 'Paytm': ['Web-Services', 'https://paytm.com'], 'Anydesk': ['Remote-Access', 'https://anydesk.com/en'], 'Telegram': ['Messaging', 'https://telegram.org']}
# app_name, app_cat_url = random.choice(list(dictionary.items()))
# print(app_name)
# print(app_cat_url[0])
# print(app_cat_url[1])
# cmd = f'python /home/testAutomation/https_request_arg.py "{[app_cat_url[1]]}"'
# print(cmd)
#
# qos_dscp_param_wlan = [(22672655, "set-qos", 0),
#                        (22672656, "set-qos", 1),
#                        (22672657, "set-qos", 2),
#                        (22674539, "set-qos", 3),
#                        (22674541, "set-dscp", 55),
#                        (22674542, "set-dscp", 40)]
#
#
# @pytest.mark.DPI_qos
# @pytest.mark.parametrize("TESTID, action, qos_dscp", qos_dscp_param_wlan)
# def test_dpi_qos_dscp_ap_group(self, device_details, cnmaestro_session, TESTID, action, qos_dscp):
#     try:
#         device_inst, device_name = device_details
#         device_mac = device_inst.get_mac_address()
#         client_shell = None
#         wired_shell = None
#         client_capture_path = "/home/sitindia"
#         Productivity_index, risk_index = 2, 3
#         precedence = 1
#         app_name_list = ["test_qos_dscp_wlan"]
#         # conditions for qos validation
#         if qos_dscp == 0:
#             lower_range, upper_range = 8, 23
#             log.info(f"QOS range for QOS value {qos_dscp}: {lower_range} to {upper_range}")
#         elif qos_dscp == 1:
#             lower_range, upper_range = 0, 7
#             log.info(f"QOS range for QOS value {qos_dscp}: {lower_range} to {upper_range}")
#             lower_range_, upper_range_ = 24, 31
#             log.info(f"QOS range for QOS value {qos_dscp}: {lower_range_} to {upper_range_}")
#         elif qos_dscp == 2:
#             lower_range, upper_range = 32, 47
#             log.info(f"QOS range for QOS value {qos_dscp}: {lower_range} to {upper_range}")
#         elif qos_dscp == 3:
#             lower_range, upper_range = 48, 63
#             log.info(f"QOS range for QOS value {qos_dscp}: {lower_range} to {upper_range}")
#         status, msg = device_inst._cli_create_custom_application(category="custom",
#                                                                  ip_hostname_list=[wired_ip],
#                                                                  application_name_list=app_name_list,
#                                                                  Productivity_index=Productivity_index,
#                                                                  risk_index=risk_index)
#         assert status, "Failed to create custom DPI configurations"
#         # conditions for setting action in cnMaestro
#         if action == "set-qos":
#             qos_value = qos_dscp
#             dscp_value = " "
#         else:
#             qos_value = " "
#             dscp_value = qos_dscp
#         status, msg = device_inst._cli_application_control_wlan_level_filter(action=action,
#                                                                              command="application-control",
#                                                                              app_cat_list=app_name_list,
#                                                                              precedence=precedence,
#                                                                              filter=1,
#                                                                              config_type="application",
#                                                                              acp_name="test_custom_qos_dscp_wlan",
#                                                                              acp_type="wlan", qos=qos_value,
#                                                                              dscp=dscp_value)
#         assert status, f"Error message: {msg}"
#
#
#     except Exception as e:
#         log.critical(f"An exception of type {type(e).__name__} occurred")
#         log.critical(traceback.format_exc())
#         raise
#
# ####################################################################################
# def speed_test_validation(device_inst):
#     """
#         Summary: This method is used to perform speedtest etsi in AP
#             param: device_inst
#     """
#     try:
#         data = {}
#         res = device_inst._cli_session.send_cmd("speedtest etsi 10.110.219.15:9000 100 1000 3 mbps", timeout=180)
#         log.debug(res)
#         result = res.split("\n")
#         pattern_1 = r"Latency: (\d+\.\d+\w+)\sJitter: (\d+\.\d+\w+)"
#         pattern_2 = r"Download: (\d+\.\d+\w+)\sUpload: (\d+\.\d+\w+)"
#         match_1 = re.search(pattern_1, result[1])
#         match_2 = re.search(pattern_2, result[2])
#         if match_1 and match_2:
#             data["Latency"] = match_1.group(1)
#             data["Jitter"] = match_1.group(2)
#             data["Download"] = match_2.group(1)
#             data["Upload"] = match_2.group(2)
#         log.info(data)
#         pattern = "(\d+\.\d+)"
#         speed_test_output = {}
#         for key in data:
#             match = re.search(pattern, data[key])
#             if match:
#                 speed_test_output[key] = match.group(0)
#         log.info(f"Speed test output: {speed_test_output}")
#         if not speed_test_output:
#             return False, "Failed to get speed test data"
#         return True, speed_test_output
#     except Exception as e:
#         log.critical(f"An exception of type {type(e).__name__} occurred")
#         log.critical(traceback.format_exc())
#         raise

##############################################################################################
# url = "https://qa-us-east-1-srv-4.cloud.cambiumnetworks.com/0/cn-srv/config/acp?fields=name,types,shared,mcid,acl_type,air_cleaner_enabled,mac_rule_count,ip_filtering_rule_count,application_filtering_rule_count,last_edited"
# responce = {
#   "data": {
#     "_metadata": {
#       "limit": 100,
#       "offset": 0,
#       "totalCount": 3
#     },
#     "ac_policies": [
#       {
#         "mcid": "",
#         "name": "global_filter_max_support",
#         "types": [
#           "Falcon",
#           "Gambit",
#           "Sage",
#           "Lila",
#           "Thor",
#           "Jaguar",
#           "Puma",
#           "Lion",
#           "Cheetah",
#           "Miami"
#         ],
#         "acl_type": "ap_group",
#         "air_cleaner_enabled": false,
#         "mac_rule_count": 0,
#         "ip_filtering_rule_count": 0,
#         "application_filtering_rule_count": 60,
#         "last_edited": "1715993797238",
#         "shared": false
#       },
#       {
#         "mcid": "",
#         "name": "WLAN",
#         "types": [
#           "Falcon",
#           "Gambit",
#           "Sage",
#           "Lila",
#           "Thor",
#           "Jaguar",
#           "Puma",
#           "Lion",
#           "Cheetah",
#           "Miami"
#         ],
#         "acl_type": "wlan",
#         "air_cleaner_enabled": false,
#         "mac_rule_count": 0,
#         "ip_filtering_rule_count": 0,
#         "application_filtering_rule_count": 1,
#         "last_edited": "1715261061568",
#         "shared": false
#       },
#       {
#         "mcid": "",
#         "name": "test_acp",
#         "types": [
#           "Falcon",
#           "Gambit",
#           "Sage",
#           "Lila",
#           "Thor",
#           "Jaguar",
#           "Puma",
#           "Lion",
#           "Cheetah",
#           "Miami"
#         ],
#         "acl_type": "ap_group",
#         "air_cleaner_enabled": true,
#         "mac_rule_count": 10,
#         "ip_filtering_rule_count": 0,
#         "application_filtering_rule_count": 0,
#         "last_edited": "1716574331074",
#         "shared": false
#       }
#     ]
#   },
#   "sTime": 1716784396201
# }
#

def update_out(out, user_server_ip, user_dut_ip):
    # Split the string into lines
    lines = out.split('\n')

    # Check if the ramdump block is present
    ramdump_block = ["ramdump", f"ramdump server-ip {user_server_ip}", f"ramdump dut-ip {user_dut_ip}"]

    # Extract the current IPs from the string
    current_server_ip = None
    current_dut_ip = None
    ramdump_present = False

    for line in lines:
        if line == "ramdump":
            ramdump_present = True
        elif line.startswith("ramdump server-ip "):
            current_server_ip = line.split(" ")[-1]
        elif line.startswith("ramdump dut-ip "):
            current_dut_ip = line.split(" ")[-1]

    # If the ramdump block is present and the IPs match, update the block
    if ramdump_present and current_server_ip == user_server_ip and current_dut_ip == user_dut_ip:
        updated_out = []
        for line in lines:
            if line.startswith("ramdump server-ip "):
                updated_out.append(f"ramdump server-ip {user_server_ip}")
            elif line.startswith("ramdump dut-ip "):
                updated_out.append(f"ramdump dut-ip {user_dut_ip}")
            else:
                updated_out.append(line)
        return '\n'.join(updated_out)

    # If the ramdump block is not present or the IPs don't match, return the original string
    return out


# Example usage
out = '''!
service debug wmd logging-level debug
!
!
ramdump
ramdump server-ip 10.110.153.143
ramdump dut-ip 10.110.153.12
!
'''

user_server_ip = "10.110.153.143"
user_dut_ip = "10.110.153.12"

updated_out = update_out(out, user_server_ip, user_dut_ip)
print(updated_out)
#########################################################################################################
before = """!
management http port 80
management cambium-remote validate-server-cert
management cambium-remote
management ssh idle-timeout 300
no management radius-auth
management https
management https port 443
management http
management user admin password $crypt$2$$2a$10$Utr9UrDkTFaN3atXBar1ru.NsxC8CFyOs4K7PTIfS4KQoysPUlPhy
management ssh
no management telnet
led
no poe-out
system hw-reset
country-code US
nss-offload
placement indoor
root-cause-analysis
ramdump
ramdump server-ip 10.110.214.227
ramdump dut-ip 10.110.214.30
!
wireless radio 1
 no shutdown
 frequency-band 2.4GHz
 channel auto
 channel-width 20
 channel-list 6
 rates min-unicast 1
 power auto
 beacon-interval 100
 guard-interval 0
 auto-rf dynamic-channel channel-hold-time 120
 auto-rf dynamic-power mode by-band 
 wmm-parameters downstream txoplimit vi 3008
 wmm-parameters downstream txoplimit vo 1504
 wmm-parameters upstream txoplimit vi 3008
 wmm-parameters upstream txoplimit vo 1504
 multicast-to-unicast
 multicast-to-unicast mode amsdu
 continuous-background-scan 
 continuous-background-scan dwell-split-time 25
!
wireless radio 2
 no shutdown
 frequency-band 5GHz
 channel auto
 channel-width 40
 channel-list 36 161
 rates min-unicast 6
 power auto
 beacon-interval 100
 guard-interval 0
 auto-rf dynamic-channel channel-hold-time 120
 auto-rf dynamic-power mode by-band 
 wmm-parameters downstream txoplimit vi 3008
 wmm-parameters downstream txoplimit vo 1504
 wmm-parameters upstream txoplimit vi 3008
 wmm-parameters upstream txoplimit vo 1504
 multicast-to-unicast
 multicast-to-unicast mode amsdu
 continuous-background-scan 
 continuous-background-scan dwell-split-time 25
!
wireless wlan 1
 ssid Test_DPI_Filter_1
 no shutdown
 vlan 1
 security wpa3-sae
 protected-mgmt-frames state mandatory
 protected-mgmt-frames sa-query-retry-time 100
 protected-mgmt-frames association-comeback 1
 passphrase $crypt$1$8oPI03z0foXsI16Z6idUZSa8wDjT6fw+
 band all
 dynamic-arp-inspection
 11v
 qbss
 max-associated-client 127
 nas-identifier AP-HOSTNAME
 network-policy-id 0
 mac-authentication policy deny
 passpoint interworking access-network-type private
 no guest-access
!
wireless wlan 2
 ssid Test_DPI_Filter_2
 no shutdown
 vlan 1
 security wpa3-sae
 protected-mgmt-frames state mandatory
 protected-mgmt-frames sa-query-retry-time 100
 protected-mgmt-frames association-comeback 1
 passphrase $crypt$1$sFTOkBEenzvTVBbMopbxZoN8jd9OPFLb
 band all
 dynamic-arp-inspection
 11v
 qbss
 max-associated-client 127
 nas-identifier AP-HOSTNAME
 network-policy-id 0
 mac-authentication policy deny
 passpoint interworking access-network-type private
 no guest-access
!
rtls aeroscout server-port 12092
!
!
multicast-snoop br0
multicast-snoop br1
!
!
interface portchannel 1
 switchport mode access
 switchport access vlan 1
!
interface eth 1
 switchport mode access
 switchport access vlan 1
!
interface eth 2
 switchport mode access
 switchport access vlan 1
!
interface eth 3
 switchport mode access
 switchport access vlan 1
!
interface vlan 1
 ip address zeroconf
 management-access all
 ip dhcp request-option-all
 ip address dhcp
!
pppoe server
 shutdown
 tcp-mss-clamp
 management-access
!


hostname XV2-22H-E536B7
timezone Asia/Kolkata
location bangalore
snmp-server read-community $crypt$1$ylZopSPc55W97gqHHiqUaKf3g+xVAYOu
snmp-server write-community $crypt$1$0wLlt8gVrtf16VZulfHe/nAkMaG68BqI
snmp-server
no wifiperf
!
ip gw-source-precedence static 1
ip gw-source-precedence dhcpc 2
ip gw-source-precedence pppoe 3
ipv6 gw-source-precedence static 1
ipv6 gw-source-precedence auto-config/dhcpc 2

!
filter  global-filter
  stateful
  application-control
!
lldp
lldp tx-interval 30
lldp pba
lldp pba-auth-key $crypt$1$ZmhGY06O3e7SOl4YsiazPszIDE64wGfJ
power policy sufficient
power lldp policy auto
power alerts policy yes
power bootloop enabled
logging syslog 7

service debug wmd logging-level debug
!"""

after = """!
management http port 80
management cambium-remote validate-server-cert
management cambium-remote
management ssh idle-timeout 300
no management radius-auth
management https
management https port 443
management http
management user admin password $crypt$2$$2a$10$Utr9UrDkTFaN3atXBar1ru.NsxC8CFyOs4K7PTIfS4KQoysPUlPhy
management ssh
no management telnet
led
no poe-out
system hw-reset
country-code US
nss-offload
placement indoor
root-cause-analysis
ramdump
ramdump server-ip 10.110.214.227
ramdump dut-ip 10.110.214.30
!
wireless radio 1
 no shutdown
 frequency-band 2.4GHz
 channel auto
 channel-width 20
 channel-list 6
 rates min-unicast 1
 power auto
 beacon-interval 100
 guard-interval 0
 auto-rf dynamic-channel channel-hold-time 120
 auto-rf dynamic-power mode by-band 
 wmm-parameters downstream txoplimit vi 3008
 wmm-parameters downstream txoplimit vo 1504
 wmm-parameters upstream txoplimit vi 3008
 wmm-parameters upstream txoplimit vo 1504
 multicast-to-unicast
 multicast-to-unicast mode amsdu
 continuous-background-scan 
 continuous-background-scan dwell-split-time 25
!
wireless radio 2
 no shutdown
 frequency-band 5GHz
 channel auto
 channel-width 40
 channel-list 36 161
 rates min-unicast 6
 power auto
 beacon-interval 100
 guard-interval 0
 auto-rf dynamic-channel channel-hold-time 120
 auto-rf dynamic-power mode by-band 
 wmm-parameters downstream txoplimit vi 3008
 wmm-parameters downstream txoplimit vo 1504
 wmm-parameters upstream txoplimit vi 3008
 wmm-parameters upstream txoplimit vo 1504
 multicast-to-unicast
 multicast-to-unicast mode amsdu
 continuous-background-scan 
 continuous-background-scan dwell-split-time 25
!
wireless wlan 1
 ssid Test_DPI_Filter_1
 no shutdown
 vlan 1
 security wpa3-sae
 protected-mgmt-frames state mandatory
 protected-mgmt-frames sa-query-retry-time 100
 protected-mgmt-frames association-comeback 1
 passphrase $crypt$1$8oPI03z0foXsI16Z6idUZSa8wDjT6fw+
 band all
 dynamic-arp-inspection
 11v
 qbss
 max-associated-client 127
 nas-identifier AP-HOSTNAME
 network-policy-id 0
 mac-authentication policy deny
 passpoint interworking access-network-type private
 no guest-access
!
wireless wlan 2
 ssid Test_DPI_Filter_2
 no shutdown
 vlan 1
 security wpa3-sae
 protected-mgmt-frames state mandatory
 protected-mgmt-frames sa-query-retry-time 100
 protected-mgmt-frames association-comeback 1
 passphrase $crypt$1$sFTOkBEenzvTVBbMopbxZoN8jd9OPFLb
 band all
 dynamic-arp-inspection
 11v
 qbss
 max-associated-client 127
 nas-identifier AP-HOSTNAME
 network-policy-id 0
 mac-authentication policy deny
 passpoint interworking access-network-type private
 no guest-access
!
rtls aeroscout server-port 12092
!
!
multicast-snoop br0
multicast-snoop br1
!
!
interface portchannel 1
 switchport mode access
 switchport access vlan 1
!
interface eth 1
 switchport mode access
 switchport access vlan 1
!
interface eth 2
 switchport mode access
 switchport access vlan 1
!
interface eth 3
 switchport mode access
 switchport access vlan 1
!
interface vlan 1
 ip address zeroconf
 management-access all
 ip dhcp request-option-all
 ip address dhcp
!
pppoe server
 shutdown
 tcp-mss-clamp
 management-access
!


hostname XV2-22H-E536B7
timezone Asia/Kolkata
location bangalore
snmp-server read-community $crypt$1$ylZopSPc55W97gqHHiqUaKf3g+xVAYOu
snmp-server write-community $crypt$1$0wLlt8gVrtf16VZulfHe/nAkMaG68BqI
snmp-server
no wifiperf
!
ip gw-source-precedence static 1
ip gw-source-precedence dhcpc 2
ip gw-source-precedence pppoe 3
ipv6 gw-source-precedence static 1
ipv6 gw-source-precedence auto-config/dhcpc 2

!
filter  global-filter
  stateful
  application-control
!
lldp
lldp tx-interval 30
lldp pba
lldp pba-auth-key $crypt$1$ZmhGY06O3e7SOl4YsiazPszIDE64wGfJ
power policy sufficient
power lldp policy auto
power alerts policy yes
power bootloop enabled
logging syslog 7

service debug wmd logging-level debug
!"""
#########################################################
# import requests
# import sys
# import time
#
#
# def http_client_script(app_urls):
#     result = {}
#     header = {"Cache-Control": "no-cache",
#               "Pragma": "no-cache",
#               "Cookie": ""
#               }
#     for url in app_urls:
#         try:
#             try:
#                 try:
#                     time.sleep(5)
#                     response = requests.get(url, timeout=30, headers=header)
#                     print(response.status_code)
#                     if response.status_code == 200:
#                         result[url] = "Success"
#                         # print(response.status_code)
#                         # print(response.url)
#                 except:
#                     time.sleep(5)
#                     response = requests.get(url, timeout=30, headers=header)
#                     if response.status_code == 200:
#                         result[url] = "Success"
#                         # print(response.status_code)
#                         # print(response.url)
#             except:
#                 time.sleep(5)
#                 response = requests.get(url, timeout=30, headers=header)
#                 if response.status_code == 200:
#                     result[url] = "Success"
#                     # print(response.status_code)
#                     # print(response.url)
#         except Exception as e:
#             # print(f"Other error occurred:{e}")
#             result[url] = "Fail"
#     return result
#
#
# if __name__ == "__main__":
#     argument_list = sys.argv
#     urls_list = argument_list[1]
#     urls = eval(urls_list)
#     out = http_client_script(urls)
#     print(out)
########################################################################
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.common.exceptions import WebDriverException, TimeoutException
# import sys
# import time
#
#
# def check_url_accessible(url: str, timeout: int = 10) -> bool:
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
#                 return True
#             else:
#                 print(driver.name)
#                 print(f"[WARNING] URL '{url}' loaded but has no title.")
#                 return True
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
#     test_url = "https://www.ndtv.com"  # change to your URL
#     result = check_url_accessible(test_url)
#     sys.exit(0 if result else 1)
##################################################################################
result = """
# fw_printenv
artsum=7b451ae2a8641661ccb2448435f5bafc
baudrate=115200
bootargs=console=ttyMSM0,115200n8 cnss2.bdf_integrated=0x24 cnss2.bdf_pci0=0x50 cnss2.skip_radio_bmap=4
bootcmd=bootipq
bootdelay=4
dump_compressed=1
dump_prefix=ramdump_10.110.153.12_
dump_to_nand=1
eth1addr=b4:a2:5c:e5:36:b8
eth2addr=b4:a2:5c:e5:36:b9
ethaddr=b4:a2:5c:e5:36:b7
fdt_high=0x4A400000
fdtcontroladdr=4a97c320
flash_type=7
hwid=2
image=1
ipaddr=10.110.153.12
machid=8040002
meshmode=none
netmask=255.255.255.0
nss=1
regulatory_domain=FCC
serverip=10.110.153.143
soc_hw_version=20180101
soc_version_major=1
soc_version_minor=1
stderr=serial@78AF000
stdin=serial@78AF000
stdout=serial@78AF000
ver=U-Boot Cheetah 2016.01 v2.7.5b (Sep 23 2025 - 13:06:16 +0000)
bootcount=0
"""

ipaddr_regex = r"ipaddr=(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})"
match_ipaddr = re.search(ipaddr_regex, result)
if match_ipaddr:
    ipaddr = match_ipaddr.group(1)
    print(ipaddr)
else:
    print("ipaddr not found")

serverip_regex = r"serverip=(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})"
match_serverip = re.search(serverip_regex, result)
if match_serverip:
    serverip = match_serverip.group(1)
    print(serverip)
else:
    print("serverip not found")
