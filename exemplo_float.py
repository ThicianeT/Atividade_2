import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from cliente_modbus import ClienteModbus

if __name__ == '__main__':
    c = ClienteModbus('localhost', 502)
    c.conectar()

    end = 200
    val = 25697.85

    print('escrevendo', val, 'no endereco', end)
    c.escrever_float(end, val)

    lido = c.ler_float(end)
    print('lido:', lido)

    c.desconectar()
