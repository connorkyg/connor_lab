import os
import subprocess
from docker import cells


def command(cmd):
    return subprocess.run(cmd, shell=True)


if __name__ == '__main__':
    local = '/SSR'
    for i in cells.Agent:
        os.chmod(f'{local}/{cells.Agent}', cells.Agent[i])