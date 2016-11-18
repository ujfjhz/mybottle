from bottle import route, run, template, get, post, request, static_file, error, redirect, abort, response, view

@route('/hello/<name>/par1/<par1>')
def index(name,par1):
    return template('<b>Hello {{name}}{{par1}}</b>!', name=name, par1=par1)

@route('/tpltest1/<name>')
def index(name):
    return template('hello_template', name=name)

@route('/tpltest2/<name>/<fname>')
@view('hello_template')
def index(name,fname):
    return dict(name=name,fname=fname)

@get('/login') # or @route('/login')
def login():
    return '''
        <form action="/login" method="post">
            Username: <input name="username" type="text" />
            Password: <input name="password" type="password" />
            <input value="Login" type="submit" />
        </form>
    '''

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

@route('/hello')
def hello():
    if request.get_cookie("account", secret='some-secret-key'):
        return "you have already logged in, look around"
    else:
        return "please login first"

@route('/getname')
def getname():
    return request.cookies.account or 'Guest'

run(host='localhost', port=8787, debug=True, reloader=True)
