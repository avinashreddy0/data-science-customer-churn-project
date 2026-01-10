import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')

from sklearn.preprocessing import OrdinalEncoder,LabelEncoder,StandardScaler
from sklearn.model_selection import train_test_split,cross_val_score
from sklearn.ensemble import AdaBoostClassifier
from sklearn.metrics import accuracy_score,roc_auc_score,recall_score,precision_score
from imblearn.over_sampling import SMOTE
import shap
import joblib

#loading data set 

df = pd.read_csv(r'C:\Users\indur\OneDrive\Desktop\depolyment projects\zomato_project\govinda\clean.csv')
print(df.to_string())
print(df.head())

#preprocessing

encoder_gender = OrdinalEncoder()
df[['gender']] = encoder_gender.fit_transform(df[['gender']])
encoder_city = OrdinalEncoder()
df[['city']] = encoder_city.fit_transform(df[['city']])

#feature and target

x = df[['age','gender','city','total_orders','total_revenue','days_since_last_order']]
y = df['churn']

#standard scaler

scaler = StandardScaler()
x_feature = scaler.fit_transform(x)


#train_test_split 

x_train,x_test,y_train,y_test = train_test_split(x_feature,y,test_size=0.2,random_state=42)

#SMOTE

smote = SMOTE(random_state=42)
x_train_smote,y_train_smote = smote.fit_resample(x_train,y_train)

#model

model = AdaBoostClassifier()
model.fit(x_train,y_train)
y_pred = model.predict(x_test)
print('predication_value:',y_pred)
y_pred_prob = model.predict_proba(x_test)
print('y_pred_prob:',y_pred_prob)

#evalution 

print('accuracy_score_value:',accuracy_score(y_test,y_pred))
print('precision_score:',y_test,y_pred)
print('recall_score:',y_test,y_pred)
print('roc_auc_score:',y_test,y_pred_prob)

#cross_val_score 

cross_val_scores = cross_val_score(model,x,y,cv=5)
print('cross_val_score:',cross_val_score)

#saving

joblib.dump(model,'customer_churn.pkl')
joblib.dump(encoder_gender,'gender.pkl')
joblib.dump(encoder_city,'city.pkl')
joblib.dump(scaler,'scaking.pkl')
