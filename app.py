
import streamlit as st

from src.screens.home_screen import home_screen
from src.screens.teacher_screen import teacher_screen
from src.screens.student_screen import student_screen

from src.components.dialog_auto_enroll import auto_enroll_dialog

def main():
    st.set_page_config(
        page_title='SnapClass - Making Attendance faster using AI',
        page_icon="https://i.ibb.co/YTYGn5qV/logo.png"
    )

    if 'login_type' not in st.session_state:
        st.session_state['login_type'] = None

    # Read join code from URL and persist in session_state
    join_code = st.query_params.get('join-code')
    if join_code and 'join_code' not in st.session_state:
        st.session_state.join_code = join_code

    # Use session_state for join_code (persists across reruns)
    stored_join_code = st.session_state.get('join_code')

    # If join code exists, switch to student screen
    if stored_join_code:
        if st.session_state.login_type != 'student':
            st.session_state.login_type = 'student'
            st.rerun()

    match st.session_state['login_type']:
        case 'teacher':
            teacher_screen()

        case 'student':
            student_screen()

        case None:
            home_screen()

    # Auto enroll student
    if (
        stored_join_code
        and st.session_state.get('is_logged_in')
        and st.session_state.get('user_role') == 'student'
    ):
        auto_enroll_dialog(stored_join_code)
        # Clear after use to prevent re-enrollment
        del st.session_state.join_code


if __name__ == "__main__":
    main()
