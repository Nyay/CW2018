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
    lex = [request.args['lex1'], request.args['lex2']]
    print(lex)
    gr = [request.args['gr1'], request.args['gr2']]
    print(gr)
    num = [request.args['num1'], request.args['num2']]
    print(num)
    if word != '':
        print('DONE')
        output = search.get_lines(search.search_word(word))
        return render_template('result.html', result=output, word_flag=True)
    elif len(lex) != 0 or len(gr) != 0:
        if lex[1] == '' and gr[1] == '':
            output = search.get_lines(search.lexgram_search(gr[0], lex[0]))
            return render_template('result.html', result=output, word_flag=True)
        else:
            output = search.get_lines(search.func_name(search.lexgram_search(gr[0], lex[0]), search.lexgram_search(gr[1], lex[1]), 1))
            return render_template('result.html', result=output, word_flag=True)

