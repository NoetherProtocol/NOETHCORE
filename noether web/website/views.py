from flask import Blueprint, render_template

views = Blueprint('views', __name__)

@views.route('/')
def home():
	return render_template("template.html")

@views.route('whitepaper')
def whitepaper():
	return render_template("whitepaper.html")

@views.route('about')
def about():
	return render_template("about.html")

@views.route('contact')
def contact():
	return render_template("contact.html")