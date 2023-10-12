class Jar:
    def __init__(self, capacity=12):
        self.capacity = capacity 
        self._size = 0

    def __str__(self):
        if self._size > 0:
            return "🍪" * self._size 
        else:
            return ""

    def deposit(self, n):
        if n < 0:
            raise ValueError("Cannot deposit negative amount")
        elif n > 0:
            new_size = n + self.size

            if new_size > self.capacity:
                raise ValueError("Jar is too full")
            else:
                self._size += n 

    def withdraw(self, n):
        if n < 0:
            raise ValueError("Cannot withdraw negative amount")
        elif n > self._size:
            raise ValueError("Not enough cookies in the jar")
        else:
            self._size -= n 

    @property
    def capacity(self):
        return self._capacity 

    @capacity.setter
    def capacity(self, n):
        if n < 0:
            raise ValueError("Capacity cannot be negative")
        self._capacity = n

    @property
    def size(self):
        return self._size

