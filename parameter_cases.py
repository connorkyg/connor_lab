# todo: parameter 경우의 수를 여기서 관리할 예정
os_list = ['windows', 'linux', 'solaris', 'hpux', 'aix', 'network']
for i in range(len(os_list)):
    os = os_list[i]
params = {
    'get_AgentDownload': {
        'os': os
    },
    'get_AssetStatusPortDetail': {
        'aiNo': 1
    }
}