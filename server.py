from flask import Flask, render_template, redirect, request
import tornado.wsgi
import tornado.httpserver
import optparse
import os
import argparse

# define path parameters
DEMO_FOLDER = './demo/'
DEMO_URL_PREFIX = '/demo/'
LIB_FOLDER = './lib/'
LIB_URL_PREFIX = '/lib/'
CSS_FOLDER = './css/'
CSS_URL_PREFIX = '/css/'

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

def start_tornado(app, port=5000):

    # set url prefix for tornado static file handler
    demo_url = DEMO_URL_PREFIX + '(.*)'
    demo_url = demo_url.replace("\\", "\\\\")
    lib_url = LIB_URL_PREFIX + '(.*)'
    lib_url = lib_url.replace("\\", "\\\\")
    css_url = CSS_URL_PREFIX + '(.*)'
    css_url = css_url.replace("\\", "\\\\")
   
    # start Tornado server
    wsgi_app = tornado.wsgi.WSGIContainer(app)
    tornado_app = tornado.web.Application(
        [
            (demo_url, tornado.web.StaticFileHandler, {'path': DEMO_FOLDER}),
            (lib_url, tornado.web.StaticFileHandler, {'path': LIB_FOLDER}),
            (css_url, tornado.web.StaticFileHandler, {'path': CSS_FOLDER}),
            ('.*', tornado.web.FallbackHandler, dict(fallback=wsgi_app))
        ])

    tornado_app.listen(port)
    print("Tornado server starting on port {}".format(port))
    tornado.ioloop.IOLoop.instance().start()


def start_from_terminal(app):
    """
    Parse command line options and start the server.
    """
    parser = optparse.OptionParser()
    parser.add_option(
        '-p', '--port',
        help="which port to serve content on",
        type='int', default=8888)

    opts, args = parser.parse_args()

    # Start server
    start_tornado(app, opts.port)



if __name__ == '__main__':

    start_from_terminal(app)
