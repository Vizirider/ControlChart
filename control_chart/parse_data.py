import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import dash_table
import dash_bootstrap_components as dbc
import plotly.graph_objs as go
import pandas as pd
import base64
import datetime
import io


def parse_data(contents, filename):
    content_type, content_string = contents.split(',')

    decoded = base64.b64decode(content_string)
    try:
        if 'csv' in filename:
            df = pd.read_csv(
                io.StringIO(decoded.decode('utf-8')))
        elif 'xls' in filename:
            df = pd.read_excel(io.BytesIO(decoded))
        elif 'txt' or 'tsv' in filename:
            df = pd.read_csv(
                io.StringIO(decoded.decode('utf-8')), delimiter=r'\s+')
    except Exception as e:
        print(e)
        return html.Div([
            'There was an error processing this file.'
        ])
    xlist = []
    for x in range(1, len(df)+1):
        xlist.append(x)
    if len(df.columns)==4:
        df = pd.DataFrame({'X' : xlist, 'Y' : df.iloc[:,0],'D' : df.iloc[:,1], 'M' : df.iloc[:,2],'T' : df.iloc[:,3]})
    elif len(df.columns)==5:
        df = pd.DataFrame({'X' : df.iloc[:,0], 'Y' : df.iloc[:,1],'D' : df.iloc[:,2], 'M' : df.iloc[:,3],'T' : df.iloc[:,4]})
    elif len(df.columns)==2:
        df = pd.DataFrame({'X' : df.iloc[:,0], 'Y' : df.iloc[:,1],'D' : xlist, 'M' : xlist,'T' : xlist})
    elif len(df.columns)==1:
        df = pd.DataFrame({'X' : xlist, 'Y' : df.iloc[:,0],'D' : xlist, 'M' : xlist,'T' : xlist})
    else:
        df = pd.DataFrame({'X' : xlist, 'Y' : df.iloc[:,0],'D' : xlist, 'M' : xlist,'T' : xlist})      
    # ,'D' : xlist, 'M' : xlist,'T' : xlist
    # ,'D' : df.iloc[:,1], 'M' : df.iloc[:,2],'T' : df.iloc[:,3]
    return df
    html.Div([
        'Successful data import filename: ' + filename
    ])
