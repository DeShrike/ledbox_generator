import constants
import uuid

class Ellipse():
	def __init__(self, x:float, y:float, r:float, color:str):
		self.x = x
		self.y = y
		self.rx = r
		self.ry = r
		self.color = color
		self.id = "ellipse_" + str(uuid.uuid4())

	def write_to_file(self, fd):
		# print(f"Writing: {self.id}")
		xml = constants.ELLIPSE_XML
		xml = xml.replace("{{ID}}", self.id)
		xml = xml.replace("{{X}}", str(self.x))
		xml = xml.replace("{{Y}}", str(self.y))
		xml = xml.replace("{{RX}}", str(self.rx))
		xml = xml.replace("{{RY}}", str(self.ry))
		xml = xml.replace("{{COLOR}}", self.color)
		fd.write(xml)
