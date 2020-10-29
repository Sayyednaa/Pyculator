import subprocess


print("Hello!  I'm A Calculator Coded By Nawab Abdul Ali\n")
print("What Do You Want To Do?:\n","1:Addition\n","2:Subtraction\n",
      "3:Multiply\n","4:Divide:\n","5:Lcm\n","6:HCF\n")
print("Please Choose Any One Option:")
user = int(input(""))  
if user == 1:
     subprocess.call("add.py", shell=True)

         

    
if user == 2:
        subprocess.call("subtract.py", shell=True)
   


if user == 3:
         subprocess.call("multiply.py", shell=True)
    
if user == 4:
        subprocess.call("Divide.py", shell=True)   
    
if user == 5:
    subprocess.call("lcm.py", shell=True)
 
 
if user == 6:
    subprocess.call("hcf.py", shell=True)
#else:
    #print("Please chose one option listed above.")






#num = int(input('enter num:\n'))
#ns = int(input('enter num2:\n'))

#a = num+ns
#print(a)