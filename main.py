import streamlit as st
from model import wiki_fact

st.title("Historical_Fact_Checker 📖")
st.sidebar.subheader(("The reference is Wikipedia."),divider='rainbow')
st.sidebar.subheader(("This ChatBot is powerd by openai chatGPT3.5"),divider='rainbow')

query= st.text_area('Enter your sentence here:')
button=st.button('Submit')

if button :
    response=wiki_fact(query)
    st.caption('Based on Wikipedia, this is the response of your query:')
    st.write(response)

