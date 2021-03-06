import textwrap
from functools import wraps
import requests
import jwt
import json
from werkzeug.wrappers import Response


def auth_failed(self, request, backend_svc, backend_svc_method):
    response = Response("ITTZ Rocks!")
    response.status = '401 Unauthorized'
    return response


def requires_auth(f):
    @wraps(f)
    def decorated(self, request, backend_svc, backend_svc_method):
        _authz_secret = '-----BEGIN PUBLIC KEY-----\n' + '\n'.join(
            textwrap.wrap(self.config.get('AUTHZ_SECRET'),
                          64)) + '\n-----END PUBLIC KEY-----'
        _authz_jwt_algorithms = self.config.get('AUTHZ_ALGORITHMS', ['ES256'])
        _request_encoded_jwt = \
            request.headers.get('Authorization').split('Bearer ')[-1]
        _request_payload = jwt.decode(_request_encoded_jwt, _authz_secret,
                                      algorithms=_authz_jwt_algorithms)
        _authz_url = self.config.get('AUTHZ_URL')
        _authz_payload = {
            "principal": _request_payload['sub'],
            # drn:partition:region:projectId:svcType:svc:instance::actions
            "resource": "drn:aws:cn-north-1:oap:oap:" + str(
                backend_svc) + ":" + str(backend_svc_method) + "::" + str(
                request.method),
        }
        print(_authz_payload)
        _authz_headers = {
            "Content-Type": "application/json"
        }

        resp = requests.post(_authz_url, data=json.dumps(_authz_payload),
                             verify=False, headers=_authz_headers)
        print(resp.json()['data'])
        if resp.json()['data'] is not True:
            return auth_failed(self, request, backend_svc,
                               backend_svc_method)
        return f(self, request, backend_svc, backend_svc_method)

    return decorated
