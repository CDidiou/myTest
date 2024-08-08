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
  [8, 'Charleville-Mézières']
      ]

# Create the pandas DataFrame
df = pd.DataFrame(data, columns=['numDep', 'pref'])

# print dataframe.
print(df)
