### Fractal e Gerador de Imagens

Este repositório contém um projeto em desenvolvimento para a criação de imagens fractais e a geração de imagens com cores aleatórias usando Python e a biblioteca PIL (Python Imaging Library).

#### Funcionalidades

- **Geração de Imagens**: Cria imagens com dimensões especificadas e preenche com cores aleatórias.
- **Manipulação de Pixels**: Permite a manipulação de pixels específicos antes de salvar a imagem.
- **Salvamento em Diretório**: As imagens geradas são salvas em um diretório específico com um timestamp e número aleatório para organização.

#### Estrutura do Projeto

- **`main.py`**: Script principal que gera e salva as imagens.
- **`Output/`**: Diretório onde as imagens geradas são salvas.

#### Como Usar

1. Clone o repositório:
    ```bash
    git clone https://github.com/gabrieljsantos/Fractal.Image-Generator.git
    cd Fractal.Image-Generator
    ```

2. Instale as dependências necessárias:
    ```bash
    pip install pillow
    ```

3. Execute o script principal:
    ```bash
    python Fractal.py
    ```

4. As imagens geradas serão salvas no diretório `Output`.

#### Estrutura do Código

```python
from PIL import Image, ImageDraw
import os
import random
import datetime

def create_output_directory():
    # Obter o tempo atual
    tempo_atual = datetime.datetime.now()
    print(f"Tempo atual: {tempo_atual}")

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
    print(f"Imagem {index} salva como {caminho_imagem}")

for i in range(n_img):
    image_generator(i)
```

#### Status do Projeto

🚧 **Em Desenvolvimento** 🚧

Este projeto está em desenvolvimento ativo. Feedbacks e contribuições são bem-vindos!

#### Contribuição

1. Faça um fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/nova-feature`)
3. Commit suas mudanças (`git commit -m 'Adiciona nova feature'`)
4. Envie para o repositório remoto (`git push origin feature/nova-feature`)
5. Abra um Pull Request

#### Licença

Este projeto está licenciado sob a Licença MIT. Veja o arquivo `LICENSE` para mais detalhes.

#### Contato

Para mais informações, entre em contato com o desenvolvedor.