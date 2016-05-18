
import redis
import MySQLdb
import json
import psycopg2
from pymongo import MongoClient

def get_3s_redis_connection():
    r = redis.Redis(host = '192.168.1.17', port = 6480, db = 0, password='123456')
    return r

def get_3s_key(key_id):
    r = get_3s_redis_connection()
    res = r.get(key_id)
    return res

def get_3s_psql_connection():
    conn = psycopg2.connect(database = "mob1log", user = "mob_tech", password = "Pr3j5KcQlM16",host = "datastore-redshift.lenzmx.com", port = "5439") 
    return conn

def get_3s_psql_sql(sql):
    conn = get_3s_psql_connection()
    cur = conn.cursor()
    cur.execute(sql)
    results = cur.fetchall()
    cur.close()
    conn.close()
    return results

def get_adn_mongo_connection():
    conn = MongoClient("192.168.1.54", 27017)
    return conn

def get_adn_mysql_connection():
    conn = MySQLdb.connect(host = 'adn-mysql-external.mobvista.com', user = 'mob_adn_ro', passwd = 'blueriver123', db = 'mob_adn')
    return conn

def get_adn_mysql_sql(sql):
    conn = get_adn_mysql_connection()
    cur = conn.cursor()
    cur.execute(sql)
    result = cur.fetchall()
    cur.close()
    conn.close()
    return result

def get_adn_psql_connection():
    conn = psycopg2.connect(database = "data", user = "root", password = "adn2015DATA", host = "adn-adserver-datamining.mobvista.com", port = "5439") 
    return conn

def get_adn_psql_sql(sql):
    conn = get_adn_psql_connection()
    cur = conn.cursor()
    sql = 'select count(*), campaign_id from log_click where extra10=6 and date=%s group by campaign_id' % ('20160322')
    cur.execute(sql)
    results = cur.fetchall()
    cur.close()
    conn.close()
    return results
