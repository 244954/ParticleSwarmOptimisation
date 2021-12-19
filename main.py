from Swarm import Swarm
from Plotter import Plotter
import sys

beta = 1.  # współczynik swojego najlepszego wyniku
eta = 1.  # współczynik globalnego najlepszego wyniku
alfa = .92  # współczyni hamowania
max_iterations = 500

if __name__ == '__main__':  # argv (beta, eta, alpha, file_name, max_iterations

    if len(sys.argv) >= 6:
        max_iterations = int(sys.argv[5])
        swarm = Swarm(float(sys.argv[1]), float(sys.argv[2]), float(sys.argv[3]), sys.argv[4])
        plot = Plotter(swarm, max_iterations)
    else:
        swarm = Swarm(beta, eta, alfa, 'diet_perfect.txt')
        plot = Plotter(swarm, max_iterations)
