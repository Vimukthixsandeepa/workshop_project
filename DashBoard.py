import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd

# Load the dataset
file_path = 'wine_df_cleaned.csv'
wine_df = pd.read_csv(file_path)

# Initialize the Dash app with a Bootstrap theme
app = dash.Dash(_name_, external_stylesheets=[dbc.themes.SOLAR])  # Try other themes like BOOTSTRAP, COSMO
app.title = "Wine Insights Dashboard"

# Layout of the dashboard
app.layout = dbc.Container([
    # Navbar
    dbc.NavbarSimple(
        brand="Wine Insights Dashboard",
        brand_href="#",
        color="primary",
        dark=True,
        className="mb-4"
    ),

    # Dropdown filter
    dbc.Row([
        dbc.Col([
            html.Label("Select Country:", className="fw-bold"),
            dcc.Dropdown(
                id='country-dropdown',
                options=[{'label': country, 'value': country} for country in wine_df['Country'].unique()],
                value=wine_df['Country'].unique()[0],
                className="mb-4"
            )
        ], width=4)
    ], className="mb-4"),

    # Charts: Bar and Scatter
    dbc.Row([
        dbc.Col(dcc.Graph(id='bar-chart', config={"displayModeBar": False}), width=6),
        dbc.Col(dcc.Graph(id='scatter-plot', config={"displayModeBar": False}), width=6)
    ]),

    # Charts: Pie and Box
    dbc.Row([
        dbc.Col(dcc.Graph(id='pie-chart', config={"displayModeBar": False}), width=6),
        dbc.Col(dcc.Graph(id='box-plot', config={"displayModeBar": False}), width=6)
    ]),

    # Line chart
    dbc.Row([
        dbc.Col(dcc.Graph(id='line-chart', config={"displayModeBar": False}), width=12)
    ]),

    # Sensory Scores: Bold, Tannin, Sweet, Acidic
    dbc.Row([
        dbc.Col(dcc.Graph(id='bold-box-plot', config={"displayModeBar": False}), width=6),
        dbc.Col(dcc.Graph(id='tannin-box-plot', config={"displayModeBar": False}), width=6)
    ]),

    dbc.Row([
        dbc.Col(dcc.Graph(id='sweet-box-plot', config={"displayModeBar": False}), width=6),
        dbc.Col(dcc.Graph(id='acidic-box-plot', config={"displayModeBar": False}), width=6)
    ]),

    # Footer
    html.Footer(
        "© 2024 Wine Insights, All Rights Reserved",
        className="text-center mt-4"
    )
], fluid=True)

# Callback to update charts based on country selection
@app.callback(
    [Output('bar-chart', 'figure'),
     Output('scatter-plot', 'figure'),
     Output('pie-chart', 'figure'),
     Output('box-plot', 'figure'),
     Output('line-chart', 'figure'),
     Output('bold-box-plot', 'figure'),
     Output('tannin-box-plot', 'figure'),
     Output('sweet-box-plot', 'figure'),
     Output('acidic-box-plot', 'figure')],
    [Input('country-dropdown', 'value')]
)
def update_charts(selected_country):
    # Filter data based on selected country
    filtered_df = wine_df[wine_df['Country'] == selected_country]

    # Bar chart: Average rating by wine style
    bar_chart = px.bar(
        filtered_df.groupby('Wine style')['Rating'].mean().reset_index(),
        x='Wine style', y='Rating',
        title="Average Rating by Wine Style",
        labels={'Rating': 'Average Rating'},
        color='Rating',
        text_auto=True,
        template='plotly_dark'
    )

    # Scatter plot: Price vs Rating
    scatter_plot = px.scatter(
        filtered_df, x='Price', y='Rating',
        title="Price vs Rating",
        color='Alcohol content',
        size='Number of Ratings',
        hover_name='Name',
        template='plotly_dark'
    )

    # Pie chart: Food pairings
    food_counts = filtered_df[['Beef', 'Pasta', 'Lamb', 'Poultry', 'Cheese', 'Fish', 'Seafood']].sum()
    pie_chart = px.pie(
        names=food_counts.index, values=food_counts.values,
        title="Popular Food Pairings",
        template='plotly_dark'
    )

    # Box plot: Alcohol content by wine style
    box_plot = px.box(
        filtered_df, x='Wine style', y='Alcohol content',
        title="Alcohol Content by Wine Style",
        color='Wine style',
        template='plotly_dark'
    )

    # Line chart: Average price over ratings
    avg_price_df = filtered_df.groupby('Rating')['Price'].mean().reset_index()
    line_chart = px.line(
        avg_price_df, x='Rating', y='Price',
        title="Average Price Over Ratings",
        template='plotly_dark'
    )

    # Box plot: Bold by wine style
    bold_box_plot = px.box(
        filtered_df, x='Wine style', y='Bold',
        title="Boldness by Wine Style",
        color='Wine style',
        template='plotly_dark'
    )

    # Box plot: Tannin by wine style
    tannin_box_plot = px.box(
        filtered_df, x='Wine style', y='Tannin',
        title="Tannin Level by Wine Style",
        color='Wine style',
        template='plotly_dark'
    )

    # Box plot: Sweet by wine style
    sweet_box_plot = px.box(
        filtered_df, x='Wine style', y='Sweet',
        title="Sweetness by Wine Style",
        color='Wine style',
        template='plotly_dark'
    )

    # Box plot: Acidic by wine style
    acidic_box_plot = px.box(
        filtered_df, x='Wine style', y='Acidic',
        title="Acidity by Wine Style",
        color='Wine style',
        template='plotly_dark'
    )

    return bar_chart, scatter_plot, pie_chart, box_plot, line_chart, bold_box_plot, tannin_box_plot, sweet_box_plot, acidic_box_plot

# Run the app
if _name_ == '_main_':
    app.run_server(debug=True)