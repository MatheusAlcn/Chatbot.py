import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def enviar_mensagem(mensagem, lista_mensagens):
    # Função para enviar uma mensagem ao modelo e obter a resposta.

    # Adiciona a mensagem do usuário à lista de mensagens.
    lista_mensagens.append({"role": "user", "content": mensagem})
    try:
        # Faz a chamada à API do ChatGPT usando o modelo "gpt-3.5-turbo".
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=lista_mensagens,
        )
        # Retorna a resposta do modelo.
        return response["choices"][0]["message"]
    except Exception as e:
        # Captura e exibe erros que possam ocorrer durante a chamada à API.
        print(f"Erro ao enviar mensagem: {e}")
        return None

# Personalização do comportamento do assistente.
personalizacao = """
Você é um assistente inteligente e amigável. Responda de forma clara e concisa.
"""

# Inicializa a lista de mensagens com a personalização do assistente.
lista_mensagens = [{"role": "system", "content": personalizacao}]

# Inicia o loop de interação com o usuário.
while True:
    texto = input("Escreva aqui sua mensagem (ou 'sair' para encerrar): ")
    
    # Verifica se o usuário deseja encerrar a conversa.
    if texto.lower() == "sair":
        print("Fim da conversa.")
        break
    else:
        # Envia a mensagem do usuário e obtém a resposta do ChatGPT.
        resposta = enviar_mensagem(texto, lista_mensagens)
        if resposta:
            # Exibe a resposta do ChatGPT e a adiciona à lista de mensagens.
            print(f"ChatBot: {resposta['content']}")
            lista_mensagens.append(resposta)
        else:
            # Exibe uma mensagem de erro caso a resposta não seja obtida.
            print("Desculpe, não foi possível obter uma resposta.")
