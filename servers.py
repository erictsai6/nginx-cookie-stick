import argparse
from src.workers.server_spawn import ServerSpawn
import signal
import sys
import time

parser = argparse.ArgumentParser(description='Servers Spawn Script')
parser.add_argument('-p', '--port', type=int, help='Starting port number for the servers, increments port # with each server', default=5001)
parser.add_argument('-n', '--number', type=int, help='Number of servers to spawn', default=1)

args = parser.parse_args()

def signal_handler(signal, frame):
    print('Killing the spawned servers')
    sys.exit(0)

def main():

    global args
    global app

    signal.signal(signal.SIGINT, signal_handler)

    print 'Servers script - spawns multiple servers'

    number_of_servers = args.number
    starting_port = args.port

    server_list = []

    for i in range(0, number_of_servers):
        print 'server localhost:' + str(starting_port + i) + ' weight=1;'
        server_list.append(ServerSpawn(starting_port + i))
        server_list[i].daemon = True
        server_list[i].start()
    
    # Sleeps until interrupted
    while True: 
        time.sleep(100)
    
if __name__ == '__main__':
    main()