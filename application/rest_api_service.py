import json
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
        request_data = json.loads(request.get_data(as_text=True))
        bsrm = getattr(getattr(self, backend_svc),
                       backend_svc_rpc_method)
        response = bsrm(**request_data)
        if type(response) is list or type(response) is dict:
            return json.dumps(response)
        else:
            return response

    @http('GET,PUT,POST,DELETE', '/echo')
    def echo(self, request):
        return request.method
