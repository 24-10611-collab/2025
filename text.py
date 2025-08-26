import streamlit as st

# 페이지 설정
st.set_page_config(page_title="MBTI 궁합 테스트", page_icon="💖")

# MBTI 궁합 데이터
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

# 제목
st.title("🌟 MBTI 궁합 테스트 🌟")
st.markdown("✨ 당신의 성격 유형과 잘 맞는 MBTI 궁합을 확인해보세요! ✨")

# 드롭다운
user_mbti = st.selectbox("👇 당신의 MBTI를 선택하세요 👇", list(compatibility.keys()))

# 결과 출력
st.success(
    f"💘 당신의 MBTI **[{user_mbti}]** 와 잘 맞는 유형은 👉 {', '.join(compatibility[user_mbti])} 👈 입니다! 🎯"
)

# 이미지 표시
try:
    st.image(f"images/{user_mbti}.png", width=250)
except FileNotFoundError:
    st.warning("⚠️ 해당 MBTI 이미지가 없습니다. images 폴더에 추가해주세요!")

# 추가 안내
st.info("📖 참고: 이 결과는 재미로 보는 MBTI 궁합이에요. 실제 성격은 다를 수 있어요 😆")
