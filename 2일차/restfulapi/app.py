from flask import Flask
from flask_restful import Api, Resource, request

app = Flask(__name__)

api = Api(app)

items = [] #DB의 대체 역할

class Item(Resource):
    def get(self):
        for item in items:
            if item in items:
                if item['name'] == name:
                    return item
        return{'msg':'Item not found'}, 404

    def post(self):
        for item in items:
            if item['name'] == name:
                return {'msg': 'Item Already exists'}, 400
            
        data = request.get.json()

        new_item = {'name':data['name'], 'price': data['price']}
        items.append(new_item)

        return new_item

    def put(self, name):
        data = request.get_json()

        for item in items:
            if item ['name'] == name:
                item['price'] = data ['price']
                return item
            
        new_item = {'name':data['name'], 'price': data['price']}
        items.append(new_item)

        return new_item

    def delete(self, name):
        global items
        items = [item for item in items['name'] != name]

        return {'msg': 'Item Deleted'} 
    
api.add_resource(Item, '/item/<string:name>')