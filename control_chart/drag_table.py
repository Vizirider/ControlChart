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
import time
import io
from .parse_data import parse_data

def table_callback(app):
    @app.callback(Output('table1', 'data'),
                  [
                   Input('table1', "page_current"), Input(
                       'table1', "page_size"),
                   Input('upload-data', 'contents'),
                    Input('upload-data', 'filename')])
    def drag_table(page_current, page_size, contents, filename):

        if contents:
            contents = contents[0]
            filename = filename[0]
            df = parse_data(contents, filename)
            df = pd.DataFrame({'X' : df.iloc[:,0], 'Y' : df.iloc[:,1]})

        return df.iloc[page_current *
                              page_size:(page_current + 1)*page_size].to_dict('records')

