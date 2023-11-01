import pywhatkit
import time

def enviar_resposta(message):
    response = "Olá! Este é um bot de resposta automática. Você enviou: " + message
    return response

def bot_whatsapp():
    # Número de telefone para enviar mensagens
    telefone = "+5551981614740"  # Substitua pelo número de telefone do destinatário

    while True:
        hora_atual = time.localtime()
        if hora_atual.tm_hour == 12 and hora_atual.tm_min == 0:
            mensagem = "Olá, é meio-dia!"
            pywhatkit.sendwhatmsg(telefone, mensagem, hora_atual.tm_hour, hora_atual.tm_min + 1)
        # Verificar se há novas mensagens
        pywhatkit.sendwhatmsg(telefone, enviar_resposta("Olá!"), hora_atual.tm_hour, hora_atual.tm_min)
        time.sleep(60)

if __name__ == "__main__":
    bot_whatsapp()
