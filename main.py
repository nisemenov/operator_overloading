class Snow:
    def __init__(self, v):
        self.qty = int(v)

    def __add__(self, other):
        # self.qty += other
        return Snow(self.qty + other)

    def __sub__(self, other):
        return Snow(self.qty - other)

    def __mul__(self, other):
        return Snow(self.qty * other)

    def __truediv__(self, other):
        return Snow(round(self.qty / other))

    def make_snow(self, n):
        list_snow = ['*' * n for i in range(int(self.qty / n))]
        list_snow.append('*' * (self.qty % n))
        return repr('\n'.join(list_snow))

    def __call__(self, new_value):
        self.qty = new_value

    def __repr__(self):
        return f'{self.qty = }'
