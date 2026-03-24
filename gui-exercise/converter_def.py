def convert(feet, inches):
    feet_to_meters = feet * 0.3048
    inches_to_meters = inches * 0.0254

    meters = feet_to_meters + inches_to_meters

    return meters