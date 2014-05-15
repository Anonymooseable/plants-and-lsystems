import random
import bisect
import itertools

class StochasticRule:
    def __init__(self, *output_sets):
        self.output_sets = output_sets
        self.sum = sum([s[1] for s in output_sets])

    def __call__(self):
        # Shamelessly stolen from the docs (random module)
        choices, weights = zip(*self.output_sets)
        cumdist = list(itertools.accumulate(weights))
        x = random.random() * cumdist[-1]
        return choices[bisect.bisect(cumdist, x)]
