from pandas_datareader import data
import datetime
from bokeh.plotting import figure
from bokeh.embed import components

start1 = datetime.datetime(2018, 10, 30)
end1 = datetime.datetime(2019, 5, 30)

df = data.DataReader("TSLA", "yahoo", start=start1, end=end1)


def values(c, o):
    if c > o:
        value = "Increase"
    elif c < o:
        value = "Decrease"
    else:
        value = "equal"
    return value

    df["Status"] = [values(c, o) for c, o in zip(df.Close, df.Open)]
    df["Middle"] = (df.Open + df.Close) / 2
    df["Height"] = abs(df.Close - df.Open)

    df["Status"] = [values(c, o) for c, o in zip(df.Close, df.Open)]


    p = figure(x_axis_type="datetime", width=1000, height=300, sizing_mode="scale_width")
    p.title.text = "Candlestick Chart"
    p.grid.grid_line_alpha = 0.2

    hours_12 = 12 * 60 * 60 * 1000

    p.segment(df.index, df.High, df.index, df.Low, color="Black")

    p.rect(df.index[df.Status == "Increase"], df.Middle[df.Status == "Increase"],
           hours_12, abs(df.Open - df.Close), fill_color="blue", line_color="black")

    p.rect(df.index[df.Status == "Decrease"], df.Middle [df.Status == "Decrease"],
           hours_12, abs(df.Open - df.Close), fill_color="red", line_color="black")

    views, div1 = components(p)
    return render_template("teslabody.html", views=views, div1=div1)
