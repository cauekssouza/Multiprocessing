from multiprocessing import Process, Value
import time
import random


estoque = 0

def maquina(nome):
    global estoque
    for _ in range(5):
        atual = estoque
        time.sleep(random.uniform(0.1, 0.3))
        estoque = atual + 1
        print(f"{nome} produziu uma geladeira. Estoque atual é {estoque}")

if __name__ == '__main__':
    processos = []
    for i in range(3):
        p = Process(target=maquina, args=(f'Máquina {i+1}',))
        processos.append(p)
        p.start()

    for p in processos:
        p.join()

    print(f"\n[Versão 1] Estoque final (sem condição de corrida): {estoque}")
