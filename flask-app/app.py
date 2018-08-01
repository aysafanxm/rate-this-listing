from flask import Flask, request, render_template
from waitress import serve
from sklearn.metrics import mean_squared_error, r2_score
import json
import pickle
import numpy as np
import pandas as pd
import vecstack
import xgboost as xgb
import dill as pickle


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


def parse_form(form):
    res_dict = {}
    for k, v in form.items():
        if k in ALL_COLS:
            res_dict[k] = v
        elif v in ALL_COLS:
            res_dict[v] = 1.
    for cname in ALL_COLS:
        if cname not in res_dict.keys():
            res_dict[cname] = 0.
    return pd.DataFrame(res_dict, index=[0], dtype=float)


def get_col_value(colname, input_df, stats):
        res = None
        if colname in input_df.columns:
            res = input_df[colname]
        else:
            res = stats.loc['50%', colname]
        return res


def normalize_numeric(df):
    outdf = pd.DataFrame(columns=df.columns)

    for c in df.columns:
        mmin = NSTATS.loc['min', c]
        mmax = NSTATS.loc['max', c]
        outdf[c] = (df[c] - 1. * mmin) / (mmax - mmin)
    return outdf


def reformulate_input(inp):
    num = pd.DataFrame(columns=NCOLS)
    cat = pd.DataFrame(columns=CCOLS)
    amen = pd.DataFrame(columns=ACOLS)
    for c in NCOLS:
        num[c] = get_col_value(c, inp, NSTATS)
    num = normalize_numeric(num)
    for c in CCOLS:
        cat[c] = get_col_value(c, inp, CSTATS)
    for c in ACOLS:
        amen[c] = get_col_value(c, inp, ASTATS)
    return pd.concat([num, cat, amen], axis=1)


FORM_KEYS = init_form_keys()
NCOLS, CCOLS, ACOLS = init_column_names()
ALL_COLS = list(NCOLS) + list(CCOLS) + list(ACOLS)
NSTATS, CSTATS, ASTATS = init_col_stats()


with open('./data/comb_vecstack_stack.pkl', 'rb') as f:
    MODEL_STACK = pickle.load(f)

with open('./data/comb_vecstack_clf.pkl', 'rb') as f:
    MODEL_CLF = pickle.load(f)

@app.route('/')
def home():
    return render_template('home.html')


@app.route('/userreview', methods=['POST','GET'])
def user_review():
    if request.method == 'POST':
        inp = parse_form(request.form)
        # print inp

        reformed_inp = reformulate_input(inp)
        
        result = MODEL_CLF.predict(MODEL_STACK.transform(reformed_inp))

        return render_template('result.html', prediction=result)


if __name__ == '__main__':
    app.debug = True
    # app.run(host='0.0.0.0')
    serve(app)
