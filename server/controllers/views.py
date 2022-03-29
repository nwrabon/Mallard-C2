import flask
import threading
import common


view_routes = flask.Blueprint('views', __name__)


@view_routes.route('/')
@view_routes.route('/clients')
def clients():
	return flask.render_template('index.html', hosts=common.hosts)


@view_routes.route('/payloads/<client>')
def payloads(client):
	return flask.render_template('payloads.html', client=client)
