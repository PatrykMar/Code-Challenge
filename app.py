#!/usr/bin/env python3
import os

import aws_cdk as cdk
import aws_cdk.aws_dynamodb as dynamodb
from backend.component import Backend


app = cdk.App()


# Component Stack
# Entry point of the CDK
# It will create a stack in AWS CloudFormation with GenCodeChallengeStack supplied.

Backend(app,
        "GenCodeChallenge",
        env=cdk.Environment(account='420717141005', region='eu-west-1'),
        #api_lambda_reserved_concurrency=1, # Couldn't reserve but would be 1 due to account limit
        database_dynamodb_billing_mode=dynamodb.Billing.on_demand()
    )

app.synth()
