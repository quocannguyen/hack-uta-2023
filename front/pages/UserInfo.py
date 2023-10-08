import streamlit as st

#Asks the user about their biological sex, age, weight, and height
form1 = st.form(key="Info")
form1.header("User info:")
sex = form1.radio("Sex:",["Male", "Female"])
age = form1.number_input("Age:", 1, 110)
weight = form1.number_input("Weight in kg:", 25,250)
height = form1.number_input("Height in m:", 0.90,2.50)
goal = form1.text_input("Your goal with this app: ")

#Calculates the BMI of user and gives appropriate comments
if form1.form_submit_button("Calculate your BMI here"):
    BMI = weight/(height*height)
    st.write("Your BMI value is: ", str(BMI))
    if (BMI<19):
        st.write("You are underweight.")
    elif(BMI >= 19 and BMI <25):
        st.write("You are healthy. Good job!")
    elif(BMI >= 25 and BMI <30):
        st.write("You are overweight.")
    elif(BMI >= 30 and BMI <40):
        st.write("You are obese.")
    else:
        st.write("You are extremely obese.")


    suggestion = st.expander("Expand here to see suggestions.")
    with suggestion:
        if (BMI<19):
            suggestion.write("Since you are underweight, you should increase your calorie intake to build fat and muscle.")
            suggestion.write("This can be achieved by consuming food that is high in carbohydrate, protein, or fat content.")
        elif(BMI >= 19 and BMI <25):
            suggestion.write("Keep maintaining an active lifestyle and a balanced diet.")
        elif(BMI >= 25 and BMI <30):
            suggestion.write("You should exercise more and maybe keep an eye on your food intake.")
        elif(BMI >= 30 and BMI <40):
            suggestion.write("You should look to make significant lifestyle changes. Physical fitness and dieting can make yourself")
        else:
            suggestion.write("Please begin dieting and physical fitness. Your health is in danger.")