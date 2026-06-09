# Help-CLI

O **Help-CLI** é uma ferramenta de linha de comando (CLI) projetada para automatizar tarefas simples e organizar arquivos de forma eficiente. O projeto foi recentemente reestruturado como um pacote Python instalável.

## 🚀 Funcionalidades

A CLI fornece os seguintes comandos:

- **`ola`**: Um comando simples que recebe um nome e retorna uma saudação.
- **`mapping`**: Organiza automaticamente os arquivos no diretório atual, movendo-os para pastas categorizadas por extensão.
  - **Segurança**: Inclui uma solicitação de confirmação antes de iniciar a movimentação.
  - **Filtros**: Ignora automaticamente arquivos de sistema e configuração como `.py`, `.gitignore`, `.md`, `requirements.txt` e `LICENSE`.

### Categorias de Organização:
- **Documentos**: `.pdf`, `.docx`, `.txt`, `.xlsx`
- **Imagens**: `.jpg`, `.jpeg`, `.png`, `.gif`
- **Executáveis**: `.exe`, `.msi`
- **Vídeos**: `.mp4`, `.mkv`
- **Outros**: Arquivos com extensões não mapeadas.

## 🛠️ Instalação e Uso

Como o projeto agora é um pacote, você pode instalá-lo localmente para usar o comando `help_cli` de qualquer lugar no seu terminal.

### 1. Instalação Local (Modo Editável)
No diretório raiz do projeto, execute:
```bash
pip install -e .
```

### 2. Como Usar
Após a instalação, você pode chamar a ferramenta diretamente pelo nome definido no `setup.py`:

```bash
# Saudação
help_cli ola "Seu Nome"

# Organização de arquivos
help_cli mapping
```

## 📂 Estrutura do Projeto

- `help_cli/`: Diretório principal do pacote.
  - `main.py`: Contém a lógica dos comandos da CLI.
- `setup.py`: Configuração de instalação do pacote.

## 🚧 Status do Projeto

Este projeto está em constante evolução. A reestruturação para pacote permite uma distribuição mais fácil e melhor organização do código.
