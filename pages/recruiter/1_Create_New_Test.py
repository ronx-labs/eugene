import streamlit as st
from streamlit_extras.switch_page_button import switch_page
from st_pages import show_pages, Page, hide_pages

from utils.init import initialize_app
from utils.components import sidebar_logout


def create_new_test():
    # Page Config
    st.set_page_config(
        page_title="New Test | Neuradev Coding Test Platform",
        initial_sidebar_state="expanded",
    )
    
    # Show/Hide Pages on Sidebar
    show_pages([
        Page(path='Home.py'),
        Page(path='pages/recruiter/1_Create_New_Test.py'),
        Page(path='pages/recruiter/2_My_Tests.py'),
    ])
    hide_pages(["candidate"])
    
    # Add Logout button to sidebar
    sidebar_logout()
    
    # Header
    st.header("Create New Test")
    
    
# Run the Streamlit app
if __name__ == '__main__':
    initialize_app()
    
    if st.session_state.is_authenticated and st.session_state.role == "recruiter":
        create_new_test()
    else:
        switch_page('home')