from flask import Flask, request, render_template, redirect, url_for
import helper as helper

app = Flask(__name__)

filename = './data/counts.txt'

@app.route('/')
@app.route('/index', methods=['GET', 'POST', 'DELETE', 'PUT'])
def go_home():

    return render_template('index.html')


@app.errorhandler(404)
def return_404(string='string'):
    return render_template('404_handler.html')


@app.route('/statistics')
def return_stats():
    method_count = helper.create_dict_from_file(filename)
    return render_template('stats.html', method_count=method_count)

@app.route('/request-counter', methods=['GET', 'POST', 'DELETE', 'PUT'])
def count_req():
    method_count = helper.create_dict_from_file(filename)
    if request.method in method_count.keys():
        method_count[request.method] += 1
        method_count = helper.sort_dict(method_count)
        helper.write_dict_to_file(method_count, filename)
    return redirect(request.referrer)
if __name__ == '__main__':
    app.run(debug=True,
            host='0.0.0.0',
            port=7000)


