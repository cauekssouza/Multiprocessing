from multiprocessing import Process, Value
import time
import random

def maquina(nome, estoque):
    for _ in range(5):
        atual = estoque.value  
        time.sleep(random.uniform(0.1, 0.3))  
        estoque.value = atual + 1  
        print(f"{nome} produziu uma geladeira. Estoque atual é {estoque.value}")

if __name__ == '__main__':
    estoque = Value('i', 0)
    processos = []
    for i in range(3):
        p = Process(target=maquina, args=(f'Máquina {i+1}', estoque))
        processos.append(p)
        p.start()

    for p in processos:
        p.join()

    print(f"\n[Versão Sem controle] Estoque final (com condição de corrida): {estoque.value}")
