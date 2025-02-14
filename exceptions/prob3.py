from custom_error import CustomError


def ask():
    try:
        input_data = int(input('Input an integer'))
        print(input_data ** 2)
    except ValueError:
        print('Only numbers are accepted')
        raise CustomError('Custom Error !!!')
    except CustomError:
        print('Error')
    


ask()