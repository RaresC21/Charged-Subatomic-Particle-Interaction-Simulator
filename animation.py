import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import sampleParticles

from physics import *
from electricField import *

def go(i, graph, particles):
    points = []
    colors = []
    for cur in particles:
       points.append((cur.xs[i], cur.ys[i]))
       colors.append(cur.color)

    graph.set_offsets(tuple(points))
    graph.set_facecolors(tuple(colors))
    return graph

def animate(plt, particles, ef) :
    step_size = 10
    iterations = 1000
    simulate(particles, ef, 0.05, iterations, step_size)

    fig = plt.figure()
    graph = plt.scatter([], [])
    plt.xlim(-10, 10)
    plt.ylim(-10, 10)

    ani = FuncAnimation(fig, go, frames = iterations // step_size, 
        repeat=False, interval=120,
        fargs = [graph, particles])
    ani.save("mine.mp4")