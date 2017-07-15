from particle import *

# Sample sets of particles 

particle_set = [ 
	[Particle(0,0, 1)],
	[Particle(-1,0, 1), Particle(1,0,-1)],
	[Particle(-2,0, 1), Particle(2,0,1)],
	[Particle(-2,0, 1), Particle(2,0,1), Particle(0, 2, 1)],
	[Particle(-2,0, 1), Particle(2,0,1), Particle(0, 2, -1)],
	[Particle(-2,0, 1), Particle(2,0,-1), Particle(0, 2, 1)],
	[Particle(-2,0, 1), Particle(2,0,1), Particle(0, 2, 1), Particle(0,-2,1)],
	[Particle(-2,0, 1), Particle(2,0,1), Particle(0, 2, -1), Particle(0,-2,-1)],
	[Particle(-2,0, -1), Particle(2,0,1), Particle(0, 2, 1), Particle(0,-2,-1)],
	[Particle(-2,4, -1), Particle(-3,-1,1.5), Particle(0,2,-1)],
	[Particle(-4,-2, 1), Particle(-3,1,1), Particle(0, 0, -1), 
			Particle(1,2,1), Particle(2,-1,-3)],
	[Particle(-3,0,1), Particle(-2,0,1),Particle(-1,0,1),Particle(0,0,1), 
			Particle(1,0,1), Particle(2,0,1), Particle(3,0,1)],
	[Particle(-2,-4,1), Particle(-1,-4,1), Particle(0,-4,1), Particle(1,-4,1), Particle(2,-4,1),
               Particle(-3,-3,-1), Particle(-4,-2,-1), Particle(-5,-1,-1), 
                Particle(3,-3,-1), Particle(4,-2,-1), Particle(5,-1,-1)]
]
