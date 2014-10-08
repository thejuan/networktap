#!/usr/bin/env python

import web
import os

render = web.template.render('/opt/monitor/web/templates/')

urls = (
    '/search', 'search'
)

db = web.database(dbn='sqlite', db='/opt/monitor/log.db')

class search:
    def GET(self):
        data = db.select("urls", what="*")
	web.header('Content-Type', 'txt/csv')
	web.header('Content-Disposition', 'attachment; filename=urls.csv')
	return render.search(data)


if __name__ == "__main__":

    application = web.application(urls, globals())
    application.run()
