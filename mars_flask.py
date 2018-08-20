from flask import Flask, render_template
from flask import jsonify
from flask import request
from flask_pymongo import PyMongo

app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'mars_db'
app.config['MONGO_URI'] = 'mongodb://localhost:27017/mars_db'
mongo = PyMongo(app)

mars_dict = []
coll = mongo.db.mars_coll
for x in coll.find():
    mars_dict.append(x)

@app.route('/', methods=['GET'])
def homepage():
  return render_template('scrape_home.html')

@app.route('/scrape', methods=['GET'])
def scraped_page():
    print(mars_dict)
    return render_template('scrape_data.html', data = mars_dict[0])

app.run(debug=True, port=5545)