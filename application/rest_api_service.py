import json

import nameko
import yaml
import requests

from nameko.web.handlers import http
from nameko.rpc import RpcProxy  # noqa W0611
from nameko.dependency_providers import Config
from application.auth import requires_auth


class APIServer:
    name = "rest_api_service"

    config = Config()
    yaml2dict = yaml.load(open('config/config.yaml').read(),
                          Loader=yaml.FullLoader)
    backend_services = yaml2dict.get('SERVICES')
    for k, v in backend_services.items():
        if v:
            exec('{} = RpcProxy("{}")'.format(k, k))

    @http('POST,GET', '/r/<string:backend_svc>/<string:backend_svc_method>')
    @requires_auth
    def http2rpc(self, request, backend_svc, backend_svc_method):
        try:
            request_data = json.loads(request.get_data(as_text=True))
            try:
                bsvc = getattr(self, backend_svc)
                try:
                    bsrm = getattr(bsvc, backend_svc_method)
                    try:
                        response = bsrm(**request_data)
                        if type(response) is list or type(response) is dict:
                            return json.dumps(response)
                        else:
                            return response
                    except nameko.exceptions.IncorrectSignature:
                        return "ERROR: argument is wrong, please check."
                except nameko.exceptions.MethodNotFound:
                    return "ERROR: No backend method " + backend_svc_method
            except AttributeError:
                return "ERROR: No backend service " + backend_svc
        except json.decoder.JSONDecodeError:
            return "ERROR: If no argument, please use {}"

    @http('POST,GET', '/h/<string:backend_svc>/<string:backend_svc_method>')
    @requires_auth
    def http2http(self, request, backend_svc, backend_svc_method):
        request_url = "http://" + backend_svc + "/" + backend_svc_method
        request_method = request.method.lower()
        request_data = request.get_data(as_text=True)
        request_headers = {"Content-Type": "application/json"}
        response = getattr(requests, request_method)(request_url,
                                                     data=request_data,
                                                     headers=request_headers,
                                                     verify=False)

        return response.text
