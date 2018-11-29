def cough_dec(func):
    def func_wrapper():
        # code before func is invoked
        print('*cough*')
        func()
        # code after func is invoked
        print('*cough*')

    return func_wrapper


@cough_dec
def question():
    print('Can you discount that?')


question()
