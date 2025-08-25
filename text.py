import streamlit as st

# 페이지 설정 (항상 최상단)
st.set_page_config(page_title="💖 MBTI 궁합 테스트 💖", page_icon="🌟")

# MBTI 궁합 데이터
compatibility = {
    "INTJ": {"best": ["ENFP 🌈", "ENTP 💡"], "desc": "🧠 계획적인 INTJ는 자유로운 ENFP/ENTP와 잘 맞습니다."},
    "INFP": {"best": ["ENFJ 🤝", "ENTJ 🏆"], "desc": "🌸 이상주의적인 INFP는 이끌어주는 ENFJ/ENTJ와 좋은 관계를 맺습니다."},
    "ENTJ": {"best": ["INTP 🔍", "INFJ 🔮"], "desc": "👑 리더십 강한 ENTJ는 사색적인 INTP/INFJ와 잘 맞습니다."},
    "ENFP": {"best": ["INFJ ✨", "INTJ 🧩"], "desc": "⚡ 에너지가 넘치는 ENFP는 통찰력 있는 INFJ/INTJ와 궁합이 좋습니다."},
    "INTP": {"best": ["ENTJ 🚀", "ESTJ 📊"], "desc": "💡 아이디어 많은 INTP는 추진력 있는 ENTJ/ESTJ와 잘 맞습니다."},
    "INFJ": {"best": ["ENFP 🌟", "ENTP 🎉"], "desc": "🔮 통찰력 있는 INFJ는 활발한 ENFP/ENTP와 시너지가 좋습니다."},
    "ESTJ": {"best": ["ISTP 🛠", "INTP 🧪"], "desc": "📏 체계적인 ESTJ는 유연한 ISTP/INTP와 궁합이 좋습니다."},
    "ESFJ": {"best": ["ISFP 🎨", "ISTP 🔧"], "desc": "💞 친절한 ESFJ는 온화한 ISFP/ISTP와 잘 어울립니다."},
    "ISTJ": {"best": ["ESFP 🎭", "ESTP 🏄"], "desc": "📚 원칙적인 ISTJ는 자유로운 ESFP/ESTP와 균형이 좋습니다."},
    "ISFJ": {"best": ["ESFP 🎵", "ESTP 🏃"], "desc": "🌼 헌신적인 ISFJ는 활발한 ESFP/ESTP와 잘 맞습니다."},
    "ISTP": {"best": ["ESTJ 🗂", "ESFJ 💐"], "desc": "🛠 실용적인 ISTP는 조직적인 ESTJ/ESFJ와 좋은 관계를 가집니다."},
    "ISFP": {"best": ["ENFJ 🌹", "ESFJ 🎀"], "desc": "🎨 예술적인 ISFP는 따뜻한 ENFJ/ESFJ와 궁합이 좋습니다."},
    "ESTP": {"best": ["ISFJ 🕊", "ISTJ 🛡"], "desc": "🔥 도전적인 ESTP는 안정적인 ISFJ/ISTJ와 좋은 균형을 이룹니다."},
    "ESFP": {"best": ["ISTJ 🧱", "ISFJ 🌷"], "desc": "🎉 즐거움을 추구하
