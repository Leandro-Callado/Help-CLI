import typer
from pathlib import Path
import shutil

# Inicializa o app do Typer
app = typer.Typer()

@app.command()
def ola(name: str):
    """
    Comando simples para dizer olá (ex: python cli.py ola Leandro)
    """
    print(f"Olá {name}")

@app.command()
def mapping():
    """
    Organiza a pasta atual separando os arquivos por extensão.
    (ex: python main.py mapping)
    """
    pasta_alvo = Path.cwd()
    rules = {
        "Documentos": [".pdf", ".docx", ".txt", ".xlsx"],
        "Imagens": [".jpg", ".jpeg", ".png", ".gif"],
        "Executaveis": [".exe", ".msi"],
        "Videos": [".mp4", ".mkv"]
    }

    # 1. Lista de arquivos sagrados que NUNCA devem ser movidos
    arquivos_ignorados = [".gitignore", ".md", "requirements.txt", "LICENSE"]

    print(f"Scanning through current folder: {pasta_alvo.absolute()}\n")

    # 2. Trava de segurança nativa do Typer
    confirmacao = typer.confirm("Você tem certeza que deseja organizar os arquivos desta pasta?")
    if not confirmacao:
        print("Operação cancelada. Nenhum arquivo foi movido.")
        raise typer.Abort() # Interrompe a execução

    for arquivo in pasta_alvo.iterdir():
        # 3. Adicionamos a verificação dos arquivos ignorados na condição
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
    
# Ponto de entrada do CLI
if __name__ == "__main__":
    app()