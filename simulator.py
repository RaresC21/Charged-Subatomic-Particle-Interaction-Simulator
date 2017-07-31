import time
import particle
import plotUtils
import electricField
import sampleParticles
import matplotlib as mat
mat.use("PDF")
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

from animation import *

# Create 'size' of plot
sz = 10
plt.axis((-sz, sz, -sz, sz))
plt.ion()

particles = sampleParticles.particle_set[5]

ef = Electric_Field(particles)
plotUtils.draw(plt, ef)

plt.draw()

images = PdfPages("fields.pdf")
images.savefig()
images.close()

animate(plt, particles, ef)