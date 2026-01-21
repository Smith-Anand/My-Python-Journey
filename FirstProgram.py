# Write a program to input p, r, n and find out interest using simple input 
# output statement. 

p = float(input("Enter the principal amount"));
r = float(input("Enter the rate of Interest"));
n= float(input("Enter the time of Interest"));

s_i = (p*r*n)/100;

print("The simple interest is : ", s_i);
print("The amount after interest is ", p+s_i);