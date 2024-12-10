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
