from flask import Flask, request, jsonify
from threading import Thread
from queue import Queue
import requests
import time

app = Flask(__name__)
servidor_url = "http://localhost:9000/"  
request_queue = Queue()
response_dict = {}  

def enqueue_request(request_id, method_name, *args):
    """Função que enfileira requisições."""
    request_data = {
        "request_id": request_id,
        "method_name": method_name,
        "args": args
    }
    request_queue.put(request_data)
    return f"Request {request_id} enqueued."

def process_queue():
    """Processa a fila de requisições."""
    while True:
        request_data = request_queue.get()
        if request_data:
            request_id = request_data["request_id"]
            method_name = request_data["method_name"]
            args = request_data["args"]
            try:
                
                response = requests.post(f"{servidor_url}{method_name}", json=args)
                response_dict[request_id] = response.json()  
                print(f"Requisição processada: {method_name} - Resposta armazenada para request_id {request_id}")
            except Exception as e:
                response_dict[request_id] = f"Erro: {e}"  
                print(f"Erro ao processar requisição {method_name}: {e}")
            finally:
                request_queue.task_done()

@app.route('/enqueue_request', methods=['POST'])
def handle_enqueue_request():
    """Endpoint para enfileirar requisições."""
    data = request.json
    request_id = data["request_id"]
    method_name = data["method_name"]
    args = data.get("args", [])
    result = enqueue_request(request_id, method_name, *args)
    return jsonify({"message": result})

@app.route('/get_response/<request_id>', methods=['GET'])
def handle_get_response(request_id):
    """Endpoint para obter a resposta de uma requisição."""
    response = response_dict.pop(request_id, "Resposta ainda não disponível. Tente novamente mais tarde.")
    return jsonify({"response": response})

if __name__ == "__main__":
   
    thread = Thread(target=process_queue, daemon=True)
    thread.start()

    app.run(host="0.0.0.0", port=80)
