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

def figure_callback(app):
    @app.callback(Output('sample2', 'figure'),
                  [Input('year-picker', 'value'), Input('month-picker', 'value'), Input('term-picker', 'value'),
                    Input('upload-data', 'contents'),
                    Input('upload-data', 'filename'),
                    Input('user-spec','value')])
    def update_figure(selected_year, selected_month, selected_term, contents, filename, userspec):
        if contents:
            contents = contents[0]
            filename = filename[0]
            df = parse_data(contents, filename)
                    
        traces = []
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

        
        
        atlag = pd.Series(df_filter['Y'].mean(), df_filter['X'])
        szoras = pd.Series(df_filter['Y'].std(ddof=0), df_filter['X'])
        userline = pd.Series(userspec, df_filter['X'])

        traces.append(go.Scatter(
            x=df_filter['X'],
            y=df_filter['Y'],
            mode='markers',
            name='Mintavétel',
            opacity=0.7,
            marker={'size': 15}
        )),
        traces.append(go.Scatter(
            x=df_filter['X'],
            y=atlag,
            mode='lines',
            name='Mintavétel átlaga',
            line={'color': 'green'}
        )),
        traces.append(go.Scatter(
            x=df_filter['X'],
            y=atlag+szoras,
            mode='lines',
            name='Szigma 1',
            opacity=0.7,
            line={'color': 'yellow'}
        )),
        traces.append(go.Scatter(
            x=df_filter['X'],
            y=atlag-szoras,
            mode='lines',
            line={'color': 'yellow'},
            opacity=0.7,
            name='Szigma 1',
            showlegend=False
        )),
        traces.append(go.Scatter(
            x=df_filter['X'],
            y=atlag+2*szoras,
            mode='lines',
            name='Szigma 2',
            line={'color': 'orange'}
        )),
        traces.append(go.Scatter(
            x=df_filter['X'],
            y=atlag-2*szoras,
            mode='lines',
            line={'color': 'orange'},
            name='Szigma 2',
            showlegend=False
        )),
        traces.append(go.Scatter(
            x=df_filter['X'],
            y=atlag+3*szoras,
            mode='lines',
            name='Szigma 3',
            line={'color': 'red'}
        )),
        traces.append(go.Scatter(
            x=df_filter['X'],
            y=atlag-3*szoras,
            mode='lines',
            line={'color': 'red'},
            name='Szigma 3',
            showlegend=False
        )),
        traces.append(go.Scatter(
            x=df_filter['X'],
            y=userline,
            mode='lines',
            line={'color': 'grey', 'width': 5},
            name='Konstans: '+userspec,
        )),
        return {
            'data': traces,
            'layout': go.Layout(
                title='Mintavételek',
                xaxis={'title': 'Sorszáma'},
                yaxis={'title': 'Mintavétel értéke'},
                hovermode='closest'
            ),

        }
