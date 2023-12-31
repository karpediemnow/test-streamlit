import streamlit as st
#import streamlit_authenticator as stauth

#https://blog.streamlit.io/streamlit-quests-getting-started-with-streamlit/#:~:text=Streamlit%20Quests%3A%20Getting%20started%20with%20Streamlit%201%20Two,Streamlit%20apps%20in%20the%20Gallery%20...%20Altri%20elementi


#https://blog.streamlit.io/tag/llms/

#https://docs.streamlit.io/streamlit-community-cloud/get-started/deploy-an-app/connect-to-data-sources/secrets-management

#https://docs.streamlit.io/library/api-reference/session-state

def main():
    st.set_page_config(page_title="Test")
    tabHome, tabConfig = st.tabs(["🏠 Home", "🛠️ Config"])
    
    with tabHome:
      #st.image('img/Ask_Book_Questions_Workflow.jpg') 
      st.write("Welcome to Home Page")

    with tabConfig:
       
       # Everything is accessible via the st.secrets dict:
       st.write("DB username:", st.secrets["db_username"])
       st.write("DB password:", st.secrets["db_password"])
       st.write("My cool secrets:", st.secrets["my_cool_secrets"]["things_i_like"])

       #placeholder = st.empty()
       #psw = placeholder.text_input("Password to hash:")
       #hashed_passwords = stauth.Hasher([psw]).generate()
       #st.write("\""+hashed_passwords+"\"")          






if __name__ == '__main__':
    main()    