#!venv/bin/python
from app import app
import argparse

parser = argparse.ArgumentParser(description="firmware server dev mode")
parser.add_argument('--port',type=int,default=5000,help="listen port")
parser.add_argument('--external',action='store_true',help="make server available externally")
args = parser.parse_args()

if (args.external):
    host = '0.0.0.0'
else:
    host = '127.0.0.1'

if __name__ == "__main__":
    app.run(host=host,port=args.port)
