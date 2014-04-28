import random

class StochasticRule:
    def __init__(self, *output_sets):
        self.output_sets = output_sets
        self.sum = sum([s[1] for s in output_sets])

    def __iter__(self):
        r = random.randrange(self.sum + 1)
        subtotal = 0
        for s, factor in self.output_sets:
            subtotal += factor
            if r <= subtotal:
                return iter(s)
