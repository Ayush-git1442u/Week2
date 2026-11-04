def first_call():
    second_call()

def second_call():
    third_call()

def third_call():
    result = 1 + "Hello" #This line will raise TypeError

first_call()