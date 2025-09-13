import streamlit as st
from hiring_process import information_parser

with st.sidebar:
    st.header("Intelligence Hiring Assistant", divider = "rainbow")

    st.markdown("**I am here to make hiring easy!**")

    full_name = st.text_input("Full Name")

    email_address = st.text_input("Email Address")

    phone_number = st.text_input("Phone Number")

    yoe = st.text_input("Years of Experience")

    desired_position = st.text_input("Desired Position")

    current_location = st.text_input("Current Location")

    tech_stack = st.text_input("Tech Stack")

    if st.button("submit"):

        candidate_data = {
            "full_name":full_name,
            "email_address":email_address,
            "phone_number":phone_number,
            "yoe":yoe,
            "desired_position":desired_position,
            "current_location":current_location,
            "tech_stack":tech_stack
        }

        valid = information_parser(**candidate_data)

        if valid:
            if not 'candidate_data' in st.session_state:
                st.session_state['candidate_data'] = candidate_data

    # st.session_state['candidate_data'] = candidate_data

            st.switch_page("pages/testpage.py")

    
st.subheader("TalentScout's Recruitment Process",divider = "rainbow")

st.write("How your recuritment process should like")

# st.write("You need to provide basic details such as")

st.write("<h5>Provide Basic Candidate Details: </h5>", unsafe_allow_html = True)

st.markdown("""
                        
**Full Name**

Eg: G.J.Rahul
             
**Email Address**
            
Eg: g.j.rahul1@gmail.com
            
**Phone Number**

Eg: 8147000000
            
**Years of Experience**

Eg: 2
            
**Desired Position(s)**
            
Eg: Data Scientist
        
**Current Location**

Eg: Banglore
                
**Tech Stack**
            
Eg: Python, Django, SQL
            
""")

st.warning("Techstack should contain programming languages, tools, databases, frameworks")

st.write(" ")

st.write("<h5> Proctored Interview: </h5>",unsafe_allow_html=True)

st.markdown(""" 
            
 Once I recieve your basic details, you would be prompted to attempt a proctored interview based on the position you are applying for.

""")

st.write(" ")

st.write("<h5>Results:</h5>",unsafe_allow_html=True)

st.markdown("""
Someone from TalentScout would get in touch with you, if we find you as a best fit.
""")

st.write(" ")

st.write("<center> <h6>All the best!</h6> </center>",unsafe_allow_html = True)