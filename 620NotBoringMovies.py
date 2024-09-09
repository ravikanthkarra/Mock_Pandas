import pandas as pd


def not_boring_movies(cinema: pd.DataFrame) -> pd.DataFrame:
    # result = []
    # for i in range(len(cinema)):        
    #     id = cinema['id'][i]
    #     desc = cinema['description'][i]
    #     if id % 2 == 1 and desc != 'boring':
    #         result.append([id, cinema['movie'][i], desc, cinema['rating'][i]])

    # # print(result[0])
    # return pd.DataFrame(result, columns=['id','movie','description','rating'])
    result = cinema[(cinema['id'] % 2 == 1) & (cinema['description'] != 'boring')]
    result = result[['id', 'movie', 'description', 'rating']]
    return result.sort_values(by='rating', ascending=False)