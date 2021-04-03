#!/usr/bin/env python3

from aws_cdk import core

from cdk_crud.cdk_crud_stack import CdkCrudStack


app = core.App()
CdkCrudStack(app, "cdk-crud", env={'region': 'us-west-2'})

app.synth()
