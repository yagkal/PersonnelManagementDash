from dash import html, dcc
import dash_bootstrap_components as dbc

def create_input_layout():
    return dbc.Container([
        html.H2("Yeni Personel Kaydı", className="my-3 text-center"),
        dbc.Row([
            dbc.Col([
                dbc.Label("Ad:"),
                dbc.Input(id="input-ad", type="text", placeholder="Ad giriniz"),
                dbc.Label("Soyad:", className="mt-2"),
                dbc.Input(id="input-soyad", type="text", placeholder="Soyad giriniz"),
                dbc.Label("Departman:", className="mt-2"),
                dbc.Input(id="input-departman", type="text", placeholder="Departman giriniz"),
                dbc.Label("Maaş:", className="mt-2"),
                dbc.Input(id="input-maas", type="number", placeholder="Maaş giriniz"),
                dbc.Button("Kaydet", id="btn-save", color="primary", className="mt-3 w-100"),
                dbc.Button("Temizle", id="input-btn-clean", color="secondary", className="mt-2 w-100"),
                html.Div(id="input-alert", className="mt-3")
            ], width=6)
        ], justify="center")
    ], fluid=True)
