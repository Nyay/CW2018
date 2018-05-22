from flask import render_template, request
from app import app
from app import search
from app import setup


@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html",
                           title='Home')


@app.route('/form')
def form():
    word = request.args['word']
    lex = [request.args['lex1'], request.args['lex2']]
    gr = [request.args['gr1'], request.args['gr2']]
    num = request.args['num']
    if word != '':
        output = setup.setup_line(search.get_lines_2(search.search_word(word)))
        return render_template('result.html', result=output, word_flag=True)
    elif len(lex) != 0 or len(gr) != 0:
        if lex[1] == '' and gr[1] == '':
            output = search.get_lines(search.lexgram_search(gr[0], lex[0]))
            output2 = setup.setup_line(search.get_lines_2(search.lexgram_search(gr[0], lex[0])))
            return render_template('result.html', result=output2, word_flag=True)
        else:
            output = search.get_lines(search.func_name(search.lexgram_search(gr[0], lex[0]),
                                                       search.lexgram_search(gr[1], lex[1]), int(num)))
            output2 = setup.setup_line(search.get_lines_2(search.func_name(search.lexgram_search(gr[0], lex[0]),
                                                       search.lexgram_search(gr[1], lex[1]), int(num))))
            return render_template('result.html', result=output2, word_flag=True)


@app.route('/text')
def text():
    ids = request.args['text']
    text = search.get_text(ids)
    return render_template('text.html', result=text)
