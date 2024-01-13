from os import environ, getcwd, path, system

import boto3

service_name = path.basename(getcwd())

env = environ['ENVIRONMENT']


client = boto3.client('ecs')

response = client.describe_task_definition(
    taskDefinition=f'{env}-expense-report-{service_name}'
)

task_definition = response.get('taskDefinition')


variables = ''
for container in task_definition.get('containerDefinitions', []):
    for variable in container.get('environment', []):
        variables += f'--env {variable["name"]}={variable["value"]} '
        environ[variable['name']] = variable['value']

from src.controller.messages import extract_prediction_expense

if __name__ == '__main__':
    extract_prediction_expense()
