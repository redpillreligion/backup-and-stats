
import json as JSON
import plotly
import plotly.graph_objs as go

authors = {}
categories = {}
with open('authors.json') as f:
    authors = JSON.load(f)

with open('categories.json') as f:
    categories = JSON.load(f)


trace1 = go.Pie(labels=authors.keys(), values=authors.values(), hoverinfo='label+percent', textinfo='value', 
               textfont=dict(size=20),
               marker=dict(line=dict(color='#000000', width=2)))
layout1 = go.Layout(title='Red Pill Religion Articles by Author')
fig1 = go.Figure(data=[trace1], layout=layout1)
plotly.offline.plot(fig1, filename='authors', auto_open=True)

trace2 = go.Pie(labels=categories.keys(), values=categories.values(), hoverinfo='label+percent', textinfo='value', 
               textfont=dict(size=20),
               marker=dict(line=dict(color='#000000', width=2)))
layout2 = go.Layout(title='Red Pill Religion Articles by Categories')
fig2 = go.Figure(data=[trace2], layout=layout2)
plotly.offline.plot(fig2, filename='categories', auto_open=True)


