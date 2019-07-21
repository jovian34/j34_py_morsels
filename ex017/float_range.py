from math import ceil


class FloatRange:

    def __init__(self, start, stop='tester', step=1.0):
        self.start = float(start)
        try:
            self.stop = float(stop)
        except ValueError:
            self.stop = stop
        self.step = float(step)

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

    def __len__(self):
        if self.stop == 'tester':
            return int(self.start)
        difference = (self.stop - self.start)
        if self.step > 0 > difference:
            return 0
        if self.step < 0 < difference:
            return 0
        return ceil(difference / self.step)

    def __reversed__(self):
        if self.stop == 'tester':
            current_value = self.start - self.step
        else:
            current_value = self.start + (self.step * (len(self) - 1))

        for i in range(len(self)):
            yield current_value
            current_value += self.step * -1


float_range = FloatRange
