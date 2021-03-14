import constants

class Path():
	def __init__(self, id:str, closed:bool):
		self.id = id
		self.nodes = []
		self.closed = closed
		self.color = "000000"
		self.flip_xy = False

	def write_to_file(self, fd):
		if len(self.nodes) == 0:
			return
		xml = constants.PATH_XML
		xml = xml.replace("{{ID}}", self.id)
		xml = xml.replace("{{COLOR}}", self.color)
		xml = xml.replace("{{NODETYPES}}", "c" * len(self.nodes))
		path_data = self.generate_svg_path()
		xml = xml.replace("{{DATA}}", path_data)
		fd.write(xml)

	def last_x(self) -> float:
		return self.nodes[-1][0]

	def last_y(self) -> float:
		return self.nodes[-1][1]

	def generate_svg_path(self) -> str:
		data = ""
		ixx = 1 if self.flip_xy else 0
		ixy = 0 if self.flip_xy else 1
		x = self.nodes[0][ixx]
		y = self.nodes[0][ixy]
		data += f"M {x},{y}"
		for node in self.nodes[1:]:
			dx = node[ixx] - x
			dy = node[ixy] - y
			if dx == 0 and dy != 0:
				y = node[ixy]
				data += f" V {y}"
			elif dx != 0 and dy == 0:
				x = node[ixx]
				data += f" H {x}"
			else:
				data += f" L {x},{y}"

		if self.closed:
			data = data + " Z"

		print(data)
		return data

	def add_node(self, x:float, y:float):
		self.nodes.append( (x, y) )
