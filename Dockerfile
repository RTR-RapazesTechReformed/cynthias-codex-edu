# Use a imagem oficial do Python como base
FROM python:3.10-slim

RUN apt-get update && apt-get install -y \
    build-essential \
    default-libmysqlclient-dev \
    pkg-config \
    && rm -rf /var/lib/apt/lists/*

# Define o diretório de trabalho dentro do contêiner
WORKDIR /app

# Copia o arquivo de requisitos para o diretório de trabalho
COPY requirements.txt .

# Instala as dependências do projeto
RUN pip install --no-cache-dir -r requirements.txt

# Copia o restante do código do projeto para o diretório de trabalho
COPY . .

# Define a variável de ambiente para o Django
ENV DJANGO_SETTINGS_MODULE=CynthiasCodex.settings

# Expõe a porta que o Django usará
EXPOSE 80

# Comando para rodar as migrações e iniciar o servidor
CMD ["sh", "-c", "python manage.py migrate && python manage.py makemigrations && python manage.py collectstatic --no-input
&& python manage.py runserver 0.0.0.0:80"]
