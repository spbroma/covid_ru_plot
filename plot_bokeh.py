from bokeh.plotting import figure, output_file, show
from bokeh.models import Label
from get_data import get_data
import bokeh
import numpy as np

data = get_data()

fig = figure(plot_width=1400, y_axis_type="log")


def get_pallete(pallete):
    return pallete[list(pallete.keys())[-1]]

colors = get_pallete(bokeh.palettes.Set3)

for i in range(data.value_align.shape[0]):
# for i in range(3):
    y = data.value_align[i]
    x = np.arange(len(y))
    ci = i % len(colors)
    fig.line(x=x, y=y, legend_label=data.label[i], color=colors[ci])
    if len(x) > 0:
        # fig.text(x=x[-1], y=y[-1], text=data.label[i])
        # fig.text(x=x[-1], y=y[-1], text='qe')
        fig.add_layout(Label(x=x[-1], y=y[-1], text=data.label[i]))
    # fig.circle(x=x, y=y)

# fig.axis

output_file('bokeh.html')

show(fig)