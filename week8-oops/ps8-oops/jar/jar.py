# cookie jar

class Jar:
    def __init__(self,capacity=12):
        if capacity < 0:
            raise ValueError
        self.capacity = capacity
        self.size = 0
        
    def __str__(self):
        return f"{self.size * '🍪'}"

    
    def capacity(self):
        return f"{self.capacity}"
    
    def size(self):
        return f"{self.size}"
    
    def deposit(self,n):
        if self.capacity < n:
            raise ValueError
        
        self.size += n

    def withdraw(self,n):
        if self.size < n:
            raise ValueError
        
        self.size -= n
    
    
    


def main():
    jar = Jar()
    jar.deposit(2)
    print(jar)
    jar.deposit(4)
    print(jar)
    jar.deposit(5)
    print(jar)
    jar.withdraw(3)
    print(jar)
    print(f"Jar Capacity: {jar.capacity}")
    print(f"Size of Jar: {jar.size}")
    

    


if __name__ == "__main__":
    main()
    
    