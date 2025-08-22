def greet(name):
    if not name.strip():
        return "Helllo,Stranger!"
    return f"Hello,{name}!"
name = input("Enter your name:")
print(greet(name))