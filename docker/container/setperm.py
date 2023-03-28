import os
# import cells # COMMENT: 실제 container 내에서는 현재 경로에 cells 있음
from docker.host import cells

if __name__ == '__main__':
    local = '/SSR'
    for i in cells.Agent:
        os.system(f'chmod {int(cells.Agent[i])} {local}/{i}')
    os.chown(f'{local}/', 0, 0)


    local = '/SSR'
    for i in cells.Agent_oct:
        print(type(oct(cells.Agent_oct[i])))
        print(oct(cells.Agent_oct[i]))
        # print(f'{local}/{i}')