import 

#Asks the user about their biological sex, weight, and height
st.header("User info:")
st.radio("Sex:",["Male", "Female"])
st.number_input("Weight in lbs:", 50,500)
st.number_input("Height in inches:", 4.00,7.00)