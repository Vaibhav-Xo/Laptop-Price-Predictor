#importing libraries
import streamlit as st
import pickle as pk
import numpy as np

#importing model
pipe= pk.load(open('pipe.pkl','rb'))
df= pk.load(open('df.pkl','rb'))

st.title("Laptop Price Predictor 💻")

#creating grid

#1st row: making 3 cols left_column, middle_column, right_column
left_column, middle_column, right_column = st.columns(3)

with left_column:
  #Company
  company= st.selectbox('Company',df['Company'].unique())

with middle_column:
  #TypeName
  typename= st.selectbox('TypeName',df['TypeName'].unique())

with right_column:
  #Opsys
  opsys= st.selectbox('Operating System',df['OpSys'].unique())


#2nd row: making 3 cols left_column, middle_column, right_column
left_column, middle_column, right_column = st.columns(3)

with left_column:
  #Processor
  processor= st.selectbox('Processor',df['Processor'].unique())

with middle_column:
  #Display Size
  size= st.number_input('Display_Size(inches)')

with right_column:
  #Display
  display= st.selectbox('Display_Type',df['Display'].unique())


#3rd row: making 3 cols left_column, middle_column, right_column
left_column, middle_column, right_column = st.columns(3)

with left_column:
  #IPS
  ips= st.selectbox('IPS',['No', 'Yes'])

with middle_column:
  #Touchscreen
  touchscreen= st.selectbox('Touchscreen',['No', 'Yes'])

with right_column:
  #GpuBrand
  gpu= st.selectbox('GPU',df['Gpu_Brand'].unique())


#4th row: making 3 cols left_column, middle_column, right_column
left_column, middle_column, right_column = st.columns(3)

with left_column:
  #Ram
  ram= st.selectbox('RAM(GB)',np.sort(df['Ram'].unique()))

with middle_column:
  #SSD
  ssd= st.selectbox('SSD(GB)',np.sort(df['SSD'].unique()))

with right_column:
  #hybrid_storage
  hybrid= st.selectbox('Hybrid_Stoage(GB)',np.sort(df['Hybrid_Storage'].unique()))

#5th row: making 3 cols left_column, middle_column, right_column
left_column, middle_column, right_column = st.columns(3)

with left_column:
  #X_res
  x_res= st.selectbox('X_Resolution',np.sort(df['X_res'].unique()))

with middle_column:
  #Y_res
  y_res= st.selectbox('Y_Resolution',np.sort(df['Y_res'].unique()))

with right_column:
  #Weight
  weight= st.number_input('Weight(kg)')

if st.button('Predict_Price'):
  #query
  if touchscreen == 'No':
    touchscreen = 0
  else:
    touchscreen = 1

  if ips == 'No':
    ips = 0
  else:
    ips = 1

  query=np.array([company,typename,opsys,processor,size,display,ips,touchscreen,x_res,y_res,ram,ssd,hybrid,gpu,weight])

  query= query.reshape(1,15)
  st.title("The Predicted Price of Laptop = Rs "+str(int(np.exp(pipe.predict(query)[0]))))
