def accounts(f):
    def wrapper(f);
    print("Run the function")
    f()
    print("Function finished")
    return wrapper
def hello():
    print("hello, wrld")
hello()
cars = input("Would u like to run the function?")
if cars == "yes":
    accounts();
else:
    break;
x = int(input("x: "))
y = int(input("y: "))
