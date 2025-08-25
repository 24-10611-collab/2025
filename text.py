import streamlit as st

# 페이지 설정 (맨 위에!)
st.set_page_config(page_title="MBTI 궁합 테스트", page_icon="💖")

# MBTI 궁합 데이터 (심플 버전 + 이모지)
compatibility = {
    "INTJ": ["ENFP 🌈", "ENTP 💡"],
    "INTP": ["ENTJ 🚀", "ESTJ 📊"],
    "ENTJ": ["INTP 🔍", "INFJ 🔮"],
    "ENTP": ["INFJ ✨", "INTJ 🧩"],
    "INFJ": ["ENFP 🌟", "ENTP 🎉"],
    "INFP": ["ENFJ 🤝", "ENTJ 🏆"],
    "ENFJ": ["INFP 🌙", "ISFP 🎨"],
    "ENFP": ["INFJ 🌌", "INTJ 🧠"],
    "ISTJ": ["ESFP 🎭", "ESTP 🏄"],
    "ISFJ": ["ESFP 🎵", "ESTP 🏃"],
    "ESTJ": ["ISTP 🛠", "INTP 🧪"],
    "ESFJ": ["ISFP 🌺", "ISTP 🔧"],
    "ISTP": ["ESTJ 🗂", "ESFJ 💐"],
    "ISFP": ["ENFJ 🌹", "ESFJ 🎀"],
    "ESTP": ["ISFJ 🕊", "ISTJ 🛡"],
    "ESFP": ["ISTJ 🧱", "ISFJ 🌷"],
}

# 타이틀
st.title("🌟 MBTI 궁합 테스트 🌟")
st.markdown("✨ 당신의 성격 유형과 잘 맞는 MBTI 궁합을 확인해보세요! ✨")

# 드롭다운으로 MBTI 선택
user_mbti = st.selectbox("👇 당신의 MBTI를 선택하세요 👇", list(compatibility.keys()))

# 결과 출력
st.success(f"💘 당신의 MBTI **[{user_mbti}]** 와 잘 맞는 유형은 👉 {', '.join(compatibility[user_mbti])} 👈 입니다! 🎯")
st.info("📖 참고: 이 결과는 재미로 보는 MBTI 궁합입니다. 실제 성격은 다를 수 있어요 😆")
