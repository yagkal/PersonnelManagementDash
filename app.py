import os
import secrets

import dash
import dash_bootstrap_components as dbc
from dash import Input, Output, dcc, html
from flask import session

from callbacks.login_callbacks import register_login_callbacks
from callbacks.input_callbacks import register_input_callbacks
from callbacks.edit_callbacks import register_edit_callbacks
from callbacks.report_callbacks import register_report_callbacks
from layouts.login_layout import create_login_layout
from layouts.input_layout import create_input_layout
from layouts.edit_layout import create_edit_layout
from layouts.report_layout import create_report_layout

app = dash.Dash(
    __name__,
    external_stylesheets=[dbc.themes.BOOTSTRAP],
    suppress_callback_exceptions=True,
)
server = app.server
server.secret_key = os.getenv("FLASK_SECRET_KEY") or secrets.token_hex(32)


def create_navbar():
    return dbc.NavbarSimple(
        children=[
            dbc.NavItem(dbc.NavLink("Yeni Kayıt", href="/", active="exact")),
            dbc.NavItem(dbc.NavLink("Güncelle / Sil", href="/edit", active="exact")),
            dbc.NavItem(dbc.NavLink("Raporlama", href="/report", active="exact")),
            dbc.NavItem(
                dbc.Button("Çıkış", id="logout-button", color="outline-light", className="ms-2")
            ),
        ],
        brand=f"Personel Yönetimi | {session['username']}",
        brand_href="/",
        color="dark",
        dark=True,
        className="mb-4",
    )


app.layout = html.Div([
    dcc.Location(id="url", refresh=False),
    html.Div(id="page-content"),
])


@app.callback(Output("page-content", "children"), Input("url", "pathname"))
def display_page(pathname):
    if "username" not in session:
        return create_login_layout()

    if pathname == "/edit":
        page = create_edit_layout()
    elif pathname == "/report":
        page = create_report_layout()
    else:
        page = create_input_layout()

    return html.Div([create_navbar(), page])



register_login_callbacks(app)
register_input_callbacks(app)
register_edit_callbacks(app)
register_report_callbacks(app)

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8050, debug=True)
