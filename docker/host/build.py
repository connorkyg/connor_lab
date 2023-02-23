import os
import datetime
import subprocess
import argparse
from ping3 import ping

import ingredients
import cells

now = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
os.system('echo This module can only be executed on the SSR network')
os.system('echo This module can only be executed on the SSR network')
os.system('echo This module can only be executed on the SSR network')
os.system('echo This module can only be executed on the SSR network')
os.system('echo This module can only be executed on the SSR network')


def command(cmd):
    return subprocess.run(cmd, shell=True)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-a', '--agent_version', type=str, required=True, help='Enter agent version (ex. 2.41.4841755)')
    parser.add_argument('-ssip', '--ss_manager_ip', type=str, default='192.168.199.224', help='Enter SolidStep manager ip (ex. 192.168.1.100')
    # parser.add_argument('-meip', '--me_manager_ip', type=str, default='192.168.199.222', help='Enter MetiEye manager ip (ex. 192.168.1.100')
    args = parser.parse_args()

    try:
        ping('192.168.1.112')
        os = 'linux'
        remote = f'192.168.1.112:/DATA1/lab/LAB/SolidStep/Agent/{args.agent_version}/{os}'
        path = '/mnt/ssr_mount'
        local = f'./tmp_{now}/{args.agent_version}'  # COMMENT: dockerfile이 위치한 경로 기준이므로, 상대 경로로 표시해주어야 함 (현재 경로가 무난)

        # mkdir -> mount -> cp to local
        command(f'mkdir -p {path}')
        command(f'mkdir -p {local}')
        # os.makedirs(path, exist_ok=True)
        # os.makedirs(local, exist_ok=True)
        command(f'mount {remote} {path}')
        for file in cells.Agent:
            command(f'cp {path}/{file} {local}')

        ingredients.dockerfile(local, args)

        command(f'docker build -t agent:{args.agent_version} .')
        command(f'umount -f {path}')
        command(f'rmdir /mnt/ssr_mount')
    except:
        print('[ERROR] Something went wrong')
        command(f'umount -f {path}')
        command(f'rmdir /mnt/ssr_mount')