import csv

lista_legal = ["data","produto","categoria","quantidade","preco_unitario","vendedor","regiao"]
dict_legal = {"data": [],"produto": [],"categoria": [],"quantidade": [],"preco_unitario": [],"vendedor": [],"regiao": []}

def deserialize(data):
    with open(data, "r", encoding="utf-8") as df:
        test = csv.reader(df)
        
        for lista in list(test)[1:]:
            [dict_legal[chave].append(valor) for chave, valor in zip(lista_legal, lista)]

    return dict_legal

def create_sales_df(df):
    lista_produtos = df["produto"]
    lista_quantidades = df["quantidade"]
    dict_product_value = {}

    for produto, valor in zip(lista_produtos, lista_quantidades):
        if produto not in dict_product_value:
            dict_product_value.update({produto: valor})
        else:
            dict_product_value[produto] = int(dict_product_value[produto]) + int(valor)

    return dict_product_value

def total_sales_by_product(dict_product_value):
    [print(f"Produto {product}: {dict_product_value[product]} Unidades Vendidas") for product in dict_product_value]

def best_seller(dict_product_value):
    produto_mais_vendido = ('UAU', 0)

    for produto in dict_product_value.items():
        if produto[1] > produto_mais_vendido[1]:
            produto_mais_vendido = produto

    print(f"\nO produto mais vendido foi {produto_mais_vendido[0]} com {produto_mais_vendido[1]} vendas\n")

def best_month(almost_df):
    months = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
    index_dict = {month: [] for month in months}
    products_by_month_dict = {}

    for month in months:
        for date in almost_df['data']:
            if date[5:7] == month:
                index_dict[month].append(almost_df['data'].index(date))

    for month, value in index_dict.items():
        if value:
            placeholder_dict = {"produto": [], "quantidade": []}
            for index in value:
                placeholder_dict["produto"].append(almost_df["produto"][index])
                placeholder_dict["quantidade"].append(almost_df["quantidade"][index])
            products_by_month_dict[month] = placeholder_dict
                
    # ESQUEÇA TUDO ACIMA, SÓ CONFIA

    best_sales_month = ['01', 0]
    best_sales_placeholder = ['01', 0]

    for month in products_by_month_dict:
        for number in products_by_month_dict[month]['quantidade']:
            best_sales_placeholder[1] += int(number)
        if best_sales_placeholder[1] > best_sales_month[1]:
            best_sales_month = best_sales_placeholder
        best_sales_placeholder = ['01', 0]

    # CONFIA

    print(f"O melhor mês foi o {best_sales_month[0]} com {best_sales_month[1]} vendas")

if __name__ == "__main__":
    data = "exercises\\fundamentos_programacao\\Python 12 ( Gerador Relatorio )\\vendas.csv"
    almost_df = deserialize(data)

    sales_df = create_sales_df(almost_df)

    # calcular total por categoria
    total_sales_by_product(sales_df)
    # produto mais vendido
    best_seller(sales_df)
    # mês de pico e percentual de cada categoria
    best_month(almost_df)
