from app import db
from sqlalchemy.dialects.postgresql import JSON


class Result(db.Model):
    __tablename__ = 'results'

    id = db.Column('id', db.Integer, primary_key=True)
    url = db.Column('url', db.String())
    result_all = db.Column(JSON)
    result_no_stop_words = db.Column(JSON)

    def __init__(self, url, result_all, result_no_stop_words):
        self.url = url
        self.result_all = result_all
        self.result_no_stop_words = result_no_stop_words

    def __repr__(self):
        return '<id {}>'.format(self.id)


class Test(db.Model):
	__tablename__="results"

	id1 = db.Column('id', db.Integer, primary_key=True)
    	url1 = db.Column('url', db.String())
    	result_all = db.Column(JSON)
    	result_no_stop_words = db.Column(JSON)

    	def __init__(self, url, result_all, result_no_stop_words):
        	self.url = url
	        self.result_all = result_all
        	self.result_no_stop_words = result_no_stop_words

    	def __repr__(self):
        	return '<id {}>'.format(self.id)
