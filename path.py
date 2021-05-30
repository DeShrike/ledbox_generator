import constants
from helpers import Rotation, rotate_point

class Path():
	def __init__(self, id:str, closed:bool):
		self.id = id
		self.nodes = []
		self.closed = closed
		self.color = "000000"
		self.flip_xy = False
		self.delta = (0, 0)

	def move(self, delta):
		self.delta = delta

	def write_to_file(self, fd):
		if len(self.nodes) == 0:
			return
		# print(f"Writing: {self.id}")
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

	def format_number(self, num:float) -> str:
		s = f"{float(num):.6f}"
		return s

	def generate_svg_path(self) -> str:
		data = ""
		translated = []

		ixx = 1 if self.flip_xy else 0
		ixy = 0 if self.flip_xy else 1

		for node in self.nodes:
			translated.append((node[ixx] + self.delta[ixx], node[ixy] + self.delta[ixy]))

		x = translated[0][0]
		y = translated[0][1]
		data += f"M {self.format_number(x)},{self.format_number(y)}"
		for node in translated[1:]:
			dx = node[0] - x
			dy = node[1] - y
			if dx == 0 and dy != 0:
				y = node[1]
				data += f" V {self.format_number(y)}"
			elif dx != 0 and dy == 0:
				x = node[0]
				data += f" H {self.format_number(x)}"
			else:
				x = node[0]
				y = node[1]
				data += f" L {self.format_number(x)},{self.format_number(y)}"

		if self.closed:
			data = data + " Z"

		# print(data)
		return data

	def add_node(self, x:float, y:float, rotation:Rotation = None):
		if rotation is None:
			self.nodes.append( (x, y) )
		else:
			rotated = rotate_point(rotation.cx, rotation.cy, x, y, rotation.angle)
			self.nodes.append( rotated )
