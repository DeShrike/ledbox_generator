import constants
import uuid

class Text():
	def __init__(self, x:int, y:int, color:str, text:str):
		self.x = x
		self.y = y
		self.text = text
		self.color = color
		self.id = str(uuid.uuid4())

	def write_to_file(self, fd):
		xml = constants.TEXT_XML
		xml = xml.replace("{{ID}}", self.id)
		xml = xml.replace("{{X}}", str(self.x))
		xml = xml.replace("{{Y}}", str(self.y))
		xml = xml.replace("{{TEXT}}", self.text)
		xml = xml.replace("{{COLOR}}", self.color)
		fd.write(xml)
