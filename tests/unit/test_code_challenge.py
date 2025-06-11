import aws_cdk as core
import aws_cdk.assertions as assertions

from gen_code_challenge.gen_code_challenge_stack import GenCodeChallengeStack

# example tests. To run these tests, uncomment this file along with the example
# resource in gen_code_challenge/gen_code_challenge_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = GenCodeChallengeStack(app, "gen-code-challenge")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
