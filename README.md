import streamlit as st

# MBTI별 추천 직업 데이터 (16유형)
career_dict = {
    "ISTJ": ["📊 회계사", "🏛️ 행정 공무원", "📋 프로젝트 매니저"],
    "ISFJ": ["🩺 간호사", "👩‍🏫 교사", "🤝 사회복지사"],
    "INFJ": ["🧠 심리상담가", "✍️ 작가", "⚖️ 인권 변호사"],
    "INTJ": ["📈 데이터 과학자", "🧑‍💼 전략 컨설턴트", "🔬 연구원"],

    "ISTP": ["⚙️ 엔지니어", "🛩️ 파일럿", "🚑 응급 구조사"],
    "ISFP": ["🎨 디자이너", "🎭 예술가", "💆 물리치료사"],
    "INFP": ["📚 작가", "💬 상담가", "🌍 사회운동가"],
    "INTP": ["🧑‍🔬 연구원", "💻 소프트웨어 개발자", "🎓 교수"],

    "ESTP": ["💼 세일즈 매니저", "🚀 기업가", "⚽ 스포츠 코치"],
    "ESFP": ["🎤 배우", "🌍 여행 가이드", "🎉 이벤트 플래너"],
    "ENFP": ["📢 마케터", "📰 언론인", "🌱 창업가"],
    "ENTP": ["⚖️ 변호사", "💡 벤처기업가", "📺 광고 전문가"],

    "ESTJ": ["🪖 군인", "🏢 경영자", "📂 프로젝트 매니저"],
    "ESFJ": ["🍎 초등교사", "👩‍⚕️ 간호사", "🙋 HR 전문가"],
    "ENFJ": ["📚 교육자", "🎤 정치인", "🤲 커뮤니티 리더"],
    "ENTJ": ["👔 CEO", "⚖️ 변호사", "📊 투자 분석가"]
}

# 페이지 설정
st.set_page_config(page_title="MBTI 진로 추천", page_icon="🌟", layout="centered")

# 타이틀
st.markdown("<h1 style='text-align: center; color: #FF69B4;'>🌈✨ MBTI 기반 진로 추천기 ✨🌈</h1>", unsafe_allow_html=True)
st.write("당신의 MBTI를 선택하면 어울리는 진로를 화려하게 추천해드릴게요 💎")

st.markdown("---")

# MBTI 선택
mbti_list = list(career_dict.keys())
user_mbti = st.selectbox("💖 당신의 MBTI를 선택하세요 💖", mbti_list)

# 결과 출력
if user_mbti:
    st.markdown(f"<h2 style='color: #FFD700;'>🌟 {user_mbti} 유형에게 어울리는 진로 🌟</h2>", unsafe_allow_html=True)
    careers = career_dict.get(user_mbti, [])
    
    for c in careers:
        st.markdown(f"<div style='font-size:20px; padding:5px;'>✨ {c}</div>", unsafe_allow_html=True)

    st.markdown("---")
    st.success("💡 자신에게 맞는 진로를 찾아보세요! 🚀")
