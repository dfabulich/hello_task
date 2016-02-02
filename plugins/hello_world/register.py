from hello_world import *
from pants.goal.task_registrar import TaskRegistrar as task
from pants.build_graph.build_file_aliases import BuildFileAliases

def register_goals():
	task(name='hello-world', action=HelloWorldTask).install('hello-world')

def build_file_aliases():
  return BuildFileAliases(
    targets={
      'hello_world': HelloWorldTarget,
    },
  )
