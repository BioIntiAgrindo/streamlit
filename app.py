import pandas as pd
import plotly.graph_objects as go
import streamlit as st

# 비밀번호 설정 (이곳에 원하는 비밀번호를 입력하세요)
PASSWORD = "bia2024"

# 비밀번호 입력 받기
st.title("비공개 동적 통계 페이지")
password = st.text_input("비밀번호를 입력하세요", type="password")

# 비밀번호 검증
if password == PASSWORD:
    st.success("비밀번호가 일치합니다!")

    # 엑셀 파일 불러오기
    file_path = '설문최종문서.xlsx'  # 엑셀 파일 경로
    data = pd.read_excel(file_path, sheet_name='Sheet1')

    # "Average" 제외한 이름 필터링
    names_list = data['Name'].dropna().unique().tolist()
    filtered_names = [name for name in names_list if "Average" not in name]

    # "Average" 행 데이터 추출 (평균 값)
    average_data = data[data['Name'] == 'Average'].iloc[0].loc['Q1':'Q13'].values

    # 이름 선택 박스 생성 (검색 가능하도록 설정)
    selected_name = st.sidebar.selectbox("이름을 선택하세요:", filtered_names, key="name_select")

    # 선택한 이름의 정보와 데이터 가져오기
    individual_data = data[data['Name'] == selected_name]

    # 개인 정보 표시
    st.write(f"### 이름: {selected_name}")
    st.write(f"**Area:** {individual_data['area'].values[0]}")
    st.write(f"**Department:** {individual_data['department'].values[0]}")
    st.write(f"**Posisi:** {individual_data['posisi'].values[0]}")

    # Q1~Q13, SQ1~SQ13 점수 추출
    peer_evaluation = individual_data.loc[:, 'Q1':'Q13'].values.flatten()
    self_evaluation = individual_data.loc[:, 'SQ1':'SQ13'].values.flatten()

    # Plotly를 사용한 반응형 그래프 생성
    fig = go.Figure()

    # Peer Evaluation 점수 플롯
    fig.add_trace(go.Scatter(
        x=list(range(1, 14)),
        y=peer_evaluation,
        mode='markers+lines',
        name="Peer Evaluation (Q1-Q13)",
        marker=dict(color='blue'),
        hovertemplate='Peer Score: %{y}<extra></extra>'
    ))

    # Average 점수 플롯
    fig.add_trace(go.Scatter(
        x=list(range(1, 14)),
        y=average_data,
        mode='markers+lines',
        name="Average (Q1-Q13)",
        marker=dict(color='green'),
        hovertemplate='Average Score: %{y}<extra></extra>'
    ))

    # Self Evaluation 점수 플롯
    fig.add_trace(go.Scatter(
        x=list(range(1, 14)),
        y=self_evaluation,
        mode='markers+lines',
        name="Self Evaluation (SQ1-SQ13)",
        marker=dict(color='red'),
        hovertemplate='Self Score: %{y}<extra></extra>'
    ))

    # 그래프 레이아웃 설정
    fig.update_layout(
        title=f"Evaluation Scores for {selected_name}",
        xaxis_title="Question Number",
        yaxis_title="Score",
        legend_title="Evaluation Type",
        hovermode="x"
    )

    # Streamlit에 Plotly 그래프 표시
    st.plotly_chart(fig)

    # 각 문항별 자가평가, 상향평가, 평균, 평균과 상향평가의 차이 계산
    question_numbers = [f"Q{i}" for i in range(1, 14)]
    evaluation_data = {
        "Self Evaluation": self_evaluation,
        "Peer Evaluation": peer_evaluation,
        "Average": average_data,
        "Difference (Average - Peer)": average_data - peer_evaluation
    }

    # DataFrame 생성 및 전치, 인덱스 숨기기
    evaluation_df = pd.DataFrame(evaluation_data, index=question_numbers).T
    st.write("### 각 문항별 점수 비교")
    st.dataframe(evaluation_df.style.format(precision=2), use_container_width=True)

    # 정성 평가 구분 선택 박스 추가
    st.sidebar.header("정성 평가 구분 선택")
    evaluation_type = st.sidebar.radio("정성 평가 구분을 선택하세요:", ["자가 평가", "상향 평가"])

    # 선택된 평가 구분에 따른 코멘트 출력 함수
    def display_comments(comments):
        for q, text in comments.items():
            st.write(f"**{q}**: {text if pd.notna(text) else 'No response provided'}")

    # 자가 평가 또는 상향 평가에 따른 코멘트 가져오기 및 표시
    if evaluation_type == "자가 평가":
        self_comments = {
            'SQ14 (Self-Strengths)': individual_data['SQ14'].values[0],
            'SQ15 (Self-Areas for Improvement)': individual_data['SQ15'].values[0],
            'SQ16 (Self-Additional Comments)': individual_data['SQ16'].values[0]
        }
        st.write("### Self-Evaluation Comments")
        display_comments(self_comments)
    else:
        peer_comments = {
            'Q14 (Strengths)': individual_data['Q14'].values[0],
            'Q15 (Areas for Improvement)': individual_data['Q15'].values[0],
            'Q16 (Additional Comments)': individual_data['Q16'].values[0]
        }
        st.write("### Peer Evaluation Comments")
        display_comments(peer_comments)

else:
    st.error("올바른 비밀번호를 입력하세요.")