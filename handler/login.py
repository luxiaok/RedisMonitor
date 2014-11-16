#!/usr/bin/python
#-*- coding:utf8 -*-
# Desgin By Xiaok
from application.main import *

class LoginHandler(BaseHandler):
    def get(self,*args):
        #print args # 传入了一个login的参数进来了
        self.render2("login.html")

    def post(self):
        self.redirect("/dashboard")

class LogoutHandler(BaseHandler):
    def get(self):
        self.redirect("/login")