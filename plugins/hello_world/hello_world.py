from pants.task.task import Task
from pants.build_graph.target import Target

class HelloWorldTask(Task):
	def execute(self):
		self.context.log.warn("hello world")

class HelloWorldTarget(Target):
	pass
