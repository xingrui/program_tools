import sys
import csv

def main():
    csv_writer = csv.writer(sys.stdout)
    csv_writer.writerow(['campaign_id','injected_cvr','normal_cvr','injected_install', 'injected_click', 'normal_install', 'normal_click'])
    csv_writer.writerow([1,2,3,"4",True,False,'7',float(9)])
    csv_writer.writerow([',,,,,', 123, 456])

if __name__ == "__main__":
    main()
