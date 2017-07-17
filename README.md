# Charged-Subatomic-Particle-Interaction-Simulator
Simulates the movements of Charged Subatomic Particles and shows a representation of the Electric field created.

![alt tag](http://oi67.tinypic.com/ih4n82.jpg)

## Docker
This project can be run in a docker container.
 
To build the image: `docker build -t particle_simulator .`

To run: ``docker run --rm -v `pwd`:/data particle_simulator /data/simulator.py``

