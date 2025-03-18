# Hiring Assistant Chatbot

## Project Overview

The **Hiring Assistant Chatbot** is an AI-powered tool designed to streamline the technical interview process for TalentScout, a fictional recruitment platform. Built using Streamlit and powered by Google’s Gemini 1.5 Pro model via LangChain, this chatbot automates candidate screening by collecting personal details, conducting a technical interview based on the candidate’s tech stack, and adapting questions dynamically. Key features include:

- **Candidate Information Gathering**: Collects details like name, email, experience, and tech stack through a user-friendly Streamlit interface.
- **Technical Interview**: Asks 3-5 questions per tech stack category (e.g., Python, Django), tailoring difficulty based on the candidate’s experience and responses.
- **Personalized Responses**: Adapts questions based on user history and correctness of previous answers.
- **Deployment on Streamlit Community Cloud**: Hosted on Streamlit’s free cloud platform for easy access and scalability.

This project was developed as part of an assignment to demonstrate proficiency in building AI-driven applications with Streamlit, LangChain, and cloud deployment.

---

## Installation Instructions

Follow these steps to set up and run the Hiring Assistant Chatbot locally on your machine.

### Prerequisites
- **Python 3.12**
- **LangChain**
- **Gemini API Key**
- **Streamlit**

### Steps
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/gjrahul/Data_Science.git
   cd AI-Hiring-Assistant
   ```

2. **Create a Virtual Environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**:
   - Ensure `requirements.txt` is in the root directory with the following content:
     ```
     streamlit==1.32.0
     langchain==0.1.20
     langchain-google-genai==1.0.3
     google-cloud-storage==2.16.0
     ```
   - Install the dependencies:
     ```bash
     pip install -r requirements.txt
     ```

4. **Configure the API Key**:
   - In `hiring_process.py`, replace the `api_key` in the `model()` function with your Google API key:
     ```python
     api_key = "your-google-api-key"
     ```
   - Alternatively, set it as an environment variable:
     ```bash
     export GOOGLE_API_KEY="your-google-api-key"  # On Windows: set GOOGLE_API_KEY=your-google-api-key
     ```

5. **Run the Application Locally**:
   ```bash
   streamlit run main.py
   ```
   - Open the provided URL (e.g., `http://localhost:8501`) in your browser to access the app.

---

## Usage Guide

1. **Access the Main Page**:
   - Open the app in your browser (locally at `http://localhost:8501` or at the deployed URL).
   - You’ll see a sidebar titled "Intelligence Hiring Assistant" and a main section titled "TalentScout's Recruitment Process."

2. **Enter Candidate Details**:
   - In the sidebar, fill out the form with:
     - Full Name (e.g., "G J Rahul")
     - Email Address (e.g., "rahul@example.com")
     - Phone Number (e.g., "1234567890")
     - Years of Experience (e.g., "0")
     - Desired Position (e.g., "Data Scientist")
     - Current Location (e.g., "Hyderabad")
     - Tech Stack (e.g., "Python, LangChain")
   - Click the "Submit" button. If the input passes validation, you’ll be redirected to the interview page.

3. **Participate in the Interview**:
   - The AI will greet you (e.g., "Hello G J Rahul, welcome to TalentScout! Are you ready…?").
   - Respond to the AI’s questions in the chat interface.
   - The AI will ask one question at a time, tailoring follow-ups based on your answers and correctness.
   - After 3-5 questions per tech stack category, the AI will conclude with a thank-you message, and the interview will end.

4. **Deployed App**:
   - If deployed, access the app at the URL provided by Streamlit Community Cloud (e.g., `https://your-app-name.streamlit.app`).

---

## Technical Details

### Libraries Used
- **Streamlit (1.32.0)**: Frontend framework for building the interactive UI.
- **LangChain (0.1.20)**: Framework for integrating the Gemini model, managing prompts, and maintaining conversation memory.
- **langchain-google-genai (1.0.3)**: Integration for Google’s Gemini 1.5 Pro model.
- **google-cloud-storage (2.16.0)**: For potential future integration with Google Cloud Storage (not used in the current version).

### Model Details
- **Model**: Google Gemini 1.5 Pro, accessed via the Vertex AI API.
- **Why Gemini?**: Chosen for its availability through Google Cloud, strong natural language understanding, and integration with LangChain. It supports complex prompt structures and conversational tasks effectively.

### Architectural Decisions
- **Streamlit Multi-Page App**:
  - Used Streamlit’s multi-page feature (`pages/` directory) to separate the main page (`main.py`) for information gathering and the interview page (`testpage.py`).
  - This improves modularity and user experience by splitting the workflow into distinct stages.
- **LangChain with Conversation Memory**:
  - Employed `ConversationBufferMemory` to maintain chat history, ensuring the AI can reference previous questions and responses for continuity.
  - Used a `RunnablePassthrough` to merge chat history into the prompt dynamically.
- **Deployment on Streamlit Community Cloud**:
  - Chose Streamlit Community Cloud for its free hosting, ease of deployment, and support for real-time Streamlit apps without requiring extensive server configuration.

---

## Prompt Design

The prompt, defined in `hiring_process.py` within the `prompt_template()` function, governs how the AI interacts with candidates. It handles both personalization and technical question generation.

### Information Gathering
- The prompt uses data collected from the Streamlit UI (`fullname`, `tech_stack`, `yoe`, `desired_position`) to personalize the interview.
- Example: "Hello {fullname}, welcome to TalentScout! Are you ready to begin your interview for the {desired_position} position?"

### Technical Question Generation
- The prompt instructs the AI to:
  - Ask 3-5 questions per tech stack category (e.g., "Python, LangChain" results in 3-5 Python questions, then 3-5 LangChain questions).
  - Ask **one question at a time** and wait for the candidate’s response before proceeding.
  - Tailor questions based on:
    - Years of experience (`yoe`).
    - Correctness of previous answers (e.g., increase difficulty after 2 correct answers).
- Example Flow:
  - First question: "Python is dynamically typed. What does that mean…?"
  - If answered correctly: "Great job! Let’s dive deeper. How would you optimize a Pandas DataFrame operation…?"

### Key Prompt Features
- **Turn-Based Interaction**: Ensures one question per interaction, using `user_response` and `history` to maintain context.
- **Professional Tone**: Maintains a conversational yet professional demeanor, politely ignoring off-topic requests.

---

## Challenges & Solutions

### Challenge 1: Prompting - Single Shot Question Delivery
- **Problem**: Initially, the AI asked all questions at once and ended the interview prematurely.
- **Solution**: Revised the prompt to enforce turn-based interaction, tracking questions and responses via chat history, and clarifying the end condition.

### Challenge 2: Immediate Window Closure After User Input
- **Problem**: The chat window closed after user input due to Streamlit’s rerun behavior.
- **Solution**: Controlled reruns with `st.rerun()`, moved the completion check after AI responses, and used `st.stop()` to halt interaction without closing the window.

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## Deployment on Streamlit Community Cloud

To deploy this app on Streamlit Community Cloud:

1. **Fork or Clone the Repository**:
   - Fork this repository on GitHub or clone it locally and push your changes to your GitHub repository (e.g., `https://github.com/gjrahul/Data_Science`).

2. **Create a Streamlit Community Cloud Account**:
   - Sign up at [streamlit.io/cloud](https://streamlit.io/cloud) using your GitHub account.

3. **Deploy the App**:
   - Connect your GitHub repository to Streamlit Community Cloud.
   - Select the `AI-Hiring-Assistant` directory and `main.py` as the entry point.
   - Streamlit will automatically detect the `requirements.txt` and deploy the app.
   - Once deployed, you’ll receive a URL (e.g., `https://your-app-name.streamlit.app`).

4. **Configure the API Key**:
   - Since the app uses the Gemini API, add your Google API key as a **Streamlit Community Cloud secret**:
     - In the Streamlit Community Cloud dashboard, go to "Secrets" for your app.
     - Add a secret named `GOOGLE_API_KEY` with your API key value.
     - Update `hiring_process.py` to use the secret:
       ```python
       import os
       api_key = os.getenv("GOOGLE_API_KEY", "your-google-api-key")
       ```
   - This ensures the API key is securely managed in the cloud environment.

5. **Access the App**:
   - Visit the provided URL (e.g., `https://ai-hiring-assistant.streamlit.app/`) to use the deployed app.

---

## Contributing

Contributions are welcome! Please open an issue or submit a pull request on GitHub.

---

### Author
- **G J Rahul** - [Your GitHub Profile](https://github.com/gjrahul)

