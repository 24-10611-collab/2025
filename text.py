
import streamlit as st

# MBTI 궁합 데이터 (간단 예시)
compatibility = {
    "INTJ": ["ENFP", "ENTP"],
    "INTP": ["ENTJ", "ESTJ"],
    "ENTJ": ["INTP", "INFJ"],
    "ENTP": ["INFJ", "INTJ"],
    "INFJ": ["ENFP", "ENTP"],
    "INFP": ["ENFJ", "ENTJ"],
    "ENFJ": ["INFP", "ISFP"],
    "ENFP": ["INFJ", "INTJ"],
    "ISTJ": ["ESFP", "ESTP"],
    "ISFJ": ["ESFP", "ESTP"],
    "ESTJ": ["ISTP", "INTP"],
    "ESFJ": ["ISFP", "ISTP"],
    "ISTP": ["ESTJ", "ESFJ"],
    "ISFP": ["ENFJ", "ESFJ"],
    "ESTP": ["ISFJ", "ISTJ"],
    "ESFP": ["ISTJ", "ISFJ"],
}

st.set_page_config(page_title="MBTI 궁합 테스트", page_icon="💖")

st.title("💖 MBTI 궁합 웹")
st.write("자신의 MBTI를 입력하면 잘 맞는 MBTI 유형을 알려드립니다!")

# 사용자 입력
user_mbti = st.text_input("당신의 MBTI를 입력해주세요 (예: INFP)").upper()

if user_mbti:
    if user_mbti in compatibility:
        matches = compatibility[user_mbti]
        st.success(f"당신의 MBTI [{user_mbti}]와 잘 맞는 유형은 👉 {', '.join(matches)} 입니다!")
    else:
        st.error("올바른 MBTI를 입력해주세요. (예: INFP, ENTP 등)")
