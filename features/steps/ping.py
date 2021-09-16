from behave import *


@given("la app esta encendida")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass


@when("si le pego al /ping")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.response = context.client.get("/ping")


@then('recibo un mensaje "{}"')
def step_impl(context, message_content):
    """
    :param message_content: String
    :type context: behave.runner.Context
    """
    assert context.response.status_code == 200
    assert context.response.json()['message'] == message_content