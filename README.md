# nginx-cookie-stick
POC to test cookie stickiness on nginx 1.7+ and real time nginx reload

## How to use
This only runs on linux machines because it requires NGINX+ which is the commercial 
version of nginx.  If you want to play around with it I suggest that you do the 30 day
free trial for now but it will require a phone call from a sales person so be warned
if you do not want to deal with human interaction.
- install nginx+ - the instructions they provide should suffice
- sudo ./startup.sh
- virtualenv venv
- source venv/bin/activate
- pip install -r requirements.txt
- python servers.py


## Killing nginx processes quickly
- ps -ef | grep nginx | grep master | awk '{print $2}' | sudo xargs kill