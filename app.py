from dash import Dash, html, dcc
from components.layout import create_layout

# Initialize the Dash app
app = Dash(__name__, external_stylesheets=['/assets/style.css'])
app.title = "Pricing Analysis Dashboard"

# Set the layout of the app
app.layout = create_layout(app)

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
