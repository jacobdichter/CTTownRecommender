import pandas as pd

df = pd.read_csv("ct_place_medianage.csv")
ct_towns = pd.read_csv("ct_towns_only.csv", header=None)

print(df.head())

print(df.shape)

new_df = []
relevant_index = 0

for index, row in df.iterrows():
    if index == relevant_index:
        new_df.append(row)
        relevant_index += 4


new_df = pd.DataFrame(new_df)
print(new_df.head())

new_df.drop(columns=['Label'], inplace=True)
print(new_df.head())
print(new_df.columns)

outfile = 'modified_medianage.csv'
# new_df.to_csv(outfile)

print(ct_towns.head())

new_df['Match'] = ct_towns.iloc[:,0].isin(new_df['Place'])

new_df.to_csv(outfile)
