def validate_pin(pin):

    check = pin.isnumeric()

    if check and len(pin) == 4:
        return True
    if check and len(pin) == 6:
        return True
    else:
        return False   
    

print(validate_pin("-12345"))