from dash import Dash, html, dcc, Input, Output
import dash_bootstrap_components as dbc
from components.main_layout import create_main_layout
from components.all_tabs import first_tab_layout, second_tab_layout, third_tab_layout, fourth_tab_layout, fifth_tab_layout


def main() -> None:
    app = create_app()

    @app.callback(Output('tabs-content', 'children'),
                  [Input('tabs', 'value')])
    def render_content(tab: str) -> html.Div:
        if tab == 'tab-1':
            return first_tab_layout()
        elif tab == 'tab-2':
            return second_tab_layout(app)
        elif tab == 'tab-3':
            return third_tab_layout()
        elif tab == 'tab-4':
            return fourth_tab_layout()
        elif tab == 'tab-5':
            return fifth_tab_layout()
    
    
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
