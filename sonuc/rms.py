# -*- coding: utf-8 -*-
"""
Created on Tue May 11 20:06:08 2021

@author: MustafaKuşoğlu
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from keras import models
from keras import layers
from keras import optimizers,losses
from sklearn import preprocessing
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error,mean_absolute_error
from keras.callbacks import CSVLogger
from sklearn.metrics import accuracy_score



df=pd.read_csv('merge_with_tufe.csv')
df['Tarih']=pd.to_datetime(df['Tarih'])
df=df.sort_values(by='Tarih')


df=df.drop(['Unnamed: 0','Unnamed: 0.1','Tarih',],axis=1)
scaler = preprocessing.MinMaxScaler()
train=df.iloc[:,:6]
test=df.iloc[:,6:]
names=train.columns
d = scaler.fit_transform(train)
train = pd.DataFrame(d, columns=names)
test=test.reset_index(drop=True)



x_train,x_test,y_train,y_test=train_test_split(train,test,test_size=0.2,shuffle=True)
def build_model():
    model=models.Sequential()
    model.add(layers.Dense(16,activation='relu',input_shape=(6,),))
    model.add(layers.Dense(16,activation='relu'))
    model.add(layers.Dense(1))
    model.compile(optimizer='rmsprop',loss='mse',metrics=['mae','mape','mse','accuracy'])
    return model


num_epoch=1000
model=build_model()
csv_logger =  CSVLogger("16x16_1000e_opt=rmsprop_loss=mse_split=2_random.csv", append=True)
model.fit(x_train,y_train,
              epochs=num_epoch,batch_size=1,verbose=1,callbacks=[csv_logger])

his=pd.read_csv('16x16_1000e_opt=rmsprop_loss=mse_split=2_random.csv')
tahm=model.predict(x_test)
tah=pd.DataFrame(tahm)

#1
def build_model1():
    model=models.Sequential()
    model.add(layers.Dense(16,activation='relu',input_shape=(6,),))
    model.add(layers.Dense(16,activation='relu'))
    model.add(layers.Dense(1))
    model.compile(optimizer='rmsprop',loss='mae',metrics=['mae','mape','mse','accuracy'])
    return model


num_epoch1=1000
model1=build_model1()
csv_logger1 =  CSVLogger("16x16_1000e_opt=rmsprop_loss=mae_split=2_random.csv", append=True)
model1.fit(x_train,y_train,
              epochs=num_epoch1,batch_size=1,verbose=1,callbacks=[csv_logger1])

his1=pd.read_csv('16x16_1000e_opt=rmsprop_loss=mae_split=2_random.csv')
tahm1=model1.predict(x_test)
tah1=pd.DataFrame(tahm1)

#2
def build_model2():
    model=models.Sequential()
    model.add(layers.Dense(16,activation='relu',input_shape=(6,),))
    model.add(layers.Dense(16,activation='relu'))
    model.add(layers.Dense(1))
    model.compile(optimizer='rmsprop',loss='huber_loss',metrics=['mae','mape','mse','accuracy'])
    return model


num_epoch2=1000
model2=build_model2()
csv_logger2 =  CSVLogger("16x16_1000e_opt=rmsprop_loss=huber_split=2_random.csv", append=True)
model2.fit(x_train,y_train,
              epochs=num_epoch2,batch_size=1,verbose=1,callbacks=[csv_logger2])

his2=pd.read_csv('16x16_1000e_opt=rmsprop_loss=huber_split=2_random.csv')
tahm2=model2.predict(x_test)
tah2=pd.DataFrame(tahm2)

#3
def build_model3():
    model=models.Sequential()
    model.add(layers.Dense(16,activation='relu',input_shape=(6,),))
    model.add(layers.Dense(16,activation='relu'))
    model.add(layers.Dense(1))
    model.compile(optimizer='rmsprop',loss='mse',metrics=['mae','mape','mse','accuracy'])
    return model


num_epoch3=5000
model3=build_model3()
csv_logger3 =  CSVLogger("16x16_5000e_opt=rmsprop_loss=mse_split=2_random.csv", append=True)
model3.fit(x_train,y_train,
              epochs=num_epoch3,batch_size=1,verbose=1,callbacks=[csv_logger3])

his3=pd.read_csv('16x16_5000e_opt=rmsprop_loss=mse_split=2_random.csv')
tahm3=model3.predict(x_test)
tah3=pd.DataFrame(tahm3)
#4
def build_model4():
    model=models.Sequential()
    model.add(layers.Dense(16,activation='relu',input_shape=(6,),))
    model.add(layers.Dense(16,activation='relu'))
    model.add(layers.Dense(1))
    model.compile(optimizer='rmsprop',loss='mae',metrics=['mae','mape','mse','accuracy'])
    return model


num_epoch4=5000
model4=build_model4()
csv_logger4 =  CSVLogger("16x16_5000e_opt=rmsprop_loss=mae_split=2_random.csv", append=True)
model4.fit(x_train,y_train,
              epochs=num_epoch4,batch_size=1,verbose=1,callbacks=[csv_logger4])

his4=pd.read_csv('16x16_5000e_opt=rmsprop_loss=mae_split=2_random.csv')
tahm4=model4.predict(x_test)
tah4=pd.DataFrame(tahm4)

#5
def build_model5():
    model=models.Sequential()
    model.add(layers.Dense(16,activation='relu',input_shape=(6,),))
    model.add(layers.Dense(16,activation='relu'))
    model.add(layers.Dense(1))
    model.compile(optimizer='rmsprop',loss='huber_loss',metrics=['mae','mape','mse','accuracy'])
    return model


num_epoch5=5000
model5=build_model5()
csv_logger5 =  CSVLogger("16x16_5000e_opt=rmsprop_loss=huber_loss_split=2_random.csv", append=True)
model5.fit(x_train,y_train,
              epochs=num_epoch5,batch_size=1,verbose=1,callbacks=[csv_logger5])

his5=pd.read_csv('16x16_5000e_opt=rmsprop_loss=huber_loss_split=2_random.csv')
tahm5=model5.predict(x_test)
tah5=pd.DataFrame(tahm5)

#--------------------
df2=pd.read_csv('merge_with_tufe.csv')
df2=df2.drop(['Unnamed: 0','Unnamed: 0.1','Tarih',],axis=1)
scaler2 = preprocessing.MinMaxScaler()
train2=df2.iloc[:,:6]
test2=df2.iloc[:,6:]
names2=train2.columns
d2 = scaler2.fit_transform(train2)
train2 = pd.DataFrame(d2, columns=names2)
test2=test2.reset_index(drop=True)



x_train2,x_test2,y_train2,y_test2=train_test_split(train2,test2,test_size=0.2,shuffle=False)

def build_model6():
    model=models.Sequential()
    model.add(layers.Dense(16,activation='relu',input_shape=(6,),))
    model.add(layers.Dense(16,activation='relu'))
    model.add(layers.Dense(1))
    model.compile(optimizer='rmsprop',loss='mse',metrics=['mae','mape','mse','accuracy'])
    return model


num_epoch6=1000
model6=build_model6()
csv_logger6 =  CSVLogger("16x16_1000e_opt=rmsprop_loss=mse_split=2_bk.csv", append=True)
model6.fit(x_train2,y_train2,
              epochs=num_epoch6,batch_size=1,verbose=1,callbacks=[csv_logger6])

his6=pd.read_csv('16x16_1000e_opt=rmsprop_loss=mse_split=2_bk.csv')
tahm6=model6.predict(x_test2)
tah6=pd.DataFrame(tahm6)

#1
def build_model7():
    model=models.Sequential()
    model.add(layers.Dense(16,activation='relu',input_shape=(6,),))
    model.add(layers.Dense(16,activation='relu'))
    model.add(layers.Dense(1))
    model.compile(optimizer='rmsprop',loss='mae',metrics=['mae','mape','mse','accuracy'])
    return model


num_epoch7=1000
model7=build_model7()
csv_logger7 =  CSVLogger("16x16_1000e_opt=rmsprop_loss=mae_split=2_bk.csv", append=True)
model7.fit(x_train2,y_train2,
              epochs=num_epoch7,batch_size=1,verbose=1,callbacks=[csv_logger7])

his7=pd.read_csv('16x16_1000e_opt=rmsprop_loss=mae_split=2_bk.csv')
tahm7=model7.predict(x_test2)
tah7=pd.DataFrame(tahm7)

#2
def build_model8():
    model=models.Sequential()
    model.add(layers.Dense(16,activation='relu',input_shape=(6,),))
    model.add(layers.Dense(16,activation='relu'))
    model.add(layers.Dense(1))
    model.compile(optimizer='rmsprop',loss='huber_loss',metrics=['mae','mape','mse','accuracy'])
    return model


num_epoch8=1000
model8=build_model8()
csv_logger8 =  CSVLogger("16x16_1000e_opt=rmsprop_loss=huber_split=2_bk.csv", append=True)
model8.fit(x_train2,y_train2,
              epochs=num_epoch8,batch_size=1,verbose=1,callbacks=[csv_logger8])

his8=pd.read_csv('16x16_1000e_opt=rmsprop_loss=huber_split=2_bk.csv')
tahm8=model8.predict(x_test2)
tah8=pd.DataFrame(tahm8)

#3
def build_model9():
    model=models.Sequential()
    model.add(layers.Dense(16,activation='relu',input_shape=(6,),))
    model.add(layers.Dense(16,activation='relu'))
    model.add(layers.Dense(1))
    model.compile(optimizer='rmsprop',loss='mse',metrics=['mae','mape','mse','accuracy'])
    return model


num_epoch9=5000
model9=build_model9()
csv_logger9 =  CSVLogger("16x16_5000e_opt=rmsprop_loss=mse_split=2_bk.csv", append=True)
model9.fit(x_train2,y_train2,
              epochs=num_epoch9,batch_size=1,verbose=1,callbacks=[csv_logger9])

his9=pd.read_csv('16x16_5000e_opt=rmsprop_loss=mse_split=2_bk.csv')
tahm9=model9.predict(x_test2)
tah9=pd.DataFrame(tahm9)
#4
def build_model10():
    model=models.Sequential()
    model.add(layers.Dense(16,activation='relu',input_shape=(6,),))
    model.add(layers.Dense(16,activation='relu'))
    model.add(layers.Dense(1))
    model.compile(optimizer='rmsprop',loss='mae',metrics=['mae','mape','mse','accuracy'])
    return model


num_epoch10=5000
model10=build_model10()
csv_logger10 =  CSVLogger("16x16_5000e_opt=rmsprop_loss=mae_split=2_bk.csv", append=True)
model10.fit(x_train2,y_train2,
              epochs=num_epoch10,batch_size=1,verbose=1,callbacks=[csv_logger10])

his10=pd.read_csv('16x16_5000e_opt=rmsprop_loss=mae_split=2_bk.csv')
tahm10=model10.predict(x_test2)
tah10=pd.DataFrame(tahm10)

#10
def build_model17():
    model=models.Sequential()
    model.add(layers.Dense(16,activation='relu',input_shape=(6,),))
    model.add(layers.Dense(16,activation='relu'))
    model.add(layers.Dense(1))
    model.compile(optimizer='rmsprop',loss='huber_loss',metrics=['mae','mape','mse','accuracy'])
    return model


num_epoch17=5000
model17=build_model17()
csv_logger17 =  CSVLogger("16x16_5000e_opt=rmsprop_loss=huber_loss_split=2_bk.csv", append=True)
model17.fit(x_train2,y_train2,
              epochs=num_epoch17,batch_size=1,verbose=1,callbacks=[csv_logger17])

his17=pd.read_csv('16x16_5000e_opt=rmsprop_loss=huber_loss_split=2_bk.csv')
tahm17=model17.predict(x_test2)
tah17=pd.DataFrame(tahm17)

#----------
df3=pd.read_csv('merge_with_tufe.csv')
df3=df3.iloc[::-1]

df3=df3.drop(['Unnamed: 0','Unnamed: 0.1','Tarih',],axis=1)
scaler3 = preprocessing.MinMaxScaler()
train3=df3.iloc[:,:6]
test3=df3.iloc[:,6:]
names3=train3.columns
d3 = scaler3.fit_transform(train3)
train3 = pd.DataFrame(d3, columns=names3)
test3=test3.reset_index(drop=True)



x_train3,x_test3,y_train3,y_test3=train_test_split(train3,test3,test_size=0.2,shuffle=False)


def build_model11():
    model=models.Sequential()
    model.add(layers.Dense(16,activation='relu',input_shape=(6,),))
    model.add(layers.Dense(16,activation='relu'))
    model.add(layers.Dense(1))
    model.compile(optimizer='rmsprop',loss='mse',metrics=['mae','mape','mse','accuracy'])
    return model


num_epoch11=1000
model11=build_model11()
csv_logger11 =  CSVLogger("16x16_1000e_opt=rmsprop_loss=mse_split=2_kb.csv", append=True)
model11.fit(x_train3,y_train3,
              epochs=num_epoch11,batch_size=1,verbose=1,callbacks=[csv_logger11])

his11=pd.read_csv('16x16_1000e_opt=rmsprop_loss=mse_split=2_kb.csv')
tahm11=model11.predict(x_test3)
tah11=pd.DataFrame(tahm11)

#1
def build_model12():
    model=models.Sequential()
    model.add(layers.Dense(16,activation='relu',input_shape=(6,),))
    model.add(layers.Dense(16,activation='relu'))
    model.add(layers.Dense(1))
    model.compile(optimizer='rmsprop',loss='mae',metrics=['mae','mape','mse','accuracy'])
    return model


num_epoch12=1000
model12=build_model12()
csv_logger12 =  CSVLogger("16x16_1000e_opt=rmsprop_loss=mae_split=2_kb.csv", append=True)
model12.fit(x_train3,y_train3,
              epochs=num_epoch12,batch_size=1,verbose=1,callbacks=[csv_logger12])

his12=pd.read_csv('16x16_1000e_opt=rmsprop_loss=mae_split=2_kb.csv')
tahm12=model12.predict(x_test3)
tah12=pd.DataFrame(tahm12)

#2
def build_model13():
    model=models.Sequential()
    model.add(layers.Dense(16,activation='relu',input_shape=(6,),))
    model.add(layers.Dense(16,activation='relu'))
    model.add(layers.Dense(1))
    model.compile(optimizer='rmsprop',loss='huber_loss',metrics=['mae','mape','mse','accuracy'])
    return model


num_epoch13=1000
model13=build_model13()
csv_logger13 =  CSVLogger("16x16_1000e_opt=rmsprop_loss=huber_split=2_kb.csv", append=True)
model13.fit(x_train3,y_train3,
              epochs=num_epoch13,batch_size=1,verbose=1,callbacks=[csv_logger13])

his13=pd.read_csv('16x16_1000e_opt=rmsprop_loss=huber_split=2_bk.csv')
tahm13=model13.predict(x_test3)
tah13=pd.DataFrame(tahm13)

#3
def build_model14():
    model=models.Sequential()
    model.add(layers.Dense(16,activation='relu',input_shape=(6,),))
    model.add(layers.Dense(16,activation='relu'))
    model.add(layers.Dense(1))
    model.compile(optimizer='rmsprop',loss='mse',metrics=['mae','mape','mse','accuracy'])
    return model


num_epoch14=5000
model14=build_model14()
csv_logger14 =  CSVLogger("16x16_5000e_opt=rmsprop_loss=mse_split=2_kb.csv", append=True)
model14.fit(x_train3,y_train3,
              epochs=num_epoch14,batch_size=1,verbose=1,callbacks=[csv_logger14])

his14=pd.read_csv('16x16_5000e_opt=rmsprop_loss=mse_split=2_kb.csv')
tahm14=model14.predict(x_test3)
tah14=pd.DataFrame(tahm14)
#4
def build_model15():
    model=models.Sequential()
    model.add(layers.Dense(16,activation='relu',input_shape=(6,),))
    model.add(layers.Dense(16,activation='relu'))
    model.add(layers.Dense(1))
    model.compile(optimizer='rmsprop',loss='mae',metrics=['mae','mape','mse','accuracy'])
    return model


num_epoch15=5000
model15=build_model15()
csv_logger15 =  CSVLogger("16x16_5000e_opt=rmsprop_loss=mae_split=2_kb.csv", append=True)
model15.fit(x_train3,y_train3,
              epochs=num_epoch15,batch_size=1,verbose=1,callbacks=[csv_logger15])

his15=pd.read_csv('16x16_5000e_opt=rmsprop_loss=mae_split=2_kb.csv')
tahm15=model15.predict(x_test3)
tah15=pd.DataFrame(tahm15)

#10
def build_model16():
    model=models.Sequential()
    model.add(layers.Dense(16,activation='relu',input_shape=(6,),))
    model.add(layers.Dense(16,activation='relu'))
    model.add(layers.Dense(1))
    model.compile(optimizer='rmsprop',loss='huber_loss',metrics=['mae','mape','mse','accuracy'])
    return model


num_epoch16=5000
model16=build_model16()
csv_logger16 =  CSVLogger("16x16_5000e_opt=rmsprop_loss=huber_loss_split=2_kb.csv", append=True)
model16.fit(x_train3,y_train3,
              epochs=num_epoch16,batch_size=1,verbose=1,callbacks=[csv_logger16])

his16=pd.read_csv('16x16_5000e_opt=rmsprop_loss=huber_loss_split=2_kb.csv')
tahm16=model16.predict(x_test3)
tah16=pd.DataFrame(tahm16)