"""Task : 5 Tuple Packing and Unpacking: 
    Create a function that takes three numbers as arguments, packs them into a tuple, 
    and then unpacks them to return their sum and product."""

numbers = ()

def tuple_numbers(*numbers):
    
    print(type(numbers))
    print("The Packed Values : ",numbers)

    def unpack(sum, numbers):
        print("The Unpacked Values : ",*numbers)
        
        # sum = 0
        for add in numbers:
            sum = sum + add    
        print("The sum of the unpacked values",sum)

        product = 1
        for multiply in numbers:
            product = product * multiply
        print("The product of the unpacked values",product)

    unpack(0, numbers)

tuple_numbers(10, 20, 30)
