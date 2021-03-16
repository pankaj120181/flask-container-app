from flask import Flask, render_template
from flask_bootstrap import Bootstrap


app = Flask(__name__)

bootstrap = Bootstrap(app)
app.config['BOOTSTRAP_BOOTSWATCH_THEME'] = 'cerulean'
#app.config['BOOTSTRAP_BOOTSWATCH_THEME'] = 'minty'



@app.route('/')
def home():
    return render_template('dogs.html')

@app.route('/blog')
def blog():
    return render_template('blog.html')

@app.route('/blog/2021/dogs')
def blog2021():
    return 'This is my blog on dogs year 2021!'


@app.route('/about')
def about():
    return 'This is about page!'

@app.route('/explore')
def explore():
    return 'Let\'s explore more on this!'

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)