import threading
import time
import random

NUM_FILOSOFOS = 5
hashis = [threading.Semaphore(1) for _ in range(NUM_FILOSOFOS)]
garcom = threading.Semaphore(NUM_FILOSOFOS - 1)  # evita deadlock

def jantar(filosofo_id):
    esquerda = filosofo_id
    direita = (filosofo_id + 1) % NUM_FILOSOFOS

    while True:
        print(f"Filósofo {filosofo_id} está pensando.")
        time.sleep(random.uniform(1, 3))

        print(f"Filósofo {filosofo_id} está com fome.")
        
        garcom.acquire()

        hashis[esquerda].acquire()
        print(f"Filósofo {filosofo_id} pegou o hashi esquerdo ({esquerda}).")

        hashis[direita].acquire()
        print(f"Filósofo {filosofo_id} pegou o hashi direito ({direita}).")

        print(f"Filósofo {filosofo_id} está comendo.")
        time.sleep(random.uniform(1, 3))

        hashis[esquerda].release()
        hashis[direita].release()
        print(f"Filósofo {filosofo_id} devolveu os hashis.")

        garcom.release()

# Criando e iniciando threads
filosofos = []
for i in range(NUM_FILOSOFOS):
    t = threading.Thread(target=jantar, args=(i,))
    filosofos.append(t)
    t.start()

for t in filosofos:
    t.join()
