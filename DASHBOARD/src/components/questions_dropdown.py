from dash import Dash, html, dcc


def style_dropdown():
    return {'width': '500px', 'padding-top': '20px'}


def render_tab_w_dropdown(dropdown_tab_label: str, i_d: str, options_list: list) -> dcc.Tab:
    return dcc.Tab(
        label=dropdown_tab_label,
        value=dropdown_tab_label,
        children=[
            dcc.Dropdown(
                id=i_d,
                options=[{"label": option, "value": option} for option in options_list],
                placeholder='Select',
                multi=False,
                optionHeight=80,
                style=style_dropdown()
            )
        ]
    )
