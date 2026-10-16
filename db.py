import psycopg2
import pandas as pd
from flask import session
from config import DB_CONFIG


def get_connection():
    # Dash callback'i doğrudan çağrılsa bile giriş yapmadan DB erişimi olmasın.
    if "username" not in session:
        raise PermissionError("Veritabanına erişmek için giriş yapmalısınız.")
    return psycopg2.connect(**DB_CONFIG)


def execute_query(query, params=None):
    """Ekleme, Güncelleme, Silme işlemleri için."""
    conn = get_connection()
    cur = conn.cursor()
    try:
        cur.execute(query, params)
        conn.commit()
    except Exception:
        conn.rollback()
        raise
    finally:
        cur.close()
        conn.close()


def fetch_data(query, params=None):
    """Veri okuma işlemleri için."""
    conn = get_connection()
    try:
        return pd.read_sql_query(query, conn, params=params)
    finally:
        conn.close()
