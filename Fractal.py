import os
import datetime
import math
from PIL import Image

# Função para criar o diretório de saída
def create_output_directory():
    # Obter o tempo atual
    tempo_atual = datetime.datetime.now()

    # Formatar o tempo atual
    tempo_formatado = tempo_atual.strftime("%Y-%m-%d_%H.%M.%S")

    # Gera um número inteiro aleatório entre 100 e 999 (inclusive)
    numero_inteiro = 999

    # Criar o diretório "Output" se não existir
    if not os.path.exists("Output"):
        os.makedirs("Output")
    
    # Nome do diretório com timestamp e número aleatório
    nome_diretorio = f"Output/Result_Rnd{numero_inteiro}_{tempo_formatado}"
    
    # Criar o diretório
    os.makedirs(nome_diretorio, exist_ok=True)

    return nome_diretorio

# Função para gerar os dados da imagem do Conjunto de Mandelbrot
def image_data_generator(index, index_limit):
    global image_data
    for iw in range(image_height):
        line = []
        for ih in range(image_width):
            # Calcula o valor de suavização
            c = complex((index * 2) / index_limit - 1, (index * 2) / index_limit - 1)
            suavizacao = mandelbrot(c)
            
            # Mapeia a suavização para o intervalo de 0 a 255
            intensidade = int(255 * suavizacao / MAX_ITERATIONS)
            
            # Gera uma cor suavizada
            cor = (intensidade, intensidade, intensidade)
            line.append(cor)
        image_data.append(line)

# Função para calcular o Conjunto de Mandelbrot
def mandelbrot(c):
    z = 0
    n = 0
    while abs(z) <= 2 and n < MAX_ITERATIONS:
        z = z*z + c
        n += 1
    return n

# Função para gerar uma imagem do Conjunto de Mandelbrot
def image_generator(index, xmin, xmax, ymin, ymax):
    global image_data, diretorio_de_saida
    image_data = []  # Reset image_data for each call
    image_data_generator(index, n_img)

    # Criar uma nova imagem
    imagem = Image.new("RGB", (image_width, image_height), "black")

    # Preencher a imagem com os dados gerados
    for y in range(image_height):
        for x in range(image_width):
            # Mapeia as coordenadas do pixel para o plano complexo
            zx = xmin + (x / (image_width - 1)) * (xmax - xmin)
            zy = ymin + (y / (image_height - 1)) * (ymax - ymin)
            c = complex(zx, zy)
            # Verifica se o ponto pertence ao conjunto de Mandelbrot
            cor = mandelbrot(c)
            # Mapeia o número de iterações para uma cor
            imagem.putpixel((x, y), (cor % 256, (cor * 2) % 256, (cor * 3) % 256))

    # Nome do arquivo com base no índice
    nome_arquivo = f"img_{index}.png"
    caminho_imagem = os.path.join(diretorio_de_saida, nome_arquivo)
    
    # Salvar a imagem
    imagem.save(caminho_imagem)


# Criar o diretório de saída e obter seu nome
diretorio_de_saida = create_output_directory()

# Variáveis globais
MAX_ITERATIONS = 100
image_data = []
image_width = 200
image_height = 200
n_img = 500
Delta = 0.005
x = 2
y = 2
exp = 1 #exponent


# Executar a geração de imagens
for i in range(n_img):
    xmin = -x + i * (Delta ** exp)
    xmax = x - i * (Delta ** exp)
    ymin = -y + i * (Delta ** exp)
    ymax = y - i * (Delta ** exp)
    image_generator(i, xmin, xmax, ymin, ymax)