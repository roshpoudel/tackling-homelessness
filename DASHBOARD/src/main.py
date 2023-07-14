from dash import Dash, html, dcc, Input, Output, State
import dash_bootstrap_components as dbc
from components.main_layout import create_main_layout
from components.all_tabs import home_page_layout, first_tab_layout, second_tab_layout, third_tab_layout, fourth_tab_layout, fifth_tab_layout
from data import tab_2_graphs
import plotly.graph_objects as go


def main() -> None:
    app = create_app()

    @app.callback(Output('tabs-content', 'children'),
                  [Input('tabs', 'value')])
    def render_content(tab: str) -> html.Div:
        if tab == 'tab-0':
            return home_page_layout()
        elif tab == 'tab-1':
            return first_tab_layout()
        elif tab == 'tab-2':
            return second_tab_layout()
        elif tab == 'tab-3':
            return third_tab_layout()
        elif tab == 'tab-4':
            return fourth_tab_layout()
        elif tab == 'tab-5':
            return fifth_tab_layout()

    @app.callback(Output('explore-pva-graph1', 'figure'),
                  Output('explore-pva-graph2', 'figure'),
                [Input('explore-pva-tabs', 'value'),
                Input('dropdown-lothomeless', 'value'),
                Input('dropdown-healthscale', 'value'),
                Input('dropdown-risksandbarriers', 'value'),
                Input('dropdown-householdtype', 'value'),
                Input('dropdown-livingsituation', 'value')])
    def update_graph(explore_pva_tabs, dropdown_lothomeless, dropdown_healthscale, dropdown_risksandbarriers, dropdown_householdtype, dropdown_livingsituation):
        labels_and_ids = dict(zip(['Length of Time Homeless', 'Health Scale', 'Risk and Barriers', 'Household Type', 'Living Situation'],
                         [dropdown_lothomeless, dropdown_healthscale, dropdown_risksandbarriers, dropdown_householdtype, dropdown_livingsituation]))
        
        try:
            col_name = labels_and_ids[explore_pva_tabs]
            try:
                # create a plot based on the selected dropdown options
                fig1 = tab_2_graphs.create_plot(col_name, y_axis='count') 
                fig2 = tab_2_graphs.create_plot(col_name, y_axis='percent')
                return fig1, fig2
            except:
                return go.Figure(data=[], layout=go.Layout(title=go.layout.Title(text="Please select an option from the dropdowns above"))), go.Figure()
    
        except KeyError:
            return go.Figure(), go.Figure()
        
    run_server(app)


def create_app() -> Dash:
    app = Dash(__name__, external_stylesheets=[dbc.themes.LUX], title="Dashboard", suppress_callback_exceptions=True)
    app.layout = create_main_layout(app)
    return app

def run_server(app: Dash) -> None:
    app.run_server(debug=True)


if __name__ == "__main__":
    main()
