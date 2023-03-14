import streamlit as st
import pandas as pd
from xgboost import XGBClassifier

model = XGBClassifier()
model.load_model('xgb_model.json')

st.title('Retained  :rocket:')
st.caption('Created by: Amin Ahmed and Amadin Ahmed')
st.text("")
st.markdown('All of the efforts that you put into obtaining a customer in the customer journey is useless if they dont stay on the platform. If we can find a way to predict if a customer is likely to leave your platform, the business can take preventative actions to assist the customer. Ex: talking to the customer to gain qualitative insights or even give them a promotional offer / incentive. ')
st.text("")

from PIL import Image

image = Image.open('report.png')

st.image(image, caption='Classification Report')

def predicts(PhoneService_No, PhoneService_Yes, Contract_Month_to_month, Contract_One_year, Contract_Two_year, PaperlessBilling_No, PaperlessBilling_Yes, PaymentMethod_Bank, PaymentMethod_Credit, PaymentMethod_Electronic, PaymentMethod_Mailed, gender_Female, gender_Male, Partner_No, Partner_Yes, Dependents_No, Dependents_Yes, MultipleLines_No, MultipleLines_Yes, InternetService_DSL, InternetService_Fiber, InternetService_No, OnlineSecurity_No, OnlineSecurity_Yes, OnlineBackup_No, OnlineBackup_Yes, DeviceProtection_No, DeviceProtection_Yes, TechSupport_No, TechSupport_Yes, StreamingTV_No, StreamingTV_Yes, StreamingMovies_No, StreamingMovies_Yes, tenure, MonthlyCharges, TotalCharges, SeniorCitizen):


    col = ['PhoneService_No', 'PhoneService_Yes', 'Contract_Month-to-month', 'Contract_One year', 
            'Contract_Two year', 'PaperlessBilling_No', 'PaperlessBilling_Yes', 
            'PaymentMethod_Bank transfer (automatic)', 'PaymentMethod_Credit card (automatic)', 
            'PaymentMethod_Electronic check', 'PaymentMethod_Mailed check', 'gender_Female', 
            'gender_Male', 'Partner_No', 'Partner_Yes', 'Dependents_No', 'Dependents_Yes', 
            'MultipleLines_No', 'MultipleLines_Yes', 'InternetService_DSL', 'InternetService_Fiber optic', 
            'InternetService_No', 'OnlineSecurity_No', 'OnlineSecurity_Yes', 'OnlineBackup_No', 
            'OnlineBackup_Yes', 'DeviceProtection_No', 'DeviceProtection_Yes', 'TechSupport_No', 
            'TechSupport_Yes', 'StreamingTV_No', 'StreamingTV_Yes', 'StreamingMovies_No', 
            'StreamingMovies_Yes', 'tenure', 'MonthlyCharges', 'TotalCharges', 'SeniorCitizen']
    prediction = model.predict(pd.DataFrame([[PhoneService_No, PhoneService_Yes, Contract_Month_to_month, Contract_One_year, Contract_Two_year, PaperlessBilling_No, PaperlessBilling_Yes, PaymentMethod_Bank, PaymentMethod_Credit, PaymentMethod_Electronic, PaymentMethod_Mailed, gender_Female, gender_Male, Partner_No, Partner_Yes, Dependents_No, Dependents_Yes, MultipleLines_No, MultipleLines_Yes, InternetService_DSL, InternetService_Fiber, InternetService_No, OnlineSecurity_No, OnlineSecurity_Yes, OnlineBackup_No, OnlineBackup_Yes, DeviceProtection_No, DeviceProtection_Yes, TechSupport_No, TechSupport_Yes, StreamingTV_No, StreamingTV_Yes, StreamingMovies_No, StreamingMovies_Yes, tenure, MonthlyCharges, TotalCharges, SeniorCitizen]], columns= col))[0]
    return prediction

if st.button('Customer 1 Prediction'):
    PhoneService_No                         =     0.00
    PhoneService_Yes                         =    1.00
    Contract_Month_to_month                   =   1.00
    Contract_One_year                          =  0.00
    Contract_Two_year                          =  0.00
    PaperlessBilling_No                        =  0.00
    PaperlessBilling_Yes                       =  1.00
    PaymentMethod_Bank  =  0.00
    PaymentMethod_Credit  =    0.00
    PaymentMethod_Electronic  =            0.00
    PaymentMethod_Mailed       =           1.00
    gender_Female               =                 0.00
    gender_Male                  =                1.00
    Partner_No                    =               1.00
    Partner_Yes                    =              0.00
    Dependents_No                   =             1.00
    Dependents_Yes                   =            0.00
    MultipleLines_No                  =           1.00
    MultipleLines_Yes                  =          0.00
    InternetService_DSL                 =         1.00
    InternetService_Fiber               =  0.00
    InternetService_No                   =        0.00
    OnlineSecurity_No                     =       0.00
    OnlineSecurity_Yes                     =      1.00
    OnlineBackup_No                         =     0.00
    OnlineBackup_Yes                         =    1.00
    DeviceProtection_No                       =   1.00
    DeviceProtection_Yes                      =   0.00
    TechSupport_No                            =   1.00
    TechSupport_Yes                           =   0.00
    StreamingTV_No                            =   1.00
    StreamingTV_Yes                            =  0.00
    StreamingMovies_No                          = 1.00
    StreamingMovies_Yes                          =0.00
    tenure                           =            2.00
    MonthlyCharges                    =          53.85
    TotalCharges                       =        108.15
    SeniorCitizen                       =         0.00
    col = ['PhoneService_No', 'PhoneService_Yes', 'Contract_Month-to-month', 'Contract_One year', 
            'Contract_Two year', 'PaperlessBilling_No', 'PaperlessBilling_Yes', 
            'PaymentMethod_Bank transfer (automatic)', 'PaymentMethod_Credit card (automatic)', 
            'PaymentMethod_Electronic check', 'PaymentMethod_Mailed check', 'gender_Female', 
            'gender_Male', 'Partner_No', 'Partner_Yes', 'Dependents_No', 'Dependents_Yes', 
            'MultipleLines_No', 'MultipleLines_Yes', 'InternetService_DSL', 'InternetService_Fiber optic', 
            'InternetService_No', 'OnlineSecurity_No', 'OnlineSecurity_Yes', 'OnlineBackup_No', 
            'OnlineBackup_Yes', 'DeviceProtection_No', 'DeviceProtection_Yes', 'TechSupport_No', 
            'TechSupport_Yes', 'StreamingTV_No', 'StreamingTV_Yes', 'StreamingMovies_No', 
            'StreamingMovies_Yes', 'tenure', 'MonthlyCharges', 'TotalCharges', 'SeniorCitizen']
    prediction = model.predict(pd.DataFrame([[PhoneService_No, PhoneService_Yes, Contract_Month_to_month, Contract_One_year, Contract_Two_year, PaperlessBilling_No, PaperlessBilling_Yes, PaymentMethod_Bank, PaymentMethod_Credit, PaymentMethod_Electronic, PaymentMethod_Mailed, gender_Female, gender_Male, Partner_No, Partner_Yes, Dependents_No, Dependents_Yes, MultipleLines_No, MultipleLines_Yes, InternetService_DSL, InternetService_Fiber, InternetService_No, OnlineSecurity_No, OnlineSecurity_Yes, OnlineBackup_No, OnlineBackup_Yes, DeviceProtection_No, DeviceProtection_Yes, TechSupport_No, TechSupport_Yes, StreamingTV_No, StreamingTV_Yes, StreamingMovies_No, StreamingMovies_Yes, tenure, MonthlyCharges, TotalCharges, SeniorCitizen]], columns= col))[0]
    if prediction == 1:
        st.error(f' This customer 1 is likely to churn.')
    elif prediction == 0:
        st.success(f' This customer 1 is not likely to churn.')

if st.button('Customer 2 Prediction'):
    PhoneService_No                        =       0.00
    PhoneService_Yes                       =       1.00
    Contract_Month_to_month                 =      0.00
    Contract_One_year                        =     1.00
    Contract_Two_year                         =    0.00
    PaperlessBilling_No                        =   1.00
    PaperlessBilling_Yes                        =  0.00
    PaymentMethod_Bank      = 0.00
    PaymentMethod_Credit         =0.00
    PaymentMethod_Electronic           = 0.00
    PaymentMethod_Mailed                  = 1.00
    gender_Female                                = 0.00
    gender_Male                                  = 1.00
    Partner_No                                   = 1.00
    Partner_Yes                                  = 0.00
    Dependents_No                                = 1.00
    Dependents_Yes                               = 0.00
    MultipleLines_No                             = 1.00
    MultipleLines_Yes                            = 0.00
    InternetService_DSL                          = 1.00
    InternetService_Fiber                = 0.00
    InternetService_No                           = 0.00
    OnlineSecurity_No                             =0.00
    OnlineSecurity_Yes                           = 1.00
    OnlineBackup_No                              = 1.00
    OnlineBackup_Yes                              =0.00
    DeviceProtection_No                          = 0.00
    DeviceProtection_Yes                          =1.00
    TechSupport_No                                =1.00
    TechSupport_Yes                              = 0.00
    StreamingTV_No                               = 1.00
    StreamingTV_Yes                              = 0.00
    StreamingMovies_No                           = 1.00
    StreamingMovies_Yes                          = 0.00
    tenure                                     =  34.00
    MonthlyCharges                              = 56.95
    TotalCharges                             =  1889.50
    SeniorCitizen                             =    0.00
    col = ['PhoneService_No', 'PhoneService_Yes', 'Contract_Month-to-month', 'Contract_One year', 
            'Contract_Two year', 'PaperlessBilling_No', 'PaperlessBilling_Yes', 
            'PaymentMethod_Bank transfer (automatic)', 'PaymentMethod_Credit card (automatic)', 
            'PaymentMethod_Electronic check', 'PaymentMethod_Mailed check', 'gender_Female', 
            'gender_Male', 'Partner_No', 'Partner_Yes', 'Dependents_No', 'Dependents_Yes', 
            'MultipleLines_No', 'MultipleLines_Yes', 'InternetService_DSL', 'InternetService_Fiber optic', 
            'InternetService_No', 'OnlineSecurity_No', 'OnlineSecurity_Yes', 'OnlineBackup_No', 
            'OnlineBackup_Yes', 'DeviceProtection_No', 'DeviceProtection_Yes', 'TechSupport_No', 
            'TechSupport_Yes', 'StreamingTV_No', 'StreamingTV_Yes', 'StreamingMovies_No', 
            'StreamingMovies_Yes', 'tenure', 'MonthlyCharges', 'TotalCharges', 'SeniorCitizen']
    prediction = model.predict(pd.DataFrame([[PhoneService_No, PhoneService_Yes, Contract_Month_to_month, Contract_One_year, Contract_Two_year, PaperlessBilling_No, PaperlessBilling_Yes, PaymentMethod_Bank, PaymentMethod_Credit, PaymentMethod_Electronic, PaymentMethod_Mailed, gender_Female, gender_Male, Partner_No, Partner_Yes, Dependents_No, Dependents_Yes, MultipleLines_No, MultipleLines_Yes, InternetService_DSL, InternetService_Fiber, InternetService_No, OnlineSecurity_No, OnlineSecurity_Yes, OnlineBackup_No, OnlineBackup_Yes, DeviceProtection_No, DeviceProtection_Yes, TechSupport_No, TechSupport_Yes, StreamingTV_No, StreamingTV_Yes, StreamingMovies_No, StreamingMovies_Yes, tenure, MonthlyCharges, TotalCharges, SeniorCitizen]], columns= col))[0]
    if prediction == 1:
        st.error(f' This customer 2 is likely to churn.')
    elif prediction == 0:
        st.success(f' This customer 2 is not likely to churn.')

Phone_button = st.radio(
    "Do you have Phone services?",
    ('PhoneService_No', 'PhoneService_Yes'))

if Phone_button == 'PhoneService_No':
    PhoneService_No                        =       1.00
    PhoneService_Yes                       =       0.00
if Phone_button == 'PhoneService_Yes':
    PhoneService_No                        =       0.00
    PhoneService_Yes                       =       1.00



Contract = st.radio(
    "Do you have Phone services?",
    ('Contract_Month_to_month', 'Contract_One_year','Contract_Two_year'))

if Contract == 'Contract_Month_to_month':
    Contract_Month_to_month                 =      1.00
    Contract_One_year                        =     0.00
    Contract_Two_year                         =    0.00

elif Contract == 'Contract_One_year':
    Contract_Month_to_month                 =      0.00
    Contract_One_year                        =     1.00
    Contract_Two_year                         =    0.00

elif Contract == 'Contract_Two_year':
    Contract_Month_to_month                 =      0.00
    Contract_One_year                        =     0.00
    Contract_Two_year                         =    1.00


PaperlessBilling = st.radio(
    "Do you have Paperless Billing?",
    ('PaperlessBilling_No', 'PaperlessBilling_Yes'))

if PaperlessBilling == 'PaperlessBilling_No':
    PaperlessBilling_No                        =       1.00
    PaperlessBilling_Yes                       =       0.00
elif PaperlessBilling == 'PaperlessBilling_Yes':
    PaperlessBilling_No                        =       0.00
    PaperlessBilling_Yes                       =       1.00


PaymentMethod = st.radio(
    "What is your payment method??",
    ('PaymentMethod_Bank', 'PaymentMethod_Credit','PaymentMethod_Electronic','PaymentMethod_Mailed'))

if PaymentMethod == 'PaymentMethod_Bank':
    PaymentMethod_Bank                 =      1.00
    PaymentMethod_Credit                        =     0.00
    PaymentMethod_Electronic                         =    0.00
    PaymentMethod_Mailed                         =    0.00

elif PaymentMethod == 'PaymentMethod_Bank':
    PaymentMethod_Bank                 =      0.00
    PaymentMethod_Credit                        =     1.00
    PaymentMethod_Electronic                         =    0.00
    PaymentMethod_Mailed                         =    0.00

elif PaymentMethod == 'PaymentMethod_Electronic':
    PaymentMethod_Bank                 =      0.00
    PaymentMethod_Credit                        =     0.00
    PaymentMethod_Electronic                         =    1.00
    PaymentMethod_Mailed                         =    0.00

elif PaymentMethod == 'PaymentMethod_Mailed':
    PaymentMethod_Bank                 =      0.00
    PaymentMethod_Credit                        =     0.00
    PaymentMethod_Electronic                         =    0.00
    PaymentMethod_Mailed                         =    1.00
    
gender = st.radio(
    "Gender?",
    ('gender_Female', 'gender_Male'))

if gender == 'gender_Female':
    gender_Female                        =       1.00
    gender_Male                       =       0.00
if gender == 'gender_Male':
    gender_Female                        =       0.00
    gender_Male                       =       1.00

Partner = st.radio(
    "Do you have a Partner?",
    ('Partner_No', 'Partner_Yes'))

if Partner == 'Partner_No':
    Partner_No                        =       1.00
    Partner_Yes                       =       0.00
if Partner == 'Partner_Yes':
    Partner_No                        =       0.00
    Partner_Yes                       =       1.00

Dependents = st.radio(
    "Do you have Dependents?",
    ('Dependents_No', 'Dependents_Yes'))

if Dependents == 'Dependents_No':
    Dependents_No                        =       1.00
    Dependents_Yes                       =       0.00
if Dependents == 'Dependents_Yes':
    Dependents_No                        =       0.00
    Dependents_Yes                       =       1.00


MultipleLines = st.radio(
    "Do you have Multiple Lines?",
    ('MultipleLines_No', 'MultipleLines_Yes'))

if MultipleLines == 'MultipleLines_No':
    MultipleLines_No                        =       1.00
    MultipleLines_Yes                       =       0.00
if MultipleLines == 'MultipleLines_Yes':
    MultipleLines_No                        =       0.00
    MultipleLines_Yes                       =       1.00


InternetService = st.radio(
    "What type of Internet Service do you have?",
    ('InternetService_DSL', 'InternetService_Fiber','InternetService_No'))

if InternetService == 'InternetService_DSL':
    InternetService_DSL                 =      1.00
    InternetService_Fiber                        =     0.00
    InternetService_No                         =    0.00

elif InternetService == 'InternetService_Fiber':
    InternetService_DSL                 =      0.00
    InternetService_Fiber                        =     1.00
    InternetService_No                         =    0.00

elif InternetService == 'InternetService_No':
    InternetService_DSL                 =      0.00
    InternetService_Fiber                        =     0.00
    InternetService_No                         =    1.00

OnlineSecurity = st.radio(
    "Do you have Online Security?",
    ('OnlineSecurity_No', 'OnlineSecurity_Yes'))

if OnlineSecurity == 'OnlineSecurity_No':
    OnlineSecurity_No                        =       1.00
    OnlineSecurity_Yes                       =       0.00
elif OnlineSecurity == 'OnlineSecurity_Yes':
    OnlineSecurity_No                        =       0.00
    OnlineSecurity_Yes                       =       1.00

OnlineBackup = st.radio(
    "Do you have Online Backup?",
    ('OnlineBackup_No', 'OnlineBackup_Yes'))

if OnlineBackup == 'OnlineBackup_No':
    OnlineBackup_No                        =       1.00
    OnlineBackup_Yes                       =       0.00
elif OnlineBackup == 'OnlineBackup_Yes':
    OnlineBackup_No                        =       0.00
    OnlineBackup_Yes                       =       1.00
    
DeviceProtection = st.radio(
    "Do you have any Device Protection?",
    ('DeviceProtection_No', 'DeviceProtection_Yes'))

if DeviceProtection == 'DeviceProtection_No':
    DeviceProtection_No                        =       1.00
    DeviceProtection_Yes                    =       0.00
elif DeviceProtection == 'DeviceProtection_Yes':
    DeviceProtection_No                        =       0.00
    DeviceProtection_Yes                       =       1.00
    

TechSupport = st.radio(
    "Have you recently contacted Tech Support?",
    ('TechSupport_No', 'TechSupport_Yes'))

if TechSupport == 'TechSupport_No':
    TechSupport_No                        =       1.00
    TechSupport_Yes                    =       0.00
elif TechSupport == 'TechSupport_Yes':
    TechSupport_No                        =       0.00
    TechSupport_Yes                       =       1.00

StreamingTV = st.radio(
    "Do you have Streaming TV?",
    ('StreamingTV_No', 'StreamingTV_Yes'))

if StreamingTV == 'StreamingTV_No':
    StreamingTV_No                        =       1.00
    StreamingTV_Yes                    =       0.00
elif StreamingTV == 'StreamingTV_Yes':
    StreamingTV_No                        =       0.00
    StreamingTV_Yes                       =       1.00


StreamingMovies = st.radio(
    "Do you have an Movie Streaming Pagkages?",
    ('StreamingMovies_No', 'StreamingMovies_Yes'))

if StreamingMovies == 'StreamingMovies_No':
    StreamingMovies_No                        =       1.00
    StreamingMovies_Yes                    =       0.00
elif StreamingMovies == 'StreamingMovies_Yes':
    StreamingMovies_No                        =       0.00
    StreamingMovies_Yes                       =       1.00

tenure = st.number_input('Insert tenure in months')
MonthlyCharges = st.number_input('Insert Monthly Charges')
TotalCharges = st.number_input('Insert Total Charges')

SeniorCitizen                       =         0.00

if st.button('Predict Price'):

    price = predicts(PhoneService_No, PhoneService_Yes, Contract_Month_to_month, Contract_One_year, Contract_Two_year, PaperlessBilling_No, PaperlessBilling_Yes, PaymentMethod_Bank, PaymentMethod_Credit, PaymentMethod_Electronic, PaymentMethod_Mailed, gender_Female, gender_Male, Partner_No, Partner_Yes, Dependents_No, Dependents_Yes, MultipleLines_No, MultipleLines_Yes, InternetService_DSL, InternetService_Fiber, InternetService_No, OnlineSecurity_No, OnlineSecurity_Yes, OnlineBackup_No, OnlineBackup_Yes, DeviceProtection_No, DeviceProtection_Yes, TechSupport_No, TechSupport_Yes, StreamingTV_No, StreamingTV_Yes, StreamingMovies_No, StreamingMovies_Yes, tenure, MonthlyCharges, TotalCharges, SeniorCitizen)
    if price == 1:
        st.error(f' This customer is likely to churn.')
    elif price == 0:
        st.success(f' This customer is not likely to churn.')



