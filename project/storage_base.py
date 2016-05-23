import time
import csv
import sys
import datetime
import os
import redis
import MySQLdb
import json
import psycopg2
import functools 
import pickle
import urllib
from pymongo import MongoClient

valid_domain = ['app.appsflyer.com', 'app.adjust.io', 'app.adjust.com', 'control.kochava.com', 'ad.apsalar.com', 'measurementapi.com', '.api-0', 'app-adforce', 'track.uri6.com', 'lnk8.cn']
def get_domain_name(domain):
    global valid_domain
    if domain in valid_domain:
        return domain
    for d in valid_domain:
        if domain.find(d) != -1:
            return d
    return None

def add_map_count(k_v_map, key):
    if key not in k_v_map:
        k_v_map[key] = 1
    else:
        k_v_map[key] += 1

def get_hostname(url):
    proto, rest = urllib.splittype(url)
    host, rest = urllib.splithost(rest) 
    return host

def get_date():
    if len(sys.argv) == 1:
        yesterday = datetime.date.today() - datetime.timedelta(days=1)
        date_str = yesterday.strftime('%Y%m%d')
    else:
        date_str = sys.argv[1]
    return date_str

def date_to_start_end_ts(time_str):
    start_ts = date_to_timestamp(time_str)
    end_ts = start_ts + 24 * 60 * 60
    return start_ts, end_ts

def date_to_timestamp(time_str):
    time_array = time.strptime(time_str, "%Y%m%d")
    timestamp = int(time.mktime(time_array))
    return timestamp

def timestamp_to_date(timestamp):
    x = time.localtime(timestamp)
    res = time.strftime('%Y-%m-%d %H:%M:%S',x)
    return res 

def dump_file_wrapper(dump_file_name, func):
    dump_file_name = './data/' + dump_file_name
    if os.path.exists(dump_file_name):
        results = pickle.load(open(dump_file_name))
    else:
        results = func()
        pickle.dump(results, open(dump_file_name, 'w'))
    return results

def get_3s_redis_connection():
    r = redis.Redis(host = '192.168.1.17', port = 6480, db = 0, password='123456')
    return r

def get_3s_key(key_id):
    r = get_3s_redis_connection()
    res = r.get(key_id)
    return res

def get_3s_hget(key, key_id):
    r = get_3s_redis_connection()
    res = r.hget(key, key_id)
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
    cur.execute(sql)
    results = cur.fetchall()
    cur.close()
    conn.close()
    return results
