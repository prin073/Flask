# https://www.youtube.com/watch?v=PE9ZGniSDW8
# https://pythonhosted.org/Flask-Bootstrap/basic-usage.html#sample-application
# https://getbootstrap.com/docs/4.3/getting-started/introduction/

# https://getbootstrap.com/docs/4.3/components/alerts/  ==> Bootstrap components

# https://developers.google.com/speed/libraries/  ==> bootstrap src of google
# https://www.youtube.com/watch?v=S7ZLiUabaEo&t=42s  ===> Form bootstrap


from flask import Flask, render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
