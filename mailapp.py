from flask import Flask, render_template, request, redirect, flash
import views
from flask.ext.pymongo import PyMongo


app = Flask(__name__)
app.secret_key = 'aaa'
mongo = PyMongo(app)
users = {'user': 'sem', 'passwd': 1234}


@app.route('/s/<name>')
def hello_world(name):
	return render_template('index.html', name=name)
@app.route('/')
def helo():
	name ='my name'
	for x in xrange(1,10):
		flash("helo world")
	return render_template('index.html',name = name)

@app.route('/register', methods=['GET', 'POST'])
def submit():
    form = views.MyForm()
    if form.validate_on_submit():
    	if request.method=='POST':
    		if users['user']==request.form['name'] :
    			return request.form['name']+request.form['passwd']
	flash('Err '+request.form['name']+request.form['passwd']+'incurrect')
    return render_template('register.html', form=form)
@app.route('/success', methods=['GET', 'POST'])
def succes():
	if request.method=='POST':
		return request.form['name'],request.form['passwd']
	return render_template('register.html')

if __name__ == '__main__':
	app.debug = True
	app.run()