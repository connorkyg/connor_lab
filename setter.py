import yaml

with open('test.yaml', encoding='UTF-8') as f:
    _cfg = yaml.load(f, Loader=yaml.FullLoader)

KEY = _cfg['KEY']
URL = _cfg['URL']

print(KEY, URL)