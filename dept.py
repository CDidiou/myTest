# Import pandas library
import pandas as pd

# initialize list of lists
data = [
  [1, 'Bourg-en-Bresse'],
  [2, 'Laon'],
  [3, 'Moulins'],
  [4, 'Digne-les-Bains'],
  [5, 'Gap'],
  [6, 'Nice'],
  [7, 'Privas'],
  [8, 'Charleville-Mézières'],
  [9, 'Foix'],
  [10, 'Troyes'],
  [11, 'Carcassonne'],
  [12, 'Rodez'],
  [13, 'Marseille']
      ]

# Create the pandas DataFrame
df = pd.DataFrame(data, columns=['numDep', 'pref'])

# print dataframe.
print(df)
