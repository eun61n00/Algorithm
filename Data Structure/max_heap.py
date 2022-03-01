class MaxHeap:
    def __init__(self, value):
        self.heap_array = list()
        self.heap_array.append(None)
        self.heap_array.append(value)

    def move_up(self, inserted_idx):
        if inserted_idx <= 1:
            return False
        parent_idx = inserted_idx // 2
        if self.heap_array[inserted_idx] > self.heap_array[parent_idx]:
            return True
        else:
            return False

    def insert(self, value):
        if len(self.heap_array) < 1:
            self.heap_array.append(None)
            self.heap_array.append(value)
            return True

        self.heap_array.append(value)
        inserted_idx = len(self.heap_array) - 1
        while self.move_up(inserted_idx):
            parent_idx = inserted_idx // 2
            self.heap_array[parent_idx], self.heap_array[inserted_idx] = \
                self.heap_array[inserted_idx], self.heap_array[parent_idx]
            inserted_idx = parent_idx
        return True

    def move_down(self, idx):
        if len(self.heap_array) > idx * 2:
            if len(self.heap_array) > idx * 2 + 1:
                if self.heap_array[idx] < max(self.heap_array[idx * 2], self.heap_array[idx * 2 + 1]):
                    return True
                else:
                    return False
            else:
                if self.heap_array[idx] < self.heap_array[idx * 2]:
                    return True
                else:
                    return False
        else:
            return False

    def pop(self):
        if len(self.heap_array) <= 1:
            print(0)
            return True
        returned_data = self.heap_array[1]
        self.heap_array[1] = self.heap_array[-1]
        self.heap_array.pop()
        idx = 1
        while self.move_down(idx):
            if len(self.heap_array) > idx * 2 + 1:
                if self.heap_array[idx * 2] >= self.heap_array[idx * 2 + 1]:
                    self.heap_array[idx], self.heap_array[idx * 2] = \
                        self.heap_array[idx * 2], self.heap_array[idx]
                    idx = idx * 2
                else:
                    self.heap_array[idx], self.heap_array[idx * 2 + 1] = \
                        self.heap_array[idx * 2 + 1], self.heap_array[idx]
                    idx = idx * 2 + 1
            else:
                self.heap_array[idx], self.heap_array[idx * 2] = \
                    self.heap_array[idx * 2], self.heap_array[idx]
                idx = idx * 2
        print(returned_data)
        return True
