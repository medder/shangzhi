from zongfuzaixian.extensions import robot
from flask import Blueprint, request, render_template


@robot.handler
def hello(message):
    print(message)
    return render_template('base.html')


@robot.error_page
def make_error_page(url):
    return "<h1> %s not find </h1>" % url