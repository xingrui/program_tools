import sys
import time
import httplib
import json
import csv

def base_post(data, date_str):
    data_file = '' + date_str + '.txt'
    write_file = open(data_file, 'w')
    timestamp = date + 'T00:00:00Z'
    data['timestamp'] = timestamp

    data = json.dumps(data)
    server_host = 'report-es.mobvista.com'
    prefix_url = '/'

    url = 'test_script/daily_stat/'
    conn = httplib.HTTPConnection(server_host)
    req_url = prefix_url + url + date_str + '/'
    print 'http://' + server_host + req_url
    conn.request("POST", req_url, data)
    print data
    response = conn.getresponse()
    if response.status != 201:
        print ("%u, %s" % (response.status, response.reason))
    res = response.read()
    print res
    conn.close()
    write_file.write(data)

def main(date):
    data = {}
    data['injected_cvr'] = 123
    base_post(data, date)

if __name__ == "__main__":
    if len(sys.argv) == 1:
        print 'usage:' + sys.argv[0] + ' date'
        exit(1)
    date = sys.argv[1]
    main(date)
