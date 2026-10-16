from pathlib import Path

import dash_bootstrap_components as dbc
import yaml
from dash import Input, Output, State, no_update
from flask import session
from werkzeug.security import check_password_hash

USERS_FILE = Path(__file__).resolve().parent.parent / "users.yml"


def valid_user(username, password):
    """Kullanıcı adını ve parolayı users.yml dosyasıyla karşılaştırır."""
    with USERS_FILE.open("r", encoding="utf-8") as file:
        users = (yaml.safe_load(file) or {}).get("users", {})
    saved_hash = users.get(username)
    return bool(saved_hash and check_password_hash(saved_hash, password))


def register_login_callbacks(app):
    @app.callback(
        Output("url", "pathname"),
        Output("login-alert", "children"),
        Input("login-button", "n_clicks"),
        State("login-username", "value"),
        State("login-password", "value"),
        prevent_initial_call=True,
    )
    def login(n_clicks, username, password):
        if not username or not password:
            return no_update, dbc.Alert("Kullanıcı adı ve parola girin.", color="warning")

        if valid_user(username, password):
            session["username"] = username
            return "/home", ""

        return no_update, dbc.Alert("Kullanıcı adı veya parola yanlış.", color="danger")

    # Çıkış butonuna basıldığında oturumu sil ve login ekranına dön.
    @app.callback(
        Output("url", "pathname", allow_duplicate=True),
        Input("logout-button", "n_clicks"),
        prevent_initial_call=True,
    )
    def logout(n_clicks):
        if n_clicks:
            session.clear()
            return "/login"
        return no_update
