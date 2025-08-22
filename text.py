import streamlit as st

# MBTI 궁합 데이터 (best + 설명 + 이미지 URL)
compatibility = {
    "INTJ": {
        "best": ["ENFP", "ENTP"],
        "desc": "계획적인 INTJ는 자유로운 ENFP/ENTP와 잘 맞습니다.",
        "img": "https://i.imgur.com/8k5RZ0y.png"
    },
    "INFP": {
        "best": ["ENFJ", "ENTJ"],
        "desc": "이상주의적인 INFP는 이끌어주는 ENFJ/ENTJ와 좋은 관계를 맺습니다.",
        "img": "https://i.imgur.com/Q4KQ9Jl.png"
    },
    "ENFP": {
        "best": ["INFJ", "INTJ"],
        "desc": "에너지가 넘치는 ENFP는 통찰력 있는 INFJ/INTJ와 좋은 관계를 형성합니다.",
        "img": "https://i.imgur.com/3QXbU0C.png"
    },
    "ESTJ": {
        "best": ["ISTP", "INTP"],
        "desc": "체계적인 ESTJ는 유연한 ISTP/INTP와 궁합이 좋습니다.",
        "img": "https://i.imgur.com/2EdmCck.png"
    },
    # 👉 나머지 MBTI도 같은 방식으로 추가 가능
}

# 웹 페이지 설정
st.set_page_config(page_title="MBTI 궁합 테스트", page_icon="💖")

# 제목
st.title("💖 MBTI 궁합 웹")

# MBTI 선택 입력
user_mbti = st.selectbox("당신의 MBTI를 선택하세요", list(compatibility.keys()))

# 결과 출력
data = compatibility[user_mbti]
st.image(data["img"], width=250)  # MBTI 이미지 표시
st.success(f"✅ [{user_mbti}]와 잘 맞는 유형: {', '.join(data['best'])}")
st.info(f"💡 {data['desc']}")
