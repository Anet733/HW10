from flask import Flask
from utils import *

app = Flask(__name__)


@app.route('/')
def index():
    candidates = get_all()
    result = '<br>'
    for candidate in candidates:
        result += candidate['name'] + '<br>'
        result += candidate['position'] + '<br>'
        result += candidate['gender'] + '<br>'
        result += str(candidate['age']) + '<br>'
        result += candidate['skills'] + '<br>'
        result += '<br>'

    return f'<pre> {result} </pre>'


@app.route('/candidate/<int:pk>')
def get_candidate(pk):
    candidate = get_by_pk(pk)
    if not candidate:
        return 'Нет такого кандидата'
    result = '<br>'
    result += candidate['name'] + '<br>'
    result += candidate['position'] + '<br>'
    result += candidate['skills'] + '<br>'
    result += '<br>'
    picture = candidate['picture']

    return f'''
    <img src="{picture}">
    <pre> {result} </pre>
    '''


@app.route('/candidate/<skill>')
def get_candidate_2(skill):
    candidates = get_by_skill(skill)
    result = '<br>'
    for candidate in candidates:
        result += candidate['name'] + '<br>'
        result += candidate['position'] + '<br>'
        result += candidate['skills'] + '<br>'
        result += '<br>'

    return f'<pre> {result} </pre>'


app.run(debug=True)
