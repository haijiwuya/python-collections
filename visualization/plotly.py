import plotly
import plotly.offline as py
import numpy as np
import plotly.graph_objs as go

# 直方图
plotly.offline.init_notebook_mode(connected=True)

N = 100
random_x = np.linspace(0, 1, N)
random_y0 = np.random.randn(N) + 5
random_y1 = np.random.randn(N)
random_y2 = np.random.randn(N) - 5

# create traces
trace0 = go.Scatter(
    x=random_x,
    y=random_y0,
    mode='markers',
    name='markers'
)

trace1 = go.Scatter(
    x=random_x,
    y=random_y1,
    mode='lines+markers',
    name='lines+markers'
)

trace2 = go.Scatter(
    x=random_x,
    y=random_y2,
    mode='lines',
    name='lines'
)
data0 = [trace0, trace1, trace2]
py.iplot(data0)

# 散点图
trace3 = go.Scatter(
    y=np.random.randn(500),
    mode='markers',
    marker=dict(
        size=16,
        color=np.random.randn(500),
        colorscale='Viridis',
        showscale=True
    )
)
data1 = [trace3]
py.iplot(data1, filename='scatter-plot-with-colorscale')

# 气泡图
data2 = [{
    'x': [1, 3.2, 5.4, 7.6, 9.8, 12.5],
    'y': [1, 3.2, 5.4, 7.6, 9.8, 12.5],
    'mode': 'markers',
    'marker': {
        'color': [120, 125, 130, 135, 140, 145],
        'size': [15, 30, 55, 70, 90, 110],
        'showscale': True
    }
}]
py.iplot(data2)

# 柱状图
trace4 = go.Bar(
    x=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
    y=[20, 14, 25, 16, 18, 22, 19, 15, 12, 16, 14, 17],
    name='Primary Product',
    marker=dict(color='rgb(49,130,189)')
)
trace5 = go.Bar(
    x=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
    y=[19, 14, 22, 14, 16, 19, 15, 14, 10, 12, 12, 16],
    name='Secondary Product',
    marker=dict(color='rgb(204,204,204)')
)
data3 = [trace4, trace5]
py.iplot(data3)


