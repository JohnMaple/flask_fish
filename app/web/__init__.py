"""
Created by Alex
"""
from flask import Blueprint

web = Blueprint('web', __package__)

from app.web import book
from app.web import user

