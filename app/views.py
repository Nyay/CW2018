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
    lex = request.args['lex']
    gr = request.args['gr']
    if type(search.search_word(word)) is list:
        ids = search.search_word(word)
    else:
        print(type(search.search_word(word)))
        ids = []
    if type(search.search_lex(lex)) is list:
        ids2 = search.search_lex(lex)
    else:
        print(type(search.search_lex(lex)))
        ids2 = []
    if type(search.search_gram(gr)) is list:
        ids3 = search.search_gram(gr)
    else:
        print(type(search.search_gram(gr)))
        ids3 = []
    print(ids3)
    return render_template('result.html', ids=ids,
                           ids2=ids2, ids3=ids3, title='Result')
