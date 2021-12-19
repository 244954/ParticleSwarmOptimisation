import matplotlib.pyplot as plt
import matplotlib.animation as animation
from Swarm import Swarm


class Plotter:
    def __init__(self, swarm: Swarm, max_iterations: int):
        self.fig = plt.figure()
        self.ax = self.fig.add_subplot(1, 1, 1)
        self.xs = []
        self.ys = []
        self.swarm = swarm
        self.max_iterations = max_iterations
        self.texts = []
        self.ani = animation.FuncAnimation(self.fig, self.animate, interval=10)
        plt.show()

    def animate(self, i):
        self.swarm.algorithm_loop()

        # Add x and y to lists
        self.xs.append(i)
        self.ys.append(self.swarm.best_global_val)

        # Draw x and y lists
        self.ax.clear()
        self.ax.plot(self.xs, self.ys)

        # Format plot
        plt.xticks(rotation=45, ha='right')
        plt.subplots_adjust(bottom=0.30)
        plt.title('Najwyższa wartość funkcji ({:.2f}) przystosowania do iteracji {}'.format(self.swarm.best_global_val, i))
        plt.ylabel('Funkcja przystosowania [7-700]')

        xx = 0.0
        yy = 0.2

        for j in self.texts:
            self.fig.texts.remove(j)
        self.texts.clear()

        for j in range(len(self.swarm.best_global)):
            self.texts.append(plt.figtext(xx, yy, "{} - {:.2f} gram".format(self.swarm.food_reader.names[j], (self.swarm.best_global[j] * 100)), ha="left", fontsize=12))
            yy -= 0.05
            if yy < .0:
                yy = 0.2
                xx += 0.365

        if self.swarm.stop_algorithm() or int(i) >= self.max_iterations:
            self.ani.event_source.stop()

