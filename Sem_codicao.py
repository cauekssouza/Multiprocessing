from multiprocessing import Process, Value, Lock
import time
import random

def maquina(nome, estoque, lock):
    for _ in range(5):
        time.sleep(random.uniform(0.1, 0.3))
        with lock:  
            estoque.value += 1
            print(f"{nome} produziu uma geladeira. Estoque atual é {estoque.value}")

if __name__ == '__main__':
    estoque = Value('i', 0)
    lock = Lock()  
    processos = []
    for i in range(3):
        p = Process(target=maquina, args=(f'Máquina {i+1}', estoque, lock))
        processos.append(p)
        p.start()

    for p in processos:
        p.join()

    print(f"\n[Versão Com controle] Estoque final (sem condição de corrida): {estoque.value}")
