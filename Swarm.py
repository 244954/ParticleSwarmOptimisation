import numpy as np
import random
import copy
from FoodReader import FoodReader
from additional_functions import *


class Swarm:
    def __init__(self, beta: float, eta: float, alpha: float, file_name: str):
        self.eta = eta
        self.alpha = alpha
        self.beta = beta
        self.food_reader = FoodReader(file_name)

        self.food_reader.read_file()
        self._init_swarm()
        self._init_best_pos()
        self._init_global_best()
        self._init_velocities()

    def _init_swarm(self):
        self.population_size = self.food_reader.foods_number
        self.swarm = [np.array([.5] * self.population_size, dtype=float) for _ in range(self.population_size)]
        for i in range(self.population_size):
            self.swarm[i][i] += 2.5

        s2 = [np.array([0.0] * self.population_size, dtype=float) for _ in range(self.population_size)]
        for i in range(self.population_size):
            s2[i][i] += 7.0

        s3 = [np.array([0.0] * self.population_size, dtype=float) for _ in range(self.population_size)]
        for i in range(self.population_size - 1):
            s3[i][i] += 3.0
            s3[i][i + 1] += 3.0
        s3[0][self.population_size - 1] += 3.0
        s3[self.population_size - 1][self.population_size - 1] += 3.0
        self.swarm = self.swarm + s2 + s3

        self.population_size *= 3

    def _init_best_pos(self):
        assert self.food_reader
        assert self.food_reader.foods

        self.best_pos = copy.deepcopy(self.swarm)
        self.best_pos_vals = list(map(lambda xx: fitness_function(self.food_reader.foods, xx), self.best_pos))

    def _init_global_best(self):
        assert self.best_pos
        assert self.best_pos_vals

        index_max = max(range(len(self.best_pos_vals)), key=self.best_pos_vals.__getitem__)
        self.best_global = self.best_pos[index_max]
        self.best_global_val = self.best_pos_vals[index_max]

    def _init_velocities(self):
        self.velocities = copy.deepcopy(self.swarm)
        for i in range(len(self.velocities)):
            for j in range(len(self.velocities[i])):
                self.velocities[i][j] *= -.5

    def calculate_velocities(self):
        for i in range(self.population_size):
            if nonzero(self.velocities[i]):
                for j in range(len(self.velocities[i])):
                    current_beta = random.uniform(0.0, self.beta)
                    current_eta = random.uniform(0.0, self.eta)
                    self.velocities[i][j] = self.alpha * self.velocities[i][j] + \
                                            current_beta * (self.best_pos[i][j] - self.swarm[i][j]) + \
                                            current_eta * (self.best_global[j] - self.swarm[i][j])

    def update_swarm_position(self):
        for i in range(self.population_size):
            for j in range(len(self.velocities[i])):
                self.swarm[i][j] += self.velocities[i][j]
                if self.swarm[i][j] > 7.:
                    self.swarm[i][j] = 7.
                if self.swarm[i][j] < 0.:
                    self.swarm[i][j] = 0.

    def update_best_pos_and_global(self):
        for i in range(self.population_size):
            new_val = fitness_function(self.food_reader.foods, self.swarm[i])
            if new_val > self.best_pos_vals[i]:
                for j in range(len(self.swarm[i])):
                    self.best_pos[i][j] = self.swarm[i][j]
                self.best_pos_vals[i] = new_val

                if new_val > self.best_global_val:
                    for j in range(len(self.swarm[i])):
                        self.best_global[j] = self.swarm[i][j]
                    self.best_global_val = new_val

    def stop_algorithm(self) -> bool:
        for i in self.velocities:
            if nonzero(i):
                return False
        return True

    def algorithm_loop(self):
        self.calculate_velocities()
        self.update_swarm_position()
        self.update_best_pos_and_global()
        # self.print_best()

    def print_best(self):
        print_best(self.best_global, self.food_reader.names, self.best_global_val)
        """
        print("Best- {}".format(self.best_global))
        print("----Populations----")
        print_score(self.swarm, self.food_reader.names, self.best_pos_vals)
        """
