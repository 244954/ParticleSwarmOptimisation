class FoodReader:
    def __init__(self, file_name):
        self.foods = []
        self.names = []
        self.file_name = file_name
        self.foods_number = 0

    def read_file(self):
        self.foods.clear()
        self.names.clear()

        with open(self.file_name) as file:
            for line in file:
                info = line.split()
                if len(info) > 1 and info[0] != 'All' and info[0] != 'Name':
                    self.foods_number += 1
                    self.foods.append([float(i) for i in info[1:]])
                    self.names.append(info[0])
