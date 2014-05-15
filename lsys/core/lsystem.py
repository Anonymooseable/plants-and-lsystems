"""

"""

class GenerationContext:
    def __init__(self, previous_state=[], cur_depth=0):
        self.cur_depth = cur_depth
        self.previous_state = []
        self.your_position = 0

class System:
    def __init__(self, rules, axiom):
        self.rules = rules
        self.axiom = axiom

    def _do_generation(self, symbols, cur_depth=0):
        context = GenerationContext(symbols, cur_depth)
        symbols_new = []
        for context.your_position, action in enumerate(symbols):
            try:
                symbols_new.extend(self.rules[action](context))
            except KeyError:
                symbols_new.append(action)
            #context.your_position += 1
        return symbols_new

    def rolling_evaluation(self):
        cur_depth = 0
        generation = self.axiom
        while True:
            generation = self._do_generation(generation, cur_depth)
            yield generation
            cur_depth += 1

    def construct(self, depth):
        evaluator = self.rolling_evaluation()
        for x in range(depth-1):
            next(evaluator)
        return next(evaluator)

