import time

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

def show_news(choice):
    news = {
        "1": "🏅 Esportes: O seu resumo esportivo do dia!",
        "2": "🏛️ Política: Acompanhe as últimas atualizações políticas.",
        "3": "💰 Economia: Saiba mais sobre o mercado financeiro.",
        "4": "💻 Tecnologia: As tendências do mundo tech.",
        "5": "🎬 Entretenimento: As novidades do mundo do cinema e TV.",
        "6": "🔬 Ciência: Descubra as últimas inovações científicas.",
    }
    print("\n" + news.get(choice, "Opção inválida. Tente novamente."))

def main():
    name, birth_date = welcome_screen()
    while True:
        choice = news_menu()
        if choice == "0":
            print("\nObrigado por usar o DISTRIBUTED NEWS, {}! Até logo!".format(name))
            break
        else:
            show_news(choice)
            time.sleep(1)

if __name__ == "__main__":
    main()
