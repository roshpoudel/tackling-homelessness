from dash import Dash, html, dcc
from components.all_tabs import second_tab_layout


def create_main_layout(app: Dash) -> html.Div:
    return html.Div([
        dcc.Tabs(id='tabs', value='tabs', children=[
            dcc.Tab(label='Home', value='tab-0'),
            dcc.Tab(label='Demographics', value='tab-1'),
            dcc.Tab(label='Explore PVA', value='tab-2'),
            dcc.Tab(label='Findings', value='tab-3'),
            dcc.Tab(label='Recommendation and Report', value='tab-4'),
            dcc.Tab(label='About us', value='tab-5')
        ], style={'position': 'fixed', 'top': '0', 'left': '0', 'right': '0', 'zIndex': '999'}),
        html.Div(id='tabs-content', style={'padding': '20px', 'margin-top':'100px'},),
    ])
