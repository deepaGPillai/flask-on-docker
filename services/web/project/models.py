from . import db

class Customer(db.Model):
    __tablename__ = 'customer'

    id = db.Column(db.Integer, primary_key=True)
    event_id = db.Column(db.String, unique=True)
    payment_id = db.Column(db.Integer, unique=True, nullable=False)
    push_token = db.Column(db.Integer, unique=True, nullable=False)

    def __init__(self, event_id, payment_id, push_token):
        self.event_id = event_id
        self.payment_id =  payment_id
        self.push_token = push_token

class Verify_Phone(db.Model):
    __tablename__ = 'verify_phone'

    id = db.Column(db.Integer, primary_key=True)
    phone = db.Column(db.Integer, nullable=False)
    otp = db.Column(db.Integer, nullable=False)
    created = db.Column(db.Boolean)
    active = db.Column(db.Boolean)
    custom_id = db.Column(db.Integer, db.ForeignKey('customer.id'))
    event_id = db.Column(db.String, db.ForeignKey('customer.event_id'))

    def __init__(self, phone, otp, created, active, customer_id, event_id ):
        self.phone = phone
        self.otp =  otp
        self.created = created
        self.active = active
        self.custom_id = customer_id
        self.event_id = event_id


class Transaction(db.Model):
    __tablename__ = 'transaction'

    id = db.Column(db.Integer, primary_key=True)
    custom_id = db.Column(db.Integer, db.ForeignKey('customer.id'))
    event_id = db.Column(db.String, db.ForeignKey('customer.event_id'))
    auth_amount = db.Column(db.Integer)
    settle_amount = db.Column(db.Integer)
    created = db.Column(db.Boolean)
    completed = db.Column(db.Boolean)
    status = db.Column(db.String)
    reason = db.Column(db.String)

    def __init__(self, custom_id, event_id, auth_amount, settle_amount, created, completed, status, reason):
        self.custom_id = custom_id
        self.event_id = event_id
        self.auth_amount = auth_amount
        self.settle_amount = settle_amount
        self.completed = completed
        self.created = created
        self.status = status
        self.reason = reason

class Result(db.Model):
    __tablename__ = 'results'

    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String)
    result_all = db.Column(db.String)
    result_no_stop_words = db.Column(db.String)
    test = db.Column(db.String)

    def __init__(self, url, result_all, result_no_stop_words, tets):
        self.url = url
        self.result_all = result_all
        self.result_no_stop_words = result_no_stop_words
        self.test = tets



class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(128), unique=True, nullable=False)
    active = db.Column(db.Boolean(), default=True, nullable=False)

    def __init__(self, email):
        self.email = email
