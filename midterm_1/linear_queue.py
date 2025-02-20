# linear_queue.py

class LinearQueue:
    def __init__(self, size: int):
        self.max = size
        self.elements = [None] * size
        self.front = -1
        self.rear = -1

    def __repr__(self) -> str:
        return f'Queue: {self.elements} | F: {self.front} | R: {self.rear}'

    def enqueue(self, val: str) -> None:
        if self.rear == self.max - 1:
            print('Queue overflow...')
            return None 

        if self.front == -1 and self.rear == -1:
            self.front = 0
            self.rear = 0
        else: 
            self.rear += 1

        self.elements[self.rear] = val

    def dequeue(self) -> str:
        if self.front == -1 or self.front > self.rear:
            print('Queue underflow...')
            return None
        
        val = self.elements[self.front]
        self.elements[self.front] = None
        self.front += 1

        return val

    def search(self, key: str) -> bool:  # Cambiar el tipo de retorno a bool
        for index in range(self.front, self.rear + 1):
            if self.elements[index] == key:
                return True  # Retorna True si se encuentra el elemento
        return False  # Retorna False si no se encuentra el elemento