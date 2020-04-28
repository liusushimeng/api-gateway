from nameko.web.handlers import http
from nameko.dependency_providers import Config
from application.service_proxy import IntegratedService
from nameko.rpc import rpc, RpcProxy

import json


class APIServer:
    name = "rest_api_service"
    config = Config()
    print(config)
    for k,v in config.items():
        print(k,v)
    #chatops_proxy = RpcProxy('chatops_slack_service')
    
    @http('GET,PUT,POST,DELETE', '/echo')
    def echo(self, request):
        
        #chatops_proxy.send_message("#operation",JIRA_ID="IAC-11343",JIRA_LINK="https://itsc-jira.daimler.com/jira/browse/IAC-11343",JIRA_SUMMARY="OAP2_Dev_APP_Cloud9_Deployment",ChangeType="CFN",ChangeWindow="Now",Requester="Ruoran",ChangeDetails=r"```line1cell1       line1cell2line2cell1\\nline2cell2```",ValueApproved="approve",ValueDenied="deny")
        return request.method