from dash import Input, Output
import plotly.express as px
from db import fetch_data

def register_report_callbacks(app):
    @app.callback(
        [Output("chart-dept-maas", "figure"),
         Output("chart-dept-count", "figure")],
        Input("btn-refresh-report", "n_clicks")
    )
    def update_charts(n_clicks):
        df = fetch_data("SELECT * FROM personeller")
        
        if df.empty:
            fig1 = px.bar(title="Departman Bazlı Ortalama Maaş (Veri Yok)")
            fig2 = px.pie(title="Departman Bazlı Personel Sayısı (Veri Yok)")
            return fig1, fig2
            
        # 1. Grafik: Departmanlara göre Ortalama Maaş
        avg_maas = df.groupby("departman")["maas"].mean().reset_index()
        fig1 = px.bar(avg_maas, x="departman", y="maas", title="Departmanlara Göre Ortalama Maaş", color="departman")
        
        # 2. Grafik: Departmanlara göre Personel Dağılımı
        dept_count = df["departman"].value_counts().reset_index()
        dept_count.columns = ["departman", "sayi"]
        fig2 = px.pie(dept_count, names="departman", values="sayi", title="Departman Personel Dağılımı")
        
        return fig1, fig2
