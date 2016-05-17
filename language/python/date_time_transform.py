import time

def date_to_timestamp(time_str):
    time_array = time.strptime(time_str, "%Y%m%d")
    timestamp = int(time.mktime(time_array))
    return timestamp

def timestamp_to_date(timestamp):
    x = time.localtime(timestamp)
    res = time.strftime('%Y-%m-%d %H:%M:%S',x)
    return res

def main():
    timestamp = date_to_timestamp('20160517')
    print timestamp
    print timestamp_to_date(timestamp)

if __name__ == "__main__":
    main()
