import decimal
import math
def count_digits(a):
    if(a==0.0):
        return 1
    if(a<1.0 and a>-1.0):
        return 0
    return int(math.log10(abs(a)))+1
def count_decimals(a):
    d = decimal.Decimal(str(a))
    result = d.as_tuple().exponent
    decimal_count = abs(result)
    return decimal_count
class ChemNumber:
    def __init__(self,num):
        if(type(num)==ChemNumber):
            self.val=num.val
        else:
            self.val=num
        self.decimal_count=count_decimals(self.val)
        self.digits_count=count_digits(self.val)
        self.sig_figs=count_sigfigs(self.val)
    def __str__(self):
        return str(self.val)
    def __rtruediv__(self,lhs):
        return do_op(lhs, self, divide)
    def __truediv__(self,rhs):
        return do_op(self, rhs, divide)
    def __rmul__(self,lhs):
        return do_op(self, lhs, multiply)
    def __mul__(self,rhs):
        return do_op(self, rhs, multiply)
    def __add__(self,rhs):
        return do_op(self, rhs, add)
    def __radd__(self,lhs):
        return do_op(lhs,self, add)
    def __sub__(self,rhs):
        return do_op(self, rhs, subtract)
    def __rsub__(self,lhs):
        return do_op(lhs,self, subtract)
def round_chem_number(a: ChemNumber, digits_count: int):
    return ChemNumber(round(a.val,digits_count))
def count_sigfigs(a):
    return count_digits(a*10**count_decimals(a))
def divide(a: ChemNumber,b: ChemNumber):
    raw_result = ChemNumber(a.val/b.val)
    sig_figs = min(a.sig_figs,b.sig_figs)
    return round_chem_number(raw_result,sig_figs-raw_result.digits_count)
def multiply(a: ChemNumber,b: ChemNumber):
    raw_result = ChemNumber(a.val*b.val)
    sig_figs = min(a.sig_figs,b.sig_figs)
    return round_chem_number(raw_result,sig_figs-raw_result.digits_count)
def add(a: ChemNumber,b: ChemNumber):
    raw_result=ChemNumber(a.val+b.val)
    return round_chem_number(raw_result, min(a.decimal_count,b.decimal_count))
def subtract(a: ChemNumber,b: ChemNumber):
    raw_result=ChemNumber(a.val-b.val)
    return round_chem_number(raw_result, min(a.decimal_count,b.decimal_count))
def do_op(a,b,operation):
    sig_a=ChemNumber(a)
    sig_b=ChemNumber(b)
    return operation(sig_a,sig_b)
