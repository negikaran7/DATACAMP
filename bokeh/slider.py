from bokeh.io import curdoc
from bokeh.layouts import Column
from bokeh.models import ColumnDataSource, Slider
from bokeh.plotting import figure
from numpy.random import random

N=500
source=ColumnDataSource(data={'x':random(N),'y':random(N)})

plot=figure()
plot.square(x='x',y='y',source=source)

slider=Slider(start=20,end=1000,value=N,step=10,title='number of points')

def callback(attr, old, new):
    N=slider.value
    source.data={'x':random(N),'y':random(N)}
slider.on_change('value',callback)

layout=Column(slider,plot)
curdoc().add_root(layout)