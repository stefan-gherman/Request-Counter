from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)


@app.route('/')
def go_home():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True,
            host='0.0.0.0',
            port=7000)
