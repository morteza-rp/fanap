import streamlit as st
import pandas as pd

columns = ['credit.policy', 'purpose', 'int.rate', 'installment', 'log.annual.inc',
       'dti', 'fico', 'days.with.cr.line', 'revol.bal', 'revol.util',
       'inq.last.6mths', 'delinq.2yrs', 'pub.rec']


st.write("""
         ### Did Loan pay or not? 💸🧾
         This app predicts the loan payment""")

st.sidebar.header("User Input Features")

st.sidebar.markdown(""" [Example CSV input file](https://dexscreener.com/watchlist)""")

# Collect user input features into dataframe
uploaded_file = st.sidebar.file_uploader("Upload your CSV file", type=["csv"])
if uploaded_file is not None:
    input_df = pd.read_csv(uploaded_file)
else:
    def user_input_features():
        
       credit_policy = st.sidebar.select_slider("Select credit.policy:", [0, 1], 
                                          help="a binary indicator (0 or 1) indicating whether the individual meets the credit underwriting criteria of the lending institution (1) or not (0).")

       purpose = st.sidebar.selectbox("Select purpose:", ["debt_consolidation",
                                   "all_other",         
                                   "credit_card",       
                                   "home_improvement", 
                                   "small_business",   
                                   "major_purchase",   
                                   "educational" ], 
                                          help= "the purpose for which the loan was taken. Common purposes might include debt consolidation, home improvement, education, etc.")

       int_rate = st.sidebar.number_input("Input int.rate:", 
                                          help="the interest rate on the loan, expressed as a percentage. It indicates the cost of borrowing for the individual.")

       installment = st.sidebar.number_input("Input installment:", 
                                          help= "the monthly installment amount that the individual has to pay towards repaying the loan.")

       log_annual_inc = st.sidebar.number_input("Input log.annual.inc:", 
                                          help= "the natural logarithm of the individual's annual income.")

       dti = st.sidebar.number_input("Input dti:", 
                                          help= "the debt-to-income ratio")

       fico = st.sidebar.number_input("Input fico:", 
                                          help= "the FICO credit score of the individual. FICO scores are commonly used by lenders to assess credit risk and determine loan eligibility and interest rates.")

       days_with_cr_line = st.sidebar.number_input("Input days.with.cr.line:", 
                                          help= "the number of days the individual has had a credit line.")

       revol_bal = st.sidebar.number_input("Input revol.bal:", 
                                          help= "the revolving balance, which is the outstanding balance on the individual's revolving credit accounts (e.g., credit cards) at the time of data collection.")

       revol_util = st.sidebar.number_input("Input revol.util:", 
                                          help= "the revolving utilization rate, which is the ratio of the individual's revolving credit balances to their credit limits. It indicates how much of their available credit they are currently using.")

       inq_last_6mths = st.sidebar.number_input("Input inq.last.6mths:", 
                                          help="the number of inquiries made by creditors in the last 6 months.")

       delinq_2yrs = st.sidebar.number_input("Input delinq.2yrs:", 
                                          help="the number of times the individual has been delinquent on payments in the past 2 years.")

       pub_rec = st.sidebar.number_input("Input pub.rec", 
                                          help="the number of derogatory public records (e.g., bankruptcies, tax liens) associated with the individual's credit report.")

       features = pd.DataFrame([[credit_policy,purpose,int_rate,installment,log_annual_inc,dti,fico,days_with_cr_line,revol_bal,revol_util,inq_last_6mths,delinq_2yrs,pub_rec]], 
                           columns=columns)

       return features

    input_df = user_input_features()




