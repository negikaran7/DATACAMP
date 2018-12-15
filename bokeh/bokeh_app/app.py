from bokeh.io import curdoc

from bokeh.plotting import figure
from bokeh.io import show
from bokeh.models import HoverTool

# Create a blank figure with labels
p1 = figure(plot_width = 400, plot_height = 400, 
           title = 'plot 1',
           x_axis_label = 'X', y_axis_label = 'Y')

# Example data
squares_x = [1, 3, 4, 5, 8]
squares_y = [8, 7, 3, 1, 10]
circles_x = [9, 12, 4, 3, 15]
circles_y = [8, 4, 11, 6, 10]
# Add squares glyph
p1.square(squares_x, squares_y, size = 12, color = 'navy', alpha = 0.6,legend='squares1')
# Add circle glyph
p1.circle(circles_x, circles_y, size = 12, color = 'red',legend='circles1')
p1.legend.location='top_left'

p2 = figure(plot_width = 400, plot_height = 400, 
           title = 'Plot 2',
           x_axis_label = 'X', y_axis_label = 'Y')

# Example data
squares_x = [10, 3, 14, 25, 18]
squares_y = [8, 7, 3, 1, 10]
circles_x = [9, 4, 8, 7, 5]
circles_y = [8, 4, 11, 16, 10]

# Add squares glyph
p2.square(squares_x, squares_y, size = 12, color = 'yellow', alpha = 0.6,legend='squares2')
# Add circle glyph
p2.circle(circles_x, circles_y, size = 12, color = 'blue',legend='circles2')
p2.legend.location='bottom_right'

p3 = figure(plot_width = 400, plot_height = 400, 
           title = 'Plot 3',
           x_axis_label = 'X', y_axis_label = 'Y')

# Example data
squares_x = [10, 3, 14, 25, 18]
squares_y = [8, 7, 3, 1, 10]
circles_x = [9, 4, 8, 7, 5]
circles_y = [8, 4, 11, 16, 10]

# Add squares glyph
p3.square(squares_x, squares_y, size = 12, color = 'black', alpha = 0.6,legend='squares3')
# Add circle glyph
p3.circle(circles_x, circles_y, size = 12, color = 'orange',legend='circles3')
p3.legend.location='bottom_left'

#link plots
p3.x_range=p2.x_range=p1.x_range
p3.y_range=p2.y_range=p1.y_range

#tabbed plot
from bokeh.models.widgets import Tabs, Panel
from bokeh.io import output_file
from bokeh.layouts import row, column
first=Panel(child=row(p1,p2),title='first')
second=Panel(child=row(p3),title='second')
tabs=Tabs(tabs=[first,second])
output_file('tabbed_layout.html')
# show(tabs)
curdoc().add_root(tabs)