from multiprocessing import Process, Value, Lock, Queue, Pipe
import time
import random

def maquina(nome, estoque, lock, queue, conn):
    for _ in range(5):
        time.sleep(random.uniform(0.1, 0.3)) 
        with lock:
            estoque.value += 1
            valor_atual = estoque.value
        queue.put((nome, valor_atual))  
    conn.send(f"{nome} finalizou a produção.")
    conn.close()

if __name__ == '__main__':
    estoque = Value('i', 0)  
    lock = Lock()
    queue = Queue()
    conexoes = []

    processos = []
    for i in range(3):
        parent_conn, child_conn = Pipe()
        conexoes.append(parent_conn)
        p = Process(target=maquina, args=(f'Máquina {i+1}', estoque, lock, queue, child_conn))
        processos.append(p)
        p.start()

    
    mensagens = 0
    while mensagens < 15:
        nome, valor = queue.get()
        print(f"{nome} produziu uma geladeira. Estoque atual é {valor}")
        mensagens += 1

    
    for conn in conexoes:
        print(conn.recv())

    for p in processos:
        p.join()

    print(f"\n[Versão 2] Estoque final (com condição de corrida): {estoque.value}")
