from motion_detector import df
from bokeh.plotting import figure,show,output_file
from bokeh.models import HoverTool,ColumnDataSource

df["Start_String"]=df["Start"].dt.strftime("%Y-%m-%d %H:%M:%S")
df["End_String"]=df["End"].dt.strftime("%Y-%m-%d %H:%M:%S")

cds=ColumnDataSource(df)

p=figure(x_axis_type="datetime",width=500,height=100,responsive=True,title="Motion Graph")

p.xaxis.axis_label="Active Duration"
p.yaxis.minor_tick_line_color=None
p.ygrid[0].ticker.desired_num_ticks=1

hover=HoverTool(tooltips=[("Start","@Start_String"),("End","@End_String")])
p.add_tools(hover)

p.quad(top=1,bottom=0,right=df['End'],left=df['Start'],color='green',source=cds)
output_file("motion1.html")

show(p)
