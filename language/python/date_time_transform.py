import time

def date_to_timestamp(time_str):
    time_array = time.strptime(time_str, "%Y%m%d")
    timestamp = int(time.mktime(time_array))
    return timestamp

def main():
    timestamp = date_to_timestamp('20160517')
    print timestamp

if __name__ == "__main__":
    main()
