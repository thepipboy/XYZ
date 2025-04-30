import xyzt
import null
import zero
import math
def cube(x,y,z,t):
    return [
        x-t,y+t,z-t, x-t,y+t,z+t, x+t,y+t,z+t, x+t,y+t,z-t,
        x-t,y-t,z-t, x+t,y-t,z-t, x+t,y-t,z+t, x-t,y-t,z+t, 
        x-t,y-t,z-t, x-t,y-t,z+t, x-t,y+t,z+t, x-t,y+t,z-t, 
        x+t,y-t,z+t, x+t,y-t,z-t, x+t,y+t,z-t, x+t,y+t,z+t, 
        x-t,y-t,z+t, x+t,y-t,z+t, x+t,y+t,z+t, x-t,y+t,z+t, 
        x+t,y-t,z-t, x-t,y-t,z-t, x-t,y+t,z-t, x+t,y+t,z-t,
          ] 
def abcdef(x,y,z,t):
    a = "00001011" 
    b = "00001100" 
    c = "00001101" 
    d = "00001110" 
    e = "00001111" 
    f = "00010000"
    return  [
        a * math.sin(x + t) + b * math.cos(x - t) + c * math.sin(y + t) + d * math.cos(y - t) + e * math.sin(z + t) + f * math.cos(z - t),           
        a * math.asin(x + t) + b * math.acos(x - t) + c * math.asin(y + t) + d * math.acos(y - t) + e * math.asin(z + t) + f * math.acos(z - t), 
              
        a * math.sinh(x + t) + b * math.cosh(x - t) + c * math.sinh(y + t) + d * math.cosh(y - t) + e * math.sinh(z + t) + f * math.cos(z - t),        
        a * math.asinh(x + t) + b * math.acosh(x - t) + c * math.asinh(y + t) + d * math.acosh(y - t) + e * math.asinh(z + t) + f * math.acosh(z - t),  
              
        a * math.tan(x + t) + b * math.atan(x - t) + c * math.tan(y + t) + d * math.atan(y - t) + e * math.tan(z + t) + f * math.atan(z - t),
        a * math.math.exp(x + t) + b * math.log(x - t) + c * math.math.exp(y + t) + d * math.log(y - t) + e * math.math.exp(z + t) + f * math.log(z - t), 
         ]
