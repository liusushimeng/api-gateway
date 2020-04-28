from nameko.extensions import DependencyProvider
from nameko.dependency_providers import Config
from nameko.rpc import rpc, RpcProxy

class IntegratedService(DependencyProvider):

    def __init__(self, **kwargs):
        super(IntegratedService, self).__init__(**kwargs)

    def setup(self):
        self.services = {}

    def get_dependency(self, worker_ctx):
        config = self.container.config.copy()
        services = dict()
        config_services = config.get('SERVICES').items()
        for k,v in config_services:
            services[k]= RpcProxy(v)
        return services
