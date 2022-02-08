import pandas as pd

hit_df = pd.read_csv('hit_strategy.csv', header=None)
hit_df.columns = ['score','hit']

hit_dict = hit_df.to_dict()['hit']

bet_df = pd.read_csv('bet_strategy.csv', header=None)
bet_df.columns = ['score','bet']

bet_dict = bet_df.to_dict()['bet']