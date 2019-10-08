from flask import Flask, render_template

app = Flask (__name__)

@app.route('/') # décorators
def home():
    return render_template('pages/home.html')

@app.route('/about') # décorators
def about():
    return render_template('pages/about.html')

@app.route('/contact') # décorators
def contact():
    return render_template('pages/contact.html')


@app.errorhandler(404)
def page_not_found(error):
    return render_template('errors/404.html'), 404



""" 
if __name__ == "__main__":
    app.run(debug=True, host='', port=3000)
"""