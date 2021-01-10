import io
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import numpy as np

from flask import Flask, render_template, Response

from bracketingMethod.bisection import *
from bracketingMethod.false_position import *
from bracketingMethod.secant import *

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/bisection.png')
def bisection_method():
	f = "x**2 - x - 1"
	fig = bisection_plot(f, 0, 5, 10)
	output = io.BytesIO()
	FigureCanvas(fig).print_png(output)
	return Response(output.getvalue(), mimetype='image/png')

def bisection_plot(f, a, b, N, err=False):
	# Get data
	data = list(bisection(f, a, b, N, err).values())
	root = [i[4] for i in data]
	# Plot
	x = np.linspace(a,b,100)
	n = [0 for i in range(len(root))]
	fig = Figure()
	axis = fig.add_subplot(1, 1, 1)
	axis.plot(x, eval(f))
	axis.plot(root, n, "|")
	axis.grid()
	# Plotting error
	if err != False:
		error = [i[6] for i in data]
		axis.plot(n, error)
	return fig


@app.route('/false_position.png')
def false_position_method():
	f = "x**2 - x - 1"
	fig = false_position_plot(f, 0, 5, 10)
	output = io.BytesIO()
	FigureCanvas(fig).print_png(output)
	return Response(output.getvalue(), mimetype='image/png')

def false_position_plot(f, a, b, N, err=False):
	# Get data
	data = list(false_position(f, a, b, N, err).values())
	root = [i[4] for i in data]
	# Plot
	x = np.linspace(a,b,100)
	n = [0 for i in range(len(root))]
	fig = Figure()
	axis = fig.add_subplot(1, 1, 1)
	axis.plot(x, eval(f))
	axis.plot(root, n, "|")
	axis.grid()
	# Plotting error
	if err != False:
		error = [i[6] for i in data]
		axis.plot(n, error)
	return fig

@app.route('/secant.png')
def secant_method():
	f = "x**2 - x - 1"
	fig = secant_plot(f, 0, 5, 10)
	output = io.BytesIO()
	FigureCanvas(fig).print_png(output)
	return Response(output.getvalue(), mimetype='image/png')

def secant_plot(f, a, b, N):
	# Get data
	data = list(secant(f, a, b, N).values())
	root = [i[4] for i in data]
	# Plot
	x = np.linspace(a,b,100)
	n = [0 for i in range(len(root))]
	fig = Figure()
	axis = fig.add_subplot(1, 1, 1)
	axis.plot(x, eval(f))
	axis.plot(root, n, "|")
	axis.grid()
	return fig

if __name__=='__main__':
	app.run(debug=True)