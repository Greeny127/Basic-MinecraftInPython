from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from ursina.shaders import lit_with_shadows_shader
import random

app = Ursina()
voxels = []

class Voxel(Button):
	def __init__(self, position=(0,0,0)):
		super().__init__(
			parent = scene,
			position = position,
			model = 'cube',
			origin_y = .5,
			texture = 'white_cube',
			shader=lit_with_shadows_shader,
			color = color.color(0, 0, random.uniform(.9, 1.0)),
			highlight_color = color.lime,
		)


	def input(self, key):

		if self.hovered:
			if key == "q":
				self.disable = True

			if key == "e":
				self.disable = False

			if key == 'left mouse down':
				voxel = Voxel(position=self.position + mouse.normal)
				voxels.append(voxel)

			if key == 'right mouse down':
				destroy(self)
				voxels.remove(self)

for z in range(40):
	for x in range(40):

		voxel = Voxel(position=(x,0,z))
		voxels.append(voxel)

player = FirstPersonController()

pivot = Entity()
pivot.rotation = (45, 90)
entity = DirectionalLight(parent=pivot, shadows=True)
# entity._light.show_frustum()

def update():

	# pivot.rotation_x += 10 * time.dt
	if player.position[1] < -20:
		player.position = (random.randint(0, 20), 0, random.randint(0, 20))

	for i in voxels:
		if distance(player, i) >= 10:
			i.visible = False

		else:
			i.visible = True

# window.show_ursina_splash = True
app.run()