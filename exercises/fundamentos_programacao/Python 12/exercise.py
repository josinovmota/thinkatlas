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
        if produto not in dict_product_value.keys():
            dict_product_value.update({produto: valor})
        else:
            dict_product_value[produto] = int(dict_product_value[produto]) + int(valor)

    return dict_product_value

def total_sales_by_product(dict_product_value):
    [print(f"Produto {product}: {dict_product_value[product]} Unidades Vendidas") for product in dict_product_value]

def best_seller(dict_product_value):
    pass

if __name__ == "__main__":
    data = "exercises\\fundamentos_programacao\\Python 12\\vendas.csv"
    almost_df = deserialize(data)

    sales_df = create_sales_df(almost_df)

    total_sales_by_product(sales_df)

    best_seller(sales_df)
