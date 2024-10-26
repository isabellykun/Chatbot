def saudacoes(nome):
    import random
    frases = ["Bom dia! Meu nome é " + nome + ". Como vai você?", "Olá", "Oi, tudo bem?"]
    print(frases[random.randint(0,2)])

def recebeTexto():
    texto = "Cliente: " + input("Cliente: ")
    palavraProibida = ["Burro", "Bocó", "Cacete"]
    for p in palavraProibida:
        if p in texto:
            print("Boca suja!")
            return recebeTexto()
        return texto
    
def buscaResposta(nome, texto):
    with open("bd.txt", "a+") as conhecimento:
        conhecimento.seek(0)
        while True:
            viu = conhecimento.readline()
            if viu != "":
                if texto.replace("Cliente: ", "") == "Tchau":
                    print(nome + ": Volte sempre!")
                    return "fim"
                elif viu.strip() == texto.strip():
                    proximalinha = conhecimento.readline()
                    if "Chatbot: " in proximalinha:
                        return proximalinha
            else:
                print("Me desculpe, não sei o que responder!")
                conhecimento.write("\n" + texto)
                resposta_user = input("O que esperava de resposta?\n")
                conhecimento.write("\n" + "Chatbot: " + resposta_user)
                return "Entendi! Eu aprendi..."
                
def exibeResposta(resposta, nome):
    print(resposta.replace("Chatbot", nome))
    if resposta == "fim":
        return "fim"
    return "continua"                    

def exibeResposta_GUI(resposta, nome):
    return resposta.replace("Chatbot", nome)

def saudacao_GUI(nome):
    import random
    frases = ["Bom dia! Meu nome é " + nome + ". Como vai você?", "Olá", "Oi, tudo bem?"]
    return frases[random.randint(0,2)]

def salva_sugestão_GUI(sugestao):
    with open("bd-txt", "a+") as conhecimento:
        conhecimento.write("Chatbot: " + sugestao + "\n")

def buscaResposta_GUI(nome, texto):
    with open("bd.txt", "a+") as conhecimento:
        conhecimento.seek(0)
        while True:
            viu = conhecimento.readline()
            if viu != "":
               if jaccard(texto, viu) > 0.3:
                proximalinha = conhecimento.readline()
                if "Chatbot: " in proximalinha:
                    return proximalinha
            else:
                conhecimento.write(texto)
                return "Me desculpe, não sei o que responder!"
               
def jaccard(textoUsuario, textoBase):
    textoUsuario = limpa_frase(textoUsuario)
    textoBase = limpa_frase(textoBase)
    if len(textoBase) < 1: return 0
    else:
        palavra_em_comum = 0
        for palavra in textoUsuario.split():
            if palavra in textoBase.split():
                palavra_em_comum +=1
        return palavra_em_comum / (len(textoBase.split()))
    
def limpa_frase(frase):
    tirar = ["?", "!", "...", ".", ",", "Cliente: ", "\n"]
    for t in tirar:
        frase = frase.replace(t, "")
    frase = frase.upper()
    return frase