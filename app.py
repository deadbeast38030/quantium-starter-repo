from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

df = pd.read_csv('data/output.csv')
df['date'] = pd.to_datetime(df['date'])
df = df.sort_values('date')

fig = px.line(df, x='date', y='sales', color='region', title='Pink Morsel Sales Over Time', labels={'date': 'Date', 'sales': 'Sales ($)', 'region': 'Region'})

import datetime
fig.add_vline(x=datetime.datetime(2021, 1, 15).timestamp() * 1000, line_dash='dash', line_color='red', annotation_text='Price Increase', annotation_position='top right')

app = Dash(__name__)

app.layout = html.Div([
    html.H1('Pink Morsel Sales Visualiser', style={'textAlign': 'center', 'color': '#333'}),
    dcc.Graph(figure=fig)
])

if __name__ == '__main__':
    app.run(debug=True)
