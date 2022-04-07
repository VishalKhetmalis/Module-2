#220340325058 Vishal Khetmalis
#1. Write a R program to create a sequence of numbers from 20 to 50 and find the mean
#of numbers from 20 to 60 and sum of numbers from 51 to 91.
print("The sequence of numbers from 20 to 50 is: ")
print(seq(20,50))
print("The mean of numbers from 20 to 60 is: ")
print(mean(20:60))
print("The sum of numbers from 51 to 91 is: ")
print(sum(51:91))

#2. Write a R program to print the numbers from 1 to 100 and print "Fizz" for multiples
#of 3, print "Buzz" for multiples of 5, and print "FizzBuzz" for multiples of both.
print("The numbers from 1 to 100 as required are: ")
for (i in 1:100)
{
  if (i%%3==0 & i %%5==0)
  {
    print("FizzBuzz")
  }
  else if (i%%3==0)
  {
    print("Fizz")
  }
  else if (i%%5==0)
  {
    print("Buzz")
  }
  else 
    print(i)
}