import sys

class Vertex():
    def __init__(self, x: float, y: float, z: float):
        self.x = x
        self.y = y
        self.z = z

class Quad():
    def __init__(self, vix1: float, vix2: float, vix3: float, vix4: float, name: str = None, reverse: bool = False):
        self.vix1 = vix1
        self.vix2 = vix2
        self.vix3 = vix3
        self.vix4 = vix4
        self.name = name
        self.reverse = reverse

class IslandPoint():
	def __init__(self, position, roofindex: int, rooforder: int) -> None:
		self.position = position
		self.roofindex = roofindex
		self.rooforder = rooforder

class Island():
    def __init__(self, name: str, elevation: float, height: float):
        self.name = name
        self.elevation = elevation
        self.height = height
        self.points = []
        self.roofs = []  # 1-based

    def add_roof(self, indexes):
        self.roofs.append(indexes)

    def _generate_walls(self, obj3d) -> None:
        for ix, p in enumerate(self.points[:-1]):
            p1 = p.position
            p2 = self.points[ix + 1].position
            top1 = (p1[0], p1[1], self.height + self.elevation)
            top2 = (p2[0], p2[1], self.height + self.elevation)
            bottom3 = (p2[0], p2[1], self.elevation)
            bottom4 = (p1[0], p1[1], self.elevation)
            obj3d.add(top1, top2, bottom3, bottom4, f"Wall {ix}")

    def _generate_floor(self, obj3d, z: float) -> None:
        for roof in self.roofs:
            ps = [(self.points[ix - 1].position[0], self.points[ix - 1].position[1], z) for ix in roof]
            obj3d.add_polygon(ps)
        #vecs = [(p[0], p[1], z) for p in self.points[:-1]]
        #obj3d.add_polygon(vecs)

    def generate(self, obj3d) -> None:
        self._generate_walls(obj3d)
        self._generate_floor(obj3d, self.elevation)
        self._generate_floor(obj3d, self.elevation + self.height)

class Box():
    def __init__(self, width: float, depth: float, height: float, name: str = None):
            self.width = width
            self.depth = depth
            self.height = height
            self.name = name
            self.x = 0
            self.y = 0
            self.z = 0

    def __repr__(self) -> str:
        return f"Box({self.width}, {self.depth}, {self.height}, \"{self.name}\") {self.x},{self.y},{self.z}"

    def translate(self, x: float, y: float, z: float):
        self.x += x
        self.y += y
        self.z += z

    def _generate(self, obj3d):
        # bottom
        obj3d.add(
            (self.x, self.y, self.z),
            (self.x + self.width, self.y, self.z),
            (self.x + self.width, self.y + self.depth, self.z),
            (self.x, self.y + self.depth, self.z),
            f"Bottom [{self.name}]")

        # top
        obj3d.add(
            (self.x, self.y, self.z + self.height),
            (self.x + self.width, self.y, self.z + self.height),
            (self.x + self.width, self.y + self.depth, self.z + self.height),
            (self.x, self.y + self.depth, self.z + self.height),
            f"top [{self.name}]")

        # front
        obj3d.add(
            (self.x, self.y, self.z),
            (self.x + self.width, self.y, self.z),
            (self.x + self.width, self.y, self.z + self.height),
            (self.x, self.y, self.z + self.height),
            f"Front [{self.name}]")

        # back
        obj3d.add(
            (self.x, self.y + self.depth, self.z),
            (self.x + self.width, self.y + self.depth, self.z),
            (self.x + self.width, self.y + self.depth, self.z + self.height),
            (self.x, self.y + self.depth, self.z + self.height),
            f"Back [{self.name}]")

        # right
        obj3d.add(
            (self.x + self.width, self.y, self.z),
            (self.x + self.width, self.y, self.z + self.height),
            (self.x + self.width, self.y + self.depth, self.z + self.height),
            (self.x + self.width, self.y + self.depth, self.z),
            f"Right [{self.name}]")

        # left
        obj3d.add(
            (self.x, self.y, self.z),
            (self.x, self.y, self.z + self.height),
            (self.x, self.y + self.depth, self.z + self.height),
            (self.x, self.y + self.depth, self.z),
            f"Left [{self.name}]")

class Object3D():
    def __init__(self):
        self.quads = []
        self.vertices = []
        self.boxes = []
        self.polygons = []

    def save(self, filename: str):
        for box in self.boxes:
            print(box)
            box._generate(self)

        with open(filename, "w") as fo:
            fo.write(f"# {filename}\n")
            fo.write("#\n")
            fo.write("\n")
            fo.write("g box\n")

            fo.write("\n")
            fo.write("# vertices\n")
            fo.write("\n")

            for ix,  vertex in enumerate(self.vertices):
                fo.write(f"v {vertex.x} {vertex.z} {vertex.y}  # {ix + 1}\n")

            fo.write("\n")
            fo.write("# vertice normals\n")
            fo.write("\n")

            fo.write("\n")
            fo.write("# faces\n")
            fo.write("\n")

            for quad in self.quads:
                if quad.name is not None:
                    fo.write(f"\n# Quad '{quad.name}'\n")
                if quad.reverse:
                    fo.write(f"f {quad.vix4 + 1} {quad.vix3 + 1} {quad.vix2 + 1} {quad.vix1 + 1}\n")
                else:
                    fo.write(f"f {quad.vix1 + 1} {quad.vix2 + 1} {quad.vix3 + 1} {quad.vix4 + 1}\n")

            for poly in self.polygons:
                fo.write(f"\n# polygon\n")
                s = "f " + "".join([f"{v + 1} " for v in poly])
                fo.write(s + "\n")

            fo.write("\n")

    def find_vertex(self, x: float, y: float, z: float) -> int:
        for ix, v in enumerate(self.vertices):
            if v.x == x and v.y == y and v.z == z:
                return ix
        return None

    def add_polygon(self, points) -> None:
        poly = []
        print("add_polygon")
        print(points)
        for point in points:
            vix = self.find_vertex(*point)
            if vix is None:
                vix = self.add_vertex(*point)
            poly.append(vix)
        self.polygons.append(poly)

    def add_vertex(self, x: float, y: float, z: float) -> int:
        vertex = Vertex(x, y, z)
        self.vertices.append(vertex)
        return len(self.vertices) - 1

    def add_quad(self, vix1: float, vix2: float, vix3: float, vix4: float, name: str = None, reverse: bool = False) -> int:
        quad = Quad(vix1, vix2, vix3, vix4, name, reverse)
        self.quads.append(quad)
        return len(self.quads) - 1

    def add_box(self, width: float, depth: float, height: float, name: str = None) -> Box:
        b = Box(width, depth, height, name)
        self.boxes.append(b)
        return b

    def add(self, v1, v2, v3, v4, name: str = None, reverse: bool = False) -> int:
        vix1 = self.find_vertex(*v1)
        if vix1 is None:
            vix1 = self.add_vertex(*v1)

        vix2 = self.find_vertex(*v2)
        if vix2 is None:
            vix2 = self.add_vertex(*v2)

        vix3 = self.find_vertex(*v3)
        if vix3 is None:
            vix3 = self.add_vertex(*v3)

        vix4 = self.find_vertex(*v4)
        if vix4 is None:
            vix4 = self.add_vertex(*v4)

        return self.add_quad(vix1, vix2, vix3, vix4, name, reverse)

def build_object() -> Object3D:
    obj = Object3D()

    # base
    width = 45
    depth = 23
    base_height = 1
    height = 1

    b = obj.add_box(width, depth, base_height, "base")

    # island 5
    width = 1
    depth = 7
    x = 0
    y = 0

    b = obj.add_box(width, depth, height, "Island 5")
    b.translate(x, y, base_height)

    # island 6
    width = 23
    depth = 7
    x = 11
    y = 0

    b = obj.add_box(width, depth, height, "Island 6")
    b.translate(x, y, base_height)

    # island 7
    width = 1
    depth = 7
    x = 44
    y = 0

    b = obj.add_box(width, depth, height, "Island 7")
    b.translate(x, y, base_height)

    # island 1
    i = Island("Island 1", elevation = base_height, height = height)
    i.points = [
        IslandPoint((1, 8), 				x, y),
        IslandPoint((1, 8 + 9), 			x, y),
        IslandPoint((1, 8 + 14),			x, y),
        IslandPoint((1 + 4, 8 + 14), 		x, y),
        IslandPoint((1 + 20 + 20 + 3 - 4, 8 + 14), 	x, y),
        IslandPoint((1 + 20 + 20 + 3, 8 + 14),		x, y),
        IslandPoint((1 + 20 + 20 + 3, 8 + 14 - 5),	x, y),
        IslandPoint((1 + 20 + 20 + 3, 8),			x, y),
        IslandPoint((1 + 20 + 20 + 3 - 1, 8),		x, y),
        IslandPoint((1 + 20 + 20 + 3 - 1, 8 + 9),	x, y),
        IslandPoint((1 + 20 + 20 + 3 - 1 - 3, 8 + 9 + 3),	x, y),
        IslandPoint((1 + 20 + 20 + 3 - 1 - 3 - (16 + 16 + 3), 8 + 9 + 3),	x, y),
        IslandPoint((1 + 20 + 20 + 3 - 1 - 3 - (16 + 16 + 3) - 3, 8 + 9),	x, y),
        IslandPoint((1 + 20 + 20 + 3 - 1 - 3 - (16 + 16 + 3) - 3, 8),		x, y),
        IslandPoint((1 + 20 + 20 + 3 - 1 - 3 - (16 + 16 + 3) - 3 - 1, 8),	x, y)
    ]
    i.add_roof([1, 2, 13, 14])
    i.add_roof([13, 12, 4, 3, 2])
    i.add_roof([4, 5, 11, 12])
    i.add_roof([5, 6, 7, 10, 11])
    i.generate(obj)

    # island 2
    i = Island("Island 2", elevation = base_height, height = height)
    i.points = [
        IslandPoint((4,  8),		x, y),
        IslandPoint((4, 14),		x, y),
        IslandPoint((4, 17),		x, y),
        IslandPoint((6, 8 + 6 + 2 + 2),						x, y),
        IslandPoint((4 + 2 + 2, 8 + 6 + 2 + 2),					x, y),
        IslandPoint((4 + 2 + 2 + (2 * 13 + 3), 8 + 6 + 2 + 2),	x, y),
        IslandPoint((4 + 2 + 2 + (2 * 13 + 3) + 2, 8 + 6 + 2 + 2),					x, y),
        IslandPoint((4 + 2 + 2 + (2 * 13 + 3) + 2 + 2, 8 + 6 + 2 + 2 - 2),			x, y),
        IslandPoint((4 + 2 + 2 + (2 * 13 + 3) + 2 + 2, 8 + 6 + 2 + 2 - 2 - 2),		x, y),
        IslandPoint((4 + 2 + 2 + (2 * 13 + 3) + 2 + 2, 8 + 6 + 2 + 2 - 2 - 2 - 6),	x, y),
        IslandPoint((4 + 2 + 2 + (2 * 13 + 3) + 2 + 2 - 1, 8 + 6 + 2 + 2 - 2 - 2 - 6),			x, y),
        IslandPoint((4 + 2 + 2 + (2 * 13 + 3) + 2 + 2 - 1, 8 + 6 + 2 + 2 - 2 - 2 - 6 + 6),			x, y),
        IslandPoint((4 + 2 + 2 + (2 * 13 + 3) + 2 + 2 - 1 - 3, 8 + 6 + 2 + 2 - 2 - 2 - 6 + 6 + 3),	x, y),
        IslandPoint((4 + 2 + 2 + (2 * 13 + 3) + 2 + 2 - 1 - 3 - (13 * 2 + 3), 8 + 6 + 2 + 2 - 2 - 2 - 6 + 6 + 3),				x, y),
        IslandPoint((4 + 2 + 2 + (2 * 13 + 3) + 2 + 2 - 1 - 3 - (13 * 2 + 3) - 3, 8 + 6 + 2 + 2 - 2 - 2 - 6 + 6 + 3 - 3),		x, y),
        IslandPoint((4 + 2 + 2 + (2 * 13 + 3) + 2 + 2 - 1 - 3 - (13 * 2 + 3) - 3, 8 + 6 + 2 + 2 - 2 - 2 - 6 + 6 + 3 - 3 - 6),	x, y),
        IslandPoint((4, 8), x, y),
    ]
    i.add_roof([1, 2, 15, 16])
    i.add_roof([2, 3, 4, 5, 14, 15])
    i.add_roof([5, 6, 13, 14])
    i.add_roof([6, 7, 8, 9, 12, 13])
    i.add_roof([9, 10, 11, 12])
    i.generate(obj)

    # island 3
    i = Island("Island 3", elevation = base_height, height = height)
    i.points = [
        IslandPoint((7, 8), x, y),
        IslandPoint((7, 8 + 3), x, y),
        IslandPoint((7, 8 + 3 + 2), x, y),
        IslandPoint((7 + 2, 8 + 3 + 2 + 2), x, y),
        IslandPoint((7 + 2 + 2, 8 + 3 + 2 + 2), x, y),
        IslandPoint((7 + 2 + 2 + (2 * 10 + 3), 8 + 3 + 2 + 2), x, y),
        IslandPoint((7 + 2 + 2 + (2 * 10 + 3) + 2, 8 + 3 + 2 + 2), x, y),
        IslandPoint((7 + 2 + 2 + (2 * 10 + 3) + 2 + 2, 8 + 3 + 2 + 2 - 2), x, y),
        IslandPoint((7 + 2 + 2 + (2 * 10 + 3) + 2 + 2, 8 + 3 + 2 + 2 - 2 - 5), x, y),
        IslandPoint((7 + 2 + 2 + (2 * 10 + 3) + 2 + 2 - 1, 8 + 3 + 2 + 2 - 2 - 5), x, y),
        IslandPoint((7 + 2 + 2 + (2 * 10 + 3) + 2 + 2 - 1, 8 + 3 + 2 + 2 - 2 - 5 + 3), x, y),
        IslandPoint((7 + 2 + 2 + (2 * 10 + 3) + 2 + 2 - 1 - 3, 8 + 3 + 2 + 2 - 2 - 5 + 3 + 3), x, y),
        IslandPoint((7 + 2 + 2 + (2 * 10 + 3) + 2 + 2 - 1 - 3 - (2 * 10 + 3), 8 + 3 + 2 + 2 - 2 - 5 + 3 + 3), x, y),
        IslandPoint((7 + 2 + 2 + (2 * 10 + 3) + 2 + 2 - 1 - 3 - (2 * 10 + 3) - 3, 8 + 3 + 2 + 2 - 2 - 5 + 3 + 3 - 3), x, y),
        IslandPoint((7 + 2 + 2 + (2 * 10 + 3) + 2 + 2 - 1 - 3 - (2 * 10 + 3) - 3, 8 + 3 + 2 + 2 - 2 - 5 + 3 + 3 - 3 - 3), x, y),
        IslandPoint((7, 8), x, y),
    ]
    i.add_roof([1, 2, 15, 16])
    i.add_roof([2, 3, 4, 5, 14, 15])
    i.add_roof([5, 6, 13, 14])
    i.add_roof([6, 7, 8, 9, 12, 13])
    i.add_roof([9, 10, 11, 12])
    i.generate(obj)

    # island 4
    i = Island("Island 4", elevation = base_height, height = height)
    i.points = [
        IslandPoint((10, 8), x, y),
        IslandPoint((10, 8 + 2), x, y),
        IslandPoint((10 + 2, 8 + 2 + 2), x, y),
        IslandPoint((10 + 2 + (3 + 2 * 9), 8 + 2 + 2), x, y),
        IslandPoint((10 + 2 + (3 + 2 * 9) + 2, 8 + 2 + 2 - 2), x, y),
        IslandPoint((10 + 2 + (3 + 2 * 9) + 2, 8 + 2 + 2 - 2 - 2), x, y),
        IslandPoint((10, 8), x, y),
    ]
    i.add_roof([1, 2, 3, 4, 5, 6])
    i.generate(obj)

    return obj

def main():
    obj = build_object()
    obj.save("ledhelper.obj")

if __name__ == "__main__":
    main()
