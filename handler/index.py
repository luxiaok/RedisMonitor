#!/usr/bin/python
#-*- coding:utf8 -*-
# Desgin By Xiaok
from application.main import *

class IndexHandler(BaseHandler):
    #@Auth
    def get(self):
        self.render2("index.html")

class AjaxDashboardHandler(BaseHandler):
    #@Auth
    def get(self):
        self.render2("dashboard.html")