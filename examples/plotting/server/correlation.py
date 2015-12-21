import time

from numpy import cumprod, linspace, random

from bokeh.plotting import figure, show, output_server, vplot

num_points = 300

now = time.time()
dt = 24*3600 # days in seconds
dates = linspace(now, now + num_points*dt, num_points) * 1000 # times in ms
acme = cumprod(random.lognormal(0.0, 0.04, size=num_points))
choam = cumprod(random.lognormal(0.0, 0.04, size=num_points))

TOOLS = "pan,wheel_zoom,box_zoom,reset,save"

r = figure(x_axis_type = "datetime", tools=TOOLS)
r.title = "Stock Returns"
r.grid.grid_line_alpha=0.3

r.line(dates, acme, color='#1F78B4', legend='ACME')
r.line(dates, choam, color='#FB9A99', legend='CHOAM')

c = figure(tools=TOOLS)
c.title = "ACME / CHOAM Correlations"
c.grid.grid_line_alpha=0.3

c.circle(acme, choam, color='#A6CEE3', legend='close')

output_server("correlation")

show(vplot(r, c)) # open a browser
