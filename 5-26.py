def decorator_function(f):
    def new_function():
        print('Additional functionality before')
        f()
        print('Additional functionality after')
        
    return new_function

@decorator_function
def decorated_function():
    print("Original Functionality")

decorated_function()
