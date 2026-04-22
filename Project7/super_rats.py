# Giant Rat Breeding
import time
import random
import statistics

# Constants (weights in grams)
goal = 50000
num_rats = 20
initial_min_weight = 200
initial_max_weight = 600
initial_mode_weight = 300
mutate_odds = 0.01
mutate_min = 0.5
mutate_max = 1.2
litter_size = 8
litters_per_year = 10
generation_limit = 50

# Making sure there are even number of rats for breeding purposes
if num_rats % 2 != 0:
    num_rats += 1

def populate(num_rats, min_wt, max_wt, mode_wt):
    """Initialize a population with a triangular distribution of weights."""
    return [int(random.triangular(min_wt, max_wt, mode_wt))\
            for i in range(num_rats)]

def fitness(population, goal):
    """Measure population fitness based on an attribute mean vs target."""
    ave = statistics.mean(population)
    return ave / goal

def select(population, to_retain):
    """Cull a population to only retain a specified number of members."""
    sorted_population = sorted(population)
    to_retain_by_sex = to_retain//2
    members_per_sex = len(sorted_population)//2
    females = sorted_population[:members_per_sex]
    males = sorted_population[members_per_sex:]
    selected_females = females[-to_retain_by_sex:]
    selected_males = males[-to_retain_by_sex:]
    return selected_males, selected_females

def breed(males, females, litter_size):
    """Crossover genes among members (weights) of a population."""
    random.shuffle(males)
    random.shuffle(females)
    children = []
    for male, female in zip(males, females):
        for child in range(litter_size):
            child = random.randint(female, male)
            children.append(child)
    return children

def mutate(children, mutate_odds, mutate_min, mutate_max):
    """Randomly alter rat weights using input odds and fractional changes."""
    for index, rat in enumerate(children):
        if mutate_odds >= random.random():
            children[index] = round(rat * random.uniform(mutate_min, mutate_max))
    return children