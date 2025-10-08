import plotly.express as px
import pandas as pd
import os 
import webbrowser

file_path = 'bob_usdt_history.csv'
output_dir = 'plots'
output_file = 'bob_usdt_chart.html'
output_path = os.path.join(output_dir, output_file)


df = pd.read_csv(file_path, parse_dates=['Timestamp'])
fig  = px.line(df, x='Timestamp', y='Price', title='BOB/USDT Exchange Rate Over Time')

fig.update_layout(
    xaxis_title="Timestamp",
    yaxis_title="Price (BOB)",
    template="plotly_white"
)

fig.write_html(output_path)

webbrowser.open(f'file://{os.path.abspath(output_path)}')
