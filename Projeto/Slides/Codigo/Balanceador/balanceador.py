from flask import Flask, jsonify
import requests
import threading
import time
import os
import subprocess

app = Flask(__name__)

# Função para consultar os servidores ativos no registro
def consultar_servidores():
    try:
        resposta = requests.get("https://registro-de-servicos.up.railway.app/consultar_servidores")
        if resposta.status_code == 200:
            print(resposta.json())
            return resposta.json()
        else:
            print(f"Erro ao consultar servidores: Código {resposta.status_code}")
            return {}
    except Exception as e:
        print("Erro ao consultar servidores:", e)
        return {}

def escolher_servidor(): 
    servidores = consultar_servidores()  # Variável local para armazenar a lista de servidores
    if servidores:
        # Filtra os servidores que não estão sobrecarregados
        servidores_disponiveis = {ip: dados for ip, dados in servidores.items() if not dados['sobrecarregado']}
        
        if servidores_disponiveis:
            # Usa a função lambda para encontrar o servidor com o menor número de threads
            servidor_mais_livre = min(servidores_disponiveis, key=lambda ip: servidores_disponiveis[ip]['threads'])
            print(f"Servidor escolhido: {servidor_mais_livre} com {servidores_disponiveis[servidor_mais_livre]['threads']} threads.")
            return servidor_mais_livre
        else:
            print("Nenhum servidor disponível e não sobrecarregado.")
            return None
    else:
        print("Nenhum servidor disponível.")
        return None

# Rota para o proxy solicitar o IP do servidor
@app.route("/balancear", methods=["GET"])
def balancear():
    # Chama a função para escolher o servidor
    servidor_ip = escolher_servidor()

    # Verifica se foi retornado um IP de servidor ou um erro
    if servidor_ip:
        return jsonify({"ip": servidor_ip}), 200  # Responde com o IP do servidor e código 200
    else:
        return jsonify({"error": "Nenhum servidor disponível"}), 500  # Caso não haja servidores disponíveis, retorna código 500
    

if __name__ == "__main__":
       # Porta padrão fornecida pela variável de ambiente PORT, se não, usa 8080
    porta = int(os.getenv("PORT", 8080))  
    # Iniciar o servidor Flask
    app.run(host="0.0.0.0", port=porta)

