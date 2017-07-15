import plot
import particle
import electricField
import sampleParticles
import matplotlib.pyplot as plt

# Create 'size' of plot
sz = 10
plt.axis((-sz, sz, -sz, sz))
plt.ion()

particles = sampleParticles.particle_set[5]

ef = electricField.Electric_Field(particles)
plot.draw(plt, ef)

plt.draw()
plt.show(block=True)

