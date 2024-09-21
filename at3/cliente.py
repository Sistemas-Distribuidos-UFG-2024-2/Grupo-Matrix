import asyncio

async def cliente():
    s2_ip = '127.0.0.1'
    s2_port = 5000

    for i in range(5):
        try:
            print("Tentando conectar ao servidor...")
            # Abre a conexão de forma assíncrona
            reader, writer = await asyncio.open_connection(s2_ip, s2_port)
            break
        except ConnectionRefusedError:
            print("Conexão recusada. Tentando novamente...")
            await asyncio.sleep(2)
    else:
        print("Não foi possível conectar ao servidor após 5 tentativas.")
        return

    print("Conectado ao servidor.")

    # Envia dados de forma assíncrona
    writer.write(b'hello')
    await writer.drain()  # Aguarda até que os dados sejam enviados

    # Recebe dados de forma assíncrona
    data = await reader.read(1024)
    print('Resposta recebida:', data.decode())

    # Fecha a conexão
    writer.close()
    await writer.wait_closed()

# Inicia o loop de eventos assíncronos
asyncio.run(cliente())
