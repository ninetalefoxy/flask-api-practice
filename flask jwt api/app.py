from flask import Flask, jsonify, request, make_response

app = Flask(__name__)




@app.route('/unprotected',methods=[])
def unprotected():
    return ''

@app.route('/protected',methods=[])
def protected():
    return ''

@app.route('/login')
def login():
    auth = request.authorization

    if auth and auth.password == 'password':
        return ''
    return make_response('Could Verify!',401,{'WWW-Authenticate':'Basic realm="Login Required"'})



if __name__ == "__main__":
    app.run(debug=True)