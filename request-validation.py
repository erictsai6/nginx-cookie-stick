'''
Runs many fresh requests against the designated ninjutsu URL and keeps 
count of the breakdown.  Validates that the weight provided is accurate 
'''

import requests
import argparse

parser = argparse.ArgumentParser(description='Request Validation')
parser.add_argument('-n', '--number', type=int, help='Number of requests to trigger', default=1000)
parser.add_argument('--host', type=str, help='Ninjutsu server to hit', default='http://localhost:5000')

args = parser.parse_args()

def main():

    global args

    count_dict = {}

    print 'Starting request validation'

    number = args.number
    host = args.host
    
    for i in range(0, number):
        r = requests.get(host)
        port_num = str(r.json()['port'])
        count_dict[port_num] = count_dict.get(port_num, 0) + 1

    for k in count_dict:
        print k, ':', count_dict[k]

    print 'Finished request validation'

if __name__ == '__main__':
    main()