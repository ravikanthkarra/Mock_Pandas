import pandas as pd


def sales_analysis(product: pd.DataFrame, sales: pd.DataFrame) -> pd.DataFrame:
    result = sales[(sales['sale_date'] < '2019-01-01') | (sales['sale_date'] > '2019-03-31')]
    # print(result)
    product1 = product[product['product_id'].isin(sales['product_id'])]
    print(product1)
    result = product1[~product1['product_id'].isin(result['product_id'])]
    # print(result)
    # result = result.merge(product, left_on = 'product_id', right_on = 'product_id', how = 'left')
    return result[['product_id', 'product_name']]
    return product
