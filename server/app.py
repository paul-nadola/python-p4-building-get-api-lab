#LMS SOLUTION
from flask import Flask, make_response
from flask_migrate import Migrate

from models import db, Bakery, BakedGood

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

migrate = Migrate(app, db)

db.init_app(app)

@app.route('/')
def home():
    return '<h1>Bakery GET-POST-PATCH-DELETE API</h1>'

@app.route('/bakeries')
def bakeries():

    bakeries = Bakery.query.all()
    bakeries_serialized = [bakery.to_dict() for bakery in bakeries]

    response = make_response(
        bakeries_serialized,
        200
    )
    return response

@app.route('/bakeries/<int:id>')
def bakery_by_id(id):

    bakery = Bakery.query.filter_by(id=id).first()
    bakery_serialized = bakery.to_dict()

    response = make_response(
        bakery_serialized,
        200
    )
    return response

@app.route('/baked_goods/by_price')
def baked_goods_by_price():
    baked_goods_by_price = BakedGood.query.order_by(BakedGood.price).all()
    baked_goods_by_price_serialized = [
        bg.to_dict() for bg in baked_goods_by_price
    ]
    
    response = make_response(
        baked_goods_by_price_serialized,
        200
    )
    return response

@app.route('/baked_goods/most_expensive')
def most_expensive_baked_good():
    most_expensive = BakedGood.query.order_by(BakedGood.price.desc()).limit(1).first()
    most_expensive_serialized = most_expensive.to_dict()

    response = make_response(
        most_expensive_serialized,
        200
    )
    return response

if __name__ == '__main__':
    app.run(port=5555, debug=True)

#MY SOLUTION
# from flask import Flask, make_response, jsonify
# from flask_migrate import Migrate

# from models import db, Bakery, BakedGood

# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# app.json.compact = False

# migrate = Migrate(app, db)

# db.init_app(app)

# @app.route('/')
# def index():
#     return '<h1>Bakery GET API</h1>'

# @app.route('/bakeries')
# def bakeries():

#     bakeries = []
#     for bakery in Bakery.query.all():
#         bakery_dict = {
#             "id": bakery.id,
#             "name": bakery.name,
#             "created_at": bakery.created_at
#         }
#         bakeries.append(bakery_dict)
    
#     response = make_response(
#         jsonify(bakeries),
#         200
#     )
#     response.headers["Content-Type"] = "application/json"
#     return response

# @app.route('/bakeries/<int:id>')
# def bakery_by_id(id):
#     bakery = Bakery.query.filter_by(id = id).first()
#     if bakery is None:
#         return jsonify({'error': 'No bakery found'}), 404
#     bakery_dict = {
#         "id": bakery.id,
#         "name": bakery.name,
#         "created_at": bakery.created_at
#     }
#     # bakery_dict = bakery.to_dict()
#     response = make_response(
#         jsonify(bakery_dict), 200
#     )

#     response.headers["Content-Type"] = "application/json"
#     return response

# @app.route('/baked_goods/by_price')
# def baked_goods_by_price():
#     baked_goods = BakedGood.query.order_by(BakedGood.price.desc()).all()
#     if baked_goods is None:
#         return jsonify({'error': 'No baked goods found'}), 404
#     goods = []
#     for good in baked_goods:
#         goods_dict = {
#             "id": good.id,
#             "name": good.name,
#             "price": good.price,
#             "bakery_id": good.bakery_id,
#             "created_at": good.created_at,
#             "updated_at": good.updated_at
#         }
#         goods.append(goods_dict)
#     response = make_response(
#         jsonify(goods), 200
#     )

#     response.headers["Content-Type"] = "application/json"
#     return response

# @app.route('/baked_goods/most_expensive')
# def most_expensive_baked_good():
#     baked_good = BakedGood.query.order_by(BakedGood.price.desc()).first()
#     if baked_good is None:
#         return jsonify({'error': 'No baked goods found'}), 404
    
#     baked_good_dict = {
#             "id": baked_good.id,
#             "name": baked_good.name,
#             "price": baked_good.price,
#             "bakery_id": baked_good.bakery_id,
#             "created_at": baked_good.created_at,
#             "updated_at": baked_good.updated_at
#         }
#     response = make_response(
#         jsonify(baked_good_dict), 200
#     )
#     return response

# if __name__ == '__main__':
#     app.run(port=5555, debug=True)