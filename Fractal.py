from PIL import Image, ImageDraw
import os
import random
import datetime

def create_output_directory():
    # Obter o tempo atual
    tempo_atual = datetime.datetime.now()

    # Formatar o tempo atual
    tempo_formatado = tempo_atual.strftime("%Y-%m-%d_%H.%M.%S")

    # Gera um número inteiro aleatório entre 100 e 999 (inclusive)
    numero_inteiro = random.randint(100, 999)

    # Criar o diretório "Output" se não existir
    if not os.path.exists("Output"):
        os.makedirs("Output")
    
    # Nome do diretório com timestamp e número aleatório
    nome_diretorio = f"Output/Result_Rnd{numero_inteiro}_{tempo_formatado}"
    
    # Criar o diretório
    os.makedirs(nome_diretorio, exist_ok=True)

    return nome_diretorio

# Criar o diretório de saída e obter seu nome
diretorio_de_saida = create_output_directory()

# Data
image_data = []

# Parametros
image_width = 200
image_height = 200
n_img = 5

def image_data_generator(index, index_limit):
    global image_data
    for iw in range(image_height):
        line = []
        for ih in range(image_width):
            cor = (
                random.randint(int(index * 255 / index_limit), 255),
                random.randint(int(index * 255 / index_limit), 255),
                random.randint(int(index * 255 / index_limit), 255)
            )
            line.append(cor)
        image_data.append(line)

def image_generator(index):
    global image_data, diretorio_de_saida
    image_data = []  # Reset image_data for each call
    image_data_generator(index, n_img)

    # Criar uma nova imagem
    imagem = Image.new("RGB", (image_width, image_height), "white")

    # Preencher a imagem com os dados gerados
    for y in range(image_height):
        for x in range(image_width):
            imagem.putpixel((x, y), image_data[y][x])

    # Nome do arquivo com base no índice
    nome_arquivo = f"img_{index}.png"
    caminho_imagem = os.path.join(diretorio_de_saida, nome_arquivo)
    
    # Salvar a imagem
    imagem.save(caminho_imagem)

for i in range(n_img):
    image_generator(i)
