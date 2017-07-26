from flask import Flask, render_template
from flask import request
from werkzeug.contrib.fixers import ProxyFix

from MainAlgorithm import allocatedVideo

app = Flask(__name__)


@app.route('/')
def entry_point():
    return render_template('InitialPage.html')


@app.route('/query', methods=['POST'])
def query():
    users = request.form['Users']
    reviewCount = request.form['ReviewCount']
    videoAllocation = allocatedVideo(n=users, m=reviewCount)
    return render_template("Result.html", user_list=videoAllocation)

app.wsgi_app = ProxyFix(app.wsgi_app)

if __name__ == '__main__':
    app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
    app.run()
