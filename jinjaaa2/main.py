## integrate html with flask
## http verb get snd push


'''
{% %} for statements
{{}} 
{# #}
'''


from flask import Flask , redirect, url_for,render_template, request

app= Flask(__name__)


@app.route('/')
def welcome():
    return render_template('index.html')



@app.route('/success/<int:score>') # variable rules 
def success(score):
    res=""
    if score>=50:
        res='pass'
    else:
        res='fail'
    exp={'score':score,'res':res }
    return render_template('result.html',result=exp)

@app.route('/fail/<int:score>') # variable rules 
def fail(score):
   return "marks" + str(score)

## result checker
@app.route('/results/<int:marks>') # variable rules 
def results(marks):
   result= ""
   if marks<50:
       result="fail"
   else:
       result='success'
   return redirect(url_for(result, score=marks))
    
# result checker html page
@app.route('/submit',methods=['POST','GET'])
def submit():
    total_score=0
    if request.method=='POST':
        science=float(request.form['science'])
        maths=float(request.form['maths'])
        c=float(request.form['c'])
        english=float(request.form['english'])
        total_score=(science+maths+c+english)/4
    res=''
    if total_score>=50:
        res="success"
    else:
        res="fail"
    return redirect(url_for(res,score=total_score))

if __name__== '__main__':
    app.run(debug=True)