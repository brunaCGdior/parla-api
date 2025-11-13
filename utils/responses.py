from flask import jsonify

def ok(data=None, msg="OK"):
    body = {"success": True, "message": msg}
        if data is not None:
                body["data"] = data
                    return jsonify(body), 200

                    def created(data=None, msg="Created"):
                        body = {"success": True, "message": msg}
                            if data is not None:
                                    body["data"] = data
                                        return jsonify(body), 201

                                        def error(msg="Error", code=400, errors=None):
                                            body = {"success": False, "message": msg}
                                                if errors:
                                                        body["errors"] = errors
                                                            return jsonify(body), code
                                                            