#Importem les llibreries
import plotly.graph_objs as go
from plotly.offline import plot

#Creem les dades de la gràfica
x = [1,2,3,4,5,6]
y = [2,4,6,8,10]

#Creem la grafica
data = [go.Scatter(x=x,y=y)]

#Configurem el layout de la gràfica 
layout= go.Layout(tittle='Mi grafica', xaxis=dict(title='Eix X'), yaxis=dict(title='Eje Y'))

#Creem la figura
fig = go.Figure(data=data,layout=layout)

#Exportem la gràfica a un archiu HTML
plot(fig, filename = 'mi_grafica.html')
