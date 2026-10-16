from dash import html, dcc
import dash_bootstrap_components as dbc

def create_report_layout():
    return dbc.Container([
        html.H2("Personel Raporlama Ekranı", className="my-3 text-center"),
        dbc.Button("Raporu Yenile", id="btn-refresh-report", color="info", className="mb-3"),
        dbc.Row([
            dbc.Col([
                dcc.Graph(id="chart-dept-maas")
            ], width=6),
            dbc.Col([
                dcc.Graph(id="chart-dept-count")
            ], width=6)
        ])
    ], fluid=True)
