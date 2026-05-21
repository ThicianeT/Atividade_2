import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from cliente_modbus import ClienteModbus

if __name__ == '__main__':
    c = ClienteModbus('localhost', 502)
    c.conectar()

    end = 300
    c.escrever_holding_register(end, 0b0000000000001010)

    print('bits iniciais:')
    bits = c.ler_bits_register(end)
    for i, b in enumerate(bits):
        print(f'  bit{i:2d}: {b}')

    c.escrever_bit_register(end, 0, 1)
    c.escrever_bit_register(end, 3, 0)

    print('\nbits depois:')
    bits = c.ler_bits_register(end)
    for i, b in enumerate(bits):
        print(f'  bit{i:2d}: {b}')

    c.desconectar()
