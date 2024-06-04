import streamlit as st

columns = ['credit.policy', 'purpose', 'int.rate', 'installment', 'log.annual.inc',
       'dti', 'fico', 'days.with.cr.line', 'revol.bal', 'revol.util',
       'inq.last.6mths', 'delinq.2yrs', 'pub.rec', 'not.fully.paid']


st.title('Did Loan pay or not? 💸🧾')
credit_policy = st.select_slider("Select credit.policy:", [0, 1], 
                                   help="a binary indicator (0 or 1) indicating whether the individual meets the credit underwriting criteria of the lending institution (1) or not (0).")

purpose = st.selectbox("Select purpose:", ["debt_consolidation",
                                "all_other",         
                                "credit_card",       
                                "home_improvement", 
                                "small_business",   
                                "major_purchase",   
                                "educational" ], 
                                   help= "the purpose for which the loan was taken. Common purposes might include debt consolidation, home improvement, education, etc.")

int_rate = st.number_input("Input int.rate:", 
                                   help="the interest rate on the loan, expressed as a percentage. It indicates the cost of borrowing for the individual.")

installment = st.number_input("Input installment:", 
                                   help= "the monthly installment amount that the individual has to pay towards repaying the loan.")

log_annual_inc = st.number_input("Input log.annual.inc:", 
                                   help= "the natural logarithm of the individual's annual income.")

dti = st.number_input("Input dti:", 
                            help= "the debt-to-income ratio")

fico = st.number_input("Input fico:", 
                            help= "the FICO credit score of the individual. FICO scores are commonly used by lenders to assess credit risk and determine loan eligibility and interest rates.")

days_with_cr_line = st.number_input("Input days.with.cr.line:", 
                            help= "the number of days the individual has had a credit line.")

revol_bal = st.number_input("Input revol.bal:", 
                                   help= "the revolving balance, which is the outstanding balance on the individual's revolving credit accounts (e.g., credit cards) at the time of data collection.")

revol_util = st.number_input("Input revol.util:", 
                                   help= "the revolving utilization rate, which is the ratio of the individual's revolving credit balances to their credit limits. It indicates how much of their available credit they are currently using.")

inq_last_6mths = st.number_input("Input inq.last.6mths:", 
                                   help="the number of inquiries made by creditors in the last 6 months.")

delinq_2yrs = st.number_input("Input delinq.2yrs:", 
                                   help="the number of times the individual has been delinquent on payments in the past 2 years.")

pub_rec = st.number_input("Input pub.rec", 
                                   help="the number of derogatory public records (e.g., bankruptcies, tax liens) associated with the individual's credit report.")
 




