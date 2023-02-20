import os
from docker import cells

if __name__ == '__main__':
    local = '/SSR'
    for i in cells.Agent:
        os.chmod(f'{local}/{cells.Agent}', cells.Agent[i])
    os.chown(f'{local}/*', 0, 0)