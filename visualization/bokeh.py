'''
    安装bokeh：安装完pip后，通过命令：pip install bokeh
    bokeh的主要概念是图形一次构建一层。
    首先创建一个图形(figure)，然后在图形中添加称为图形符号(glyphs)的元素。
    glyphs可以根据所需的用途呈现多种形状：圆形(circles)，线条(lines)，补丁(patches)，条形(bars)，弧形(arcs)等。
'''
# bokeh basics
from bokeh.plotting import figure
from bokeh.io import show, output_notebook

# create a blank figure with labes
p = figure(plot_width=600, plot_height=600, title='Example Glyphs', x_axis_label='X', y_axis_label='Y')

# Example data
squares_x = [1, 3, 4, 5, 8]
squares_y = [8, 7, 3, 1, 10]
circles_x = [9, 12, 4, 3, 15]
circles_y = [8, 4, 11, 6, 10]

# add squares glyph
p.square(squares_x, squares_y, size=12, color='navy', alpha=0.6)
# add circle glyph
p.circle(circles_x, circles_y, size=12, color='red')

# set to output the plot in the notebook
output_notebook()
# show the plot
show(p)
