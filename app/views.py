from flask import render_template, request
from app import app
from app import search


@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html",
                           title='Home')


@app.route('/form')
def form():
    word = request.args['word']
    print(word)
    lex = request.args['lex']
    ids = search.search_word(word)
    print(ids)
    gr = search.search_gram(request.args['gr'])
    print(gr)
    return render_template('result.html', ids=ids,
                           ids2=search.search_lex(lex),
                           ids3=gr, title='Result')
