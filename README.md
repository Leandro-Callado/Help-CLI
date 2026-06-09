# Help-CLI

O **Help-CLI** é uma ferramenta de linha de comando (CLI) focada em produtividade, organização automática de arquivos e manutenção de espaço em disco.

## 🚀 Funcionalidades

Atualmente, o projeto conta com duas ferramentas principais:

### 1. `mapping`
Organiza automaticamente o diretório onde o comando é executado, movendo arquivos para pastas específicas com base em suas extensões.
- **Confirmação de Segurança**: Solicita permissão antes de realizar qualquer alteração.
- **Preservação de Arquivos**: Ignora automaticamente arquivos críticos como scripts Python (`.py`), configurações do Git (`.gitignore`), documentação (`.md`), e arquivos de licença ou requisitos.

#### Categorias de Organização:
- **Documentos**: `.pdf`, `.docx`, `.txt`, `.xlsx`
- **Imagens**: `.jpg`, `.jpeg`, `.png`, `.gif`
- **Executáveis**: `.exe`, `.msi`
- **Vídeos**: `.mp4`, `.mkv`
- **Outros**: Extensões não mapeadas.

### 2. `compact`
Identifica, compacta em um arquivo `.zip` e remove arquivos que não foram modificados há um determinado número de dias. Ideal para realizar "limpezas pesadas" e liberar espaço.
- **Parâmetro de Tempo**: Permite definir o limite de dias (padrão é 90 dias).
- **Segurança**: Solicita confirmação antes de compactar e apagar os arquivos originais.
- **Inteligência**: Ignora arquivos ocultos, scripts Python e outros arquivos ZIP para evitar recursividade ou perda de dados essenciais.

## 🛠️ Instalação e Uso

O projeto está estruturado como um pacote Python, facilitando a instalação e o uso global.

### 1. Instalação Local
No diretório raiz do projeto, instale em modo editável:
```bash
pip install -e .
```

### 2. Como Utilizar
Após instalado, utilize os comandos diretamente no terminal:

```bash
# Organizar a pasta atual por extensão
help_cli mapping

# Compactar arquivos não modificados há mais de 90 dias (padrão)
help_cli compact

# Compactar arquivos não modificados há mais de 30 dias
help_cli compact --dias 30
```

## 📂 Estrutura do Projeto

- `help_cli/`: Pacote principal contendo o código-fonte.
  - `main.py`: Implementação dos comandos utilizando a biblioteca `typer`.
- `setup.py`: Script de configuração para instalação e definição do ponto de entrada da CLI.
- `.gitignore`: Configurado para ignorar caches, ambientes virtuais e artefatos de build.

## 🚧 Status do Projeto

O Help-CLI está em desenvolvimento ativo. O foco atual é adicionar mais ferramentas de utilidade diária e melhorar a robustez das operações de arquivo.
