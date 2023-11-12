import streamlit as st
from main import *


st.image('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ-7VlXnxXV96-d5xM1lAKSFl1tofEO2S1HiA&usqp=CAU', width=300)
st.title(":zap: Password Generator")


option = st.radio(
                  'Select a password generator',
                  ('Random password', 'Memorable password', 'Pin code')
        
)


if option == "Pin code":
    lenght = st.slider('select lenght of pin code.', 4, 32)
    generator = PinGenerator(lenght)
elif option == "Random password":
    lenght = st.slider('select lenght of random code.', 4, 32)
    include_symbols = st.toggle('include symbols ')
    include_number = st.toggle('include number ')
    generator = RandomPasswordGenerator(lenght, include_symbols, include_number)
elif option == 'Memorable password':
    lenght = st.slider('select number of words.', 4, 32)
    seperator = st.text_input('seperator', value='-')
    capitalization = st.toggle('Capitalization')
    generator = MemorablePasswordGenerator(lenght, seperator, capitalization)

password = generator.generate()
st.write (f'Your password is: {password}')

