from flask import Flask, request, jsonify
import pandas as pd
import csv
import requests
import threading
import socket

app = Flask(__name__)

# Obter URL do banco de dados do ambiente
DATABASE_URL = os.getenv("DATABASE_URL")

# Configurar conexão global
try:
    conn = psycopg2.connect(DATABASE_URL)
    cursor = conn.cursor()
    print("Conexão com o banco de dados PostgreSQL estabelecida!")
except Exception as e:
    print("Erro ao conectar ao banco de dados:", e)
    conn = None

@app.route('/noticias', methods=['POST'])
def criar_noticia():
    dados = request.json
    try:
        with conn.cursor() as cursor:
            query = """
                INSERT INTO noticia (id, manchete, subtitulo, texto, data_publicacao, autor, classificacao_etaria, categoria)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            """
            cursor.execute(query, (
                dados["id"], dados["manchete"], dados["subtitulo"], dados["texto"],
                dados["data_publicacao"], dados["autor"], dados["classificacao_etaria"], dados["categoria"]
            ))
            conn.commit()
        return jsonify({"message": "Notícia criada com sucesso."}), 201
    except Exception as e:
        conn.rollback()
        return jsonify({"erro": f"Erro ao criar notícia: {e}"}), 500

@app.route('/noticias', methods=['GET'])
def ler_noticias():
    try:
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM noticia")
            rows = cursor.fetchall()
            colunas = [desc[0] for desc in cursor.description]
            noticias = [dict(zip(colunas, row)) for row in rows]
        return jsonify(noticias), 200
    except Exception as e:
        return jsonify({"erro": f"Erro ao listar notícias: {e}"}), 500

@app.route('/noticias/<int:id>', methods=['PUT'])
def atualizar_noticia(id):
    dados = request.json
    try:
        with conn.cursor() as cursor:
            # Gerar o comando SQL dinamicamente com base nos campos fornecidos
            campos = ", ".join([f"{key} = %s" for key in dados.keys()])
            valores = list(dados.values()) + [id]
            query = f"UPDATE noticia SET {campos} WHERE id = %s"
            cursor.execute(query, valores)
            conn.commit()
            if cursor.rowcount == 0:
                return jsonify({"erro": "ID não encontrado."}), 404
        return jsonify({"message": f"Notícia com ID {id} atualizada com sucesso."}), 200
    except Exception as e:
        conn.rollback()
        return jsonify({"erro": f"Erro ao atualizar notícia: {e}"}), 500

@app.route('/noticias/<int:id>', methods=['DELETE'])
def deletar_noticia(id):
    try:
        with conn.cursor() as cursor:
            query = "DELETE FROM noticia WHERE id = %s"
            cursor.execute(query, (id,))
            conn.commit()
            if cursor.rowcount == 0:
                return jsonify({"erro": "ID não encontrado."}), 404
        return jsonify({"message": f"Notícia com ID {id} deletada com sucesso."}), 200
    except Exception as e:
        conn.rollback()
        return jsonify({"erro": f"Erro ao deletar notícia: {e}"}), 500

@app.route('/categorias', methods=['GET'])
def listar_categorias():
    try:
        with conn.cursor() as cursor:
            query = "SELECT DISTINCT categoria FROM noticia"
            cursor.execute(query)
            categorias = [row[0] for row in cursor.fetchall()]
        return jsonify(categorias), 200
    except Exception as e:
        return jsonify({"erro": f"Erro ao listar categorias: {e}"}), 500

@app.route('/noticias/categoria/<string:categoria>', methods=['GET'])
def noticias_por_categoria(categoria):
    try:
        with conn.cursor() as cursor:
            query = "SELECT * FROM noticia WHERE categoria = %s"
            cursor.execute(query, (categoria,))
            rows = cursor.fetchall()
            if not rows:
                return jsonify({"erro": f"Não foram encontradas notícias na categoria '{categoria}'."}), 404
            colunas = [desc[0] for desc in cursor.description]
            noticias = [dict(zip(colunas, row)) for row in rows]
        return jsonify(noticias), 200
    except Exception as e:
        return jsonify({"erro": f"Erro ao buscar notícias por categoria: {e}"}), 500

@app.route('/noticias/<int:id>', methods=['GET'])
def obter_noticia_por_id(id):
    try:
        with conn.cursor() as cursor:
            query = "SELECT * FROM noticia WHERE id = %s"
            cursor.execute(query, (id,))
            row = cursor.fetchone()
            if not row:
                return jsonify({"erro": f"Notícia com ID {id} não encontrada."}), 404
            colunas = [desc[0] for desc in cursor.description]
            noticia = dict(zip(colunas, row))
        return jsonify(noticia), 200
    except Exception as e:
        return jsonify({"erro": f"Erro ao buscar notícia: {e}"}), 500


def retornar_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    ip = s.getsockname()[0]
    s.close()
    return ip

# Função para registrar o servidor no Registro de Serviços
def registrar_servico():
    try:
        resposta = requests.post("http://localhost:8080/registrar-servidor", json={
            "ip": retornar_ip(),
            "localizacao": "Brasil",
            "threads": threading.active_count()
        })
        print("Serviço registrado:", resposta.json())
    except Exception as e:
        print(f"Erro ao registrar serviço: {e}")

if __name__ == "__main__":
    registrar_servico()
    app.run(host="0.0.0.0", port=9000)
