import os
import subprocess
import argparse
from ping3 import ping

from docker import cells


def mount(remote, local):
    command(f'mount {remote} {local}')


def command(cmd):
    return subprocess.run(cmd, shell=True)


parser = argparse.ArgumentParser()
parser.add_argument('--agent_version', type=str, required=True, help='Enter agent version')
args = parser.parse_args()

try:
    ping('192.168.1.112')
except:
    print('[ERROR] cannot connect to samba server')

remote = f'192.168.1.112:/DATA1/lab/LAB/SolidStep/Agent/'
path = '/mnt/ssr_mount'
local = f'/tmp/agent/{args.agent_version}'

manager_ip = '192.168.199.222'

init = f'''\
FROM ubuntu:22.04

LABEL maintainer="Connor Kwon"
LABEL email1="kwonyounggyu@ssrinc.co.kr"
LABEL email2="connorkyg@gmail.com"
LABEL description="SSR Agent setup"


WORKDIR /

# RUN apt update && apt-get install -y \
#     python3.9 \
#     python3-pip \
#     nfs-common
RUN mkdir -p /SSR
COPY --chown=root:root /test/ /SSR
# COPY {local}/{args.agent_version}/linux /SSR
#
# ENTRYPOINT python3 /tmp/docker/set_perm.py
# ENTRYPOINT python3 /tmp/docker/sacfg.py --SOLIDSTEP_MANAGER={manager_ip}
# ENTRYPOINT /SSR/SA-linux-64 --start

EXPOSE 443/tcp\
'''

# mkdir -> mount -> cp to local
os.makedirs(path, exist_ok=True)
os.makedirs(local, exist_ok=True)
mount(remote, path)
for file in cells.Agent:
    command(f'cp {path}/{args.agent_version}/linux/{file} {local}')

with open(file='./dockerfile', mode='w+', encoding='utf-8') as f:
    f.write(init)

try:
    command(f'docker build -t agent:{args.agent_version} .')
except:
    print('[ERROR] Docker image build failed')
