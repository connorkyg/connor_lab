import os
# import cells # COMMENT: 실제 container 내에서는 현재 경로에 cells 있음
from docker.host import cells

if __name__ == '__main__':
    local = '/SSR'
    for i in cells.Agent:
        os.chmod(f'{local}/{cells.Agent}', cells.Agent[i])
    os.chown(f'{local}/*', 0, 0)