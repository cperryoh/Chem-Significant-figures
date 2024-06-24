import decimal
import math
def count_digits(a):
    return int(math.log10(a))+1
def count_decimals(a):
    d = decimal.Decimal(str(a))
    result = d.as_tuple().exponent
    decimal_count = abs(result)
    return decimal_count
def count_sigfigs(a):
    return count_digits(a*10**count_decimals(a))
def divide(a,b):
    raw_result = a/b
    result_digits = count_digits(raw_result)
    sig_figs = min(count_sigfigs(a),count_sigfigs(b))
    return round(raw_result,sig_figs-result_digits)
def multiply(a,b):
    raw_result = a*b
    result_digits = count_digits(raw_result)
    sig_figs = min(count_sigfigs(a),count_sigfigs(b))
    return round(raw_result,sig_figs-result_digits)
def add(a,b):
    raw_result=a+b
    return round(raw_result,min(count_decimals(a),count_decimals(b)))
def subtract(a,b):
    raw_result=a-b
    return round(raw_result,min(count_decimals(a),count_decimals(b)))
def do_op(a,b,operation):
    fb=0.0
    fa=0.0
    if(type(b)==float or type(b)==int):
        fb=float(b)
    elif(type(b)==ChemNumber):
        fb=b.val

    if(type(a)==float or type(a)==int):
        fa=float(a)
    elif(type(a)==ChemNumber):
        fa=a.val
    return ChemNumber(operation(fa,fb))
class ChemNumber:
    def __init__(self,val):
        self.val=val
    def __str__(self):
        return str(self.val)
    def __rtruediv__(self,rhs):
        return do_op(rhs, self.val, divide)
    def __truediv__(self,rhs):
        return do_op(self.val, rhs, divide)
    def __rmul__(self,rhs):
        return do_op(self.val, rhs, multiply)
    def __mul__(self,rhs):
        return do_op(self.val, rhs, multiply)
    def __add__(self,rhs):
        return do_op(self.val, rhs, add)
    def __radd__(self,rhs):
        return do_op(rhs,self.val, add)
    def __sub__(self,rhs):
        return do_op(self.val, rhs, subtract)
    def __rsub__(self,rhs):
        return do_op(rhs,self.val, subtract)
