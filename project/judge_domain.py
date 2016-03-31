
import sys
import json
import traceback

valid_domain = ['app.appsflyer.com', 'app.adjust.io', 'app.adjust.com', 'control.kochava.com', 'ad.apsalar.com', 'measurementapi.com', '.api-0', 'app-adforce', 'track.uri6.com', 'lnk8.cn']
def get_domain_name(domain):
    global valid_domain
    if domain in valid_domain:
        return domain
    for d in valid_domain:
        if domain.find(d) != -1:
            return d
    return None

def main():
    res = get_domain_name('app.adjust.io')
    print res
    res = get_domain_name('app.adjust.i')
    print res

if __name__ == '__main__':
    main()
