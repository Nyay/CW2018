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
    lex_gr = search.lexgram_search(gr, lex)
    if type(search.search_word(word)) is list:
        ids = search.search_word(word)
    else:
        print(type(search.search_word(word)))
        ids = []

    return render_template('result.html', ids=ids, ids3=lex_gr, title='Result')
