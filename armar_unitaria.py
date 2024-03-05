import qutip as q
import numpy as np

cant_qubits = 4


I = q.identity(2)
X = q.sigmax()
Y = q.sigmay()
Z = q.sigmaz()
paulis = [I, X, Y, Z]
dic_paulis_1 = {'I': paulis[0] ,'X': paulis[1], 'Y': paulis[2], 'Z': paulis[3] }

def lista_prod_tensorial (lista1, lista2):
    lista_producto = []
    for op1 in lista1:
        for op2 in lista2:
            lista_producto.append(q.tensor(op1, op2))    
    return lista_producto

def dic_prod_tensorial (dic1, dic2):
    dic_producto = {}
    for key1 in dic1:
        for key2 in dic2:
            dic_producto[key1 + key2] =q.tensor(dic1[key1], dic2[key2])
    return dic_producto

def armar_dic_paulis (cant_qubits):
   dic_paulis_n = {'I': paulis[0] ,'X': paulis[1], 'Y': paulis[2], 'Z': paulis[3] }
   for i in range(1,cant_qubits):
        dic_paulis_n = dic_prod_tensorial (dic_paulis_n, dic_paulis_1)
   return   dic_paulis_n




def armar_unitaria (a):
    H = 0
    for i in range(len(a)):
        H = H + a[i] * dic_paulis_n[keys[i]]
    H = 1j * H
    U = H.expm()
    return U


cant_qubits = 4

dic_paulis_n = armar_dic_paulis(cant_qubits)
keys = list(dic_paulis_n.keys()) 
a= np.random.rand (4 **cant_qubits)
U = armar_unitaria(a)
print('Es unitaria?:', U.check_isunitary())
#print(U.data)


def funcion_costo (a):
    U = armar_unitaria(a)
    u_sparsa = U.data
    u = U.full()
    suma =np.abs(np.sum (u_sparsa))
    return suma

import scipy.optimize as opt

result = opt.minimize(funcion_costo, a, method = 'SLSQP')
print(result)
