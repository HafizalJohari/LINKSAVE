from flask import render_template, flash, redirect, url_for, request
from app import app, db
from app.models import User, Link
from app.forms import LoginForm, RegistrationForm, SaveLinkForm
from flask_login import current_user, login_user, logout_user, login_required
from requests_html import HTMLSession
from bs4 import BeautifulSoup
from PIL import Image
import io
import requests

@app.route('/')
@app.route('/index')
@login_required
def index():
    user = current_user
    links = user.links.all()
    return render_template('index.html', title='Home', user=user, links=links)

# Add other view functions here