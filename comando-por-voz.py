import speech_recognition as sr
import os

# Função para ouvir e reconhecer a fala
def ouvir_microfone():
    # Habilita o microfone do usuário
    microfone = sr.Recognizer()

    # Usando o microfone
    with sr.Microphone() as source:
        # Chama um algoritmo de reducao de ruidos no som
        microfone.adjust_for_ambient_noise(source)

        # Frase para o usuario dizer algo
        print("Diga alguma coisa: ")

        # Armazena o que foi dito numa variavel
        audio = microfone.listen(source)
    
    try:
        # Reconhece o que foi dito
        frase = microfone.recognize_google(audio, language='pt-BR')

        if "navegador" in frase:
            os.system("start chrome.exe")
            return False
        
        elif "Excel" in frase:
            os.system("start excel.exe")
            return False
        
        elif "Explorer" in frase:
            os.system("start explorer.exe")
            return False
               
        elif "Fechar" in frase:
            os.system("exit")
            return True
        
        # Retornando a frase dita
        print("Voce disse: " + frase)

    except sr.UnknownValueError:
        print("Não entendi")

    return frase

while True:
    if ouvir_microfone():
        break
