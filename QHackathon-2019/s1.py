from random import getrandbits
from qiskit import QuantumCircuit, execute, Aer

TARGET = 100

def grb(n):
    """Returns a random bit-string of length n."""
    r = bin(getrandbits(n))[2:]
    if len(r)<n:
        r = '0'*(n-len(r)) + r
    return r

def BB84(t):
    target = 2*t

    alice_bits = grb(target)
    alice_directions = grb(target)
    bob_directions = grb(target)
    bob_bits = ''

    # Alice has random bits and directions,
    # Bob has random directions and make measurements accordingly,
    for i in range(target):
        circ = QuantumCircuit(1,1)

        if(alice_bits[i]=='1'):
            circ.x(0)
        if(alice_directions[i]=='1'):
            circ.h(0)
        if(bob_directions[i]=='1'):
            circ.h(0)
        circ.measure(0,0)
        bob_bits += execute(circ, Aer.get_backend("qasm_simulator"), shots=1, memory=True).result().get_memory()[0]

    # After qubit communication and measurement, Alice and Bob compare their directions,
    clean_up = filter(lambda x: x[0]==x[1], zip(alice_directions, bob_directions, alice_bits, bob_bits))

    # After getting rid of different ones, their bits are (supposedly) same on both ends
    bits_both = [(i[2], i[3]) for i in clean_up]
    # print(all(filter(lambda x: x[0]==x[1], bits_both)))

    # Time to control
    

BB84(TARGET)
