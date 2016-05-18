from storage_base import *

def get_3s_channel(channel_id):
    res = get_3s_key('channel:%s' % str(channel_id))
    channel_obj = json.loads(res)
    print channel_obj['name']

def get_3s_psql(channel_id):
    sql = 'select * from %s where network=%s limit 1' % ('mob_install_log', str(channel_id))
    results = get_3s_psql_sql(sql)
    print results

def get_adn_mongo(publisher_id):
    conn = get_adn_mongo_connection()
    db = conn.new_adn
    content = db.publisher.find({'publisherId':publisher_id})
    for i in content:
        print i['publisher']['username']

def get_adn_mysql():
    sql = 'select promote_url,direct_url from campaign_list limit 1'
    results = get_adn_mysql_sql(sql)
    print results 

def get_adn_psql(channel_id):
    sql = 'select count(*), campaign_id from log_click where extra10=6 and date=%s group by campaign_id' % ('20160517')
    results = get_adn_psql_sql(sql)
    print results

def main():
    get_3s_channel(441)
    get_3s_psql(441)
    get_adn_mongo(6028)
    get_adn_mysql()
    get_adn_psql(123)

if __name__ == "__main__":
    main()
