import time
import requests
import uuid

# Base URL do servidor Flask
base_url = "http://136.248.75.174:8001"

def print_line(char='=', length=50):
    print(char * length)

def welcome_screen():
    print_line()
    print(" " * 12 + "🚀 DISTRIBUTED NEWS 🚀")
    print_line()
    print("\nBem-vindo ao DISTRIBUTED NEWS!")
    time.sleep(1)
    
    name = input("Digite seu nome: ")
    birth_date = input("Digite sua data de nascimento (DD/MM/AAAA): ")
    print("\nÓtimo, {}! Vamos começar.".format(name))
    time.sleep(1)
    return name, birth_date

def news_menu():
    print("\n" + "=" * 50)
    print("📰 Escolha o tipo de notícia que você quer ler: ")
    print("=" * 50)
    print("1 - Esportes 🏅")
    print("2 - Política 🏛️")
    print("3 - Economia 💰")
    print("4 - Tecnologia 💻")
    print("5 - Entretenimento 🎬")
    print("6 - Ciência 🔬")
    print("0 - Sair")
    print("=" * 50)

    choice = input("Digite o número da sua escolha: ")
    return choice

def show_news_paginated(choice, page_size=5):
    categorias = {
        "1": "Esportes",
        "2": "Política",
        "3": "Economia",
        "4": "Tecnologia",
        "5": "Entretenimento",
        "6": "Ciência"
    }
    
    categoria = categorias.get(choice)
    if not categoria:
        print("Opção inválida. Tente novamente.")
        return
    
    request_id = str(uuid.uuid4())  
    response = requests.post(f"{base_url}/enqueue_request", json={
        "request_id": request_id,
        "method_name": "/noticias/categoria/",
        "args": [categoria]
    })
    
    if response.status_code != 200:
        print("Erro ao enviar a requisição.")
        return
    
    while True:
        response = requests.get(f"{base_url}/get_response/{request_id}")
        response_data = response.json().get("response", "Resposta ainda não disponível. Tente novamente mais tarde.")
        if response_data != "Resposta ainda não disponível. Tente novamente mais tarde.":
            break
        time.sleep(0.5)  

    if not isinstance(response_data, list) or not response_data:
        print("Nenhuma notícia encontrada para a categoria escolhida.")
        return

    noticias = response_data
    total_news = len(noticias)
    current_page = 0

    while True:
        start = current_page * page_size
        end = start + page_size
        news_page = noticias[start:end]

        print(f"\nMostrando notícias {start + 1} a {min(end, total_news)} de {total_news} para a categoria '{categoria}':")

        for noticia in news_page:
            print(f"ID: {noticia['id']}")
            print(f"Manchete: {noticia['manchete']}")
            print(f"Subtítulo: {noticia['subtitulo']}")
            print("-" * 50)

        # Navegação da página
        print("\nOpções:")
        if start > 0:
            print("P - Página Anterior")
        if end < total_news:
            print("N - Próxima Página")
        print("L - Ler uma notícia")
        print("S - Sair")

        option = input("Escolha uma opção: ").strip().upper()

        if option == "N" and end < total_news:
            current_page += 1
        elif option == "P" and start > 0:
            current_page -= 1
        elif option == "L":
            news_id = input("Digite o ID da notícia que deseja ler: ")
            show_news_detail(news_id)
        elif option == "S":
            break
        else:
            print("Opção inválida. Tente novamente.")

def show_news_detail(news_id):
    request_id = str(uuid.uuid4())  
    response = requests.post(f"{base_url}/enqueue_request", json={
        "request_id": request_id,
        "method_name": "/noticias/",
        "args": [news_id]
    })
    
    if response.status_code != 200:
        print("Erro ao enviar a requisição.")
        return
    
   
    while True:
        response = requests.get(f"{base_url}/get_response/{request_id}")
        response_data = response.json().get("response", "Resposta ainda não disponível. Tente novamente mais tarde.")
        if response_data != "Resposta ainda não disponível. Tente novamente mais tarde.":
            break
        time.sleep(0.5) 

    if isinstance(response_data, dict):
        print("\n--- Detalhe da Notícia ---")
        print(f"ID: {response_data['id']}")
        print(f"Manchete: {response_data['manchete']}")
        print(f"Subtítulo: {response_data['subtitulo']}")
        print(f"Texto: {response_data['texto']}")
        print(f"Data de Publicação: {response_data['data_publicacao']}")
        print(f"Autor: {response_data['autor']}")
        print(f"Classificação Etária: {response_data['classificacao_etaria']}")
        print("-" * 50)
    else:
        print("Notícia não encontrada.")
        
def main():
    name, birth_date = welcome_screen()
    while True:
        choice = news_menu()
        if choice == "0":
            print("\nObrigado por usar o DISTRIBUTED NEWS, {}! Até logo!".format(name))
            break
        else:
            show_news_paginated(choice)
            time.sleep(1)

if __name__ == "__main__":
    main()
