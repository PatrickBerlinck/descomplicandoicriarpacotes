"""
setup.py: Script para configurar e empacotar o projeto para distribuição no PyPI.
"""
import setuptools

# Lendo o conteúdo do README.md para a descrição longa
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    # Nome do pacote no PyPI
    name="grimaud_calculator",
    # Versão do seu pacote
    version="0.1.0",
    # Autor do pacote
    author="Seu Nome", # Substitua pelo seu nome
    # E-mail do autor
    author_email="seu.email@example.com", # Substitua pelo seu e-mail
    # Breve descrição do pacote
    description="Uma calculadora simples com operações básicas.",
    # Descrição longa lida do README.md
    long_description=long_description,
    # Formato da descrição longa (geralmente Markdown)
    long_description_content_type="text/markdown",
    # URL do seu repositório GitHub (opcional, mas recomendado)
    url="https://github.com/seu-usuario/grimaud-calculator", # Substitua pela URL do seu projeto no GitHub
    # Lista de pacotes a serem incluídos na distribuição
    packages=setuptools.find_packages(),
    # Classificadores que ajudam os usuários a encontrar seu pacote
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 3 - Alpha", # Ex: 3 - Alpha, 4 - Beta, 5 - Production/Stable
        "Topic :: Utilities",
        "Topic :: Scientific/Engineering :: Mathematics",
    ],
    # Versão mínima do Python necessária
    python_requires='>=3.6',
    # Ponto de entrada para scripts de linha de comando (opcional)
    # entry_points={
    #     'console_scripts': [
    #         'grimaudcalc=grimaud_calculator.calculator:calculate',
    #     ],
    # },
)
