class Park:

    counter = 0

    def __init__(self, name="", area=0.0, length_of_tracks=0.0, number_of_trees=0, age=0, availability_of_bench=False):
        self.name = name
        self.area = area
        self.length_of_tracks = length_of_tracks
        self.number_of_trees = number_of_trees
        self.age = age
        self.availability_of_bench = availability_of_bench

    def __del__(self):
        pass

    def __str__(self):
        return "\nІм'я = " + self.name + "\nПлоща = " + str(self.area) + "\nДовжина доріжок = " + \
               str(self.length_of_tracks) + "\nКількість дерев = " + \
               str(self.number_of_trees) + "\nВік = " + str(self.age) + "\nНаявність лавочок = " + \
               str(self.availability_of_bench)

    @staticmethod
    def add_to_counter(added_number):
        Park.counter += added_number
