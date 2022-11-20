import os
import pandas as pd
from sklearn.impute import SimpleImputer

def get_data(datadir):
    '''
    load and clean the training data
    '''
    file_path = os.path.join(datadir, 'patient_3_sleep.csv')
    
    data = pd.read_csv(file_path) #check to make sure it ends in .csv
    labels = data['summary_date'].apply(pd.to_datetime).dt.day_name()
    data = data.drop(columns = ['timestamp', 'hypnogram_5min', 'summary_date', 'rmssd', 'type'])
    data_cols = data.columns
    imp_mean = SimpleImputer(missing_values=np.nan, strategy='mean')
    imp_mean.fit(data)
    data = imp_mean.transform(data)
    data = pd.DataFrame(data, columns = data_cols)
    
    return pd.concat([data, labels], axis = 1)
  
  
def read_test(datadir):
    '''
    Reads raw test data from disk.
    (Would normally be more complicated!)
    '''

    fp = os.path.join(datadir, 'test.csv')
    return pd.read_csv(fp)
    
