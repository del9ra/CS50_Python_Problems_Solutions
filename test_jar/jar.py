class Jar:
    def __init__(self, capacity=12):
        self.capacity = capacity
        self.n = 0

    def __str__(self):
        return f"{self.n*'🍪'}"

    def deposit(self, n):
        self.n = self.n + n
        if self.n > self.capacity:
            raise ValueError("Too many cookies")

    def withdraw(self, n):
        if n > self.n:
            raise ValueError("No cookies")
        self.n = self.n - n

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, capacity): #проверяю capacity, который передается как параметр, но не self
        if capacity < 0:
            raise ValueError("Capacity cannot be negative")
        self._capacity = capacity


    @property
    def size(self):
        return self.n