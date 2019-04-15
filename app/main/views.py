from flask import render_template,request,redirect,url_for
from . import main
from ..request import *



@main.route('/')
def index():
	'''
	View root page function that returns the index page and its data
	'''

	general_news = get_news('general')

	return render_template('index.html',general=general_news)
