from flask import Flask
import requests
import json
import csv
import gzip
import shutil
import os


lstfinal = [] # list to keep the items is sorted order by price hence making 'N cheapest products' API a constant time operation
dict = {} #dictionary to keep item with id as key and details as value to make 'retrieve a single product by its id' API a constant time O(1) operation


def create_app():
    #download file from amazon s3
    url = 'https://s3-eu-west-1.amazonaws.com/pricesearcher-code-tests/python-software-developer/products.json'
    r = requests.get(url, allow_redirects=True)
    open('products.json', 'wb').write(r.content)
    lstfinalnew=[]
    
    #parse and load the data from file into the list and dictionary
    with open('products.json', 'r') as f:
        lst = json.load(f)
        for prod in lst:
            dict[prod['id']] = prod
            if 'price' in prod and prod['price'] != '' and prod['price'] is not None:
                prod['price'] = float(str(prod['price']))
                lstfinal.append(prod)
    
    #unzip the second file           
    if os.path.exists('products.csv.gz'): # Assuming the file exists in the same directory
        with gzip.open('products.csv.gz', 'rb') as f_in:
            if not os.path.exists('products.csv'):
                with open('products.csv', 'wb') as f_out:
                    shutil.copyfileobj(f_in, f_out)
                    
    #parse and load the data from this file into list and dictionary                
    if os.path.exists('products.csv'):        
        with open('products.csv') as reader:
            csvobj = csv.reader(reader)
            next(csvobj, None)
            for row in csvobj:
                row[4] = row[4].replace(' ','').replace('"','')
                value = "{{'id' : '{0}', 'name' : '{1}', 'brand' : '{2}', 'retailer' : '{3}', 'price' : {4}, 'in_stock' : '{5}'}}".format(row[0],row[1],row[2],row[3],row[4],row[5])
                dict[row[0]] = value
                if row[4] is  None or row[4] == '':
                    continue
                else:
                    import ast
                    value = ast.literal_eval("{{'id':'{0}','name':'{1}','brand':'{2}','retailer':'{3}','price':'{4}','in_stock':'{5}'}}".format(row[0],row[1],row[2],row[3],row[4],row[5]))
                    value['price'] = float(value['price'])
                    lstfinal.append(value)
                
     
    #sort the values in list based on price          
    from operator import itemgetter         
    lstfinal.sort(key=itemgetter('price'))
    
    #start the api server with endpoints given
    app = Flask(__name__)
    from psearch.search.routes import search
    app.register_blueprint(search)
    return app