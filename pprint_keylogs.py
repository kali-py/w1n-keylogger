import pprint
import json

with open('logs.json', 'rb') as key_log:
    key_log = json.loads(key_log.read().decode())
    pprint.pprint(key_log)
