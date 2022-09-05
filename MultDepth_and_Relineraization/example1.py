import numpy as np
from Pyfhel import Pyfhel
HE = Pyfhel(key_gen=True,context_params={
    'scheme':'BFV',
    'n' : 2**13 , #  number of slot per plain text , higher n higher noise
    't' : 65537 , #plaintext modulus and bits . Higher
    't_bits' : 20 , # budget , but operations take loger
    'sec' : 128 #security parameter
})
HE.relinKeyGen()
# print("\n BFV context generation")
# print({HE})
# print({HE.n})

# array declaration
arr1 = np.arange(HE.n,dtype=np.int64)
# print(arr1.size) # 8192 = 2**13
print("arr1 ",arr1) # 0 1 2 ... ... 8190 8191
arr2 = np.array([1,-1,1],dtype=np.int64)
print("arr2 ",arr2) # output - [ 1 -1  1]

# print("\nA2. Integer Encryption")

ctxt1 = HE.encryptInt(arr1)
# print({ctxt1})
ctxt2 = HE.encryptInt(arr2)
# print({ctxt2})

# print("Securly mutiplying as much as we can ")
step = 0
lvl = HE.noise_level(ctxt1)
# print(lvl) # output - 146

while lvl > 0:
    print(f"\tStep {step}: noise_lvl {lvl}, res {HE.decryptInt(ctxt1)[:4]}")
    step += 1
    ctxt1 *= ctxt2
    print('ctxt1',HE.decryptInt(ctxt1))
    ctxt1 = ~(ctxt1)
    lvl = HE.noise_level(ctxt1)
    # print('lvl',{lvl})
print(f"\t Final Step {step}: noise_lvl {lvl} res {HE.decryptInt(ctxt1)[:4]}")

