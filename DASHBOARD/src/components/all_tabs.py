from dash import html, dcc, Input, Output
import dash_bootstrap_components as dbc
from components.questions_dropdown import render_tab_w_dropdown
from data import tab_1_graphs
from data import tab_2_graphs

# import sys
# sys.path.append('DASHBOARD/src/utils')

def style_dropdown():
    return {'width': '500px'}

class Questions:
    LOT_HOMELESS = [
        "LOT Homeless"]
    HEALTH_SCALE = [
        "Health Scale"]
    RISKS_AND_BARRIERS = ['HBP Flag',
                          'Income',
                          'Evicted',
                          'Primary Language English',
                          'Discrimination',
                          'Foster',
                          'Bad Credit - Debt',
                          'Criminal Record',
                          'ER 1 Time',
                          'Have you ever experienced abuse or violence by a partner / family member?',
                          'Household 6']
    HOUSEHOLD_TYPE = ['HOH Age Range',
                      'Living Situation Details',
                      'Including yourself, how many people are in your household?',
                      'Other Adults in Household',
                      'Other adult age range',
                      'Pregnant household member',
                      'Children',
                      'Children Age 4 or',
                      'Fleeing DV', ]
    LIVING_SITUATION = ['Living Situation']


def first_tab_layout() -> html.Div:
    # def graphs_layout(ids: list) -> dbc.Row:
    #     return dbc.Row([dbc.Col(dcc.Loading(dcc.Graph(id=i_d), type='circle'), width=6) for i_d in ids])

    return html.Div([
        dcc.Tabs(id='demographics-tabs', value='demographics-tabs', vertical=True, children=[
            dcc.Tab(label='Race', value='race', children=[
                    dbc.Row([
                        dbc.Col(dcc.Loading(
                            dcc.Graph(id='race-pit-graph-pie', figure=tab_1_graphs.race_pit_graph_pie()), type='circle')),
                        dbc.Col(dcc.Loading(
                            dcc.Graph(id='race-pva-graph-pie', figure=tab_1_graphs.race_pva_graph_pie()), type='circle'))
                    ]),
                    dbc.Row([
                        dbc.Col(dcc.Loading(
                            dcc.Graph(id='race-pit-vs-pva-graph-bar', figure=tab_1_graphs.race_pit_vs_pva_graph_bar()), type='circle'), width=12),
                    ]),
                    # dbc.Row([
                    #     dbc.Col(
                    #     html.Div([
                    #         html.Hr(),
                    #         html.P('This is a TextBox.', style={'textAlign': 'center', 'margin': 'auto'}),
                    #         html.Hr(),
                    #     ]), width=12),
                    # ]),
                    ]),
            dcc.Tab(label='Sex', value='sex', children=[
                    dbc.Row([
                        dbc.Col(dcc.Loading(
                            dcc.Graph(id='sex-pit-graph-pie',  figure=tab_1_graphs.sex_pit_graph_pie()), type='circle')),
                        dbc.Col(dcc.Loading(
                            dcc.Graph(id='sex-pva-graph-pie',  figure=tab_1_graphs.sex_pva_graph_pie()), type='circle'))
                    ]),
                    dbc.Row([
                        dbc.Col(dcc.Loading(
                            dcc.Graph(id='sex-pit-vs-pva-graph-bar', figure=tab_1_graphs.sex_pit_vs_pva_graph_bar()), type='circle'), width=12),
                    ]),
                    ]),
            dcc.Tab(label='Age', value='age', children=[
                    dbc.Row([
                        dbc.Col(dcc.Loading(
                            dcc.Graph(id='age-pit-graph-pie', figure=tab_1_graphs.age_pit_graph_pie()), type='circle'), width=6),
                        dbc.Col(dcc.Loading(
                            dcc.Graph(id='age-pva-graph-pie', figure=tab_1_graphs.age_pva_graph_pie()), type='circle'), width=6)
                    ]),
                    dbc.Row([
                        dbc.Col(dcc.Loading(
                            dcc.Graph(id='age-pit-vs-pva-graph-bar', figure=tab_1_graphs.age_pit_vs_pva_graph_bar()), type='circle'), width=12),
                    ]),
                    ])
        ], style={'padding': '20px'}),
    ])


def second_tab_layout() -> html.Div:
    labels_and_ids = zip(['Length of Time Homeless', 'Health Scale', 'Risk and Barriers', 'Household Type', 'Living Situation'],
                         ['dropdown-lothomeless', 'dropdown-healthscale', 'dropdown-risksandbarriers', 'dropdown-householdtype', 'dropdown-livingsituation'])
    questions = [Questions.LOT_HOMELESS, Questions.HEALTH_SCALE, Questions.RISKS_AND_BARRIERS, Questions.HOUSEHOLD_TYPE, Questions.LIVING_SITUATION]
    children_ = []
    i=0
    for label, id in labels_and_ids:
        children_.append(render_tab_w_dropdown(label, id, questions[i]))
        i += 1
    # @app.callback(Output('explore-pva-graph', 'figure'),
    #             [Input('dropdown-lothomeless', 'value'),
    #             Input('dropdown-healthscale', 'value'),
    #             Input('dropdown-risksandbarriers', 'value'),
    #             Input('dropdown-householdtype', 'value'),
    #             Input('dropdown-livingsituation', 'value')])
    # def update_graph(dropdown_lothomeless, dropdown_healthscale, dropdown_risksandbarriers, dropdown_householdtype, dropdown_livingsituation):
    #     print('callback triggered')
    #     # Combine the dropdown values into a single parameter if needed
    #     col_name = str(dropdown_lothomeless) + str(dropdown_healthscale) + str(dropdown_risksandbarriers) + str(dropdown_householdtype) + str(dropdown_livingsituation)
    #     print(col_name)
    #     # create a plot based on the selected dropdown options
    #     fig = tab_2_graphs.create_plot(col_name)
    #     return fig
    
    return html.Div([
        dcc.Tabs(id='explore-pva-tabs', value='explore-pva-tabs', vertical=True, children=children_),
        dcc.Graph(id='explore-pva-graph'),
    ])
    
#     return html.Div([
#     dcc.Tabs(id='explore-pva-tabs', value='explore-pva-tabs', vertical=True, children=[
#         dcc.Tab(label='Length of Time Homeless', value='lothomeless', children=[
#             dcc.Dropdown(
#                 id='dropdown-lothomeless',
#                 options=[{'label':option, 'value':option} for option in Questions.LOT_HOMELESS],
#                 placeholder='Select',
#                 multi=False,
#                 optionHeight=100,
#                 style=style_dropdown()
#             ), dcc.Graph(id='explore-pva-graph')
#         ]),
#         dcc.Tab(label='Health Scale', value='healthscale', children=[
#             dcc.Dropdown(
#                 id='dropdown-healthscale',
#                 options=[{'label':option, 'value':option} for option in Questions.HEALTH_SCALE],
#                 placeholder='Select',
#                 multi=False,
#                 optionHeight=100,
#                 style=style_dropdown()
#             ), dcc.Graph(id='explore-pva-graph')
#         ]),
#         dcc.Tab(label='Risk and Barriers', value='risksandbarriers', children=[
#             dcc.Dropdown(
#                 id='dropdown-risksandbarriers',
#                 options=[{'label':option, 'value':option} for option in Questions.RISKS_AND_BARRIERS],
#                 placeholder='Select',
#                 multi=False,
#                 optionHeight=100,
#                 style=style_dropdown()
#             ), dcc.Graph(id='explore-pva-graph')
#         ]),
#         dcc.Tab(label='Household Type', value='householdtype', children=[
#             dcc.Dropdown(
#                 id='dropdown-householdtype',
#                 options=[{'label':option, 'value':option} for option in Questions.HOUSEHOLD_TYPE],
#                 placeholder='Select',
#                 multi=False,
#                 optionHeight=100,
#                 style=style_dropdown()
#             ), dcc.Graph(id='explore-pva-graph')
#         ]),
#         dcc.Tab(label='Living Situation', value='livingsituation', children=[
#             dcc.Dropdown(
#                 id='dropdown-livingsituation',
#                 options=[{'label':option, 'value':option} for option in Questions.LIVING_SITUATION],
#                 placeholder='Select',
#                 multi=False,
#                 optionHeight=100,
#                 style=style_dropdown()
#             ), dcc.Graph(id='explore-pva-graph')
#         ]),
#     ]),
# ])



def third_tab_layout() -> html.Div:
    tabs_and_values = zip(['Length of Time Homeless', 'Health Scale', 'Risk and Barriers', 'Household Type', 'Living Situation'],
                          ['findings-lothomeless', 'findings-healthscale', 'findings-risksandbarriers', 'findings-householdtype', 'findings-livingsituation'])
    return html.Div([
        dcc.Tabs(id='findings-tabs', value='findings-tabs', vertical=True, children=[
            dcc.Tab(label=label_, value=value_, children=[]) for label_, value_ in tabs_and_values
        ]),
    ])


def fourth_tab_layout() -> html.Div:
    return html.Div([
        html.P('Here is a detailed report on our methodologies and findings from our analysis on the PIT, PVA and VISPDAT datasets.'),
        html.A('Download Report', href='../assets/EvaluativeReport.pdf',
               download='evalreport.pdf'),
    ])


def fifth_tab_layout() -> html.Div:
    return html.Div([
        html.H3('About US', style={'text-align': 'center'}),
        html.Img(src='/path/to/image.png',
                 alt='Image of the four Datalab fellows who worked on this project'),
    ])
