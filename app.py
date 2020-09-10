from flask import Flask, render_template, request, redirect
import yfinance as yf
import pandas as pd
from bokeh.layouts import gridplot
from bokeh.plotting import figure, output_file, show
app = Flask(__name__)

@app.route('/')
def index():

	stock = "MSFT" #Stock to choose
	start = "2017-01-01"
	end = "2020-08-30"

	data = pd.DataFrame(yf.download(stock, start=start, end=end).reset_index())

	p1 = figure(x_axis_type="datetime", title="Stock Closing Prices")
	p1.grid.grid_line_alpha=0.3
	p1.xaxis.axis_label = 'Date'
	p1.yaxis.axis_label = 'Price'

	p1.line(data['Date'], data['Close'], color='green')

#	output_file("stocks.html", title="stocks.py example")

	return show(p1)


if __name__ == '__main__':
  app.run(port=5000)
