needs = [2500.0, 50.0, 70.0, 310.0, 90.0, 2.3, 30.0]


def fitness_function(foods, swarmling: list) -> float:
    nutrition = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
    score = 0.0

    for i in range(len(swarmling)):
        for j in range(len(nutrition)):
            nutrition[j] += foods[i][j] * swarmling[i]

    for i in range(len(nutrition)):
        percentage = (nutrition[i] / needs[i]) * 100.0
        if percentage > 100.0:
            score += max(1.0, 200.0 - percentage)
        else:
            score += max(1.0, percentage)
    return score


def nonzero(velocity: list):
    eps = 0.00005
    for i in velocity:
        if abs(i) > eps:
            return True
    return False


def print_score(pops, food_name, scores):
    for i in range(len(pops)):
        print("--{}--".format(scores[i]))
        for j in range(len(pops[i])):
            print("{} - {} gram".format(food_name[j], (pops[i][j] * 100)))


def print_best(best_pop, food_name, best_score):
    print("--{}--".format(best_score))
    for j in range(len(best_pop)):
        print("{} - {} gram".format(food_name[j], (best_pop[j] * 100)))
