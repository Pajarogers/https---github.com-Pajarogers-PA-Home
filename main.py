import streamlit as st
import requests

st.set_page_config(page_title="P&A Home Improvement", page_icon=":tada:", layout="wide")

st.subheader("P&A Home Improvement :house:")

st.info('Enter Client Information')
with st.form(key='myform', clear_on_submit=True):
    name=st.text_input('Enter client name')
    job_type = st.text_input('Enter Job Description')
    location = st.text_input('Location')
    hours= st.slider('Estimated Hours To Complete')
    material_cost = st.checkbox('Is material cost included')
    material_cost_job = st.text_input('Material Cost')
    payamount=st.text_input('Total Amount for job')
    submit_button = st.form_submit_button("Submit")



