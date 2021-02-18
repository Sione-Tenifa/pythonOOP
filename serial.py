"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """
    print("working")

    def __init__(self, num=0):
        self.num = num
        self.serial = num

    def number(self):
        print(self.num)

    def generate(self):
        
        self.serial += 1
        return self.serial 

    def reset(self): 
        self.serial = self.num
