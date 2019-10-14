##Test curva ellittica valori Point##

##Formula ----------> y2 = x3 +ax +b



class Point:
    def __init__(self, x, y, a, b): 
        self.a = a
        self.b = b
        self.x = x
        self.y = y
        if self.y**2 != self.x**3 + a * x + b:
            raise ValueError('({}, {}) is not on the curve'.format(x, y))


##From elliptic_curve import Point##

##>>>RESPONSE ERRATA-->
##>>> p = Point(3, 6, 8, 4)
##Traceback (most recent call last):
##  File "<stdin>", line 1, in <module>
##  File "/home/developer/Desktop/bcademy/Progetto 1/ellittic_curve.py", line 10, in __init__
##    raise ValueError('({}, {}) is not on the curve'.format(x, y))
##valueError: (3, 6) is not on the curve

##>>>RESPONSE CORRETTA-->

##>>> p = Point(-1, -1, 5, 7)  
##>>>> questi sono valori da ellittic curve corretti che non restituisce errori