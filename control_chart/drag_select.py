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
from .parse_data import parse_data


def file_callback(app):

    @app.callback(Output('sample1', 'figure'),
                  [
        Input('upload-data', 'contents'),
        Input('upload-data', 'filename'),
        Input('user-spec1','value'),
        Input('user-spec2','value')])
    def drag_select(contents, filename, userspec1, userspec2):

        if contents:
            contents = contents[0]
            filename = filename[0]
            df = parse_data(contents, filename)
            
        atlag = pd.Series(df['Y'].mean(), df['X'])
        szoras = pd.Series(df['Y'].std(ddof=0), df['X'])
        userline1 = pd.Series(userspec1, df['X'])
        userline2 = pd.Series(userspec2, df['X'])
        
        traces = []

        traces.append(go.Scatter(
            x=df['X'],
            y=df['Y'],
            mode='markers',
            name='Sampling',
            opacity=0.7,
            marker={'size': 15}
        )),
        traces.append(go.Scatter(
            x=df['X'],
            y=atlag,
            mode='lines',
            name='Sampling mean',
            line={'color': 'green'}
        )),
        traces.append(go.Scatter(
            x=df['X'],
            y=atlag+szoras,
            mode='lines',
            name='Sigma 1',
            opacity=0.5,
            line={'color': 'yellow'}
        )),
        traces.append(go.Scatter(
            x=df['X'],
            y=atlag-szoras,
            mode='lines',
            line={'color': 'yellow'},
            name='Sigma 1',
            opacity=0.5,
            showlegend=False
        )),
        traces.append(go.Scatter(
            x=df['X'],
            y=atlag+2*szoras,
            mode='lines',
            name='Sigma 2',
            opacity=0.5,
            line={'color': 'orange'}
        )),
        traces.append(go.Scatter(
            x=df['X'],
            y=atlag-2*szoras,
            mode='lines',
            line={'color': 'orange'},
            name='Sigma 2',
            opacity=0.5,
            showlegend=False
        )),
        traces.append(go.Scatter(
            x=df['X'],
            y=atlag+3*szoras,
            mode='lines',
            name='Sigma 3',
            line={'color': 'red'}
        )),
        traces.append(go.Scatter(
            x=df['X'],
            y=atlag-3*szoras,
            mode='lines',
            line={'color': 'red'},
            name='Sigma 3',
            showlegend=False
        )),
        traces.append(go.Scatter(
            x=df['X'],
            y=userline1,
            mode='lines',
            line={'color': 'grey', 'width': 5},
            name='Upper limit: '+userspec1,
        )),
        traces.append(go.Scatter(
            x=df['X'],
            y=userline2,
            mode='lines',
            line={'color': 'grey', 'width': 5},
            name='Lower limit: '+userspec2,
        )),
        return {
            'data': traces,
            'layout': go.Layout(
                title='Control Chart',
                xaxis={'title': 'Data'},
                yaxis={'title': 'Sampling value'},
                hovermode='closest',
                height=800
            ),

        }
