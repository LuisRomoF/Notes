#%%
import pandas as pd

data_1 = {'product': ['computer','monitor','printer','desk','lamp'],
                   'price': [900,800,200,350,200]
                   }
data_f1 = pd.DataFrame(data_1)


data_2 = {'product': ['computer','monitor','printer','desk'],
                    'price': [900,800,200,350]
                    }
data_f2 = pd.DataFrame(data_2)


#%%
def Validate(df1,df2):

    if df1.shape==df2.shape:
        print(f'Dataframes have the same shape: {df1.shape}')
    else:
        print(f'Dataframes have different shapes:\n Dataframe 1: {df1.shape}\n Dataframe 2: {df2.shape}')
    
    df_dscrb_1 = df1.describe(include='all',datetime_is_numeric=True)
    df_dscrb_2 = df2.describe(include='all',datetime_is_numeric=True)

    df_dscrb_1 = df1.describe(include='all',datetime_is_numeric=True)
    df_dscrb_2 = df2.describe(include='all',datetime_is_numeric=True)   

    if df_dscrb_1.equals(df_dscrb_2):
        return 'True: Dataframes have the same data'

    else:
        return 'False: Dataframes do not have the same data'

Validate(data_f1,data_f2)

#%%
df_dscrb_1 = data_f1.describe(include='all',datetime_is_numeric=True)
df_dscrb_2 = data_f2.describe(include='all',datetime_is_numeric=True)

df_match = pd.DataFrame()

for col in df_dscrb_1.columns:
    for row in range(len(df_dscrb_1.index)):
        if df_dscrb_1[col][row] == df_dscrb_2[col][row]:
            df_match[col] = 'True'
            
        else:
            df_match[col] = 'False'
            print(f'Data frames do not match on column: {col} row: {row}')
            break