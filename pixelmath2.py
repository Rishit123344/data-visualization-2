import pandas as pd 
import csv
import plotly.graph_objects as go 
df = pd.read_csv('pixelmath.csv')
studentdf = df.loc[df['student_id']=='TRL_zet']
print(studentdf.groupby('level')['attempt'].mean())
fig = go.Figure(go.Bar(x = studentdf.groupby('level')['attempt'].mean(), y = ['level1','level2','level3','level4'],orientation = 'h'  ))
fig.show()