from dash import Dash, html, dcc


def style_dropdown():
    """
    Returns a dictionary of CSS styles for the dropdown component.
    """
    return {'width': '500px', 'padding-top': '20px'}


def render_tab_w_dropdown(dropdown_tab_label: str, i_d: str, options_list: list) -> dcc.Tab:
    """
    Renders a tab with a dropdown component.

    Args:
    dropdown_tab_label (str): The label for the dropdown tab.
    i_d (str): The id for the dropdown component.
    options_list (list): A list of options for the dropdown component.

    Returns:
    dcc.Tab: A tab with a dropdown component.
    """
    return dcc.Tab(
        label=dropdown_tab_label,
        value=dropdown_tab_label,
        children=[
            dcc.Dropdown(
                id=i_d,
                options=[{"label": option, "value": option}
                         for option in options_list],
                placeholder='Select',
                multi=False,
                optionHeight=80,
                style=style_dropdown()
            )
        ]
    )
