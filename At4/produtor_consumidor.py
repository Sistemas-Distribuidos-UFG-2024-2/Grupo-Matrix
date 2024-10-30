import threading
import time
import random

# Definindo o tamanho do buffer
BUFFER_SIZE = 5

# Criando o buffer
buffer = []
buffer_lock = threading.Lock()

# Semáforos
empty = threading.Semaphore(BUFFER_SIZE)  # Contador de slots vazios
full = threading.Semaphore(0)              # Contador de slots cheios

def produtor():
    while True:
        item = random.randint(1, 100)  # Produzindo um item aleatório
        empty.acquire()                # Espera por espaço no buffer
        with buffer_lock:
            buffer.append(item)        # Adiciona o item ao buffer
            print(f'Produzido: {item} | Buffer: {buffer}')
        full.release()                 # Indica que um item foi produzido
        time.sleep(random.uniform(0.1, 1))  # Espera um tempo aleatório

def consumidor():
    while True:
        full.acquire()                 # Espera por um item no buffer
        with buffer_lock:
            item = buffer.pop(0)       # Remove o item do buffer
            print(f'Consumido: {item} | Buffer: {buffer}')
        empty.release()                # Indica que um espaço foi liberado
        time.sleep(random.uniform(0.1, 1))  # Espera um tempo aleatório

# Criando threads para o produtor e o consumidor
produtor_thread = threading.Thread(target=produtor)
consumidor_thread = threading.Thread(target=consumidor)

# Iniciando as threads
produtor_thread.start()
consumidor_thread.start()

# Aguardando as threads (opcional, pois elas rodam indefinidamente)
produtor_thread.join()
consumidor_thread.join()
