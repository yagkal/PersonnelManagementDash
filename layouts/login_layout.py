import dash_bootstrap_components as dbc
from dash import html


def create_login_layout():
    return dbc.Container(
        dbc.Row(
            dbc.Col(
                dbc.Card(dbc.CardBody([
                    html.H3("Personel Yönetim Sistemi", className="text-center mb-4"),
                    dbc.Label("Kullanıcı adı"),
                    dbc.Input(id="login-username", type="text", className="mb-3"),
                    dbc.Label("Parola"),
                    dbc.Input(id="login-password", type="password", className="mb-3"),
                    dbc.Button("Giriş Yap", id="login-button", className="w-100"),
                    html.Div(id="login-alert", className="mt-3"),
                ])),
                width=12, md=5, lg=4,
            ),
            justify="center",
            className="mt-5",
        ),
    )
