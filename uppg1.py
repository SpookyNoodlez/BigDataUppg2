import pandas as pd

topGames = {'Top selling games': ['Minecraft','Grand Theft Auto V', 'Tetris', 'Wii Sports', 'PlayerUnknowns Battlegrounds'],
        'Sales': [200000000, 135000000, 100000000, 82900000, 70000000]
        }

df = pd.DataFrame(topGames, columns = ["Top selling games", "Sales"])

print(df)

print("\n\n")

#Printar raden med index 1
print(df.iloc[[1]])

print("\n\n")

#Printar raden med index 3
print(df.iloc[[3]])