import pandas as pd


def biggest_single_number(my_numbers: pd.DataFrame) -> pd.DataFrame:
    result = my_numbers.groupby('num').size().reset_index().rename(columns={0: 'cnt'})
    result = result[(result['cnt'] == 1)].max()
    result = pd.DataFrame([result[0]], columns=['num'])
    return result
