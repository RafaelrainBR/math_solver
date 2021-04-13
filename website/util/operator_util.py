import math


class Operators:

    def __init__(self, number_list):
        self._number_list = number_list
        self._output = []

    def get_number_list(self):
        return self._number_list

    def get_output(self):
        return self._output

    def get_medium(self):
        sum_of_all = sum_all(self.get_number_list())
        list_size = len(self.get_number_list())
        medium = sum_of_all / list_size

        self._output.append(
            "M = {} = {}/{} = {}".format(
                "+".join(str(round(i)) for i in self.get_number_list()),
                sum_of_all,
                list_size,
                medium
            )
        )

        return medium

    def get_variant(self):
        medium = self.get_medium()
        numbers = self.get_number_list()
        list_size = len(numbers)

        line = ["({}-{})²".format(round(number, 2), round(medium, 2)) for number in numbers]
        self._output.append("V = " + "+".join(line))

        results = [(i-medium) for i in numbers]
        self._output.append("V = " + "+".join(["({})²".format(round(i, 2)) for i in results]))

        elevated = [pow(i, 2) for i in results]
        self._output.append("V = " + " + ".join([str(round(i)) for i in elevated]))

        sum_of_elevated = round(sum(elevated), 2)
        self._output.append("V = {}/{}".format(sum_of_elevated, list_size))

        final = sum_of_elevated/list_size
        final = round(final, 3)
        self._output.append("V = " + str(final))
        return final

    def get_default_deviation(self):
        variant = self.get_variant()

        square_root = math.sqrt(variant)
        self._output.append("DP = " + str(round(square_root, 3)))

        return square_root

    def get_medium_deviation(self):
        medium = self.get_medium()
        numbers = self.get_number_list()
        list_size = len(numbers)

        line = ["({}-{})".format(round(number), round(medium)) for number in numbers]
        self._output.append("DM = " + "+".join(line))

        results = [(i - medium) for i in numbers]
        self._output.append("DM = " + "+".join(["|{}|".format(round(i)) for i in results]))

        modules = [abs(i) for i in results]
        self._output.append("DM = " + "+".join([str(i) for i in modules]))

        sum_of_results = round(sum(modules), 2)
        self._output.append("DM = {}/{}".format(sum_of_results, list_size))

        final = sum_of_results / list_size
        final = round(final, 3)
        self._output.append("DM = " + str(final))
        return final

    def clear_output(self):
        self._output = []


pass


def sum_all(number_list):
    return sum(number_list)
