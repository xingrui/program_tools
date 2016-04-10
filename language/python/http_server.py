from requests import get as GET 
import difflib
import redis
import json
import sys 
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import io,shutil  
import urllib,time
import getopt,string
import urlparse

class MyRequestHandler(BaseHTTPRequestHandler):
    def send_reply(self, content):
        self.send_response(200)
        self.send_header("Content-type", "text/html; charset=%s" % 'utf-8')  
        self.send_header("Content-Length", str(len(content)))  
        self.end_headers()  
        self.wfile.write(content);

    def do_GET(self):
        result = urlparse.urlparse(self.path)
        if result.path != '/campaign':
            self.send_reply('not valid path')
            return
        params=urlparse.parse_qs(result.query,True)
        if 'id' not in params:
            self.send_reply('no id in params')
            return
        campaign_id = params['id'][0]
        _http = get_http_content(campaign_id).split('\n')
        _extractor = get_extractor_content(campaign_id).split('\n')
        diff = difflib.HtmlDiff().make_file(_http, _extractor)
        self.send_reply(diff)

def get_http_content(campaign_id):
    campaign_id = '100122'
    response = GET('http://3ss.mobvista.com/track/campaign/orm/' + campaign_id, params =  {"client_id": "qXJSJzzsGDPdYXR1"}, headers =  {"Authorization": "Basic Ozg5P5nB8qegPBhH"})
    return json.dumps(json.loads(response.content), indent = 4, sort_keys=True)

def get_extractor_content(campaign_id):
    r = redis.Redis(host = '192.168.1.17', port = 6480, db = 0, password='123456')
    res = r.get('campaign:%s' % str(campaign_id))
    return json.dumps(json.loads(res), indent = 4, sort_keys=True)

def main():
    try:
        server = HTTPServer(('', 8080), MyRequestHandler)
        print 'started httpserver...'
        server.serve_forever()
    except KeyboardInterrupt:
        server.socket.close()
    exit(0)
    _http = get_http_content('100122').split('\n')
    _extractor = get_extractor_content('100122').split('\n')
    diff = difflib.HtmlDiff().make_file(_http, _extractor)
    print diff

if __name__ == "__main__":
    main()
