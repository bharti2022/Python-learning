def my_func(a, b):
    x = 5  #local scope
    print(x)

if __name__ == '__main__':
    # x = 10
    my_func(1, 2)
    print(x)
    
    