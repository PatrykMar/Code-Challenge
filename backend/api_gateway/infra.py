from aws_cdk import aws_apigateway
from aws_cdk.aws_apigateway import RestApi
from constructs import Construct

class RestAPIGW(Construct):

    def __init__(self,
                 scope: Construct,
                 construct_id: str,
                 **kwargs
    ):
        super().__init__(scope, construct_id)

        self.restapi = RestApi(self,
                               "GenRestAPIGW",
                               description="GenRestAPIGW for user management and authentication"
                               )

