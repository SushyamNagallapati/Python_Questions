# def fib(number):
    
#     if number < 0:
#         print("Invalid number")
#     else:
#         a = 0
#         b = 1
        
#         print(a)
        
#         if number > 0:
#             print(b)
        
#         while True:
#             c = a + b
#             if c < 100:
#                 print(c)
#                 a = b
#                 b = c
#             else:
#                 break
        
# fib(int(input("Enter a number: ")))

# Or

number = int(input("Enter a number: "))
 
if number < 0:
    print("Its an invalid number")
else:
     
    a = 0
    b = 1
     
    print(a)
     
    if number > 0:
        print(b)
         
    for i in range(number):
        c = a + b
        if c < 100:
            print(c)
            a = b
            b = c
        else:
            break   
