import streamlit

streamlit.title('My Parents New Healthy Diner')

streamlit.header('Breakfast Menu')

streamlit.text( '🥚 Egg')

streamlit.text( '🍞 Chicken')

streamlit.text( '🌿 Veggies')

streamlit.title('🍹 Create your Own Smoothie 🍹 ')

import pandas

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

streamlit.dataframe(my_fruit_list)
