import pandas as pd

csv_data = pd.read_csv('booksummaries.csv', sep='\t')

for index, row in csv_data.iterrows():
    # Row is current row,
    for i in row:
        # Iterating row items from first to last.
        # i is current row item 
        print(i, end=" ")
    print("\n")
