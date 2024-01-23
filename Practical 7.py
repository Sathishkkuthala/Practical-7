fh = open("prac 7.txt",'w')
num=input('Enter any value:')
reverse=num[::-1]
if(reverse==num): 
    fh.write('It is a palindrome') 
else: 
    fh.write('It is not a palindrome')
fh.close()
