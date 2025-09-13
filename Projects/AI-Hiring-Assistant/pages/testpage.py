import streamlit as st
from hiring_process import hiring_assistance

def main():
    st.title("Proctored Interview")

    # Retrieve candidate data from session state
    candidate_data = st.session_state.get("candidate_data", {})
    if not candidate_data:
        st.warning("No candidate data found. Please fill out the details on the main page first.")
        return

    # Display candidate details
    st.write("**Candidate Name:**", candidate_data["full_name"])
    st.write("**Applying For:**", candidate_data["desired_position"])
    st.write("**Experience:**", candidate_data["yoe"], "years")

    # Initialize or reset chat history and interview status
    if "messages" not in st.session_state:
        st.session_state["messages"] = []
    else:
        # Clear invalid entries (strings) from messages
        st.session_state["messages"] = [
            msg for msg in st.session_state["messages"]
            if isinstance(msg, dict) and "role" in msg and "message" in msg
        ]

    if "interview_complete" not in st.session_state:
        st.session_state["interview_complete"] = False

    # AI sends the first greeting if chat history is empty
    if not st.session_state["messages"]:
        initial_response = hiring_assistance(
            full_name=candidate_data["full_name"],
            tech_stack=candidate_data["tech_stack"],
            yoe=candidate_data["yoe"],
            desired_position=candidate_data["desired_position"],
            user_response=""
        )
        st.session_state["messages"].append({"role": "assistant", "message": initial_response})
        st.rerun()  # Rerun to display the initial message

    # Function to display chat history
    def display_chat_history():
        chat_container = st.container()
        with chat_container:
            for message in st.session_state["messages"]:
                if not isinstance(message, dict):
                    st.error("Invalid message format detected in chat history.")
                    continue
                if "role" not in message or "message" not in message:
                    st.error("Invalid message format: missing 'role' or 'message' key.")
                    continue
                with st.chat_message(message["role"]):
                    st.write(message["message"])

    # Display the chat history
    display_chat_history()

    # Handle user input if the interview isn’t complete
    if not st.session_state["interview_complete"]:
        user_input = st.chat_input("Type your response here...", key="user_input")
        if user_input:
            # Append user’s message to chat history
            st.session_state["messages"].append({"role": "user", "message": user_input})

            # Get AI response
            ai_response = hiring_assistance(
                full_name=candidate_data["full_name"],
                tech_stack=candidate_data["tech_stack"],
                yoe=candidate_data["yoe"],
                desired_position=candidate_data["desired_position"],
                user_response=user_input
            )

            # Append AI response to chat history
            st.session_state["messages"].append({"role": "assistant", "message": ai_response})

            # Check if the interview is complete
            if "Thank you for taking the interview" in ai_response:
                st.session_state["interview_complete"] = True

            # Rerun to update the UI with the new messages
            st.rerun()

    # Display completion message if interview is over
    if st.session_state["interview_complete"]:
        st.success("The interview has concluded. Thank you for your time. Please close this window.")

        st.stop()

if __name__ == "__main__":
    main()