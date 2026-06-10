# Help-CLI

O **Help-CLI** é uma ferramenta de linha de comando (CLI) focada em produtividade, organização automática de arquivos e manutenção de espaço em disco.

## 🚀 Funcionalidades

Atualmente, o projeto conta com duas ferramentas principais:

### 1. `mapping`
Organiza arquivos em pastas específicas com base em suas extensões.
- **Flexibilidade de Caminho**: Permite especificar a pasta alvo com `--caminho` ou `-c`.
- **Validação Robusta**: Verifica a existência e integridade do diretório antes de operar.
- **Confirmação de Segurança**: Solicita permissão explícita mostrando a pasta afetada.
- **Preservação de Arquivos**: Ignora scripts Python, arquivos Git, README e arquivos de sistema.

#### Categorias de Organização:
- **Documentos**: `.pdf`, `.docx`, `.txt`, `.xlsx`
- **Imagens**: `.jpg`, `.jpeg`, `.png`, `.gif`
- **Executáveis**: `.exe`, `.msi`
- **Vídeos**: `.mp4`, `.mkv`
- **Outros**: Extensões não mapeadas.

### 2. `compact`
Identifica, compacta em um arquivo `.zip` e remove arquivos antigos para liberar espaço.
- **Flexibilidade de Caminho**: Agora também permite especificar a pasta alvo com `--caminho` ou `-c`.
- **Parâmetro de Tempo**: Defina o limite de dias com `--dias` ou `-d` (padrão: 90 dias).
- **Segurança**: Solicita confirmação antes de apagar qualquer arquivo, indicando a pasta alvo.
- **Inteligência**: Ignora arquivos ocultos, scripts Python e arquivos ZIP já existentes.

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
# --- Organização (mapping) ---
# Na pasta atual:
help_cli mapping
# Em uma pasta específica:
help_cli mapping -c "C:/Sua/Pasta"

# --- Limpeza (compact) ---
# Na pasta atual (arquivos com + de 90 dias):
help_cli compact
# Em uma pasta específica com limite de 30 dias:
help_cli compact -c "C:/Sua/Pasta" -d 30
```

## 📂 Estrutura do Projeto

- `help_cli/`: Pacote principal contendo o código-fonte.
  - `main.py`: Implementação dos comandos utilizando a biblioteca `typer`.
- `setup.py`: Script de configuração para instalação e definição do ponto de entrada da CLI.
- `.gitignore`: Configurado para ignorar caches, ambientes virtuais e artefatos de build.

## 🚧 Status do Projeto

O Help-CLI está em desenvolvimento ativo. O foco atual é manter a consistência entre os comandos e expandir as capacidades de automação.
