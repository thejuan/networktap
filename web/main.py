#!/usr/bin/env python

import web
import os
import tldextract

render = web.template.render('/opt/monitor/web/templates/')

urls = (
    '/search', 'search'
)

db = web.database(dbn='sqlite', db='/opt/monitor/log.db')

class search:
    def GET(self):
	query = web.input( since='2000-01-01',  to='2200-01-01', domain='*')
        data = db.select("urls", what="*", where="occurred between $query.since and $query.to", vars=locals())
	web.header('Content-Type', 'txt/csv')
	web.header('Content-Disposition', 'attachment; filename=urls.csv')
	return render.search([dict(row,domain='.'.join(tldextract.extract(row['url'])[-2:])) for row in data])


if __name__ == "__main__":

    application = web.application(urls, globals())
    application.run()
