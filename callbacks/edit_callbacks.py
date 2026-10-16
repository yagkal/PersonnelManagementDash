from dash import Input, Output, State, html, dash_table, ctx, no_update
import dash_bootstrap_components as dbc
from db import execute_query, fetch_data

def register_edit_callbacks(app):
    # Seçilen kaydı form alanlarına doldurma
    @app.callback(
        [Output("edit-ad", "value"),
         Output("edit-soyad", "value"),
         Output("edit-departman", "value"),
         Output("edit-maas", "value")],
        Input("edit-id-select", "value"),
        prevent_initial_call=True
    )
    def populate_form(selected_id):
        if not selected_id:
            return "", "", "", ""
        df = fetch_data("SELECT * FROM personeller WHERE id = %s", (selected_id,))
        if not df.empty:
            row = df.iloc[0]
            return row['ad'], row['soyad'], row['departman'], row['maas']
        return "", "", "", ""

    # Güncelleme ve Silme işlemleri
    @app.callback(
        [Output("edit-alert", "children"), 
         Output("edit-id-select", "options", allow_duplicate=True),
         Output("table-container", "children", allow_duplicate=True)],
        [Input("btn-update", "n_clicks"),
         Input("btn-delete", "n_clicks")],
        [State("edit-id-select", "value"),
         State("edit-ad", "value"),
         State("edit-soyad", "value"),
         State("edit-departman", "value"),
         State("edit-maas", "value")],
        prevent_initial_call=True
    )
    def update_or_delete(btn_update, btn_delete, selected_id, ad, soyad, dept, maas):
        if not selected_id:
            return dbc.Alert("Lütfen listeden bir kayıt seçin!", color="warning"), no_update, no_update
        
        triggered_id = ctx.triggered_id
        alertObj = None
        if triggered_id == "btn-update":
            sql = "UPDATE personeller SET ad=%s, soyad=%s, departman=%s, maas=%s WHERE id=%s"
            execute_query(sql, (ad, soyad, dept, maas, selected_id))
            alertObj = dbc.Alert(f"ID: {selected_id} güncellendi.", color="success")
            
        elif triggered_id == "btn-delete":
            sql = "DELETE FROM personeller WHERE id=%s"
            execute_query(sql, (selected_id,))
            alertObj = dbc.Alert(f"ID: {selected_id} silindi.", color="danger")
        options, table = renew_lists()
        return alertObj, options, table

    # Formu temizle
    @app.callback(
        [
            Output("edit-ad", "value", allow_duplicate=True),
            Output("edit-soyad", "value", allow_duplicate=True),
            Output("edit-departman", "value", allow_duplicate=True),
            Output("edit-maas", "value", allow_duplicate=True),
            Output("edit-alert", "children", allow_duplicate=True)
        ],
        Input("edit-btn-clean", "n_clicks"),
        prevent_initial_call=True
    )
    def clean_input_ui(n_clicks):
        try:
            if n_clicks:
                # Beş Output için beş değer döner
                return "", "", "", None, dbc.Alert("Form temizlendi!", color="info")
            
            return no_update, no_update, no_update, no_update, no_update
            
        except Exception as e:
            error_msg = dbc.Alert(f"Hata oluştu: {str(e)}", color="danger")
            return no_update, no_update, no_update, no_update, error_msg

def renew_lists():
    df = fetch_data("SELECT * FROM personeller ORDER BY id ASC")
    options = [{"label": f"{r['id']} - {r['ad']} {r['soyad']}", "value": r['id']} for _, r in df.iterrows()]
    
    table = dash_table.DataTable(
        data=df.to_dict('records'),
        columns=[{"name": i, "id": i} for i in df.columns],
        page_size=8,
        style_table={'overflowX': 'auto'}
    )
    return options, table
