
class FloatRange:

    def __init__(self, start, stop='tester', step=1.0):
        self.start = start
        self.stop = stop
        self.step = step

    def __iter__(self):
        if self.stop == 'tester':
            current_value, local_stop = 0, self.start
        else:
            current_value, local_stop = self.start, self.stop

        if self.step < 0:
            while current_value > local_stop:
                yield current_value
                current_value += self.step
        else:
            while current_value < local_stop:
                yield current_value
                current_value += self.step


float_range = FloatRange
