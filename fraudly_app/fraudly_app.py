from flask import Flask, request
import cPickle as pickle
import pandas as pd
app = Flask(__name__)



@app.route('/register')



@app.route('/score')



if __name__ == '__main__':
	app.run(host='0.0.0.0', port=8080, debug=True)