from flask import Flask
#WSGI application:  standard used to communicate between web server and web applications
app=Flask(__name__)

@app.route('/')  #decorator... it has 2 parameters: rule and options
def welcome():
    return "heeloooooooo"



if  __name__=='__main__':
    app.run(debug=True)  