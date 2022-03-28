import flask
import threading
from server import common


view_routes = flask.Blueprint('views', __name__)


@view_routes.route('/')
@view_routes.route('/clients')
def clients():
	# TODO fix access of global var from separate threads
	# with common.lock:
	# 	print(common.hosts)
	# 	return flask.render_template('index.html', hosts=common.hosts)

	return flask.render_template('index.html', hosts=[(("127.0.0.1", 1337), 1234)])
