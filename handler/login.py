#!/usr/bin/python
#-*- coding:utf8 -*-
# Desgin By Xiaok
from application.main import *

class LoginHandler(BaseHandler):
    def get(self):
        self.render2("login.html")

    def post(self):
        self.redirect("/dashboard")

class LogoutHandler(BaseHandler):
    def get(self):
        self.redirect("/login")