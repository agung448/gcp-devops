
from Flask import Flask 
app = Flask(__name__)

@app.route('/') 
def index ():
    return 'Welcome to the flask world version2 update '

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8080)