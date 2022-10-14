from datetime import datetime
from Motion_dectetor import df
#import pandas as pd
from bokeh.plotting import figure,show,output_file
from bokeh.models import HoverTool,ColumnDataSource

#df["Start_string"]=df["Start"]("%Y-%m-%d %H:%M:%S")
#df["End_string"]=df["End"].dt.strftime("%Y-%m-%d %H %M %S")
cds= ColumnDataSource(df)

p=figure(x_axis_type = 'datetime',height =200 ,width = 500 ,title="Motion Graph",sizing_mode="scale_width")
p.yaxis.minor_tick_line_color = None
p.yaxis[0].ticker.desired_num_ticks =1

hover = HoverTool(
    tooltips=[
        ("Start","@Start{%Y-%m-%d %H:%M:%S}"),("End","@End{%Y-%m-%d %H:%M:%S}")
        ],
    formatters ={
        "@Start":"datetime",
        "@End":"datetime"
    } 
)
p.add_tools(hover)

q=p.quad(left='Start',right='End',bottom=0,top=1,color='green',source =cds)

output_file("motion_plotting.html")
show(p)

