import streamlit as st

# --- 페이지 기본 설정 ---
st.set_page_config(
    page_title="타이탄 롤 아카데미",
    page_icon="🏆",
    layout="wide"
)

# --- 커스텀 CSS 스타일 (React 프리미엄 테마 반영) ---
st.markdown("""
<style>
    body { background-color: #020617; color: #f1f5f9; }
    .main-hero { text-align: center; padding: 60px 20px; background: linear-gradient(180deg, #0b1329 0%, #020617 100%); border-bottom: 1px solid #1e293b; margin-bottom: 40px; }
    .hero-title { font-size: 2.5rem; font-weight: 900; color: #ffffff; margin-bottom: 10px; }
    .hero-subtitle { font-size: 1.1rem; color: #d97706; font-weight: bold; letter-spacing: 2px; margin-bottom: 25px; }
    .card { background-color: #0b1329; padding: 24px; border-radius: 12px; margin-bottom: 20px; border: 1px solid #1e293b; transition: transform 0.3s ease; }
    .card:hover { border-color: #d97706; }
    .card-title { font-size: 1.2rem; font-weight: bold; color: #ffffff; margin-bottom: 8px; }
    .card-desc { color: #94a3b8; font-size: 0.9rem; line-height: 1.6; }
    .badge-gold { background-color: rgba(217, 119, 6, 0.1); color: #f59e0b; padding: 4px 12px; border-radius: 20px; font-size: 0.75rem; font-weight: bold; display: inline-block; margin-bottom: 10px; border: 1px solid rgba(217, 119, 6, 0.2); }
    .price-text { font-size: 1.5rem; font-weight: 800; color: #f59e0b; margin-top: 10px; }
    .footer { text-align: center; padding: 40px 20px; color: #64748b; font-size: 0.8rem; border-top: 1px solid #1e293b; margin-top: 60px; }
</style>
""", unsafe_allow_html=True)

# 메인 기능 구현
st.markdown('<div class="main-hero"><div class="hero-title">🏆 TITAN GAME COACHING COMPANY</div><div class="hero-subtitle">롤 대리 듀오 강의 전문 타이탄팀</div></div>', unsafe_allow_html=True)
st.link_button("🔥 카카오톡 1:1 실시간 상담 채널 연결", "https://open.kakao.com/o/sZPAcRri", use_container_width=True)

# 폼 구현
with st.form("consultation_form"):
    gamertag = st.text_input("소환사 닉네임 (계정명)")
    current_tier = st.text_input("현재 정확한 티어 / LP")
    position = st.selectbox("신청하실 주 포지션 라인", ["TOP", "JUG", "MID", "ADC", "SUP", "ALL"])
    submitted = st.form_submit_button("🚀 상담 양식 자동 생성")
    if submitted:
        st.code(f"소환사명: {gamertag}\n현재티어: {current_tier}\n포지션: {position}", language="markdown")
