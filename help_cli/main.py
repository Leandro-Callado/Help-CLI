import typer
from pathlib import Path
import shutil
import zipfile
import datetime

# Inicializa o app do Typer
app = typer.Typer()

@app.command()
def mapping(
    caminho: Path = typer.Option(
        Path.cwd(), 
        "--caminho", "-c", 
        help="Caminho da pasta que será organizada. O padrão é a pasta atual."
    )
):
    """
    Organiza a pasta separando os arquivos por extensão.
    (ex: help-cli mapping --caminho "C:/Users/SeuUsuario/Downloads")
    """
    # 1. Garante que o caminho é absoluto (completo) e resolve atalhos
    pasta_alvo = caminho.resolve()

    # 2. Nova Trava de Segurança: Verifica se o caminho digitado realmente existe e é uma pasta
    if not pasta_alvo.exists() or not pasta_alvo.is_dir():
        print(f"Erro: O diretório '{pasta_alvo}' não existe ou é inválido.")
        raise typer.Abort()

    rules = {
        "Documentos": [".pdf", ".docx", ".txt", ".xlsx"],
        "Imagens": [".jpg", ".jpeg", ".png", ".gif"],
        "Executaveis": [".exe", ".msi"],
        "Videos": [".mp4", ".mkv"]
    }

    arquivos_ignorados = [".gitignore", "README.md", "requirements.txt", "LICENSE"]

    print(f"Scanning through folder: {pasta_alvo}\n")

    # Atualizamos a mensagem de confirmação para mostrar a pasta exata que será afetada
    confirmacao = typer.confirm(f"Você tem certeza que deseja organizar os arquivos de '{pasta_alvo.name}'?")
    if not confirmacao:
        print("Operação cancelada. Nenhum arquivo foi movido.")
        raise typer.Abort()

    for arquivo in pasta_alvo.iterdir():
        if arquivo.is_file() and arquivo.suffix != ".py" and arquivo.name not in arquivos_ignorados:
            
            extensao = arquivo.suffix.lower()
            pasta_destino = "Outros" 

            for categoria, mapped_extensions in rules.items():
                if extensao in mapped_extensions:
                    pasta_destino = categoria   
                    break
                    
            caminho_destino = pasta_alvo / pasta_destino
            caminho_destino.mkdir(exist_ok=True)

            print(f"Movendo: {arquivo.name} ---> [{pasta_destino}]")
            shutil.move(str(arquivo), str(caminho_destino / arquivo.name))
            
    print("\nOrganização concluída com sucesso!")

@app.command()
def compact(dias: int = 90):
    """
    Zipa e apaga arquivos que não são modificados há mais de X dias (Padrão: 90).
    (ex: help-cli compact --dias 30)
    """
    pasta_alvo = Path.cwd()
    agora = datetime.datetime.now()
    
    # Calcula a data limite subtraindo os dias informados da data de hoje
    limite_tempo = agora - datetime.timedelta(days=dias)
    
    arquivos_para_zipar = []
    
    print(f"Buscando arquivos intocados desde {limite_tempo.strftime('%d/%m/%Y')}...\n")
    
    # 1. Varredura e Filtro de Tempo
    for arquivo in pasta_alvo.iterdir():
        # Ignora pastas, o próprio script, arquivos ocultos (como .gitignore) e outros zips
        if arquivo.is_file() and not arquivo.name.startswith('.') and arquivo.suffix not in [".py", ".zip"]:
            
            # Extrai a data de modificação (st_mtime) e converte para um formato legível
            data_modificacao = datetime.datetime.fromtimestamp(arquivo.stat().st_mtime)
            
            if data_modificacao < limite_tempo:
                arquivos_para_zipar.append(arquivo)
    
    if not arquivos_para_zipar:
        print(f"Nenhum arquivo mais velho que {dias} dias foi encontrado aqui.")
        return

    print(f"Encontrados {len(arquivos_para_zipar)} arquivos antigos.")
    
    # 2. Trava de Segurança
    confirmacao = typer.confirm("Deseja compactar esses arquivos e APAGAR os originais para liberar espaço?")
    if not confirmacao:
        raise typer.Abort()
        
    # 3. Criando o arquivo ZIP
    # Dá um nome único usando a data atual (ex: arquivo_morto_20260609.zip)
    nome_zip = pasta_alvo / f"arquivo_morto_{agora.strftime('%Y%m%d')}.zip"
    
    # ZIP_DEFLATED é o algoritmo padrão de compressão para diminuir o tamanho
    with zipfile.ZipFile(nome_zip, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for arquivo in arquivos_para_zipar:
            print(f"Empacotando: {arquivo.name}")
            zipf.write(arquivo, arquivo.name)
            
            # 4. Apaga o arquivo original (unlink é o equivalente moderno do os.remove)
            arquivo.unlink()
            
    print(f"\nLimpeza pesada concluída! Arquivos salvos com segurança em: {nome_zip.name}")

# Ponto de entrada do CLI
if __name__ == "__main__":
    app()