from flask import Flask, render_template
app = Flask(__name__)

@app.route('/home')
def index():
	return '<h1>Flask is frábært...</h1><a href="/sida1">Siða 1</a><h1></h1><a href="/sida2">Spurningar</a> '

@app.route('/sida1')
def sida1():
	return '<h1>siða 1, nu er gaman...</h1><a href="/home">Forsíða</a>' 

@app.route('/sida2')
def sida2():
	return render_template("http.html")

if __name__ == "__main__":
	app.run(debug=True)
