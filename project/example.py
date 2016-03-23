import redis
import MySQLdb
import json
import psycopg2
from pymongo import MongoClient

def get_3s_redis(channel_id):
    r = redis.Redis(host = '192.168.1.17', port = 6480, db = 0, password='123456')
    res = r.get('channel:%s' % str(channel_id))
    channel_obj = json.loads(res)
    print channel_obj['name']

def get_3s_psql(channel_id):
    conn = psycopg2.connect(database = "mob1log", user = "mob_tech", password = "Pr3j5KcQlM16",host = "datastore-redshift.lenzmx.com", port = "5439") 
    cur = conn.cursor()
    cur.execute('select * from %s where network=%s limit 1' % ('mob_install_log', str(channel_id)))
    row = cur.fetchone()
    print row

def get_adn_mongo(publisher_id):
    conn = MongoClient("192.168.1.54", 27017)
    db = conn.new_adn
    content = db.publisher.find({'publisherId':publisher_id})
    for i in content:
        print i['publisher']['username']

def get_adn_mysql():
    conn = MySQLdb.connect(host = 'adn-mysql-external.mobvista.com', user = 'mob_adn_ro', passwd = 'blueriver123', db = 'mob_adn')
    cur = conn.cursor()
    cur.execute('select promote_url,direct_url from campaign_list limit 1')
    result = cur.fetchone()
    print result 
    cur.close()
    conn.close()

def get_adn_psql(channel_id):
    conn = psycopg2.connect(database = "data", user = "root", password = "adn2015DATA", host = "adndataup.cj0ro5bbcusg.us-east-1.redshift.amazonaws.com", port = "5439") 
    cur = conn.cursor()
    sql = 'select count(*), campaign_id from log_click where extra10=6 and date=%s group by campaign_id' % ('20160322')
    result = cur.execute(sql)
    row = cur.fetchall()
    click_count = 0 
    campaign_id_list = []
    print row

def main():
    get_3s_redis(441)
    get_3s_psql(441)
    get_adn_mongo(6028)
    get_adn_mysql()
    get_adn_psql(123)

if __name__ == "__main__":
    main()
