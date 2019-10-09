from flask import Flask, render_template, abort

from datetime import datetime

from flask_sqlalchemy import SQLAlchemy

#from mocks import Post

app = Flask (__name__)

#Database connection
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database/db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Post(db.Model):
    __tablename__ = 'posts'
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    content = db.Column(db.Text)
    
    def __repr__(self):
        return '<Post "{}">'.format(self.title)
    

#end Database connection


@app.context_processor
def inject_now():
    return dict(now=datetime.now())
    

@app.context_processor
def utility_processor():
    def pluralize(count, singular, plural=None):
        if not isinstance(count, int):
            raise ValueError('"{}" doit être un integer'.format(count))
        
        if plural is None:
            plural = singular + 's'
            
        if count == 1:
            string = singular
        else:
            string = plural
            
        return "{} {}".format(count, string)
            
    return dict(pluralize=pluralize)


@app.route('/') # décorators
def home():
    return render_template('pages/home.html')

@app.route('/about') # décorators
def about():
    return render_template('pages/about.html')

@app.route('/contact') # décorators
def contact():
    return render_template('pages/contact.html')

@app.route('/blog') # décorators
def posts_index():
    posts = Post.query.all()
    return render_template('posts/index.html', posts=posts)

@app.route('/blog/posts/<int:id>') #décorators #'id' parameter defined ?
def posts_show(id): #so define 'id' there also
    post = Post.query.get(id)
    
    if post is None:
        abort(404)
    
    return render_template('posts/show.html', post=post)

        

@app.errorhandler(404)
def page_not_found(error):
    return render_template('errors/404.html'), 404



db.create_all()

if __name__ == "__main__":
    
    app.run()
    
# debug=True, host='', port=5000