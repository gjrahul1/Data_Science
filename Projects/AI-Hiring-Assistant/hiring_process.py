import re
import streamlit as st
from langchain.prompts import PromptTemplate
from langchain.memory import ConversationBufferMemory
from langchain_google_genai import GoogleGenerativeAI
from langchain_core.runnables import RunnablePassthrough

def information_parser(full_name, email_address, phone_number, yoe, desired_position, current_location, tech_stack):
    
    #Regex to allow only letters and spaces
    letter_pattern = re.compile(r'^[A-Za-z\s]+$')

    #regex for email 
    email_pattern = re.compile(r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$')

    #Regex to allow only numbers
    numbers_pattern = re.compile(r'^\d+$')

    #Regex for tech_stack
    tech_stack_pattern = re.compile(r'^[A-Za-z\s,]+$')

    if not letter_pattern.match(full_name):
        st.error("Full name: Should contain only letters and numbers")
        return False
    
    if not email_pattern.match(email_address):
        st.error("Email address: Should contain not contain non-alphanumeric characters")
        return False

    if not letter_pattern.match(desired_position):
        st.error("Desired position: Should contain only letters")
        return False
    
    if not numbers_pattern.match(phone_number):
        st.error("Phone number: Should contain only numbers")
        return False
    
    if not numbers_pattern.match(yoe):
        st.error("Years of experience: Should contain only numbers")
        return False
    
    if not letter_pattern.match(current_location):
        st.error("Current location: Should contain only letters")
        return False
    
    if not tech_stack_pattern.match(tech_stack):
        st.error("Tech stack: Should contain only letters (,)")
        return False

    st.success("Processed Successfully")
    return True

memory = ConversationBufferMemory(return_messages = True)

#Model
def model():
    api_key = st.secrets['gemini_key']

    return GoogleGenerativeAI(model='gemini-1.5-pro',google_api_key = api_key)

#System Prompt
def prompt_template():
    return PromptTemplate(
        input_variables=["fullname", "desired_position", "yoe", "tech_stack", "user_response", "history"],
        template="""
            - You are a helpful AI Hiring Manager. Your task is to conduct a technical interview with the candidate, {fullname}.

            Guidelines:
                - Start by greeting the candidate: "Hello {fullname}, welcome to TalentScout! Are you ready to begin your interview for the {desired_position} position?"
                - Once the candidate indicates they are ready, proceed to ask questions based on their tech stack: {tech_stack}.
                - Ask **one question at a time** and wait for the candidate's response before asking the next question.
                - Plan to ask a **strictly a total of 3-5 questions** for each category within the {tech_stack}, tailored to the candidate’s {yoe} years of experience and the {desired_position} role.
                - Use the chat history {history} to keep track of which questions have been asked and the candidate’s responses. This will help you decide what question to ask next or when to move to the next tech stack category.
                - Tailor your questions based on the candidate’s previous response {user_response}. For example, if they answer correctly, consider increasing the difficulty after they have answered at least 2 questions correctly.
                - Maintain a professional and conversational tone, ensuring continuity with previous questions and responses.
                - If the candidate asks off-topic questions or requests outside your role, respond with: "As an AI Hiring Manager, I am not authorized to provide answers or deviate from the interview process."
                - Once you have asked and received answers for 3-5 questions in each tech stack category, conclude with: "Thank you for taking the interview for the {desired_position} position at TalentScout. Please close this window."

            Helpful Navigation During Response:
                - The {tech_stack} may contain multiple categories (e.g., programming languages, tools, databases, frameworks) separated by commas (e.g., "Django, Flask, Gen AI, GCP" or "React, Javascript, MongoDB"). Ask **strictly 3-5 questions** for each category.
                - Use the candidate’s {yoe} years of experience to adjust the complexity of questions appropriately.
                - **Do not ask multiple questions in a single response.** Always ask one question, then wait for the candidate’s answer.
                - Use the chat history {history} to avoid repeating questions and to maintain the flow of the interview.

                - You shouldn't respond to queries that might contain answer to the question with key-words "Is this correct ?"

                Go to next question, if you encounter such scenerios.

                - If the user prompts "I don't know" or similar prompts, you should simply go to next question and not disclose the answer.

                - You are not supposed to correct the user and let the user know if the answer is correct or not. If you encounter such scenerios, simply as next question.

            Current User Response: {user_response}
            Chat History: {history}
        """
    )
    

def hiring_assistance(full_name,tech_stack,yoe,desired_position,user_response):

    #Prompting
    formated_prompt = prompt_template()

    #Model
    model_ = model()

    def merge_history(inputs):
        history = memory.load_memory_variables({}).get("history","")
        inputs['history'] = history
        return inputs
    
    #History Wrapper
    merge_history_runner = RunnablePassthrough(merge_history)

    chain = merge_history_runner | formated_prompt | model_

    #Wrapping inputs
    inputs = {
        "fullname": full_name,
        "tech_stack":tech_stack,
        "yoe":yoe,
        "desired_position":desired_position,
        "user_response":user_response
    }

    results = chain.invoke(inputs)

    #Save Memory
    memory.save_context({"input":inputs["user_response"]},{"response":results})

    return results