import json
import pytest

from aws_cdk import core
from cdk-crud.cdk_crud_stack import CdkCrudStack


def get_template():
    app = core.App()
    CdkCrudStack(app, "cdk-crud")
    return json.dumps(app.synth().get_stack("cdk-crud").template)


def test_sqs_queue_created():
    assert("AWS::SQS::Queue" in get_template())


def test_sns_topic_created():
    assert("AWS::SNS::Topic" in get_template())
