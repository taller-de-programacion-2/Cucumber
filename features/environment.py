from app.app import app
from behave import fixture, use_fixture
import os

# Crea una variable para poder hacer llamadas a la API
@fixture
def app_client(context, *args, **kwargs):
    app.testing = True
    context.client = app.test_client()
    yield context.client


# Hooks para hacer Rollbacks y setear variable de entorno de test
def before_all(context):
    os.environ["TEST_MODE"] = "1"

def before_feature(context, feature):
    use_fixture(app_client, context)
    context.vars = {} # Rollback de variables entre feature (vars permite compartir variables entre steps)
    context.client.post("/reset")

def after_scenario(context, scenario):
    context.client.post("/reset")

def after_all(context):
    del os.environ["TEST_MODE"]


