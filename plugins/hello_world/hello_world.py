from pants.task.task import Task

class HelloWorld(Task):
	def execute(self):
		self.context.log.warn("hello world")
