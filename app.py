import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import dash_table
import dash_bootstrap_components as dbc
import dash_auth
import plotly.graph_objs as go
import pandas as pd
import base64
import datetime
import time
import io
from control_chart.drag_select import file_callback
from control_chart.drag_table import table_callback
from control_chart.update_data import data_callback
from control_chart.update_figure import figure_callback
from control_chart.parse_data import parse_data
from control_chart.authentication import authentication

text_markdown = "\t"
with open('description.txt') as this_file:
    for a in this_file.read():
        if "\n" in a:
            text_markdown += "\n \t"
        else:
            text_markdown += a

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.LUMEN])
df = pd.read_csv('Sample_sample.csv')
auth = dash_auth.BasicAuth(app, authentication(app))

server = app.server
file_callback(app)
table_callback(app)
data_callback(app)
figure_callback(app)

PAGE_SIZE = 10
if 'D' in df.columns:
    year_options = []
    for year in df['D'].unique():
        year_options.append({'label': str(year), 'value': year})
if 'M' in df.columns:
    month_options = []
    for month in df['M'].unique():
        month_options.append({'label': str(month), 'value': month})
if 'T' in df.columns:
    term_options = []
    for term in df['T'].unique():
        term_options.append({'label': str(term), 'value': term})

app.layout = html.Div(
    dcc.Tabs([
        dcc.Tab(label='All samples', 
        children=[
            html.Div([
                dcc.Upload(
                    id='upload-data',
                    children=html.Div([
                        'Drag and Drop or ',
                        html.A('Select Files')
                    ]),
                    style={
                        'width': '100%',
                        'height': '60px',
                        'lineHeight': '60px',
                        'borderWidth': '1px',
                        'borderStyle': 'dashed',
                        'borderRadius': '5px',
                        'textAlign': 'center',
                        'margin': '10px'
                    },
                    multiple=True
                )
            ]),
            html.Div(html.P(dbc.Button(
                "ControlChart Description",
                id="collapse-button",
                className="mb-3",
                color="primary",
            ))),
            dbc.Collapse(
                dbc.Card(dbc.CardBody(dcc.Markdown(text_markdown))),
                id="collapse",
            ),
            html.Div(
                [html.P(html.Label("User specified upper limit")), dcc.Input(
                    id='user-spec1', type='text', placeholder='Upper limit', value='')],
                style={'width': '48%', 'display': 'inline-block'}),
            html.Div(
                [html.P(html.Label("User specified lower limit")), dcc.Input(
                    id='user-spec2', type='text', placeholder='Lower limit', value='')],
                style={'width': '48%', 'display': 'inline-block'}),            
            dcc.Loading(
                id="loading1",
                children=dcc.Graph(id='sample1'),
                type="circle",
            ),
            html.Div(dash_table.DataTable(id='table1',
                                          columns=[{"name": i, "id": i}
                                                   for i in df.columns],
                                          style_cell={
                                              'minWidth': '40px', 'width': '80px', 'maxWidth': '40px',
                                          },
                                          page_current=0,
                                          page_size=PAGE_SIZE,
                                          page_action='custom'),
                                          style={'display': 'flex', 'align-items': 'center', 'justify-content': 'center'}),
            html.P(html.Label("A táblázat maximum 10 sort jelenít meg, de lapozható"),style={'text-align':'center'})
        ]
        ),
        dcc.Tab(label='User specified', children=[
            html.P(html.Div(
                [html.Label("Ev"), dcc.Dropdown(id='year-picker',
                                                  options=year_options)],
                style={'width': '48%', 'display': 'inline-block'})),
            html.Div(
                [html.Label("Honap"), dcc.Dropdown(id='month-picker',
                                                   options=month_options)],
                style={'width': '48%', 'display': 'inline-block'}),
            html.Div(
                [html.Label("Prioritas"), dcc.Dropdown(
                    id='term-picker', options=term_options)],
                style={'width': '48%', 'display': 'inline-block'}),
            html.Div(
                [html.P(html.Label("Y axis constant line ")), dcc.Input(
                    id='user-spec', type='text', placeholder='Y axis constant line', value='20')],
                style={'width': '48%', 'display': 'inline-block'}),
            dcc.Loading(
                id="loading2",
                children=dcc.Graph(id='sample2'),
                type="circle",
            ),
            html.Div(dash_table.DataTable(id='table2',
                                          columns=[{"name": i, "id": i}
                                                   for i in df.columns],
                                          style_table={'overflowX': 'auto'},
                                          style_cell={
                                              'minWidth': '180px', 'width': '180px', 'maxWidth': '180px',
                                              'overflow': 'hidden',
                                              'textOverflow': 'ellipsis',
                                          },
                                          page_current=0,
                                          page_size=PAGE_SIZE,
                                          page_action='custom')),
            html.P(html.Label("A táblázat maximum 10 sort jelenít meg, de lapozható")),
        ]
        )
    ]
    )
)


@app.callback(
    Output("collapse", "is_open"),
    [Input("collapse-button", "n_clicks")],
    [State("collapse", "is_open")],
)
def toggle_collapse(n, is_open):
    if n:
        return not is_open
    return is_open


if __name__ == '__main__':
    app.run_server()
