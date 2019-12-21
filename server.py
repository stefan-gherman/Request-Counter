from flask import Flask, request, render_template, redirect, url_for
import helper as helper
app = Flask(__name__)

method_count = {'GET': 0, 'POST': 0, 'PUT': 0, 'DELETE': 0}
@app.route('/', methods = ['GET', 'POST', 'DELETE', 'PUT'])
def go_home():
    return render_template('index.html')


@app.errorhandler(404)
def return_404(string = 'string'):
    return render_template('404_handler.html')

@app.route('/statistics')
def return_stats():
    return render_template('stats.html', method_count = method_count)

if __name__ == '__main__':
    app.run(debug=True,
            host='0.0.0.0',
            port=7000)
