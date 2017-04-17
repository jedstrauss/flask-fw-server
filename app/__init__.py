import sys
from flask import Flask, request

fw_path = ''
fw_folder = 'static'
br_path = fw_path + '/br/'
br_folder = 'app/' + fw_folder + br_path
app = Flask(__name__, static_url_path=fw_path, static_folder=fw_folder)

@app.route(br_path + '<filename>', methods=['PUT'])
def br_put(filename):
    print br_folder + filename
    try:
        with open(br_folder + filename, 'w+') as f:
            f.write(request.data)
    except:
        e = sys.exc_info()
        print "Error: {0}".format(e)
        return "Internal Server Error\n",500
    else:
        return "OK\n",200
