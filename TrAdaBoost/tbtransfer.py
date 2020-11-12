import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn import decomposition
import TrAdaBoost
from sklearn.ensemble import AdaBoostClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn import svm
from sklearn import feature_selection
from sklearn import model_selection
from sklearn import metrics




import numpy as np




def append_feature(dataframe,istest):
    lack_num=np.asarray(dataframe.isnull().sum(axis=1))
    if istest:
        X=dataframe.values
        X=X[:,1:X.shape[1]]
    else:
        X=dataframe.values
        X=X[:,1:X.shape[1]]
    total_S=np.sum(X,axis=1)
    var_S=np.var(X,axis=1)
    X=np.c_[X,total_S]
    X=np.c_[X,var_S]
    X=np.c_[X,lack_num]
    
    return X
        




train_df=pd.DataFrame(pd.read_csv("/Users/b-byr/Desktop/Training Dataset/Home/CSVs/allhome.csv"))
train_df.drop(['Flow ID','Dst IP','Src Port', 'Dst Port','Src IP','Timestamp'], axis=1, inplace=True)
train_df["Flow Duration"] = np.log((train_df["Flow Duration"] + 0.1).astype(float)) 
train_df.fillna(value=-99999)

train_df1=pd.DataFrame(pd.read_csv("/Users/b-byr/Desktop/Training Dataset/TargetHome/CSVs/targethome.csv"))
train_df1.drop(['Flow ID','Dst IP','Src Port', 'Dst Port','Src IP','Timestamp'], axis=1, inplace=True)
train_df1["Flow Duration"] = np.log((train_df1["Flow Duration"] + 0.1).astype(float)) 
train_df1.fillna(value=-99999)

test_df=pd.DataFrame(pd.read_csv("/Users/b-byr/Desktop/Training Dataset/TargetHome/CSVs/targethome.csv"))
test_df.drop(['Flow ID','Dst IP','Src Port', 'Dst Port','Src IP','Timestamp'], axis=1, inplace=True)
test_df["Flow Duration"] = np.log((test_df["Flow Duration"] + 0.1).astype(float)) 
test_df.fillna(value=-99999)





train_data_T=train_df.values
train_data_S=train_df1.values
test_data_S=test_df.values
print('test print',test_data_S[1][0:5])
print ('data loaded successfully.')




label_T=train_data_T[:,train_data_T.shape[1]-1]
trans_T=append_feature(train_df,istest=False)

label_S=train_data_S[:,train_data_S.shape[1]-1]
trans_S=append_feature(train_df1,istest=False)

test_data_no=test_data_S[:,0]
test_data_S=append_feature(test_df,istest=True)





print('data split end',trans_S.shape,trans_T.shape,label_S.shape,label_T.shape,test_data_S.shape)





imputer_T=SimpleImputer(missing_values=np.nan,strategy='most_frequent')
imputer_S=SimpleImputer(missing_values=np.nan,strategy='most_frequent')
imputer_T.fit(trans_T,label_T)
imputer_S.fit(trans_S,label_S)




trans_T=imputer_S.transform(trans_T)
trans_S=imputer_S.transform(trans_S)





test_data_S=imputer_S.transform(test_data_S)




print ('data preprocessed.',trans_S.shape,trans_T.shape,label_S.shape,label_T.shape,test_data_S.shape)





X_train,X_test,y_train,y_test=model_selection.train_test_split(trans_S,label_S,test_size=0.33,random_state=42)

pred=TrAdaBoost(X_train,trans_T,y_train,label_T,X_test)
fpr,tpr,thresholds=metrics.roc_curve(y_true=y_test,y_score=pred,pos_label=1)



print (pred)









