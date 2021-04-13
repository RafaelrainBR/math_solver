from website.model.operation import *


class OperationTypes:

    def __init__(self):
        self.__types = [
            MediumOperator(),
            VariantOperator(),
            DefaultDeviationOperator(),
            MediumDeviationOperator(),
        ]

    def get_types(self):
        return self.__types
    
    pass
