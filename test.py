import pandas as pd
df = pd.read_excel('Historical Alarm Cases.xlsx')
print(df.drop['Case No.', 'Unnamed: 8', 'Unnamed: 9', 'Unnamed: 10'],axis=1,inplace=True)