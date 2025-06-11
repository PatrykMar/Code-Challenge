from typing import Any

import aws_cdk as cdk
import aws_cdk.aws_dynamodb as dynamodb
from aws_cdk.aws_apigateway import RestApi, LambdaIntegration
from constructs import Construct

from backend.database.infra import Database
from backend.runtime.infra import Runtime
from backend.api_gateway.infra import RestAPIGW


class Backend(cdk.Stack):

    def __init__(self,
                 scope: Construct,
                 construct_id: str,
                 *,
                 database_dynamodb_billing_mode: dynamodb.Billing,
                 #api_lambda_reserved_concurrency: int,
                 **kwargs: Any,
    ):

        super().__init__(scope, construct_id, **kwargs)

        database = Database(
            self,
            "Database",
            database_dynamodb_billing_mode=database_dynamodb_billing_mode,
        )


        run = Runtime(
            self,
            "Runtime",
            dynamodb_name_table=database.dynamodb_table.table_name,
            #lambda_reserved_concurrency=api_lambda_reserved_concurrency,
        )

        # Granting permissions to what is required only.
        database.dynamodb_table.grant_read_write_data(run.gen_update_lambda)
        database.dynamodb_table.grant_read_write_data(run.gen_delete_lambda)
        database.dynamodb_table.grant_read_write_data(run.gen_validate_lambda)
        database.dynamodb_table.grant_read_data(run.gen_list_lambda)

        api = RestAPIGW(self, "RestApi")

        api.restapi.add_api_key("API-KEY")
        # Usage plan was added via console in AWS due to Usage function not working as expected under debugging

        users_resource = api.restapi.root.add_resource("users")

        users_resource_name = users_resource.add_resource("{email_address}")
        users_resource_name.add_method(
            'GET',
            LambdaIntegration(run.gen_list_lambda,proxy=True),
            api_key_required=True
        )


        users_resource.add_method(
            'PUT',
            LambdaIntegration(run.gen_update_lambda, proxy=True),
            api_key_required=True
        )


        users_resource_name.add_method(
            'DELETE',
            LambdaIntegration(run.gen_delete_lambda, proxy=True),
            api_key_required=True
        )

        login_resource =  api.restapi.root.add_resource("login")

        login_resource.add_method(
            'POST',
            LambdaIntegration(run.gen_validate_lambda, proxy=True),
            api_key_required=True
        )





