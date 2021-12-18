
class RecursiveFlatten:

    def __init__(self, *inputs):
        self.outputs = []
        self.recursive_flatten(inputs)

    def recursive_flatten(self, values):
        if hasattr(values, '__iter__'):
            for sub_values in values:
                self.recursive_flatten(sub_values)
        else:
            self.outputs.append(values)


def deep_flatten(*iter_input):
    flatten = RecursiveFlatten(iter_input)
    return (value for value in flatten.outputs)

