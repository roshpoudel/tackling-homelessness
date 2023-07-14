from dash import html, dcc, Input, Output
import dash_bootstrap_components as dbc
from components.questions_dropdown import render_tab_w_dropdown
from data import tab_1_graphs
from data import tab_2_graphs

# import sys
# sys.path.append('DASHBOARD/src/utils')


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


def home_page_layout() -> html.Div:
    return html.Div([
        html.H1('Home', style={'text-align': 'center'}),
        html.P('This is the home page')
    ])


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
                    dbc.Row([
                        dbc.Col(dcc.Loading(
                            dcc.Graph(id='race-pit-vs-pva-findings-graph-bar', figure=tab_1_graphs.race_pit_vs_pva_findings_graph_bar()), type='circle'), width=12),
                    ]),
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
                    dbc.Row([
                        dbc.Col(dcc.Loading(
                            dcc.Graph(id='sex-pit-vs-pva-findings-graph-bar', figure=tab_1_graphs.sex_pit_vs_pva_findings_graph_bar()), type='circle'), width=12),
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
                    dbc.Row([
                        dbc.Col(dcc.Loading(
                            dcc.Graph(id='age-pit-vs-pva-findings-graph-bar', figure=tab_1_graphs.age_pit_vs_pva_findings_graph_bar()), type='circle'), width=12),
                    ]),
                    ])
        ], style={'padding': '20px'}),
    ])


def second_tab_layout() -> html.Div:
    labels_and_ids = zip(['Length of Time Homeless', 'Health Scale', 'Risk and Barriers', 'Household Type', 'Living Situation'],
                         ['dropdown-lothomeless', 'dropdown-healthscale', 'dropdown-risksandbarriers', 'dropdown-householdtype', 'dropdown-livingsituation'])
    questions = [Questions.LOT_HOMELESS, Questions.HEALTH_SCALE,
                 Questions.RISKS_AND_BARRIERS, Questions.HOUSEHOLD_TYPE, Questions.LIVING_SITUATION]
    children_ = []
    i = 0
    for label, id in labels_and_ids:
        children_.append(render_tab_w_dropdown(label, id, questions[i]))
        i += 1

    return html.Div([
        dcc.Tabs(id='explore-pva-tabs', value='explore-pva-tabs',
                 vertical=True, children=children_, style={'padding-right': '20px'}),
        dcc.Graph(id='explore-pva-graph1'),
        dcc.Graph(id='explore-pva-graph2'),
    ])


def third_tab_layout() -> html.Div:
    # tabs_and_values = zip(['Length of Time Homeless', 'Health Scale', 'Risk and Barriers', 'Household Type', 'Living Situation'],
    #                       ['findings-lothomeless', 'findings-healthscale', 'findings-risksandbarriers', 'findings-householdtype', 'findings-livingsituation'])
    # return html.Div([
    #     dcc.Tabs(id='findings-tabs', value='findings-tabs', vertical=True, children=[
    #         dcc.Tab(label=label_, value=value_, children=[]) for label_, value_ in tabs_and_values
    #     ]),
    # ])
    pass

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
