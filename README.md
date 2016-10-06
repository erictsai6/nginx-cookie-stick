# nginx-cookie-stick
POC to test cookie stickiness on nginx 1.7+ and real time nginx reload

## How to use
This is assuming you are running on a Mac machine with homebrew already installed
- brew update
- brew install nginx
- nginx -h
  - verify nginx 1.7 or greater is installed
- nginx -c `pwd`/conf/ninjutsu.conf -p "`pwd`"
- virtualenv venv
- source venv/bin/activate
- pip install -r requirements.txt
- python servers.py -n 3


## Killing nginx processes quickly
- ps -ef | grep nginx | grep master | awk '{print $2}' | sudo xargs kill