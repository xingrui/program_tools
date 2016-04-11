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
        params=urlparse.parse_qs(result.query,True)
        if 'id' not in params:
            self.send_reply('no id in params')
            return
        if result.path == '/campaign':
            try:
                key_id = params['id'][0]
                _http = get_http_content('campaign', key_id).split('\n')
                _extractor = get_extractor_content('campaign', key_id).split('\n')
                diff = difflib.HtmlDiff(wrapcolumn=60).make_file(_http, _extractor)
                self.send_reply(diff)
            except:
                self.send_reply('not valid key_id:[' + key_id + ']')
            return
        if result.path == '/inject_code':
            try:
                key_id = params['id'][0]
                _http = get_http_content('inject_code', key_id).split('\n')
                _extractor = get_extractor_content('inject_code', key_id).split('\n')
                diff = difflib.HtmlDiff(wrapcolumn=60).make_file(_http, _extractor)
                self.send_reply(diff)
            except:
                self.send_reply('not valid inject_code_id:[' + key_id + ']')
            return
        if result.path == '/channel':
            try:
                key_id = params['id'][0]
                _http = get_http_content('channel', key_id).split('\n')
                _extractor = get_extractor_content('channel', key_id).split('\n')
                diff = difflib.HtmlDiff(wrapcolumn=60).make_file(_http, _extractor)
                self.send_reply(diff)
            except:
                self.send_reply('not valid channel:[' + key_id + ']')
            return
        self.send_reply('not valid path')
        return

def get_http_content(data_type, key_id):
    response = GET('http://3ss.mobvista.com/track/' + data_type + '/orm/' + key_id, params =  {"client_id": "qXJSJzzsGDPdYXR1"}, headers =  {"Authorization": "Basic Ozg5P5nB8qegPBhH"})
    json_obj = json.loads(response.content)
    if data_type == 'inject_code':
        return json_obj['code']
    return json.dumps(json_obj, indent = 4, sort_keys=True)

def get_extractor_content(data_type, key_id):
    r = redis.Redis(host = '192.168.1.17', port = 6480, db = 0, password='123456')
    res = r.get('%s:%s' % (data_type, str(key_id)))
    json_obj = json.loads(res)
    if data_type == 'inject_code':
        return json_obj['code']
    return json.dumps(json_obj, indent = 4, sort_keys=True)

def main():
    try:
        server = HTTPServer(('', 9999), MyRequestHandler)
        print 'started httpserver...'
        server.serve_forever()
    except KeyboardInterrupt:
        server.socket.close()
    exit(0)

if __name__ == "__main__":
    main()
