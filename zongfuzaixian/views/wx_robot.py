from zongfuzaixian.extensions import robot


@robot.handler
def hello(message):
    return 'Hello World!'

