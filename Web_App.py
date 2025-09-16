import streamlit as st
import google.generativeai as genai
import pandas as pd

import os

api=os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=api)
model=genai.GenerativeModel("gemini-2.5-flash-lite")


# Lets Create the UI
st.title(":orange[Healthify] :blue[Your Personal Health Assistant]")
st.markdown(""" ##### This application will assist you to have a better and healthy life. You can ask anything related to health and fitness and get recommendations.""")
tips=''' Follow the Steps 
1. Enter your details in the sidebar
2. Enter your Gender, Age, Weight(kgs), Height(cms)
3. Select the number on the fitness scale (0-5). 5-Fittest, 0- No Exercise

* After filling the details, write your prompt here and get a customised response.'''

st.write(tips)

st.sidebar.header(":red[Enter your details]")
name=st.sidebar.text_input("Enter your Name")
gender=st.sidebar.selectbox("Select your Gender" , ["Male","Female"])
age=st.sidebar.number_input("Enter your Age",min_value=1,max_value=100)
weight=st.sidebar.number_input("Enter your Weight (in kgs)",min_value=1,max_value=300,value=1,step=1)  
height=st.sidebar.number_input("Enter your Height (in cms)",min_value=30,max_value=250,value=30,step=1)

bmi=pd.to_numeric(weight)/((pd.to_numeric(height)/100)**2)

fitness=st.sidebar.slider("Rate your Fitness Level (0-5)",min_value=0,max_value=5,value=0,step=1)
st.sidebar.write(f"{name} , Your BMI is {round(bmi,2)} kg/m^2")

# Lets use Genai model to get the output
user_query=st.text_input("Enter your Health related questions here >")
prompt=f'''Assume you are a Health Expert. You are required to answer the question based on the user details provided by the user such as 
gender is {gender}
age is {age} years
weight is {weight} kgs
height is {height} cms
bmi is {bmi} kg/m^2
and user rates his/her fitness as {fitness} out of 5.

Your Output should be in the following format:
* It should start by giving one two line comment on the details that are being provided by the user.
* It should explain what the real problem is based on the details provided by the user.
* It should provide all the possible causes for this problem.
* It shouuld provide all possible solutios for this problem.
* It should also mention which doctor specializattion the user should consult for this problem.
* Strictly do not recommend or advice any medicines.
Output should be in bullet points and use tables wherever required.

here is the query from the user : {user_query}
'''

response=model.generate_content(prompt)
if response:
    response=model.generate_content(prompt)
    st.write(response.text)