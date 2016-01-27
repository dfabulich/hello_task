from pants.task.task import Task

class Hello_World(Task):
	def execute(self):
		self.context.log.warn("hello world")
