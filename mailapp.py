from flask import Flask, render_template, request, redirect
import views

app = Flask(__name__)
app.secret_key = 'aaa'
users = [{'user': 'sem', 'passwd': 1234}]


@app.route('/s/<name>')
def hello_world(name):
	return render_template('index.html', name=name)
@app.route('/')
def helo():
	name ='my name'
	return render_template('index.html',name = name)

@app.route('/register', methods=['GET', 'POST'])
def submit():
    form = views.MyForm()
    if form.validate_on_submit():
        return redirect('/success')
    return render_template('register.html', form=form)
@app.route('/success', methods=['GET', 'POST'])
def succes():
	if request.method=='POST':
		return request.form['name'],request.form['passwd']
	print request.form['name']
	return submit()

if __name__ == '__main__':
	app.debug = True
	app.run()