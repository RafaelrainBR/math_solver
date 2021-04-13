from django.shortcuts import render

from website.model.operation_types import OperationTypes

operation_types = OperationTypes()


def index(request):
    global filtered
    args = {
        "types": operation_types.get_types(),
    }
    if request.GET.get('number-list'):
        numbers_raw = request.GET.get('number-list')
        args["numbers_raw"] = numbers_raw
        try:
            input_split = numbers_raw.strip().split(",")
            numbers = list(map(float, input_split))

            for _type in operation_types.get_types():
                if _type.get_location() in request.GET:
                    filtered = _type

            output = filtered.do_operations(numbers)
            args["output"] = output
            args["errors"] = False
        except ValueError:
            args["errors"] = True

    return render(request, "website/index.html", args)
