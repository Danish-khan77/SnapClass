
import streamlit as st


def footer_home():
    logo_url = "https://i.ibb.co/vC11yQB0/Dk-logo.png"

    st.markdown(f"""
        <div style="
            margin-top: 2rem;
            display: flex;
            gap: 6px;
            justify-content: center;
            align-items: center;
        ">
            <p style="
                font-weight: bold;
                color: white;
                margin: 0;
                line-height: 25px;
            ">
                Created with ❤️ by
            </p>

            <img src="{logo_url}" style="
                height: 25px;
                width: auto;
                display: block;
                object-fit: contain;
            ">
        </div>
    """, unsafe_allow_html=True)


def footer_dashboard():
    logo_url = "https://i.ibb.co/vC11yQB0/Dk-logo.png"

    st.markdown(f"""
        <div style="
            margin-top: 2rem;
            display: flex;
            gap: 6px;
            justify-content: center;
            align-items: center;
        ">
            <p style="
                font-weight: bold;
                color: black;
                margin: 0;
                line-height: 25px;
            ">
                Created with ❤️ by
            </p>

            <img src="{logo_url}" style="
                height: 25px;
                width: auto;
                display: block;
                object-fit: contain;
            ">
        </div>
    """, unsafe_allow_html=True)
