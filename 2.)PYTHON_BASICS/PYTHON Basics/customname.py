def hello_to_all(name):
    """
    this function return greeting
    """
    print(f"{name} says hello to all")

    
def bye(name):
    print(f"{name} say bye to all")

def add(a,b):
    return(a+b)

def print_name():
    print(__name__) #this will give __customname__ bcz callong through some func
    
#print(__name__) this will give __main__ calling from func    