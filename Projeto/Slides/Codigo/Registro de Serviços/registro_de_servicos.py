from flask import Flask, request, jsonify
import threading
import time
import requests
import os

# Estrutura para armazenar informações dos servidores
servidores = {}

app = Flask(__name__)

# Função para registrar ou atualizar informações de um servidor
@app.route("/registrar-servidor", methods=["POST"])
def registrar_servidor():
    dados = request.json
    ip = dados["ip"]
    localizacao = dados["localizacao"]
    threads = dados["threads"]
    
    servidores[ip] = {
        'localizacao': localizacao,
        'threads': threads,
        'sobrecarregado': False
    }
    print(f"Servidor {ip} registrado com sucesso.")
    return jsonify({"message": f"Servidor {ip} registrado com sucesso."}), 200

# Função para atualizar o status de threads e checar se o servidor está ativo
def atualizar_status_servidor(ip):
    if ip in servidores:
        try:
            # Faz uma requisição GET para obter o número de threads do servidor
            resposta = requests.get(f"http://{ip}:8000/get_threads")
            if resposta.status_code == 200:
                threads = resposta.json().get("threads")
                servidores[ip]['threads'] = threads
                
                # Verifica sobrecarga baseado em um limite de threads
                limite_threads = 100  # ajuste conforme necessário
                servidores[ip]['sobrecarregado'] = threads > limite_threads
                print(f"Servidor {ip} atualizado. Threads: {threads}. Sobrecarregado: {servidores[ip]['sobrecarregado']}")
            else:
                raise Exception("Falha ao obter threads")
                
        except Exception as e:
            del servidores[ip]
            print(f"Servidor {ip} removido devido a inatividade: {e}")
    else:
        print(f"Servidor {ip} não encontrado.")

# Thread que verifica e atualiza status dos servidores periodicamente
def monitorar_servidores():
    while True:
        for ip in list(servidores.keys()):
            atualizar_status_servidor(ip)
        time.sleep(10)  # Verifica a cada 10 segundos

# Função para consulta do balanceador, retorna todos os servidores registrados
@app.route("/consultar_servidores", methods=["GET"])
def consultar_servidor():
    print("Consulta do balanceador realizada. Todos os servidores:", servidores)
    return jsonify(servidores), 200

# Iniciar o servidor de registro de serviços usando Flask
def iniciar_registro():
    port = int(os.getenv("PORT", 9000))  # usa 9000 como padrão
    
    # Iniciar a thread de monitoramento de servidores
    threading.Thread(target=monitorar_servidores, daemon=True).start()
    
    print("Registro de Serviços em execução...")
    app.run(host="0.0.0.0", port=port)

# Iniciar o registro de serviços
iniciar_registro()
