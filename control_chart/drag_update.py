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
from .drag_select import file_callback


def file_callback_update(app):

    @app.callback(Output('sample1', 'figure'),
                  [
        Input('controlchart-button', 'click')],
        [State('chart_name','value'),        
        State('x_axis','value'),       
        State('y_axis','value')],       
        )
    def drag_select_update(click, chartname, xaxi, yaxi):
        return {
            'layout': go.Layout(
                title=chartname,
                xaxis={'title': xaxi, 'fixedrange': True},
                yaxis={'title': yaxi, 'fixedrange': True},
                hovermode='closest',
                height=800
            ),

        }
