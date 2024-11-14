from dash import html, dcc
from .tabs import generate_tabs

def create_layout(app):
    return html.Div([
        html.H1("Pricing Analysis Dashboard"),
        generate_tabs()  # This will contain all the tab components
    ])
