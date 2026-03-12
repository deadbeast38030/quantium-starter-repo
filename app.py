from dash import Dash, html, dcc, callback, Output, Input
import plotly.express as px
import pandas as pd
import datetime

df = pd.read_csv('data/output.csv')
df['date'] = pd.to_datetime(df['date'])
df = df.sort_values('date')

app = Dash(__name__)

app.layout = html.Div([
    html.H1('Pink Morsel Sales Visualiser', style={
        'textAlign': 'center',
        'color': 'white',
        'backgroundColor': '#e91e8c',
        'padding': '20px',
        'marginBottom': '20px',
        'borderRadius': '10px',
        'fontFamily': 'Arial, sans-serif',
        'letterSpacing': '2px'
    }),

    html.Div([
        html.Label('Filter by Region:', style={
            'fontWeight': 'bold',
            'fontSize': '16px',
            'fontFamily': 'Arial, sans-serif',
            'marginBottom': '10px',
            'color': '#333'
        }),
        dcc.RadioItems(
            id='region-filter',
            options=[
                {'label': 'All', 'value': 'all'},
                {'label': 'North', 'value': 'north'},
                {'label': 'South', 'value': 'south'},
                {'label': 'East', 'value': 'east'},
                {'label': 'West', 'value': 'west'}
            ],
            value='all',
            inline=True,
            style={'fontFamily': 'Arial, sans-serif', 'fontSize': '15px'},
            inputStyle={'marginRight': '5px', 'marginLeft': '15px'}
        )
    ], style={
        'backgroundColor': '#f9f9f9',
        'padding': '20px',
        'borderRadius': '10px',
        'marginBottom': '20px',
        'boxShadow': '0px 2px 6px rgba(0,0,0,0.1)'
    }),

    dcc.Graph(id='sales-chart'),

], style={
    'maxWidth': '1200px',
    'margin': 'auto',
    'padding': '30px',
    'backgroundColor': '#ffffff',
    'fontFamily': 'Arial, sans-serif'
})

@callback(
    Output('sales-chart', 'figure'),
    Input('region-filter', 'value')
)
def update_chart(selected_region):
    if selected_region == 'all':
        filtered_df = df
    else:
        filtered_df = df[df['region'] == selected_region]

    fig = px.line(
        filtered_df,
        x='date',
        y='sales',
        color='region',
        title='Pink Morsel Sales Over Time',
        labels={'date': 'Date', 'sales': 'Sales ($)', 'region': 'Region'}
    )

    fig.add_vline(
        x=datetime.datetime(2021, 1, 15).timestamp() * 1000,
        line_dash='dash',
        line_color='red',
        annotation_text='Price Increase',
        annotation_position='top right'
    )

    fig.update_layout(
        plot_bgcolor='#fff0f7',
        paper_bgcolor='white',
        font=dict(family='Arial, sans-serif', size=13),
        title_font=dict(size=20, color='#e91e8c'),
        legend=dict(bgcolor='#f9f9f9', bordercolor='#ddd', borderwidth=1)
    )

    return fig

if __name__ == '__main__':
    app.run(debug=True)
