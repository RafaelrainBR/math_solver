from website.util.operator_util import Operators


class Operation:
    def get_name(self) -> str:
        pass

    def get_location(self) -> str:
        pass

    def do_operations(self, numbers) -> list:
        pass
    pass


class MediumOperator(Operation):
    def get_name(self) -> str:
        return "Média"

    def get_location(self) -> str:
        return "media"

    def do_operations(self, numbers) -> list:
        operator = Operators(numbers)
        result = operator.get_medium()
        return operator.get_output()


class VariantOperator(Operation):
    def get_name(self) -> str:
        return "Variante"

    def get_location(self) -> str:
        return "variante"

    def do_operations(self, numbers) -> list:
        operator = Operators(numbers)
        result = operator.get_variant()
        return operator.get_output()


class DefaultDeviationOperator(Operation):
    def get_name(self) -> str:
        return "Desvio Padrão"

    def get_location(self) -> str:
        return "desvio_padrao"

    def do_operations(self, numbers) -> list:
        operator = Operators(numbers)
        result = operator.get_default_deviation()
        return operator.get_output()


class MediumDeviationOperator(Operation):
    def get_name(self) -> str:
        return "Desvio Médio"

    def get_location(self) -> str:
        return "desvio_medio"

    def do_operations(self, numbers) -> list:
        operator = Operators(numbers)
        result = operator.get_medium_deviation()
        return operator.get_output()
