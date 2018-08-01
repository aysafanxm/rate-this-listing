from flask import Flask, request, render_template
from waitress import serve
import json
import pickle
import numpy as np
import pandas as pd

app = Flask(__name__)

def init_form_keys():
    d = {
        'props': [],
        'amens': [],
        'neighbs': [],
        'bedtypes': [],
        'roomtypes': [],
        'cancels': [],
        'resps': [],
    }

    for k, v in d.items():
        fname = k + '_props.json'
        with open(fname, 'rb') as f:
            d[k] = json.loads(f.read())
    return d

def init_column_names():
    num_cols = pd.read_csv('./data/numeric_columns.csv')
    num_cols = num_cols.iloc[:, 1:].columns
    cat_cols = pd.read_csv('./data/categorical_columns.csv')
    cat_cols = cat_cols.iloc[:, 1:].columns
    amen_cols = pd.read_csv('./data/amenities_columns.csv')
    amen_cols = amen_cols.iloc[:, 1:].columns
    return (num_cols, cat_cols, amen_cols)


def init_col_stats():
    num_stats = pd.read_csv('./data/num_stats.csv', index_col=0)
    cat_stats = pd.read_csv('./data/cat_stats.csv', index_col=0)
    amen_stats = pd.read_csv('./data/amen_stats.csv', index_col=0)
    return num_stats, cat_stats, amen_stats


FORM_KEYS = init_form_keys()
NCOLS, CCOLS, ACOLS = init_column_names()
NSTATS, CSTATS, ASTATS = init_col_stats()

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/userreview', methods=['POST','GET'])
def user_review():
    if request.method=='POST':
        result=request.form
        # Log the result
        res_dict = {}
        for r in result:
            for k, vals in FORM_KEYS.items():
                for v in vals:
                    if v == result[r]:
                        print 'setting 1.'
                        res_dict[v] = 1.
                    else:
                        res_dict[v] = 0.

            for k, v in res_dict.items():
                if 0. != v:
                    print k, v

        return render_template('result.html', prediction=result)
    

if __name__ == '__main__':
    app.debug = True
    # app.run(host='0.0.0.0')
    serve(app)
