from pants.task.task import Task
from pants.build_graph.target import Target

class HelloWorldTask(Task):
	@staticmethod
	def is_hello_world_target(target):
		return isinstance(target, HelloWorldTarget)

	def execute(self):
		targets = self.context.targets(predicate=self.is_hello_world_target)
		if not targets:
			return
		self.context.log.warn("hello world")

class HelloWorldTarget(Target):
	pass
