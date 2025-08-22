import streamlit as st

# MBTI 궁합 데이터 (간단 예시 + 설명 추가)
compatibility = {
    "INTJ": {
        "best": ["ENFP", "ENTP"],
        "desc": "계획적이고 전략적인 INTJ는 자유롭고 창의적인 ENFP/ENTP와 좋은 시너지를 냅니다."
    },
    "INTP": {
        "best": ["ENTJ", "ESTJ"],
        "desc": "아이디어가 많은 INTP는 추진력 있는 ENTJ/ESTJ와 궁합이 잘 맞습니다."
    },
    "ENTJ": {
        "best": ["INTP", "INFJ"],
        "desc": "리더십 강한 ENTJ는 사색적인 INTP, 깊이 있는 INFJ와 잘 어울립니다."
    },
    "ENTP": {
        "best": ["INFJ", "INTJ"],
        "desc": "새로움과 변화를 추구하는 ENTP는 통찰력 있는 INFJ/INTJ와 좋은 조합입니다."
    },
    "INFJ": {
        "best": ["ENFP", "ENTP"],
        "desc": "사람에 대한 통찰력이 뛰어난 INFJ는 활발한 ENFP/ENTP와 잘 맞습니다."
    },
    "INFP": {
        "best": ["ENFJ", "ENTJ"],
        "desc": "이상주의적인 INFP는 이끌어주는 ENFJ/ENTJ와 좋은 관계를 맺습니다."
    },
    "ENFJ": {
        "best": ["INFP", "ISFP"],
        "desc": "타인을 배려하는 ENFJ는 따뜻한 INFP/ISFP와 궁합이 좋습니다."
    },
    "ENFP": {
        "best": ["INFJ", "INTJ"],
        "desc": "에너지가 넘치는 ENFP는 통찰력 있는 INFJ/INTJ와 좋은 관계를 형성합니다."
    },
    "ISTJ": {
        "best": ["ESFP", "ESTP"],
        "desc": "원칙적인 ISTJ는 자유로운 ESFP/ESTP와 균형을 이룹니다."
    },
    "ISFJ": {
        "best": ["ESFP", "ESTP"],
        "desc": "헌신적인 ISFJ는 활발한 ESFP/ESTP와 잘 맞습니다."
    },
    "ESTJ": {
        "best": ["ISTP", "INTP"],
        "desc": "체계적인 ESTJ는 유연한 ISTP/INTP와 궁합이 좋습니다."
    },
    "ESFJ": {
        "best": ["ISFP", "ISTP"],
        "desc": "친절한 ESFJ는 온화한 ISFP/ISTP와 잘 어울립니다."
    },
    "ISTP": {
        "best": ["ESTJ", "ESFJ"],
        "desc": "실용적인 ISTP는 조직적인 ESTJ, 따뜻한 ESFJ와 좋은 관계를 가집니다."
    },
    "ISFP": {
        "best": ["ENFJ", "ESFJ"],
        "desc": "예술적 감각이 뛰어난 ISFP는 따뜻한 ENFJ/ESFJ와 궁합이 좋습니다."
    },
    "ESTP": {
        "best": ["ISFJ", "ISTJ"],
        "desc": "도전적인 ESTP는 안정적인 ISFJ/ISTJ와 좋은 균형을 이룹니다."
    },
    "ESFP": {
        "best": ["ISTJ", "ISFJ"],
        "desc": "즐거움을 추구하는 ESFP는 책임감 있는 ISTJ/ISFJ와 잘 맞습니다."
    }
}

# 페이지 설정
st.set_page_config(page_title="MBTI 궁합 테스트", page_icon="💖")

# 제목
st.title("💖 MBTI 궁합 웹")
st.write("당신의 MBTI를 선택하면 잘 맞는 유형과 설명을 알려드립니다!")

# 드롭다운으로 MBTI 선택
mbti_list = list(compatibility.keys())
user_mbti = st.selectbox("당신의 MBTI를 선택하세요", mbti_list)

# 결과 출력
if user_mbti:
    data = compatibility[user_mbti]
    st.markdown(f"### 🌟 당신의 MBTI [{user_mbti}] 궁합 결과 🌟")
    st.success(f"✅ 잘 맞는 유형: {', '.join(data['best'])}")
    st.info(f"💡 설명: {data['desc']}")

