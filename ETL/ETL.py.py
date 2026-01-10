import pandas as pd
from sqlalchemy import create_engine
from urllib.parse import quote_plus

try:
    df = pd.read_csv(r'C:\Users\indur\OneDrive\Desktop\depolyment projects\zomato_project\govinda\clean.csv')
    print('loaded')

    user = 'root'
    password = quote_plus('induri@05')
    host = 'localhost'
    database = 'churn'

    engine = create_engine(f'mysql+pymysql://{user}:{password}@{host}/{database}')

    df.to_sql('clean',con=engine,if_exists='replace')
    print('sucessfully we loaded to data dase')
except:
    print('error??????????????????????????????:')
finally:
    print('ETL PROCESS DONE:::::::::::::::::::::::::::::')

