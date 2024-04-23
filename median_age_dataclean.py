import pandas as pd

df = pd.read_csv("DATASET/median_age_dirty.csv", header=None)

print(df.head())
print(df.shape)
print(type(df.shape))

median_age = []

mage_cleaned = []

for index, row in df.iterrows():
    if row.values[0] != '#VALUE!':
        mage_cleaned.append(list((row.values)))

print(type(mage_cleaned[0]))
print(mage_cleaned)


    # print(row.values)
    # if index == 0:
    #     median_age.append(row)

#     if index == relevant_index:
#         median_age.append(row)
#         relevant_index += 10



outfile = 'medianage_cleaned.csv'

mage_cleaned_df = pd.DataFrame(mage_cleaned)
print(type(mage_cleaned_df))
mage_cleaned_df.to_csv(outfile)