from flask_sqlalchemy import SQLAlchemy
import raw_data

from flask import Flask, request

app = Flask(__name__)
db = SQLAlchemy(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False



# модель для базы данных
class User(db.Model):
    __tablename__ = 'user'
    id: int = db.Column(db.Integer, primary_key=True)
    first_name: str = db.Column(db.String(100))
    # Text - есть знаки препинания, пробелы, разделители по строкам
    last_name: str = db.Column(db.String(100))
    age: int = db.Column(db.Integer)
    email: str = db.Column(db.String(100))
    role: str = db.Column(db.String(100))
    phone: str = db.Column(db.Text(100))

    # преобразование модели в словарь
    def to_dict(self):
        return {
            "id": self.id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "age": self.age,
            "email": self.email,
            "role": self.role,
            "phone": self.phone,
        }


# модель для базы данных
class Order(db.Model):
    __tablename__ = 'order'
    id: int = db.Column(db.Integer, primary_key=True)
    name: str = db.Column(db.String(100))
    description: str = db.Column(db.String(100))

    start_date = db.Column(db.String(100))
    end_date = db.Column(db.String(100))

    address: str = db.Column(db.String(100))
    price: int = db.Column(db.Integer())

    customer_id: int = db.Column(db.Integer(), db.ForeignKey(f'{User.__tablename__}.id'))
    executor_id: int = db.Column(db.Integer(), db.ForeignKey(f'{User.__tablename__}.id'))

    # преобразование модели в словарь
    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "start_date": self.start_date,
            "end_date": self.end_date,
            "address": self.address,
            "price": self.price,
            "customer_id": self.customer_id,
            "executor_id": self.executor_id,
        }


# модель для базы данных
class Offer(db.Model):
    __tablename__ = 'offer'
    id: int = db.Column(db.Integer, primary_key=True)
    order_id: str = db.Column(db.String(100), db.ForeignKey(f'{User.__tablename__}.id'))
    executor_id: str = db.Column(db.String(100), db.ForeignKey(f'{Order.__tablename__}.id'))

    # преобразование модели в словарь
    def to_dict(self):
        return {
            "id": self.id,
            "order_id": self.order_id,
            "executor_id": self.executor_id,
        }


def init_database():
    db.drop_all()
    db.create_all()

    for user_data in raw_data.users:
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

    for order_data in raw_data.orders:
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

    for offer_data in raw_data.offers:
        db.session.add(
            Offer(
                id=offer_data.get('id'),
                order_id=offer_data.get('order_id'),
                executor_id=offer_data.get('executor_id'),
            )
        )
        db.session.commit()

