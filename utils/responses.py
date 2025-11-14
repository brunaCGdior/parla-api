from flask import jsonify

# padrão: { success: bool, code: str, message: str, data?: any, errors?: {} }
def make_response(success: bool, code: str, message: str, data=None, errors=None, http_status=200):
    body = {
        "success": success,
        "code": code,
        "message": message
    }
    if data is not None:
        body["data"] = data
    if errors is not None:
        body["errors"] = errors
    return jsonify(body), http_status

def ok(data=None, msg="OK", code="ok"):
    return make_response(True, code, msg, data, http_status=200)

def created(data=None, msg="Created", code="created"):
    return make_response(True, code, msg, data, http_status=201)

def client_error(message="Bad Request", code="bad_request", errors=None):
    return make_response(False, code, message, errors=errors, http_status=400)

def unauthorized(message="Unauthorized", code="unauthorized"):
    return make_response(False, code, message, http_status=401)

def not_found(message="Not found", code="not_found"):
    return make_response(False, code, message, http_status=404)

def server_error(message="Server error", code="server_error"):
    return make_response(False, code, message, http_status=500)
