import numpy as np
from Pyfhel import Pyfhel
print("1 import pyfhel class and numpy for the inputs to encrypt");

HE = Pyfhel() #creating empty Phyfhel object

#Generate context for 'bfv'/'ckks' scheme
# n defines the number of plaintext slots
HE.contextGen(scheme='bfv',n=2**14,t_bits=20)
HE.keyGen()
print("2. Key setup");
print(HE)

#integer encryption
integer1 = np.array([9], dtype=np.int64)
integer2 = np.array([5], dtype=np.int64)
# print(integer1)

ctxt1 = HE.encryptInt(integer1);
ctxt2 = HE.encryptInt(integer2);

print("3. Integer Encryption, ")
# print("    int ",integer1,'-> ctxt1 ', type(ctxt1))
# print("    int ",integer2,'-> ctxt2 ', type(ctxt2))
print(ctxt1)
print(ctxt2)

ctextsum = ctxt1 + ctxt2
print('Sum ',{ctextsum})
ctextsubstraction = ctxt1 - ctxt2
print('substraction ',{ctextsubstraction})
ctextmul = ctxt1 * ctxt2
print(('Multiplication ',{ctextmul}))
# ctextDiv = ctxt1 / ctxt2

# decryption
resSum = HE.decrypt(ctextsum)
print('decrypt sum result ', resSum)

resSub = HE.decrypt(ctextsubstraction)
print('decrypted substraction res',resSub)

resMul = HE.decrypt(ctextmul)
print('decrypted multiplication res ',resMul)

# resDiv = HE.decrypt(ctextDiv)
# print('decrypted multiplication res ',resDiv)