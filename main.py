from bottle import route, run, template, get, post, request, static_file, error, redirect, abort, response, view, install
from bottle_sqlite import SQLitePlugin

install(SQLitePlugin(dbfile='/tmp/mybottle.db'))

@route('/query/<title>')
def show(db, title):
        c = db.execute('SELECT title, content FROM posts WHERE title = ?', (post_id,))
        row = c.fetchone()
        return template('query.tpl', title=row['title'], content=row['content'])

@route('/tpltest2/<name>/<fname>')
@view('hello_template')
def index(name,fname):
    return dict(name=name,fname=fname)

@route('/')
def index():
    if islogin():
        redirect('/query')
    else:
        redirect('/login')

@get('/insert') 
def insert():
    return template('insert.tpl')

@post('/insert')
def do_insert():
    title = request.forms.get('title')
    content = request.forms.get('content')
    db.execute('insert into posts values( ?,?)', (title,content))
    return 'done'

@get('/login') # or @route('/login')
def login():
    return template('login.tpl')

@post('/login') # or @route('/login', method='POST')
def do_login():
    username = request.forms.get('username')
    password = request.forms.get('password')
    if check_login(username, password):
        response.set_cookie("account", username, secret='some-secret-key')
        return "<p>Your login information was correct. You are now logged in.</p>"
    else:
        return "<p>Login failed.</p>"

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

@route('/wrong')
def wrong():
    redirect("/login")

@route('/wrong2')
def restricted():
    abort(401, "Sorry, access denied.")

def islogin():
    if request.get_cookie("account", secret='some-secret-key'):
        return True
    else:
        return False

run(host='localhost', port=8787, debug=True, reloader=True)
