# Importing necessary libraries
from dash import Dash, html, dcc, Input, Output, State
import dash_bootstrap_components as dbc
from components.main_layout import create_main_layout
from components.all_tabs import home_page_layout, first_tab_layout, second_tab_layout, ThirdTab, fourth_tab_layout, fifth_tab_layout
from data import tab_2_graphs
import plotly.graph_objects as go


def main() -> None:
    """
    The main function that creates the Dash app, defines the callbacks and runs the server.
    """
    # Creating the Dash app
    app = create_app()

    # Defining the callback for rendering the content of the tabs
    @app.callback(Output('tabs-content', 'children'),
                  [Input('tabs', 'value')])
    def render_content(tab: str) -> html.Div:
        """
        Renders the content of the selected tab.

        Parameters:
        tab (str): The ID of the selected tab.

        Returns:
        html.Div: The layout of the selected tab.
        """
        if tab == 'tab-0':
            return home_page_layout()
        elif tab == 'tab-1':
            return first_tab_layout()
        elif tab == 'tab-2':
            return second_tab_layout()
        elif tab == 'tab-3':
            return ThirdTab.third_tab_layout()
        elif tab == 'tab-4':
            return fourth_tab_layout()
        elif tab == 'tab-5':
            return fifth_tab_layout()

    # Defining the callback for updating the graphs based on the selected dropdown options
    @app.callback(Output('explore-pva-graph1', 'figure'),
                  Output('explore-pva-graph2', 'figure'),
                  [Input('explore-pva-tabs', 'value'),
                   Input('dropdown-lothomeless', 'value'),
                   Input('dropdown-healthscale', 'value'),
                   Input('dropdown-risksandbarriers', 'value'),
                   Input('dropdown-householdtype', 'value'),
                   Input('dropdown-livingsituation', 'value')])
    def update_graph(explore_pva_tabs, dropdown_lothomeless, dropdown_healthscale, dropdown_risksandbarriers, dropdown_householdtype, dropdown_livingsituation):
        """
        Updates the graphs based on the selected dropdown options.

        Parameters:
        explore_pva_tabs (str): The value of the selected tab.
        dropdown_lothomeless (str): The selected option in the Length of Time Homeless dropdown.
        dropdown_healthscale (str): The selected option in the Health Scale dropdown.
        dropdown_risksandbarriers (str): The selected option in the Risk and Barriers dropdown.
        dropdown_householdtype (str): The selected option in the Household Type dropdown.
        dropdown_livingsituation (str): The selected option in the Living Situation dropdown.

        Returns:
        tuple: The two updated graphs.
        """
        # Creating a dictionary of the dropdown labels and IDs
        labels_and_ids = dict(zip(['Length of Time Homeless', 'Health Scale', 'Risk and Barriers', 'Household Type', 'Living Situation'],
                                  [dropdown_lothomeless, dropdown_healthscale, dropdown_risksandbarriers, dropdown_householdtype, dropdown_livingsituation]))

        try:
            # Getting the column name based on the selected tab
            col_name = labels_and_ids[explore_pva_tabs]
            try:
                # Creating a plot based on the selected dropdown options
                fig1 = tab_2_graphs.create_plot(col_name, y_axis='count')
                fig2 = tab_2_graphs.create_plot(col_name, y_axis='percent')
                return fig1, fig2
            except:
                # Returning an empty plot with a message if there's an error
                return go.Figure(data=[], layout=go.Layout(title=go.layout.Title(text="Please select an option from the dropdowns above"))), go.Figure()

        except KeyError:
            # Returning empty plots if the selected tab is not in the dictionary
            return go.Figure(), go.Figure()

    # Defining the callback for updating the content of the findings tabs
    tab_functions = {
        'findings-lothomeless': ThirdTab.lothomeless_content,
        'findings-healthscale': ThirdTab.healthscale_content,
        'findings-risksandbarriers': ThirdTab.risksandbarriers_content,
        'findings-householdtype': ThirdTab.householdtype_content,
        'findings-livingsituation': ThirdTab.livingsituation_content
    }

    @app.callback([Output('findings-lothomeless', 'children'),
                   Output('findings-healthscale', 'children'),
                   Output('findings-risksandbarriers', 'children'),
                   Output('findings-householdtype', 'children'),
                   Output('findings-livingsituation', 'children')],
                  [Input('findings-tabs', 'value')])
    def update_findings_tabs(findings_tabs):
        """
        Updates the content of the findings tabs.

        Parameters:
        findings_tabs (str): The value of the selected tab.

        Returns:
        tuple: The updated content of the findings tabs.
        """
        return tuple(func() if tab == findings_tabs else None for tab, func in tab_functions.items())

    # Running the server
    run_server(app)


def create_app() -> Dash:
    """
    Creates the Dash app.

    Returns:
    Dash: The created Dash app.
    """
    app = Dash(__name__, external_stylesheets=[
               dbc.themes.LUX], title="Dashboard", suppress_callback_exceptions=True)
    app.layout = create_main_layout(app)
    return app


def run_server(app: Dash) -> None:
    """
    Runs the Dash server.

    Parameters:
    app (Dash): The Dash app to run.
    """
    app.run_server(debug=True, port=8050)


if __name__ == "__main__":
    main()
