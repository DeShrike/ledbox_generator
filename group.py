import constants
import uuid

class Group():
	def __init__(self, id):
		self.paths = []	
		self.groups = []
		self.texts = []
		self.ellipses = []
		self.id = id

	def write_to_file(self, fd):
		if len(self.groups) + len(self.paths) + len(self.texts) + len(self.ellipses) == 0:
			return
		print(f"Writing: {self.id}")
		header = constants.GROUP_START
		header = header.replace("{{ID}}", self.id)
		fd.write(header)
		for p in self.paths:
			p.write_to_file(fd)
		for g in self.groups:
			g.write_to_file(fd)
		for t in self.texts:
			t.write_to_file(fd)
		for e in self.ellipses:
			e.write_to_file(fd)
		fd.write(constants.GROUP_END)

	def add_path(self, path):
		self.paths.append(path)

	def add_ellipse(self, ellipse):
		self.ellipses.append(ellipse)
