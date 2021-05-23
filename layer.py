import constants
import uuid

class Layer():
	def __init__(self, name:str):
		self.name = name
		self.paths = []	
		self.groups = []
		self.texts = []
		self.id = str(uuid.uuid4())

	def write_to_file(self, fd):
		if len(self.groups) + len(self.paths) + len(self.texts) == 0:
			return
		print(f"Writing: {self.id}")
		header = constants.LAYER_START
		header = header.replace("{{NAME}}", self.name)
		header = header.replace("{{ID}}", self.id)
		fd.write(header)
		for p in self.paths:
			p.write_to_file(fd)
		for g in self.groups:
			g.write_to_file(fd)
		for t in self.texts:
			t.write_to_file(fd)
		fd.write(constants.LAYER_END)
