from flask import Flask, request, render_template
import pandas as pd
from templates.languages import languages


app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def my_form():
    testlist = languages
    if request.method == 'POST':
        list = []
        list.append(request.form.get('CodingPro'))
        langs = (request.form.getlist('checkbox'))
        params = [i in langs for i in testlist] 
        list = list + params

        print(list)
    return render_template('test1.html')

if __name__ == '__main__':
    app.run(debug=True)

