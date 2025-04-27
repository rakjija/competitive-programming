import sys

N = int(sys.stdin.readline())

heart = """ @@@   @@@ 
@   @ @   @
@    @    @
@         @
 @       @ 
  @     @  
   @   @   
    @ @    
     @     """

output = (heart + "\n") * (N - 1) + heart
print(output, end="")
