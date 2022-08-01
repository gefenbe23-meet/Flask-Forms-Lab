from flask import Flask, jsonify, request, render_template, redirect, url_for
import random

app = Flask(  # Create a flask app
	__name__,
	template_folder='templates',  # Name of html file folder
	static_folder='static'  # Name of directory for static files
)


username = "GefenBE"
password = "Gefen16"
facebook_friends=["Mia","Tal","Geffen", "Ruth", "Yuvv", "Ofir", "Yair"]


@app.route('/',methods=['GET', 'POST'])  # '/' for the default page
def login():
	if request.method== 'GET':
		return render_template('login.html')
	else:
		username=request.form['username']
		password=request.form['password']
		return redirect(url_for('home',username=username))

@app.route ('/home')
def home ():
	return render_template('home.html', facebook_friends=facebook_friends)

@app.route('/friend_exists',methods=['GET', 'POST'])  # '/' for the default page
def friend_exists():
	if request.method== 'GET':
		return render_template('login.html')
	else:
		username=request.form['username']
		password=request.form['password']
		return redirect(url_for('home',username=username))


if __name__ == "__main__":  # Makes sure this is the main process
	app.run( # Starts the site
    debug=True
	)