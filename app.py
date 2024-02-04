from flask import Flask, render_template

app = Flask(__name__, static_url_path='/static', template_folder='templates')


@app.route('/')
def index():
    # Pass prediction result to the HTML template
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
