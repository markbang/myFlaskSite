from flask import Flask
from spiders.pac import school_dorm

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    rest_elc = school_dorm.get_elc()
    return '宿舍剩余电量：'+ str(rest_elc)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True, threaded=True)
