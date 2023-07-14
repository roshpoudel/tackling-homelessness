from dash import Dash, html, dcc


def style_dropdown():
    return {'width': '500px'}


def render_tab_w_dropdown(dropdown_tab_label: str, i_d: str, options_list: list) -> dcc.Tab:
    return dcc.Tab(label=dropdown_tab_label, value=dropdown_tab_label, children=[
                dcc.Dropdown(
                    id=i_d,
                    options=[{"label": option, "value": option} for option in options_list],
                    placeholder='Select',
                    multi=False,
                    optionHeight=100,
                    style=style_dropdown(),
                )
            ])