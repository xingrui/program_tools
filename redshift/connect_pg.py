import psycopg2
conn = psycopg2.connect(database = "mob1log", user = "mob_tech", password = "Pr3j5KcQlM16",host = "datastore-redshift.lenzmx.com", port = "5439")
cur = conn.cursor()
cur.execute('select * from %s where network=%s limit 1' % ('mob_click_log', '441'))
row = cur.fetchone()
print row
