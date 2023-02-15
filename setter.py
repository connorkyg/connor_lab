# 다음 파일들을 /root/tmp/ 경로에서 찾아, 현재 경로로 복사합니다.


import os
import shutil

current_path = os.getcwd()
copy_path = '192.168.1.112:/DATA1/lab/LAB/SolidStep/Agent/'
agent_version = '2.41.4841755'
copy_files = ['GS-linux-64', 'GS-linux-64.info', 'Install.sh', 'MI_FMM-linux-64', 'MI_FMM-linux-64.info',
              'MI_FMMCFG.ini', 'SA-linux-64', 'SA-linux-64.info', 'SACFG.ini', 'SR-linux-64', 'SR-linux-64.info',
              'SS_AA-linux-64', 'SS_AA-linux-64.info', 'SS_AD-linux-64', 'SS_AD-linux-64.info', 'SS_AH-linux-64',
              'SS_AH-linux-64.info', 'SS_AS-linux-64', 'SS_AS-linux-64.info', 'SS_AW-linux-64', 'SS_AW-linux-64.info',
              'SS_CVE-linux-64', 'SS_CVE-linux-64.info', 'SS_unixappcfg.ini', 'SS_unixcdcfg.ini', 'SS_unixcfg.ini',
              'SS_unixdbcfg.ini', 'SS_unixhypcfg.ini', 'SS_unixpdcfg.ini', 'SS_unixpfcfg.ini', 'SS_unixwebcfg.ini',
              'Uninstaller-linux-64', 'Uninstaller-linux-64.info', 'Updater-linux-64', 'Updater-linux-64.info',
              'sa.crt', 'sa.key.pem', 'ssrca.crt', 'ssrca.pub']

for file in copy_files:
    shutil.copy(copy_path + file, current_path)
