from pathlib import Path
from machinevisiontoolbox import *
from roboticstoolbox import *
from math import pi

from bdsim import Clock, bdload, BDSim
from spatialmath import SE3
import matplotlib.pyplot as plt


sim = BDSim(animation=True)


bd = sim.blockdiagram()
print(sim.options)
sim.set_options(animation=True)

clock = bd.clock(10, unit='Hz')

robot = models.DH.Puma560()
print(robot)
q0 = [0, pi/4, pi, 0, pi/4, -pi/4]

camera = CentralCamera.Default()

lmbda = 0.5

model = Path(__file__).parent / "IBVS-arm.bd"
print(model)
# print(sim.argv)

def plot_init(camera):
	print('@@@@@plot_init')
	camera.plot_point(bd['p*'].value, 'b*')


bd = bdload(bd, model, globalvars=globals())
bd.compile()
bd.report()

print(bd['P'].value)

print('about to run')
print(sim.options)
sim.set_options(animation=False)
out = sim.run(bd, 10)
print('done')
print(out)

# sim.done(bd)
# plt.pause(5)
