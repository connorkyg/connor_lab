import os
import subprocess

# import argparse
# parser = argparse.ArgumentParser()
# parser.add_argument('--agent_version', type=str, required=True, help='Enter agent version')
# args = parser.parse_args()


def mount(remote, local):
    command(f'mount {remote} {local}')


def command(cmd):
    return subprocess.run(cmd, shell=True)


if __name__ == '__main__':
    remote = f'192.168.1.112:/DATA1/lab/LAB/SolidStep/Agent/'
    local = '/mnt/ssr_mount'
    os.makedirs(local, exist_ok=True)
    mount(remote, local)