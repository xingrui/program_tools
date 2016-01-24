import redis
import json
r = redis.Redis(host = '192.168.1.17', port = 6480, db = 0, password='123456')
res = r.get('channel:%s' % '441')
channel_obj = json.loads(res)
print json.dumps(channel_obj, indent = 4)
