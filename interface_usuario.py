import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from time import sleep
from cliente_modbus import ClienteModbus


class InterfaceUsuario:
    def __init__(self, host, port):
        self._cliente = ClienteModbus(host, port)

    def executar(self):
        self._cliente.conectar()
        try:
            while True:
                print('\nmenu:')
                print('1 - ler registrador')
                print('2 - escrever registrador')
                print('3 - escrever float')
                print('4 - ler float')
                print('5 - ver bits do registrador')
                print('6 - alterar bit')
                print('7 - tempo de varredura')
                print('8 - sair')
                op = input('op: ')

                if op == '1':
                    print('1-holding  2-coil  3-input reg  4-discrete')
                    tipo = input('tipo: ')
                    end = int(input('endereco: '))
                    n = int(input('quantas leituras: '))
                    for i in range(n):
                        if tipo == '1':
                            val = self._cliente.ler_holding_register(end)
                        elif tipo == '2':
                            val = self._cliente.ler_coil(end)
                        elif tipo == '3':
                            val = self._cliente.ler_input_register(end)
                        elif tipo == '4':
                            val = self._cliente.ler_discrete_input(end)
                        else:
                            print('tipo invalido')
                            break
                        print(f'leitura {i+1}: {val}')
                        sleep(self._cliente.get_scan_time())

                elif op == '2':
                    print('1-holding  2-coil')
                    tipo = input('tipo: ')
                    end = int(input('endereco: '))
                    val = int(input('valor: '))
                    if tipo == '1':
                        ok = self._cliente.escrever_holding_register(end, val)
                    elif tipo == '2':
                        ok = self._cliente.escrever_coil(end, val)
                    else:
                        print('tipo invalido')
                        continue
                    print('escrito' if ok else 'falhou')

                elif op == '3':
                    end = int(input('endereco (usa 2 regs): '))
                    val = float(input('valor: '))
                    ok = self._cliente.escrever_float(end, val)
                    print('float escrito' if ok else 'falhou')

                elif op == '4':
                    end = int(input('endereco (usa 2 regs): '))
                    val = self._cliente.ler_float(end)
                    print('float lido:', val)

                elif op == '5':
                    end = int(input('endereco: '))
                    bits = self._cliente.ler_bits_register(end)
                    if bits is None:
                        print('falha na leitura')
                    else:
                        for i, b in enumerate(bits):
                            print(f'  bit{i:2d}: {b}')

                elif op == '6':
                    end = int(input('endereco: '))
                    bit = int(input('bit (0-15): '))
                    estado = int(input('estado (0 ou 1): '))
                    ok = self._cliente.escrever_bit_register(end, bit, estado)
                    print('bit atualizado' if ok else 'falhou')

                elif op == '7':
                    t = float(input('novo tempo (s): '))
                    self._cliente.set_scan_time(t)
                    print('tempo atualizado')

                elif op == '8':
                    break

                else:
                    print('opcao invalida')

        except Exception as e:
            print('erro:', e)
        finally:
            self._cliente.desconectar()


if __name__ == '__main__':
    ui = InterfaceUsuario('localhost', 502)
    ui.executar()
