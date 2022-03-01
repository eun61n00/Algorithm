class MinHeap:
    def __init__(self, value):
        self.heap_array = list()
        self.heap_array.append(None)
        self.heap_array.append(value)

    def move_up(self, inserted_idx):
        if inserted_idx == 1:
            return False
        parent_idx = inserted_idx // 2
        if self.heap_array[inserted_idx] < self.heap_array[parent_idx]:
            return True

    def insert(self, value):
        if len(self.heap_array) <= 1:
            self.heap_array.append(None)
            self.heap_array.append(value)
            return True

        self.heap_array.append(value)
        inserted_idx = len(self.heap_array) - 1

        while self.move_up(inserted_idx):
            parent_idx = inserted_idx // 2
            self.heap_array[inserted_idx], self.heap_array[parent_idx] = \
                self.heap_array[parent_idx], self.heap_array[inserted_idx]
            inserted_idx = parent_idx

        return True

    def move_down(self, check_idx):
        left_child_idx = check_idx * 2
        right_child_idx = check_idx * 2 + 1

        if len(self.heap_array) <= left_child_idx:  # no left child, no right child
            return False
        elif len(self.heap_array) <= right_child_idx:  # there's only left child node
            if self.heap_array[check_idx] > self.heap_array[left_child_idx]:
                return 1
        else:  # there are both left child node and right child node
            if self.heap_array[check_idx] > min(self.heap_array[left_child_idx], self.heap_array[right_child_idx]):
                return 2

    def pop(self):
        if len(self.heap_array) <= 1:
            return None
        return_value = self.heap_array[1]
        self.heap_array[1] = self.heap_array[-1]
        self.heap_array.pop()

        check_idx = 1
        while self.move_down(check_idx):
            left_child_idx = check_idx * 2
            right_child_idx = check_idx * 2 + 1
            if self.move_down(check_idx) == 1:
                self.heap_array[check_idx], self.heap_array[left_child_idx] = \
                    self.heap_array[left_child_idx], self.heap_array[check_idx]
            else:
                if self.heap_array[left_child_idx] < self.heap_array[right_child_idx]:
                    self.heap_array[check_idx], self.heap_array[left_child_idx] = \
                        self.heap_array[left_child_idx], self.heap_array[check_idx]
                else:
                    self.heap_array[check_idx], self.heap_array[right_child_idx] = \
                        self.heap_array[right_child_idx], self.heap_array[check_idx]

        return return_value

