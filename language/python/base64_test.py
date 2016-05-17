import sys,json
import base64

for line in ['NHxzZy5yYXlqdW1wLmNvbXw1NzAzZTBmZmYxY2NiZTczMTljMTU3ODZ8Nzg5NXwyMzg5MnwwfHw1fElOfHw0NTd8NTg2fHwwfA==']:
    try:
        click_id = base64.b64decode(line.strip())
        fields = click_id.split('|')
        if len(fields) <= 3:
            continue
        click_mode = click_id.split('|')[-2]
        print fields
        print click_mode
    except TypeError, e:
        #print e
        pass
