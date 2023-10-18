from flask import (Flask, render_template, request, redirect, url_for)
from time import time

import main_web

#%%
app = Flask(__name__)

@app.route('/')
def index():
    topic = 'Поисковик'
    return render_template("index.html", topic=topic)

@app.route('/search')
def search():
    return render_template('search.html')

@app.route('/process')
def process():
    if not request.args:
        return redirect(url_for('index'))
    
    if request.args.get('query'):
        q = request.args.get('query')
    else:
        q = 'телефон'
    
    i = request.args.get('index_type')
    if request.args.get('n'):
        n = int(request.args.get('n'))
    else:
        n = 2
        
    start = time()
    
    result = main_web.make_query(query=q, index_type=i, n=n)
    
    end = time()
    
    return render_template(
        'result.html', execution_time=end - start, docs=result
        )

#%%

if __name__ == '__main__':
    app.run()