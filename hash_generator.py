
from prettytable import PrettyTable
import hashlib as h
import pyfiglet as fb

# initializing string 

list_hash = ['md5','sha1', 'sha224', 'sha256', 'sha384', 'sha512',
 'blake2b', 'blake2s','sha3_224', 'sha3_256', 'sha3_384','sha3_512',
  'shake_128', 'shake_256'
]

b = fb.figlet_format("Hash Generator",font='graffiti')
a = fb.figlet_format("Ashwin kanojia",font='digital')
print(b,a)


t = PrettyTable()
t.field_names = ['sno','Algorithms']
for n,l in enumerate(list_hash):
    t.add_row([n,l])
print(t)

print('-'*50)
str2hash = input('Enter the string to Hash :')
print('-'*50)
n = int(input('Enter your Hash Algorithm no :'))
print('-'*50)
if n==1:
    result = h.md5(str2hash.encode())
    print("The hexadecimal equivalent of hash is : ", end ="") 
    print(result.hexdigest())  
elif n==2:
    result = h.sha1(str2hash.encode())
    print("The hexadecimal equivalent of hash is : ", end ="") 
    print(result.hexdigest())  
elif n==3:
    result = h.sha224(str2hash.encode())
    print("The hexadecimal equivalent of hash is : ", end ="") 
    print(result.hexdigest())  
elif n==4:
    result = h.sha256(str2hash.encode())
    print("The hexadecimal equivalent of hash is : ", end ="") 
    print(result.hexdigest())  
elif n==5:
    result = h.sha384(str2hash.encode())
    print("The hexadecimal equivalent of hash is : ", end ="") 
    print(result.hexdigest())  
elif n==6:
    result = h.sha512(str2hash.encode())
    print("The hexadecimal equivalent of hash is : ", end ="") 
    print(result.hexdigest())  
elif n==7:
    result = h.blake2b(str2hash.encode())
    print("The hexadecimal equivalent of hash is : ", end ="") 
    print(result.hexdigest())  
elif n==8:
    result = h.blake2s(str2hash.encode())
    print("The hexadecimal equivalent of hash is : ", end ="") 
    print(result.hexdigest())  
elif n==9:
    result = h.sha3_224(str2hash.encode())
    print("The hexadecimal equivalent of hash is : ", end ="") 
    print(result.hexdigest()) 
elif n==10:
    result = h.sha3_256(str2hash.encode())
    print("The hexadecimal equivalent of hash is : ", end ="") 
    print(result.hexdigest()) 
elif n==11:
    result = h.sha3_384(str2hash.encode())
    print("The hexadecimal equivalent of hash is : ", end ="") 
    print(result.hexdigest())  
elif n==12:
    result = h.sha3_512(str2hash.encode()) 
    print("The hexadecimal equivalent of hash is : ", end ="") 
    print(result.hexdigest()) 
elif n==13:
    result = h.shake_128(str2hash.encode())
    print("The hexadecimal equivalent of hash is : ", end ="") 
    print(result.hexdigest())  
elif n==14:
    result = h.shake_256(str2hash.encode())
    print("The hexadecimal equivalent of hash is : ", end ="") 
    print(result.hexdigest())  
else :
    print('enter a valid option')
print('-'*19,'+','<--end-->','+','-'*19)






