#!/usr/bin/python
#-*- coding:utf8 -*-
#Design By Xiaok

from handler import login
from handler import index
from handler import test

HandlersURL = [
    (r"/(|login)/?", login.LoginHandler),
    (r"/logout", login.LogoutHandler),
    (r"/dashboard/?", index.IndexHandler),
    (r"/ajax/dashboard.html", index.AjaxDashboardHandler),
    (r"/test", test.TestHandler),
    #(r"/(favicon\.ico)", tornado.web.StaticFileHandler, dict(path=settings['static_path']+"images/icon")),
]
