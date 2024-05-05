from customErrors import ShortName, PhoneValidationError

def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ShortName as name:
            print(name)
        except PhoneValidationError as phone:
            print(phone)
        except Exception as error:
            print(f"{func.__name__} error, {type(error)}, {error}")
    return inner
