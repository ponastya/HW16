import json
from classes import *


@app.route("/users", methods=["GET", "POST"])
def users():
    if request.method == "GET":
        result = []
        for u in User.query.all():
            result.append(u.to_dict())

        return json.dumps(result), 200, {'Content-Type': 'application/json; charset=utf-8'}

    elif request.method == "POST":
        user_data = json.loads(request.data)

        db.session.add(
            User(
                id=user_data.get('id'),
                first_name=user_data.get('first_name'),
                last_name=user_data.get('last_name'),
                age=user_data.get('age'),
                email=user_data.get('email'),
                role=user_data.get('role'),
                phone=user_data.get('phone'),
            )
        )
        db.session.commit()

        return "", 201


@app.route("/users/<int:uid>", methods=["GET", "PUT", "DELETE"])
def user(uid: int):
    if request.method == "GET":
        return json.dumps(User.query.get(uid).to_dict()), 200, {'Content-Type': 'application/json; charset=utf-8'}
    elif request.method == "PUT":
        user_data = json.loads(request.data)
        u = User.query.get(uid)
        u.first_name=user_data["first_name"]
        u.last_name=user_data["last_name"]
        u.age=user_data["age"]
        u.email=user_data["email"]
        u.role=user_data["role"]
        u.phone=user_data["phone"]

        db.session.add(u)
        db.session.commit()

        return "", 201

    elif request.method == "DELETE":
        u = User.query.get(uid)

        db.session.delete(u)
        db.session.commit()

        return "", 204



@app.route("/orders", methods=["GET", "POST"])
def orders():
    if request.method == "GET":
        result = []
        for u in Order.query.all():
            result.append(u.to_dict())

        return json.dumps(result), 200, {'Content-Type': 'application/json; charset=utf-8'}

    elif request.method == "POST":
        order_data = json.loads(request.data)

        db.session.add(
            Order(
                id=order_data.get('id'),
                name=order_data.get('name'),
                description=order_data.get('description'),
                start_date=order_data.get('start_date'),
                end_date=order_data.get('end_date'),
                address=order_data.get('address'),
                price=order_data.get('price'),
                customer_id=order_data.get('customer_id'),
                executor_id=order_data.get('executor_id'),
            )
        )
        db.session.commit()

        return "", 201

@app.route("/orders/<int:uid>", methods=["GET", "PUT", "DELETE"])
def order(uid: int):
    if request.method == "GET":
        return json.dumps(Order.query.get(uid).to_dict()), 200, {'Content-Type': 'application/json; charset=utf-8'}

    elif request.method == "PUT":
        order_data = json.loads(request.data)
        o = Order.query.get(uid)

        o.name=order_data["name"]
        o.description=order_data["description"]
        o.start_date=order_data["start_date"]
        o.end_date=order_data["end_date"]
        o.address=order_data["address"]
        o.price=order_data["price"]
        o.customer_id=order_data["customer_id"]
        o.executor_id=order_data["executor_id"]

        db.session.add(o)
        db.session.commit()

        return "", 201

    elif request.method == "DELETE":
        o = Order.query.get(uid)

        db.session.delete(o)
        db.session.commit()

        return "", 204

@app.route("/offers", methods=["GET", "POST"])
def offers():
    if request.method == "GET":
        result = []
        for u in Offer.query.all():
            result.append(u.to_dict())

        return json.dumps(result), 200, {'Content-Type': 'application/json; charset=utf-8'}

    elif request.method == "POST":
        offers_data = json.loads(request.data)

        db.session.add(
            Offer(
                id=offers_data.get('id'),
                order_id=offers_data.get('order_id'),
                executor_id=offers_data.get('executor_id'),
            )
        )
        db.session.commit()

        return "", 201


@app.route("/offers/<int:uid>", methods=["GET", "PUT", "DELETE"])
def offer(uid: int):
    if request.method == "GET":
        return json.dumps(Offer.query.get(uid).to_dict()), 200, {'Content-Type': 'application/json; charset=utf-8'}

    elif request.method == "DELETE":
        o = Offer.query.get(uid)

        db.session.delete(o)
        db.session.commit()

        return "", 204

    elif request.method == "PUT":
        offer_data = json.loads(request.data)
        o = Offer.query.get(uid)

        o.order_id = offer_data["order_id"]
        o.executor_id = offer_data["executor_id"]

        db.session.add(o)
        db.session.commit()

        return "", 201



if __name__ == '__main__':
    init_database()
    app.run(host='0.0.0.0', port=80, debug=True)
