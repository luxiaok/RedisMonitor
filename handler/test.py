#!/usr/bin/python
#-*- coding:utf8 -*-
# Desgin By Xiaok
from application.main import *

class TestHandler(BaseHandler):
    #@Auth
    def get(self):
        self.render2("test.html")