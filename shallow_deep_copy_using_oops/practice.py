import copy


class PrintClass:

    def print_id(self, var):
        print(f"Id: {id(var)}\n")

    def print_copy_id(self, var):
        print(f"Id of copy: {id(var)}\n")

    def print_diff(self, var1, var2):
        print(var1)
        self.print_id(var1)

        print(var2)
        self.print_copy_id(var2)

    def print_before_modification(self):
        print("Before modification:\n")

    def print_after_modification(self):
        print("After modification:\n")

    def print_assignment_operator(self):
        print("Assignment operator copy:\n")

    def print_shallow_copy(self):
        print("Shallow copy:\n")

    def print_deep_copy(self):
        print("Deep copy:\n")


class PlainVariableClass(PrintClass):

    def assignment_operator(self):
        self.print_assignment_operator()
        hello = 1
        hell = hello

        self.print_before_modification()
        self.print_diff(hello, hell)

        self.print_after_modification()
        hell = 4
        self.print_diff(hello, hell)

        """
        Output:

        Before modification:

        1
        Id 1: 11753896

        1
        Id 1: 11753896

        After modification:

        1
        Id 1: 11753896

        4
        Id 4: 11753992"""

    def shallow_copy(self):
        self.print_shallow_copy()
        first = 2

        fir = copy.copy(first)

        self.print_before_modification()
        self.print_diff(first, fir)

        fir = 5
        self.print_after_modification()
        self.print_diff(first, fir)

        """
        Output:

        Before modification:

        2
        Id 2: 11753928

        2
        Id 2: 11753928

        After modification:

        2
        Id 2: 11753928

        5
        Id 5: 11754024"""

    def deep_copy(self):
        self.print_deep_copy()
        second = 3

        sec = copy.deepcopy(second)

        self.print_before_modification()
        self.print_diff(second, sec)

        sec = 6

        self.print_after_modification()
        self.print_diff(second, sec)

        """
        Output:

        Before modification:

        3
        Id 3: 11753960

        3
        Id 3: 11753960

        After modification:

        3
        Id 3: 11753960

        6
        Id 6: 11754056"""


class CollectionClass(PrintClass):

    def assignmet_operator(self):
        self.print_assignment_operator()
        marks = [12, 13, 14]
        marks_copy = marks

        self.print_before_modification()
        self.print_diff(marks, marks_copy)

        marks_copy[0] = 15

        self.print_after_modification()
        self.print_diff(marks, marks_copy)

        """
        Output:

        Before modification:

        [12, 13, 14]
        Id [12, 13, 14]: 124378630296064

        [12, 13, 14]
        Id [12, 13, 14]: 124378630296064

        After modification:

        [15, 13, 14]
        Id [15, 13, 14]: 124378630296064

        [15, 13, 14]
        Id [15, 13, 14]: 124378630296064"""

    def shallow_copy(self):
        self.print_shallow_copy()
        age = [30, 40, 50]
        age_copy = copy.copy(age)

        self.print_before_modification()
        self.print_diff(age, age_copy)

        age_copy[1] = 65

        self.print_after_modification()
        self.print_diff(age, age_copy)

        """
        Output:

        Before modification:

        [30, 40, 50]
        Id [30, 40, 50]: 124378630296064

        [30, 40, 50]
        Id [30, 40, 50]: 124378619869632

        After modification:

        [30, 40, 50]
        Id [30, 40, 50]: 124378630296064

        [30, 65, 50]
        Id [30, 65, 50]: 124378619869632"""

    def deep_copy(self):
        self.print_deep_copy()
        salary = [100, 200, 300]
        salary_copy = copy.deepcopy(salary)

        self.print_before_modification()
        self.print_diff(salary, salary_copy)

        salary_copy[2] = 500

        self.print_after_modification()
        self.print_diff(salary, salary_copy)

        """
        Output:

        Before modification:

        [100, 200, 300]
        Id [100, 200, 300]: 124378619869632

        [100, 200, 300]
        Id [100, 200, 300]: 124378630296064

        After modification:

        [100, 200, 300]
        Id [100, 200, 300]: 124378619869632

        [100, 200, 500]
        Id [100, 200, 500]: 124378630296064"""


class NestedCollectionClass(PrintClass):

    def assignmet_operator(self):
        self.print_assignment_operator()
        numbers = [12, 13, [3, 4], 14]
        numbers_copy = numbers

        self.print_before_modification()
        self.print_diff(numbers, numbers_copy)

        numbers_copy[2][1] = 15

        self.print_after_modification()
        self.print_diff(numbers, numbers_copy)

        """
        Output:

        Before modification:

        [12, 13, [3, 4], 14]
        Id: 125155756242624

        [12, 13, [3, 4], 14]
        Id of copy: 125155756242624

        After modification:

        [12, 13, [3, 15], 14]
        Id: 125155756242624

        [12, 13, [3, 15], 14]
        Id of copy: 125155756242624"""

    def shallow_copy(self):
        self.print_shallow_copy()
        values = [30, 40, [31, 41], 50]
        values_copy = copy.copy(values)

        self.print_before_modification()
        self.print_diff(values, values_copy)

        values_copy[2][0] = 6

        self.print_after_modification()
        self.print_diff(values, values_copy)

        """
        Output:

        Before modification:

        [30, 40, [31, 41], 50]
        Id: 125155757707776

        [30, 40, [31, 41], 50]
        Id of copy: 125155756242752

        After modification:

        [30, 40, [6, 41], 50]
        Id: 125155757707776

        [30, 40, [6, 41], 50]
        Id of copy: 125155756242752"""

    def deep_copy(self):
        self.print_deep_copy()
        pens = [100, 200, [900, 300], 300]
        pens_copy = copy.deepcopy(pens)

        self.print_before_modification()
        self.print_diff(pens, pens_copy)

        pens_copy[2] = 500

        self.print_after_modification()
        self.print_diff(pens, pens_copy)

        """
        Output:

        Before modification:

        [100, 200, [900, 300], 300]
        Id: 125155756242624

        [100, 200, [900, 300], 300]
        Id of copy: 125155757707776

        After modification:

        [100, 200, [900, 300], 300]
        Id: 125155756242624

        [100, 200, 500, 300]
        Id of copy: 125155757707776"""


if __name__ == "__main__":
    print("Plain Variable\n")
    plain_variable = PlainVariableClass()
    plain_variable.assignment_operator()
    plain_variable.shallow_copy()
    plain_variable.deep_copy()

    print("Collection\n")
    collection = CollectionClass()
    collection.assignmet_operator()
    collection.shallow_copy()
    collection.deep_copy()

    print("Nested Collection\n")
    nested_collection = NestedCollectionClass()
    nested_collection.assignmet_operator()
    nested_collection.shallow_copy()
    nested_collection.deep_copy()
