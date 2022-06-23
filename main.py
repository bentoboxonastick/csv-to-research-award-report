import pandas


df = pandas.read_csv('files/april-2022.csv')


total_index = df.columns.get_loc("Total")
df[df.columns[total_index:]] = df[df.columns[total_index:]].replace('[\$,]', '', regex=True).astype(float)


row_index = 0
while row_index <= len(df.index) - 1:
    row = df.iloc[[row_index]]
    total = row.loc[row_index, "Total"]

    if isinstance(total, float) and not pandas.isna(total):
        if total >= 150000.0:
            desc = row.loc[row_index, "Title"]
            fname = row.loc[row_index, "Lead PI First Name"]
            lname = row.loc[row_index, "Lead PI Last Name"]
            dept = row.loc[row_index, "PI Home Department"]
            sponsor = row.loc[row_index, "Sponsor"]
            print("Amount: " + str(total))
            print("Name: " + fname + " " + lname)
            print("Department: " + dept)
            print("Sponsor: " + sponsor)
            print("Title: " + desc)
            print(" ")
    
    row_index += 1
