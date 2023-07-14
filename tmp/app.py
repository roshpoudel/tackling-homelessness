import dash
from dash import dcc, html, Input, Output
import dash_bootstrap_components as dbc
import DASHBOARD.src.dependencies.cleaning_script as cs

def style_dropdown():
    return {'width': 'auto', 'minWidth':'200px', 'maxWidth':'500px', 'whiteSpace':'normal', 'padding': '10px'}

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.LUX])

app.layout = html.Div([
    dcc.Tabs(id='tabs', value='tabs', children=[
        dcc.Tab(label='Demographics', value='tab-1'),
        dcc.Tab(label='Explore PVA', value='tab-2'), 
        dcc.Tab(label='Findings', value='tab-3'),
        dcc.Tab(label='Recommendation and Report', value='tab-4'),
        dcc.Tab(label='About us', value='tab-5')
    ]),
    html.Div(id='tabs-content', style={'padding': '20px'}),
])

@app.callback(Output('tabs-content', 'children'),
              [Input('tabs', 'value')])
def render_content(tab):
    if tab == 'tab-1':
        return html.Div([
            dcc.Tabs(id='demographics-tabs', value='demographics-tabs', vertical=True, children=[
                dcc.Tab(label='Race', value='race', children=[
                    dbc.Row([
                        dbc.Col(dcc.Loading(dcc.Graph(id='race-pit-graph-pie'), type='circle'), width=6),
                        dbc.Col(dcc.Loading(dcc.Graph(id='race-pva-graph-pie'), type='circle'), width=6)
                    ]),
                    dbc.Row([
                        dbc.Col(dcc.Loading(dcc.Graph(id='race-pit-vs-pva-graph-bar'), type='circle'), width=12),
                    ]),
                ]),
                dcc.Tab(label='Sex', value='sex', children=[
                    dbc.Row([
                        dbc.Col(dcc.Loading(dcc.Graph(id='sex-pit-graph'), type='circle'), width=6),
                        dbc.Col(dcc.Loading(dcc.Graph(id='sex-pva-graph'), type='circle'), width=6)
                    ]),
                    dbc.Row([
                        dbc.Col(dcc.Loading(dcc.Graph(id='sex-pit-vs-pva-graph-bar'), type='circle'), width=12),
                    ]),
                ]),
                dcc.Tab(label='Age', value='age', children=[
                    dbc.Row([
                        dbc.Col(dcc.Loading(dcc.Graph(id='age-pit-graph'), type='circle'), width=6),
                        dbc.Col(dcc.Loading(dcc.Graph(id='age-pva-graph'), type='circle'), width=6)
                    ]),
                    dbc.Row([
                        dbc.Col(dcc.Loading(dcc.Graph(id='age-pit-vs-pva-graph-bar'), type='circle'), width=12),
                    ]),
                ])
            ])
        ])
    elif tab == 'tab-2':
        return html.Div([
            dcc.Tabs(id='explore-pva-tabs', value='explore-pva-tabs', vertical=True, children=[
                dcc.Tab(label='Length of Time Homeless', value='lothomeless', children=[
                    dcc.Dropdown(
                        id='dropdown-lothomeless',
                        options=[{'label': 'Option 1', 'value': 'option1'},
                                    {'label': 'Option 2', 'value': 'option2'},
                                    {'label': 'Option 3', 'value': 'option3'}],
                        value='option1',
                        style=style_dropdown()
                    )
                ]),
                dcc.Tab(label='Health Scale', value='healthscale', children=[
                    dcc.Dropdown(
                        id='dropdown-healthscale',
                        options=[{'label': 'Option 1', 'value': 'option1'},
                                    {'label': 'Option 2', 'value': 'option2'},
                                    {'label': 'Option 3', 'value': 'option3'}],
                        value='option1',
                        style=style_dropdown()
                    )
                ]),
                dcc.Tab(label='Risk and Barriers', value='risksandbarriers', children=[
                    dcc.Dropdown(
                        id='dropdown-risksandbarriers',
                        options=[{'label': 'Option 1', 'value': 'option1'},
                                    {'label': 'Option 2', 'value': 'option2'},
                                    {'label': 'Option 3', 'value': 'option3'}],
                        value='option1',
                        style=style_dropdown()
                    )
                ]),
                dcc.Tab(label='Household Type', value='householdtype', children=[
                    dcc.Dropdown(
                        id='dropdown-householdtype',
                        options=[{'label': 'Option 1', 'value': 'option1'},
                                    {'label': 'Option 2', 'value': 'option2'},
                                    {'label': 'Option 3', 'value': 'option3'}],
                        value='option1',
                        style=style_dropdown()
                    )
                ]),
                dcc.Tab(label='Living Situation', value='livingsituation', children=[
                    dcc.Dropdown(
                        id='dropdown-livingsituation',
                        options=[{'label': 'Option 1', 'value': 'option1'},
                                    {'label': 'Option 2', 'value': 'option2'},
                                    {'label': 'Option 3', 'value': 'option3'}],
                        value='option1',
                        style=style_dropdown()
                    )
                ]),
            ]),
        ])
    elif tab == 'tab-3':
        return html.Div([
            html.H3('Tab 3 content'),
            # Add your content for Tab 3 here
        ])
    elif tab == 'tab-4':
        return html.Div([
            html.H3('Tab 4 content'),
            # Add your content for Tab 4 here
        ])
    elif tab == 'tab-5':
        return html.Div([
            html.H3('Tab 5 content'),
            # Add your content for Tab 5 here
        ])

# # Callbacks for dropdowns in Explore PVA tab
# @app.callback(Output('aggregate', 'figure'),
#               [Input('dropdown-lothomeless', 'value'),
#                Input('dropdown-healthscale', 'value'),
#                Input('dropdown-risksandbarriers', 'value'),
#                Input('dropdown-householdtype', 'value'),
#                Input('dropdown-livingsituation', 'value')])
# def update_figure1(lothomeless_value, healthscale_value, risksandbarriers_value, householdtype_value, livingsituation_value):
#     # Perform calculations or data processing based on dropdown values
#     # Replace cs.figure1 with the updated figure based on the dropdown values
#     updated_figure = cs.calculate_updated_figure(lothomeless_value, healthscale_value, risksandbarriers_value, householdtype_value, livingsituation_value)
#     return updated_figure

if __name__ == '__main__':
    app.run_server(debug=True)
