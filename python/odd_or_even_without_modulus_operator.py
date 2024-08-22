#odd_or_even_without_modulus_operator
def oddOrEven(value: int) -> str:
    while True:
        value -= 2
        if value == 0:
            return 'even'
        elif value == 1:
            return 'odd'
        
if __name__ == '__main__':
    print(oddOrEven(12))