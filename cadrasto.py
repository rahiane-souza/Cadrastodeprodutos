def formatar_nome(nome):
    return nome.strip().title()

def cadrastrar_produto():
    nome = input("digite o nome do produto:")
    preco = float(input("digite o preço do produto:"))
    categoria = input("digite a categoria do produto:")
    return (formatar_nome(nome),preco,categoria)

  def salva_produto(produto):
    with open("produto.txt", "a", encoding="utf-8") as arquivos:
         linha = f"{produto[0]};{produto[1]};{produto[2]}\n"
         arquivo.write(linha)

def listar_produtos():
    try:
        with open("produtos.txt", "r", encoding="uf-8") as arquivos:
            for linha in arquivo:
                nome, preco, categoria = linha.strip()

    
