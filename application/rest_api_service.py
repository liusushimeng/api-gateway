import json

import nameko
import yaml

from nameko.web.handlers import http
from nameko.rpc import rpc, RpcProxy


class APIServer:
    name = "rest_api_service"

    yaml2dict = yaml.load(open('config/config.yaml').read(),
                          Loader=yaml.FullLoader)
    backend_services = yaml2dict.get('SERVICES')
    for k, v in backend_services.items():
        if v:
            exec('{} = RpcProxy("{}")'.format(k, k))

    @http('POST,GET', '/<string:backend_svc>/<string:backend_svc_rpc_method>')
    def http_proxy(self, request, backend_svc, backend_svc_rpc_method):
        try:
            request_data = json.loads(request.get_data(as_text=True))
            try:
                bsvc = getattr(self, backend_svc)
                try:
                    bsrm = getattr(bsvc, backend_svc_rpc_method)
                    try:
                        response = bsrm(**request_data)
                        if type(response) is list or type(response) is dict:
                            return json.dumps(response)
                        else:
                            return response
                    except nameko.exceptions.IncorrectSignature:
                        return "argument is wrong, please check."
                except nameko.exceptions.MethodNotFound:
                    return "No backend method: " + backend_svc_rpc_method
            except AttributeError:
                return "No backend service: " + backend_svc
        except json.decoder.JSONDecodeError:
            return "If no argument, please use {}"

    @http('GET,PUT,POST,DELETE', '/echo')
    def echo(self, request):
        return request.method
