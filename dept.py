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
  [13, 'Marseille'],
  [14, 'Caen'],
  [15, 'Aurillac'],
  [16, 'Angoulême'],
  [17, 'La Rochelle'],
  [18, 'Bourges'],
  [19, 'Tulle'],
  ['2A', 'Ajaccio'],
  ['2B', 'Bastia'],
  [21, 'Dijon'],
  [22, 'Saint-Brieuc'],
  [23, 'Guéret']
      ]

# Create the pandas DataFrame
df = pd.DataFrame(data, columns=['numDep', 'pref'])

# print dataframe.
print(df)
