from dash import html, dcc, dash_table
import dash_bootstrap_components as dbc
from callbacks.edit_callbacks import renew_lists

def create_edit_layout():
    # Fetch initial data on page load
    initial_options, initial_table = renew_lists()

    return dbc.Container([
        html.H2("Personel Güncelle / Sil", className="my-3 text-center"),
        dbc.Row([
            dbc.Col([
                html.H4("Kayıt Değiştir"),
                dbc.Label("Personel Seç ID:"),
                dcc.Dropdown(
                    id="edit-id-select", 
                    options=initial_options,  # Populated on load
                    placeholder="Personel Seçin"
                ),
                dbc.Label("Ad:"),
                dbc.Input(id="edit-ad", type="text"),
                dbc.Label("Soyad:"),
                dbc.Input(id="edit-soyad", type="text"),
                dbc.Label("Departman:"),
                dbc.Input(id="edit-departman", type="text"),
                dbc.Label("Maaş:"),
                dbc.Input(id="edit-maas", type="number"),
                
                dbc.Row([
                    dbc.Col(dbc.Button("Güncelle", id="btn-update", color="warning", className="w-100 mt-3")),
                    dbc.Col(dbc.Button("Sil", id="btn-delete", color="danger", className="w-100 mt-3")),
                ]),
                dbc.Button("Temizle", id="edit-btn-clean", color="secondary", className="mt-2 w-100"),
                html.Div(id="edit-alert", className="mt-3")
            ], width=4),
            
            dbc.Col([
                html.H4("Mevcut Kayıtlar"),
                html.Div(
                    initial_table, 
                    id="table-container"
                )  # Populated on load
            ], width=8)
        ])
    ], fluid=True)
