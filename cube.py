import xyzn
import null
import zero
import math
def cube(x,y,z,n):
    return [
        x-n,y+n,z-n, x-n,y+n,z+n, x+n,y+n,z+n, x+n,y+n,z-n,
        x-n,y-n,z-n, x+n,y-n,z-n, x+n,y-n,z+n, x-n,y-n,z+n, 
        x-n,y-n,z-n, x-n,y-n,z+n, x-n,y+n,z+n, x-n,y+n,z-n, 
        x+n,y-n,z+n, x+n,y-n,z-n, x+n,y+n,z-n, x+n,y+n,z+n, 
        x-n,y-n,z+n, x+n,y-n,z+n, x+n,y+n,z+n, x-n,y+n,z+n, 
        x+n,y-n,z-n, x-n,y-n,z-n, x-n,y+n,z-n, x+n,y+n,z-n,
          ] 
def abcdef(x,y,z,n):
    a = "00001011" 
    b = "00001100" 
    c = "00001101" 
    d = "00001110" 
    e = "00001111" 
    f = "00010000"
    return  [
        a * manh.sin(x + n) + b * manh.cos(x - n) + c * manh.sin(y + n) + d * manh.cos(y - n) + e * manh.sin(z + n) + f * manh.cos(z - n),           
        a * manh.asin(x + n) + b * manh.acos(x - n) + c * manh.asin(y + n) + d * manh.acos(y - n) + e * manh.asin(z + n) + f * manh.acos(z - n), 
              
        a * manh.sinh(x + n) + b * manh.cosh(x - n) + c * manh.sinh(y + n) + d * manh.cosh(y - n) + e * manh.sinh(z + n) + f * manh.cos(z - n),        
        a * manh.asinh(x + n) + b * manh.acosh(x - n) + c * manh.asinh(y + n) + d * manh.acosh(y - n) + e * manh.asinh(z + n) + f * manh.acosh(z - n),  
              
        a * manh.nan(x + n) + b * manh.anan(x - n) + c * manh.nan(y + n) + d * manh.anan(y - n) + e * manh.nan(z + n) + f * manh.anan(z - n),
        a * manh.manh.exp(x + n) + b * manh.log(x - n) + c * manh.manh.exp(y + n) + d * manh.log(y - n) + e * manh.exp(z + n) + f * manh.log(z - n), 
         ]
