import os
import aws_cdk.aws_lambda as _lambda
from constructs import Construct
from aws_cdk import Duration

import os.path
dirname = os.path.dirname(__file__)


class Runtime(Construct):

    def __init__(
            self,
            scope: Construct,
            construct_id: str,
            *,
            dynamodb_name_table: str,
            #lambda_reserved_concurrency: int,
    ):
        super().__init__(scope, construct_id)

        # Create Update Delete List Validate
        self.gen_update_lambda = _lambda.Function(
            self,
            "gen_update_lambda",
            code=_lambda.Code.from_asset(os.path.join(dirname, "update_lambda")),
            runtime=_lambda.Runtime.PYTHON_3_11,
            environment={"DYNAMODB_TABLE": dynamodb_name_table},
            timeout=Duration.seconds(300),
            #reserved_concurrent_executions=lambda_reserved_concurrency,
            function_name="gen_update_lambda",
            handler="lambda_function.lambda_handler",
        )

        self.gen_delete_lambda = _lambda.Function(
            self,
            "gen_delete_lambda",
            code=_lambda.Code.from_asset(os.path.join(dirname, "delete_lambda")),
            runtime=_lambda.Runtime.PYTHON_3_11,
            environment={"DYNAMODB_TABLE": dynamodb_name_table},
            timeout=Duration.seconds(300),
            #reserved_concurrent_executions=lambda_reserved_concurrency,
            function_name="gen_delete_lambda",
            handler="lambda_function.lambda_handler",
        )

        self.gen_list_lambda = _lambda.Function(
            self,
            "gen_list_lambda",
            code=_lambda.Code.from_asset(os.path.join(dirname, "list_lambda")),
            runtime=_lambda.Runtime.PYTHON_3_11,
            environment={"DYNAMODB_TABLE": dynamodb_name_table},
            timeout=Duration.seconds(300),
            #reserved_concurrent_executions=lambda_reserved_concurrency,
            function_name="gen_list_lambda",
            handler="lambda_function.lambda_handler",
        )

        self.gen_validate_lambda = _lambda.Function(
            self,
            "gen_validate_lambda",
            code=_lambda.Code.from_asset(os.path.join(dirname, "validate_lambda")),
            runtime=_lambda.Runtime.PYTHON_3_11,
            environment={"DYNAMODB_TABLE": dynamodb_name_table},
            timeout=Duration.seconds(300),
            #reserved_concurrent_executions=lambda_reserved_concurrency,
            function_name="gen_validate_lambda",
            handler="lambda_function.lambda_handler",
        )

