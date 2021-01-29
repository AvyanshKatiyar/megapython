from flask import Flask, render_template
import jinja2

####################

#to update on heroku
#../virtual/bin/pip3  freeze > requirements.txt
#^ get requirements



#FLask class object from flas

#initializing the class 
app=Flask(__name__)


#another menu item
@app.route("/plot/")
def plot():
    from pandas_datareader import data
    import datetime
    from bokeh.plotting import figure, show, output_file
    from bokeh.embed import components
    from bokeh.resources import CDN

    #help
    #data.DataReader?

    # AAPL is the ticker for apple
    start_time=datetime.datetime(2015,11,2)
    end_time=datetime.datetime(2016, 3,10)

    #pandas dataframe

    df=data.DataReader(name="GOOG", data_source="yahoo",start=start_time, end=end_time)

    #gets index values i.e dates
    #df.index

    close_g_open=df.index[df.Close > df.Open]
    open_g_close=df.index[df.Close < df.Open]

    df

    ################METHOD 1



    p=figure(x_axis_type="datetime", width=1000, height=300, sizing_mode="scale_width")
    p.title.text="Candle Stick Chart"

    #closing>opening then grey else red color

    #miliseconds
    hours_12=12*60*60*1000

    # close>g
    # X, midpoint, width, length
    #p.rect(close_g_open,(df.Open+df.Close)/2,hours_12, abs(df.Open-df.Close), 
        #fill_color="green", line_color="black")

    # close<open
    # X, midpoint, width, length
    #p.rect(df.index[df.Close < df.Open],(df.Open+df.Close)/2,hours_12, abs(df.Open-df.Close), 
        #fill_color="red", line_color="black")






    #output_file("CS.html")
    #show(p)
    #p.rect


    ######################## METHOD 2

    #changing transperancy of the grid
    p.grid.grid_line_alpha=0.4


    #doing the high low values 
    #layer wise therefore this is behinf
    p.segment(df.index, df.High, df.index, df.Low, color="black")


    #creating open close
    def incr_dec(c, o):
        if c>o:
            value="+"
            
        elif c<o:
            value="-"
        else:
            value="="
        return value

    df["Status"]=[incr_dec(c,o) for c,o in zip(df.Close, df.Open)]


    df["Middle"]=(df.Open+df.Close)/2
    df["Height"]=(df.Open-df.Close)



    # close>g
    # X, midpoint, width, length
    p.rect(df.index[df["Status"]=="+"],df.Middle[df["Status"]=="+"],hours_12, abs(df.Height[df["Status"]=="+"]), 
        fill_color="green", line_color="black")

    # close<open
    # X, midpoint, width, length
    p.rect(df.index[df["Status"]=="-"],df.Middle[df["Status"]=="-"],hours_12, abs(df.Height[df["Status"]=="-"]), 
        fill_color="red", line_color="black")



    #to get the various files used to make bokeh
    script1, div1 =components(p)
    cdn_js=CDN.js_files[0]
    return render_template("plot.html",script1=script1,div1=div1,cdn_js=cdn_js)

    #output_file("CS.html")

    #show(p)


    #java
    #print(script1)

    #html
    #print(div1)
            
    #we only care for the first link the other
    #2 are for iwdgets and compilers
    #cdn_js[0]

    # cdn has changed css is no longer needed?
    #so empty list is returned
    #cdn_css[]



@app.route('/')
def home():
    return render_template("home.html")

@app.route('/about/')
def about():
    return render_template("about.html")


if __name__=="__main__":
    app.run(debug=True)
    