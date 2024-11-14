from dash import dcc
from .charts import (
    generate_heatmap,
    generate_grouped_bar_chart,
    generate_region_avg_change_bar,
    generate_price_change_distribution,
    generate_outliers_scatter,
    generate_top_movers_bar_chart
)

def generate_tabs():
    return dcc.Tabs([
        dcc.Tab(label='Average Price Difference Heatmap', children=[dcc.Graph(figure=generate_heatmap())]),
        dcc.Tab(label='Average Price Difference by Brand', children=[dcc.Graph(figure=generate_grouped_bar_chart())]),
        dcc.Tab(label='Average Percentage Change by Region', children=[dcc.Graph(figure=generate_region_avg_change_bar())]),
        dcc.Tab(label='Price Change Distribution by Region', children=[dcc.Graph(figure=generate_price_change_distribution())]),
        dcc.Tab(label='Outliers in Price Difference', children=[dcc.Graph(figure=generate_outliers_scatter())]),
        dcc.Tab(label='Top Movers Analysis', children=[dcc.Graph(figure=generate_top_movers_bar_chart())]),
    ])
