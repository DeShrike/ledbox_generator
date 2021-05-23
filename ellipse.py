import constants
import uuid

class Ellipse():
	def __init__(self, x:int, y:int, r:int, color:str):
		self.x = x
		self.y = y
		self.r = r
		self.color = color
		self.id = "ellipse_" + str(uuid.uuid4())

	def write_to_file(self, fd):
		# print(f"Writing: {self.id}")
		xml = constants.ELLIPSE_XML
		xml = xml.replace("{{ID}}", self.id)
		xml = xml.replace("{{X}}", str(self.x))
		xml = xml.replace("{{Y}}", str(self.y))
		xml = xml.replace("{{R}}", str(self.r))
		xml = xml.replace("{{COLOR}}", self.color)
		fd.write(xml)
