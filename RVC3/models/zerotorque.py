import bdsim
from math import pi
import numpy as np
from roboticstoolbox.models.DH import Puma560

sim = bdsim.BDSim(animation=True)
bd = sim.blockdiagram()

puma = Puma560().nofriction()

# define the blocks
torque = bd.CONSTANT([0, 0, 0, 0, 0, 0])
robot = bd.FDYN(robot=puma, q0=puma.qz)
plot = bd.ARMPLOT(puma)

# connect the blocks
bd.connect(torque, robot)
bd.connect(robot[0], plot)

bd.compile()   # check the diagram
bd.report()    # list all blocks and wires

if __name__ == "__main__":

    out = sim.run(bd, 5)  # simulate for 5s

    bd.done()
