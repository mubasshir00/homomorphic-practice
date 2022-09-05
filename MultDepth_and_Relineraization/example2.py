import numpy as np
from Pyfhel import Pyfhel

n_mults = 8 

HE = Pyfhel(key_gen=True,context_params={
    'scheme' : 'CKKS',
    'n' : 2**14,
    'scale' : 2**30,
    'qi' : [60] + [30]*n_mults + [60]
})
HE.relinKeyGen()
# print(f"\t{HE}")

arr_x = np.array([1.1,2.2,-3.3],dtype=np.float64)
arr_y = np.array([1,-1,1],dtype=np.float64)

ctxt_x = HE.encryptFrac(arr_x)
ctxt_y = HE.encryptFrac(arr_y)

print("arr_x ",arr_x)
print("ctxt_x ",ctxt_x)
print("arr_y ",arr_y)
print("ctxt_y ",ctxt_y)

_r = lambda x: np.round(x,decimals=6)[:4]
print(f"Securely multplying {n_mults} times!")

for step in range(1,n_mults+1):
    ctxt_x *= ctxt_y #Multiply in-place
    ctxt_x = ~(ctxt_x)
