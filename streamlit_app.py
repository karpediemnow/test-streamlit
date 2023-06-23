import streamlit as st
import streamlit_authenticator as stauth

#https://blog.streamlit.io/streamlit-quests-getting-started-with-streamlit/#:~:text=Streamlit%20Quests%3A%20Getting%20started%20with%20Streamlit%201%20Two,Streamlit%20apps%20in%20the%20Gallery%20...%20Altri%20elementi


#https://blog.streamlit.io/tag/llms/


def main():
    st.set_page_config(page_title="Test")
    tabHome, tabConfig = st.tabs(["🏠 Home", "🛠️ Config"])
    
    with tabHome:
      #st.image('img/Ask_Book_Questions_Workflow.jpg') 
      st.write("Welcome to Home Page")

    with tabConfig:
       placeholder = st.empty()
       psw = placeholder.text_input("Password to hash:")
       hashed_passwords = stauth.Hasher([psw]).generate()
       st.write("\""+psw+"\"")          






if __name__ == '__main__':
    main()    