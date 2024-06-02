## building url dynamically
## flask variable rules and url building

from flask import Flask , redirect, url_for

app= Flask(__name__)


@app.route('/')
def welcome():
    return "bla"



@app.route('/success/<int:score>') # variable rules 
def success(score):
    return "the person has passed with score "+ str(score)

@app.route('/fail/<int:score>') # variable rules 
def fail(score):
    return "the person has failed with score "+ str(score)

## result checker
@app.route('/results/<int:marks>') # variable rules 
def results(marks):
   result= ""
   if marks<50:
       result="fail"
   else:
       result='success'
   return redirect(url_for(result, score=marks))
    

if __name__== '__main__':
    app.run(debug=True)