def doubler_generator():
    number = 2
    while True:
        yield number
        number *= number

doubler = doubler_generator()
print (next(doubler))

print (next(doubler))
print (next(doubler))
print (type(doubler))


def silly_generator():
    yield "Python"
    yield "Rocks"
    yield "So do you!"
    
    
gen = silly_generator()

print (next(gen))


print (next(gen))


print (next(gen))

print (next(gen))

