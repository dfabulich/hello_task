from pants.build_graph.build_file_aliases import BuildFileAliases
from hello_world.target import HelloWorld

def build_file_aliases():
	return BuildFileAliases(
		targets={
			'hello_world': HelloWorld,
		}
	)
