def dockerfile(local, args):
    init = f'''\
FROM itzconnor/work:1.0

LABEL maintainer="Connor Kwon"
LABEL email1="kwonyounggyu@ssrinc.co.kr"
LABEL email2="connorkyg@gmail.com"
LABEL description="SSR Agent setup"

RUN apt update && apt-get install -y \
    python3.9 \
    python3-pip \
    nfs-common
RUN mkdir -p /SSR
COPY --chown=root:root {local} /SSR

WORKDIR /

# ENTRYPOINT python3 /docker/setperm.py
# ENTRYPOINT python3 /docker/sacfg.py --SOLIDSTEP_MANAGER={args.ss_manager_ip}
# ENTRYPOINT /SSR/SA-linux-64 --start
# ENTRYPOINT /bin/bash

EXPOSE 443/tcp\
'''
    with open(file='./dockerfile', mode='w+', encoding='utf-8') as f:
        f.write(init)