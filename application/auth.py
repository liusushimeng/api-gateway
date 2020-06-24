from functools import wraps
import requests
import jwt
import json
from werkzeug.wrappers import Response

def auth_failed(self, request , backend_svc, backend_svc_rpc_method):
    response = Response("ITTZ Rocks!")
    response.status = '401 Unauthorized'
    return response

def requires_auth(f):
    @wraps(f)
    def decorated(self, request , backend_svc, backend_svc_rpc_method ):
        _authz_secret = '-----BEGIN PUBLIC KEY-----\n'+self.config.get('AUTHZ_SECRET')+'\n-----END PUBLIC KEY-----'
        _authz_jwt_algorithms = self.config.get('AUTHZ_ALGORITHMS',['ES256'])
        _request_encoded_jwt = request.headers.get('Authorization').split('Bearer ')[-1]
        print(_authz_secret)
        _request_payload = jwt.decode(_request_encoded_jwt, _authz_secret, algorithms=_authz_jwt_algorithms)
        _authz_url = self.config.get('AUTHZ_URL')
        _authz_payload = {
            "principal": _request_payload['sub'],
            # drn:partition:region:projectId:serviceType:service:instance::actions
            "resource": "drn:aws:cn-north-1:oap:oap:"+str(backend_svc)+":"+str(backend_svc_rpc_method)+"::"+str(request.method),
        }
        print(_authz_payload)
        _authz_headers = {
            "Content-Type":"application/json"
        }
        resp = requests.post(_authz_url, data=json.dumps(_authz_payload), verify=False, headers=_authz_headers)
        print(resp.json()['data'])
        if resp.json()['data']!=True:
            return auth_failed(self, request , backend_svc, backend_svc_rpc_method)
        return f(self, request , backend_svc, backend_svc_rpc_method)
    return decorated
    
