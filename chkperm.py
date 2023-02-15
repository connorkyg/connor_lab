import os

sample = {
    'a': '1'
}

path = "/SSR"
permissions = {
    'Agent': {
        'GS-linux-64.info': 0o644,
        'MI_FMM-linux-64.info': 0o644,
        'SA-linux-64.info': 0o644,
        'SR-linux-64.info': 0o644,
        'SS_AA-linux-64.info': 0o644,
        'SS_AD-linux-64.info': 0o644,
        'SS_AH-linux-64.info': 0o644,
        'SS_AS-linux-64.info': 0o644,
        'SS_AW-linux-64.info': 0o644,
        'SS_CVE-linux-64.info': 0o644,
        'Uninstaller-linux-64.info': 0o644,
        'Updater-linux-64.info': 0o644,
        'GS-linux-64': 0o700,
        'MI_FMM-linux-64': 0o700,
        'SA-linux-64': 0o700,
        'MI_FMMCFG.ini': 0o700,
        'SACFG.ini': 0o600,
        'SR-linux-64': 0o700,
        'SS_AA-linux-64': 0o700,
        'SS_AD-linux-64': 0o700,
        'SS_AH-linux-64': 0o700,
        'SS_AS-linux-64': 0o700,
        'SS_AW-linux-64': 0o700,
        'SS_CVE-linux-64': 0o700,
        'SS_unixappcfg.ini': 0o600,
        'SS_unixcdcfg.ini': 0o600,
        'SS_unixcfg.ini': 0o600,
        'SS_unixdbcfg.ini': 0o600,
        'SS_unixhypcfg.ini': 0o600,
        'SS_unixpdcfg.ini': 0o600,
        'SS_unixpfcfg.ini': 0o600,
        'SS_unixwebcfg.ini': 0o600,
        'Uninstaller-linux-64': 0o700,
        'Updater-linux-64': 0o700,
        'sa.crt': 0o600,
        'sa.key.pem': 0o600,
        'ssrca.crt': 0o600,
        'ssrca.pub': 0o600
    }
}


files = os.listdir(path)

for file in files:
    if file in permissions['Agent'].keys():
        os.chmod(os.path.join(path, file), permissions['Agent'][file])
        print(os.path.join(path, file))