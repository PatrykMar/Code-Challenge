import aws_cdk as cdk
import aws_cdk.aws_dynamodb as dynamodb
from constructs import Construct

class Database(Construct):

    def __init__(
            self,
            scope: Construct,
            construct_id: str,
            *,
            database_dynamodb_billing_mode: dynamodb.Billing,
    ):
        super().__init__(scope, construct_id)

        partition_key = dynamodb.Attribute(
            name="email_address",type=dynamodb.AttributeType.STRING
        )
        #DynamoDB for the users.
        self.dynamodb_table= dynamodb.TableV2(
            self,
            "GenDBTablev1",
            billing=database_dynamodb_billing_mode,
            partition_key=partition_key,
            table_name="GenDBTablev1",
            removal_policy=cdk.RemovalPolicy.DESTROY,
            deletion_protection=True,
            tags=[cdk.CfnTag(key="create by", value="Patryk")],
        )

