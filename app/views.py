from flask import render_template, request
from app import app
from app import search
from app import setup

from math import ceil


class Pagination(object):

    def __init__(self, page, per_page, total_count):
        self.page = page
        self.per_page = per_page
        self.total_count = total_count

    @property
    def pages(self):
        return int(ceil(self.total_count / float(self.per_page)))

    @property
    def has_prev(self):
        return self.page > 1

    @property
    def has_next(self):
        return self.page < self.pages

    def iter_pages(self, left_edge=2, left_current=2,
                   right_current=5, right_edge=2):
        last = 0
        for num in xrange(1, self.pages + 1):
            if num <= left_edge or \
               (num > self.page - left_current - 1 and \
                num < self.page + right_current) or \
               num > self.pages - right_edge:
                if last + 1 != num:
                    yield None
                yield num
                last = num


@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html",
                           title='Home')


@app.route('/form')
def form():
    lex = [request.args['lex1'], request.args['lex2']]
    gr = [request.args['gr1'], request.args['gr2']]
    num = request.args['num']
    if len(lex) != 0 or len(gr) != 0:
        if lex[1] == '' and gr[1] == '':
            output2 = setup.setup_line(search.get_lines_2(search.lexgram_search(gr[0], lex[0].lower())))
            return render_template('result.html', result=output2, word_flag=True)
        else:
            output2 = setup.setup_line(search.get_lines_2(search.func_name(search.lexgram_search(gr[0], lex[0].lower()),
                                                       search.lexgram_search(gr[1], lex[1]), int(num))))
            return render_template('result.html', result=output2, word_flag=True)


@app.route('/text')
def text():
    ids = request.args['text']
    text = search.get_text(ids.lower())
    return render_template('text.html', result=text[0],  coord=text[1])


@app.route('/form_word')
def form_word():
    word = request.args['word']
    if word != '':
        output = setup.setup_line(search.get_lines_2(search.search_word(word.lower())))
        return render_template('result.html', result=output, word_flag=True)
