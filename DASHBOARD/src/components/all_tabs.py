from dash import html, dcc, Input, Output
import dash_bootstrap_components as dbc
from components.questions_dropdown import render_tab_w_dropdown
from data import tab_1_graphs, tab_2_graphs, tab_3_graphs


import sys
sys.path.append('DASHBOARD/assets')


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

styles = {
        'container': {
            'width': '80%',
            'margin': '0 auto',
        },
        'section': {
            'margin-bottom': '30px',
        },
        'tab': {
            'margin-top': '20px',
        },
        'image': {
            'width': '300px',
            'margin-top': '20px',
        },
    }

def home_page_layout() -> html.Div:
    return html.Div(
        style=styles['container'],
        children=[
            html.H3("Welcome to our Data Analysis Dashboard!", style={
                    'text-align': 'center', 'margin-bottom': '30px', }),
            html.P("This dashboard provides insights and visualizations based on our analysis of the PIT (Point-in-Time) and PVA (VI-SPDAT) datasets."),
            html.P("Here is an overview of the different sections you will find in our dashboard:",
                   style=styles['section']),
            html.Hr(),
            # html.Img(src="image_url_here", alt="Dashboard Image", style=styles['image']),
            html.H4("Demographics in PIT and PVA", style=styles['tab']),
            html.P(
                "This tab focuses on the demographics within the PIT and PVA datasets."),
            html.P("It includes interactive graphs representing different demographic variables such as race, sex, and age."),
            html.P(
                "The graphs provide insights into the distribution of these variables in the datasets."),
            html.Hr(),
            html.H4("Explore the PVA Dataset", style=styles['tab']),
            html.P("The second tab allows you to explore the PVA dataset in detail."),
            html.P("It features dropdown menus where you can select specific questions related to Lot Homeless, Health Scale, Risks and Barriers, Household Type, and Living Situation."),
            html.P("Based on your selections, the dashboard dynamically generates relevant graphs to analyze the chosen variables."),
            html.Hr(),
            html.H4("Findings", style=styles['tab']),
            html.P(
                "In the third tab, you will find detailed findings from our analysis of the PVA dataset."),
            html.P("Each finding is categorized under sub-scores such as Lot Homeless, Health Scale, Risks and Barriers, Household Type, and Living Situation."),
            html.P("We present graphs and insights related to each sub-score, highlighting notable patterns and observations."),
            html.Hr(),
            html.H4("Recommendation and Report", style=styles['tab']),
            html.P(
                "The fourth tab provides recommendations and a comprehensive report on our methodologies and findings."),
            html.P(
                "You can download the report as a PDF for a deeper understanding of our analysis."),
            html.Hr(),
            html.H4("About Us", style=styles['tab']),
            html.P(
                "The fifth tab offers information about the team behind this data analysis project."),
            html.P("Feel free to explore the different tabs and interact with the visualizations to gain valuable insights from our analysis.")
        ]
    )


def first_tab_layout() -> html.Div:
    # def graphs_layout(ids: list) -> dbc.Row:
    #     return dbc.Row([dbc.Col(dcc.Loading(dcc.Graph(id=i_d), type='circle'), width=6) for i_d in ids])

    return html.Div([
        html.H3('Demographics in PIT and PVA', style={
                'text-align': 'center', 'margin-bottom': '20px'}),
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
        html.H3('Explore the PVA Dataset', style={
                'text-align': 'center', 'margin-bottom': '20px'}),
        dcc.Tabs(id='explore-pva-tabs', value='explore-pva-tabs',
                 vertical=True, children=children_, style={'padding-right': '20px', 'padding-top': '20px'}),
        dcc.Graph(id='explore-pva-graph1'),
        dcc.Graph(id='explore-pva-graph2'),
    ])


class ThirdTab:
    @classmethod
    def third_tab_layout(cls) -> html.Div:
        tabs_and_values = zip(['Length of Time Homeless', 'Health Scale', 'Risk and Barriers', 'Household Type', 'Living Situation'],
                              ['findings-lothomeless', 'findings-healthscale', 'findings-risksandbarriers', 'findings-householdtype', 'findings-livingsituation'])
        return html.Div([
            html.Div([
                html.H3('Findings', style={
                        'text-align': 'center', 'margin-bottom': '20px'}),
                html.P('Here are our findings from our analysis on the PVA dataset'),
                html.H4('Overall Scores Distribution'),
                html.Hr(),
                html.P(
                    'The overall scores distribution for the PVA dataset is as follows:'),
                dcc.Graph(id='findings-pva-graph',
                          figure=tab_3_graphs.overall_scores_distribution()),
                html.P("BIPOC Females have the lowest overall median score. The central tendency of their overall score is the lowest in demographic groupings with statistically significant sample sizes."),
            ]),
            html.P(
                'The following tabs contain the findings for each of the sub-scores in the PVA dataset'),
            html.Hr(),
            dcc.Tabs(id='findings-tabs', value='findings-tabs', vertical=True, children=[
                dcc.Tab(label=label_, value=value_, children=[
                    html.Div(id=value_),
                ]) for label_, value_ in tabs_and_values
            ]),
        ])

    @staticmethod
    def lothomeless_content() -> html.Div:
        return html.Div([
            html.P("The LOT Homeless score occupies the 10,000s place, or the top priority category. The following graph shows the distribution of scores for this category:"),
            dcc.Graph(id='findings-lothomeless-graph',
                      figure=tab_3_graphs.lot_homeless_graphs.lot_homeless_graph1()),
            html.P("75% of BIPOC Females scored a 3 or lower in this category, and 50% scored a 1 or lower. Since it occupies the highest priority category, that means that BIPOC Females are consistently falling at the bottom of the priority list."),
            dcc.Graph(id='findings-lothomeless-graph2',
                      figure=tab_3_graphs.lot_homeless_graphs.lot_homeless_graph2()),
            html.P(
                "Males (both BIPOC and White) reported higher rates of 8+ years of homelessness."),
            dcc.Graph(id='findings-lothomeless-graph3',
                      figure=tab_3_graphs.lot_homeless_graphs.lot_homeless_graph3()),
            html.P(
                "BIPOC Females had the highest reported rate of under one year of homelessness."),
            dcc.Graph(id='findings-lothomeless-graph4',
                      figure=tab_3_graphs.lot_homeless_graphs.lot_homeless_graph4()),
            html.P("50.7% of BIPOC Females scored a 1. Since this is the highest priority category, occupying the 10,000s place, that means 50% of BIPOC Females are occupying the bottom of the list."),
        ], style={'padding': '20px'})

    @staticmethod
    def healthscale_content() -> html.Div:
        return html.Div([
            html.P("The Health Scale score occupies the 1000s place, or the second highest priority category. The following graph shows the distribution of scores for this category:"),
            dcc.Graph(id='findings-healthscale-graph',
                      figure=tab_3_graphs.health_scale_graphs.health_scale_graph1()),
            dcc.Graph(id='findings-healthscale-graph2',
                      figure=tab_3_graphs.health_scale_graphs.health_scale_graph2()),
            html.P(
                "White Females report Poor health at a disporportionately high rate."),
        ], style={'padding': '20px'})

    @staticmethod
    def risksandbarriers_content() -> html.Div:
        return html.Div([
            html.P("The Risks and Barriers score occupies the 100s place, or the third highest priority category. The following graph shows the distribution of scores for this category:"),
            dcc.Graph(id='findings-risksandbarriers-graph',
                      figure=tab_3_graphs.risks_and_barriers_graphs.risks_and_barriers_graph1()),
            html.P("This section serves multiple purposes, one of the most important being accounting for risks and barriers more common among marginalized communities. However, almost every demographic grouping has the same median score of 3."),
            dcc.Graph(id='findings-risksandbarriers-graph2',
                      figure=tab_3_graphs.risks_and_barriers_graphs.risks_and_barriers_graph2()),
            html.P("5.64% of White Males and 2.5% of White Females reported having experienced housing discrimination based on race or ethnicity."),
            dcc.Graph(id='findings-risksandbarriers-graph3',
                      figure=tab_3_graphs.risks_and_barriers_graphs.risks_and_barriers_graph3()),
            html.P("58.9% of BIPOC Females and 72.5% of White Females  reported having experienced domestic violence by a partner or family member."),
            dcc.Graph(id='findings-risksandbarriers-graph4',
                      figure=tab_3_graphs.risks_and_barriers_graphs.risks_and_barriers_graph4()),
            html.P(
                "Questions in this section garner more skips than questions in other sections.")
        ], style={'padding': '20px'})

    @staticmethod
    def householdtype_content() -> html.Div:
        return html.Div([
            html.P("The Household Type score occupies the 10s place, or the fourth highest priority category. The following graph shows the distribution of scores for this category:"),
            html.P("The \"Household Type\" score ranges from 1-9, with values 8 and 9 denoting either a single or family, respectively, fleeing domestic violence."),
            dcc.Graph(id='findings-householdtype-graph',
                      figure=tab_3_graphs.household_type_graphs.household_type_graph1()),
            html.P("The median score is equal across demographic groups at 1."),
            dcc.Graph(id='findings-householdtype-graph2',
                      figure=tab_3_graphs.household_type_graphs.household_type_graph2()),
            html.P(
                "The above graph shows total 96 'yes' responses across all demographic categories."),
            html.P("However, as seen in the graph below, only 5 individuals received a score indicating they were fleeing DV, and only 9 families were scored this way."),
            dcc.Graph(id='findings-householdtype-graph3',
                      figure=tab_3_graphs.household_type_graphs.household_type_graph3()),
            dcc.Graph(id='findings-householdtype-graph4',
                      figure=tab_3_graphs.household_type_graphs.household_type_graph4()),
            dcc.Graph(id='findings-householdtype-graph5',
                      figure=tab_3_graphs.household_type_graphs.household_type_graph5()),
            html.P("The distribution of household type score by race and gender shows that while BIPOC and White Females have a high frequency of scores greater than 1, the frequency of scores '8' and '9' does not match the frequency of answering 'Yes' to the question 'Are you fleeing DV?"),
            dcc.Graph(id='findings-householdtype-graph5',
                      figure=tab_3_graphs.household_type_graphs.household_type_graph6()),
            dcc.Graph(id='findings-householdtype-graph6',
                      figure=tab_3_graphs.household_type_graphs.household_type_graph7()),
            html.P(
                "The distribution of scores in this category does not match the distribution of related answers."),

        ], style={'padding': '20px'})

    @staticmethod
    def livingsituation_content() -> html.Div:
        return html.Div([
            html.P("The Living Situation score occupies the 1s place, or the fifth highest priority category. The following graph shows the distribution of scores for this category:"),
            dcc.Graph(id='findings-livingsituation-graph',
                      figure=tab_3_graphs.living_situation_graphs.living_situation_graph1()),
            dcc.Graph(id='findings-livingsituation-graph2',
                      figure=tab_3_graphs.living_situation_graphs.living_situation_graph2()),
            dcc.Graph(id='findings-livingsituation-graph3',
                      figure=tab_3_graphs.living_situation_graphs.living_situation_graph3()),
            html.P("The distribution of scores for this subsection does not match the distribution of answers to the relevant question. While most people responded that they are living in outside or in another place not meant for habitation, very few received a high score which would indicate this."),
        ], style={'padding': '20px'})


def fourth_tab_layout() -> html.Div:
    return html.Div([
        html.H3('Recommendation and Report', style={
                'text-align': 'center', 'margin-bottom': '20px'}),
        html.P('Here is a detailed report on our methodologies and findings from our analysis on the PIT, PVA and VISPDAT datasets.'),
        html.A('Download Report', href='../assets/EvaluativeReport.pdf',
               download='evalreport.pdf'),
    ])


def fifth_tab_layout() -> html.Div:
    image_filename = 'aboutus.png'
    return html.Div(
        style=styles['container'],
        children=[
            html.H3('About US', style={'text-align': 'center', 'margin-bottom': '20px'}),
            html.Img(src=image_filename, alt='Image of the four Datalab fellows who worked on this project', style=styles['image']),
            html.Hr(),
            html.P("We are a team of four DataLab fellows partnering with the Chattanooga Regional Homeless Coalition in their efforts to ensure equitable access to resources for the Homeless Population. DataLab is a prestigious summer fellowship program hosted by the University of the South in Sewanee, TN. It focuses on utilizing data science for social good. We are one of five teams partnering with government agencies and non-profit organizations to promote data-informed decision-making."),
            html.P("We were lucky to receive guidance throughout the fellowship from our mentors, Kit Rodolfa, Research Director at Stanford RegLab, and Chris Silver, Associate Professor of Psychology at The University of the South. We received additional help and guidance from our staff mentor, Hallie Rutten, University of the South C'23.")
        ]
    )
