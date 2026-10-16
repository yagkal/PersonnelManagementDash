from dash import Input, Output, State, dash
import dash_bootstrap_components as dbc
from db import execute_query

def register_input_callbacks(app):
    
    # 1. Kaydet Callback
    @app.callback(
        # Dikkat: Birden fazla callback aynı component'i hedeflediği için allow_duplicate=True şarttır
        Output("input-alert", "children", allow_duplicate=True),
        Input("btn-save", "n_clicks"),
        State("input-ad", "value"),
        State("input-soyad", "value"),
        State("input-departman", "value"),
        State("input-maas", "value"),
        prevent_initial_call=True
    )
    def save_personel(n_clicks, ad, soyad, dept, maas):
        if not n_clicks:
            return dash.no_update
            
        if not all([ad, soyad, dept, maas]):
            return dbc.Alert("Lütfen tüm alanları doldurun!", color="danger")
        
        try:
            sql = "INSERT INTO personeller (ad, soyad, departman, maas) VALUES (%s, %s, %s, %s);"
            execute_query(sql, (ad, soyad, dept, maas))
            return dbc.Alert("Kayıt başarıyla eklendi!", color="success")
        except Exception as e:
            return dbc.Alert(f"Hata oluştu: {str(e)}", color="danger")

    # 2. Temizle Callback
    @app.callback(
        [
            Output("input-ad", "value"),
            Output("input-soyad", "value"),
            Output("input-departman", "value"),
            Output("input-maas", "value"),
            Output("input-alert", "children", allow_duplicate=True)
        ],
        Input("input-btn-clean", "n_clicks"),
        prevent_initial_call=True
    )
    def clean_input_ui(n_clicks):
        try:
            if n_clicks:
                # Tam olarak 5 elemanlı liste/tuple dönmeli
                return "", "", "", None, dbc.Alert("Form temizlendi!", color="info")
            
            return dash.no_update, dash.no_update, dash.no_update, dash.no_update, dash.no_update
            
        except Exception as e:
            error_msg = dbc.Alert(f"Hata oluştu: {str(e)}", color="danger")
            return dash.no_update, dash.no_update, dash.no_update, dash.no_update, error_msg
