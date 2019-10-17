'''
Created on 16 Oct 2019

@author: Aruna
'''
from flask import request, Blueprint
from psearch import dict, lstfinal


search = Blueprint('search',__name__) # Blueprints help with the scalability. If we need a new component (E.g., error handling), we can create a new package and create a blueprint and register with the app

@search.route('/',methods=['GET'])
@search.route('/id/<id>',methods=['GET'])
def get_prod(id='101b64ee5c364ddd88ca953'):
    if id in dict:
        return dict[id]
    else:
        return '{"Msg":"Invalid ID"}'

@search.route('/cheap/<n>',methods=['GET'])
def get_cheap(n):
    if lstfinal:
        return ('\n'.join(map(str, lstfinal[0:int(n)])))
    else:
        return '{"Msg":"No items found"}'

    