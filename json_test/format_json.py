import json
import sys 
for line in sys.stdin:
    line = line.strip()
    json_obj = json.loads(line)
    print json.dumps(json_obj, indent = 4)
