from dash import Dash, html, dcc, Input, Output, State
import dash_bootstrap_components as dbc
from components.main_layout import create_main_layout
from components.all_tabs import first_tab_layout, second_tab_layout, third_tab_layout, fourth_tab_layout, fifth_tab_layout
from data import tab_2_graphs
import plotly.graph_objects as go


def main() -> None:
    app = create_app()

    @app.callback(Output('tabs-content', 'children'),
                  [Input('tabs', 'value')])
    def render_content(tab: str) -> html.Div:
        if tab == 'tab-1':
            return first_tab_layout()
        elif tab == 'tab-2':
            return second_tab_layout()
        elif tab == 'tab-3':
            return third_tab_layout()
        elif tab == 'tab-4':
            return fourth_tab_layout()
        elif tab == 'tab-5':
            return fifth_tab_layout()

    @app.callback(Output('explore-pva-graph', 'figure'),
                [Input('dropdown-lothomeless', 'value'),
                Input('dropdown-healthscale', 'value'),
                Input('dropdown-risksandbarriers', 'value'),
                Input('dropdown-householdtype', 'value'),
                Input('dropdown-livingsituation', 'value')], cache=False)
    def update_graph(dropdown_lothomeless, dropdown_healthscale, dropdown_risksandbarriers, dropdown_householdtype, dropdown_livingsituation):
        col_names = [dropdown_lothomeless, dropdown_healthscale, dropdown_risksandbarriers, dropdown_householdtype, dropdown_livingsituation]
        col_name = next((arg for arg in col_names[::-1] if arg is not None), None)
        print(col_name)
        # create a plot based on the selected dropdown options
        fig = tab_2_graphs.create_plot(col_name) 
        return fig

    run_server(app)


def create_app() -> Dash:
    app = Dash(__name__, external_stylesheets=[
               dbc.themes.LUX], title="Dashboard")
    app.layout = create_main_layout(app)
    return app


def run_server(app: Dash) -> None:
    app.run_server(debug=True)


if __name__ == "__main__":
    main()
