from hello_world import HelloWorld
from pants.goal.task_registrar import TaskRegistrar as task

def register_goals():
	task(name='hello-world', action=HelloWorld).install('hello-world')