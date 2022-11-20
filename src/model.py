import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.impute import SimpleImputer

def build_and_predict(train_data, test_data):
  rf = RandomForestClassifier()
  
  labels = train_data['summary_date']
  features = train_data.drop(columns = ['summary_date'])
  
  rf.fit(features, labels)
  
  predictions = rf.predict(test_data)
  
  out = pd.concat([pd.Series(predictions), y_test], axis=1)

  out.to_csv("predictions")

  return out
   
  
