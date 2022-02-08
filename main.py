from table import Table
from collections import Counter
import pandas as pd

round_results = []
for round in range(200):
    table = Table()
    sim_results = []
    previous_win = True

    for _ in range(150):
        #if previous_win:
        #    bet = BET
        #else:
        #    bet = bet * 2

        table.deal(table.dealer)
        table.deal(table.player1)
        table.play_out(table.player1)
        table.play_out(table.dealer)
        table.evaluate(table.dealer, table.player1)
        #if table.results != 'Player Win':
        #    previous_win = False
        #else:
        #    previous_win = True
        table.deck.reset()
        sim_results.append(table.results)
        #print(table.results, bet, table.player1.wallet)

    round_results.append(table.player1.wallet)

rr_df = pd.DataFrame(round_results)
rr_df[0].plot.hist(grid=True, bins=30)

sum(round_results)

#print(table.player1.wallet)

#Counter(sim_results)