def car_info(manufacturer, model, **kwargs):
    """Make a dictionary representing information about a car."""
    specifications_dict = {
        "Manufacturer": manufacturer.title(),
        "Model": model.title(),
    }

    for key, value in kwargs.items():
        specifications_dict[key] = value.title()

    return specifications_dict
