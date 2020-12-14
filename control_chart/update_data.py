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

def data_callback(app):
    @app.callback(Output('table2', 'data'),
                  [Input('year-picker', 'value'), Input('month-picker', 'value'), Input('term-picker', 'value'),
                   Input('table1', "page_current"), Input(
                       'table1', "page_size"),
                   Input('upload-data', 'contents'),
                    Input('upload-data', 'filename')])
    def update_data(selected_year, selected_month, selected_term, page_current, page_size, contents, filename):

        if contents:
            contents = contents[0]
            filename = filename[0]
            df = parse_data(contents, filename)

        if selected_year is not None and selected_month is not None and selected_term is not None:
            df_filter = df.loc[(df['D'] == selected_year) & (
                df['M'] == selected_month) & (df['T'] == selected_term)]
        elif selected_year is not None and selected_month is not None and selected_term is None:
            df_filter = df.loc[(df['D'] == selected_year) &
                               (df['M'] == selected_month)]
        elif selected_year is not None and selected_month is None and selected_term is not None:
            df_filter = df.loc[(df['D'] == selected_year) &
                               (df['T'] == selected_term)]
        elif selected_year is None and selected_month is not None and selected_term is not None:
            df_filter = df.loc[(df['M'] == selected_month) &
                               (df['T'] == selected_term)]
        elif selected_year is None and selected_month is None and selected_term is not None:
            df_filter = df.loc[(df['T'] == selected_term)]
        elif selected_year is None and selected_month is not None and selected_term is None:
            df_filter = df.loc[(df['M'] == selected_month)]
        elif selected_year is not None and selected_month is None and selected_term is None:
            df_filter = df.loc[(df['D'] == selected_year)]
        else:
            df_filter = df

        return df_filter.iloc[page_current *
                              page_size:(page_current + 1)*page_size].to_dict('records')
