from math import ceil


class FloatRange:

    def __init__(self, start, stop='tester', step=1.0):
        if stop == 'tester':
            self.start = 0.0
            self.stop = start
        else:
            self.start = float(start)
            self.stop = float(stop)
        self.step = float(step)

    def __eq__(self, other):
        if other.__class__ is not self.__class__:
            return NotImplemented
        if self.__len__() == 0:
            return (self.__len__(), self.step) == (other.__len__(), other.step)
        else:
            return (self.start, self.__len__(), self.step) == (other.start, other.__len__(), other.step)

    def __iter__(self):
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
        difference = (self.stop - self.start)
        if self.step > 0 > difference:
            return 0
        if self.step < 0 < difference:
            return 0
        return ceil(difference / self.step)

    def __reversed__(self):
        current_value = self.start + (self.step * (len(self) - 1))

        for i in range(len(self)):
            yield current_value
            current_value += self.step * -1


float_range = FloatRange
