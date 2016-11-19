from bottle import route, run, template, get, post, request, static_file, error, redirect, abort, response, view, install
from bottle.ext import sqlalchemy
import os
import json
from sqlalchemy import create_engine, Column, Integer, Sequence, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
engine = create_engine('sqlite:////tmp/mybottlenew.db', echo=True)

path = os.path.abspath(__file__)
dir_path = os.path.dirname(path)

install(sqlalchemy.Plugin(
    engine, # SQLAlchemy engine created with create_engine function.
    Base.metadata, # SQLAlchemy metadata, required only if create=True.
    keyword='db', # Keyword used to inject session database in a route (default 'db').
    create=True, # If it is true, execute `metadata.create_all(engine)` when plugin is applied (default False).
    commit=True, # If it is true, plugin commit changes after route is executed (default True).
    use_kwargs=False # If it is true and keyword is not defined, plugin uses **kwargs argument to inject session database (default False).
))

class Entity(Base):
    __tablename__ = 'entity'
    id = Column(Integer, Sequence('id_seq'), primary_key=True)
    title = Column(String(50))
    content = Column(String(50))

    def __init__(self, title, content):
        self.title = title
        self.content = content

    def __repr__(self):
        return "<Entity('%d', '%s', '%s')>" % (self.id, self.title, self.content)


@route('/query')
def query():
	return template('query.tpl')

@post('/query')
def do_query(db):
    title = request.forms.get('title')

    draw = request.forms.get('draw')
    start = request.forms.get('start')
    length = request.forms.get('length')

    recordsTotal = db.query(Entity).filter_by(title=title).count()
    recordsFiltered = recordsTotal

    entities = db.query(Entity).filter_by(title=title).offset(start).limit(length)
    data=[]
    for entity in entities:
        row={}
        row['id']=entity.id
        row['title']=entity.title
        row['content']=entity.content
	data.append(row)

    result={"draw":draw,"recordsTotal":recordsTotal,"recordsFiltered":recordsFiltered,"data":data}
    resultJson=json.dumps(result)
    return resultJson

@route('/')
def index():
    if islogin():
        redirect('/query')
    else:
        redirect('/login')

@get('/insert') 
def insert():
    if isallow():
        return template('insert.tpl')
    else:
        return template('deny.tpl')

@post('/insert')
def do_insert(db):
    title = request.forms.get('title')
    content = request.forms.get('content')
    entity = Entity(title,content)
    db.add(entity)
    return template('postinsert.tpl')

@get('/login') # or @route('/login')
def login():
    return template('login.tpl')

@post('/login') # or @route('/login', method='POST')
def do_login():
    username = request.forms.get('username')
    password = request.forms.get('password')
    if check_login(username, password):
        response.set_cookie("account", username, secret='some-secret-key')
        return template("postlogin.tpl")
    else:
        return template("faillogin.tpl")

def check_login(username, password):
    if username=='cshan' and password == 'cshan':
        return True
    else:
        return False

#static files: html,css,images,text,...
@route('/static/<filename>')
def server_static(filename):
    return static_file(filename, root='/home/shanhongjie/test/tmp')

@error(404)
def error404(error):
    return 'Nothing here, sorry'

@route('/test')
def test():
    if isallow():
	    return "allow"
    else:
	    return "deny"

@route('/wrong2')
def restricted():
    abort(401, "Sorry, access denied.")

def islogin():
    if request.get_cookie("account", secret='some-secret-key'):
        return True
    else:
        return False

def isallow():
    name=request.get_cookie("account", secret='some-secret-key')
    if name == "cshan":
        return True
    else:
        return False


@route('/<filename:path>')
def send_static(filename):
    return static_file(filename, root=dir_path+'/'+'assets/') 

run(host='localhost', port=8787, debug=True, reloader=True)
