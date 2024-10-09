from flask import Flask, jsonify, request, make_response
import requests

app = Flask(__name__)

product_db = []
data = requests.get('https://dummyjson.com/products')
product_db = data.json()['products'] 

#find alle products
@app.route('/products', methods=['GET'])
def get_all_products():
    return jsonify(product_db), 200

@app.route('/product/search/<string:title>', methods=['GET'])
def get_product_by_title(title):
    for product in product_db:
        if product['title'].lower() == title.lower():
            return jsonify(product), 200

         

app.run(debug=True, host='0.0.0.0')