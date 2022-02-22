class LargeValueCache:

    def __init__(self, N: int):
        self.cap = N
        self.size = 0
        self.data = {}

    def get_capacity(self):
        return self.cap

    def lookup(self, key):
        try:
            return self.data[key]
        except:
            return None

    def update_capacity(self, N: int):
        if N < self.cap:
            for i in range(self.cap - N):
                min_key_value = (None, None)
                for key in self.data:
                    if min_key_value == (None, None):
                        min_key_value = (key, self.data[key])
                    else:
                        if self.data[key] < min_key_value[1]:
                            min_key_value = (key, self.data[key])
                print(f'Remove key: {min_key_value[0]}, value: {min_key_value[1]}')
                self.size -= 1
                del self.data[min_key_value[0]]
            self.cap = N
        else:
            self.cap = N
        print(self.data)

    def insert(self, key, value):
            try:
                # check are there any key name "key" in dict ?
                current_value = self.data[key]
                # replace current value
                self.data[key] = value
            except:
                if self.size < self.get_capacity():
                    self.data[key] = value
                    self.size += 1
                else:
                    min_key_value = (None, None)
                    for k in self.data:
                        if min_key_value == (None, None):
                            min_key_value = (k, self.data[k])
                        else:
                            if self.data[k] < min_key_value[1]:
                                min_key_value = (k, self.data[k])
                    print(f'remove key: {min_key_value[0]}, value: {min_key_value[1]}')
                    del self.data[min_key_value[0]]

                    self.data[key] = value
            print(self.data)
