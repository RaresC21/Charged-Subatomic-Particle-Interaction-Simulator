import plot
import particle
import electricField
import matplotlib.pyplot as plt

# Create 'size' of plot
sz = 10
plt.axis((-sz, sz, -	sz, sz))
plt.ion()

particles = [particle.Particle(1,1,1)]

ef = electricField.Electric_Field(particles)
plot.draw(plt, ef)

plt.draw()
plt.show(block=True)

