import pandas as pd
import plotly.graph_objects as go
import streamlit as st

# 비밀번호 설정
PASSWORD = "bia2024"
password_dic = {
    'Abdul Kholik': '200426',
    'Aceng': '537550',
    'Adi Rk Pebrianto': '338091',
    'Adi Satria Armanda Ginting': '882500',
    'Agung Gita Kurniawan': '327915',
    'Agung Riyanto': '713820',
    'Agustinus Nampur': '756677',
    'Ahmad Mulia Mediansyah': '226741',
    'Akbar Aziz': '663610',
    'An Byung Sung': '574316',
    'Andy Siyar Irawan': '651843',
    'Angga Yudha Prasetya': '780697',
    'Anggraeni Fajri Tri Astari': '419572',
    'Arie Setiawan': '448771',
    'Arif Rahman': '426512',
    'Aris Sayogo': '974746',
    'Asman': '158433',
    'Average': '277700',
    'Azis': '359220',
    'Bae Gyu Tae': '481981',
    'Baek Jong Hoon': '318180',
    'Bambang Winarto': '795467',
    'Bernard Irawan Sembiring': '699366',
    'Brahmation Riko Santoso': '342437',
    'Cho Seong Rong': '824757',
    'Crispin Utomo': '636663',
    'Dani Irfan': '783122',
    'Debel Tandibua': '240364',
    'Dedi Arapenta Purba': '275608',
    'Defri Sudianto Ariwibowo': '499610',
    'Detha Anggelina': '237353',
    'Dian Samodro Septiano': '878676',
    'Dony Randa': '435037',
    'Edoardus Welhelmus Kolyaan': '634447',
    'Eko Saputro': '875412',
    'Elfridus Anci': '858689',
    'Endang Belopadang': '427501',
    'Erwan': '459521',
    'Ester Suwarsih': '334877',
    'Feiby Pandean': '173567',
    'Fendi Prastyawan': '592256',
    'Fransiskus Halmon': '793807',
    'Fransiskus Siku Hayon': '898975',
    'Habel Upessy': '761011',
    'Han Seungwoo': '304351',
    'Hanto Wibowo': '974091',
    'Haris Hamdani': '669915',
    'Hariyanto Arif': '851582',
    'Hendra Sareng': '582855',
    'Heri Frando Siadari': '421169',
    'Hilarius Gedi': '764957',
    'Hong Jung Hwan': '835552',
    'Idham Ikhsan': '485056',
    "Imam Syafi'I": '805062',
    'Imran Nasution': '546661',
    'Irfan Syarifandhy': '611661',
    'Jeffri Sitakar': '866654',
    'Jeong Gi Won': '235833',
    'Jesika Baure': '837398',
    'Jon Kotiaro Petrus Manurung': '598368',
    'Jonathan Darma Putra': '635451',
    'Juanda Syah Tamin': '204315',
    'Karsam': '329404',
    'Kartika Dewi': '204945',
    'Kim Dong Ho': '371647',
    'Kim Inwoog': '765271',
    'Kim Jaewon': '493530',
    'Kostantinus Laluur': '138804',
    'Lee Min Woo': '905189',
    'Lee Nam Kyu': '456675',
    'Lee Sol': '495324',
    'Li Yonghao': '502236',
    'Lili Sampe': '207922',
    'M.Imanudin': '798518',
    'Mad Soleh': '737433',
    'Maharani Rahman': '811569',
    'Mahdian Wiratama': '950084',
    'Marjuki': '615287',
    'Moh. Ardhan Azwir': '802894',
    'Mohamad Muhtarom': '142537',
    'Mualim': '438033',
    'Muhamad Kayono': '948959',
    'Muhamad Muchlis Aman': '804480',
    'Mulyana': '596039',
    'Muskholil': '540701',
    'Nico Yossi Noya': '672354',
    'Novita E. Manumpil': '167331',
    'Octavianus Rapang Pakabu': '896831',
    'Park Chan Hyo': '904834',
    'Petrus Arifin': '793619',
    'Purnama Sari Septa Wijaya': '791915',
    'Renate Rita Theresia Rahaor': '883922',
    "Reynaldi Ta'Bi Sulung": '165518',
    'Reyndra Restu Perkasa': '536874',
    'Rifa’I Marzuki Hasibuan': '418365',
    'Riswadi': '280404',
    'Rubadi': '183548',
    'Sabar Raden Sinambela': '546032',
    'Saiful Anwar': '129628',
    'Saldi Baco': '319374',
    'Sartonah': '663297',
    'Sigit Eko Sunarso': '139973',
    'Silviana Wotos': '489898',
    'Simon Lamalewa': '352203',
    'Sinta Iriani': '473806',
    'Slamet Riyadi': '204181',
    'Sodikin': '488610',
    'Song Hong Ju': '570441',
    'Song In An': '162047',
    'Subali': '864738',
    'Sugeng Riyadi': '437529',
    'Sugianto': '745770',
    'Suhartono': '118300',
    'Sukarwan': '419025',
    'Sukino': '210193',
    'Sumrakih': '444045',
    'Sunardi': '659816',
    'Suparno': '569876',
    'Suprapto': '642167',
    'Suprayitno': '317265',
    'Supriyadi': '503057',
    'Supriyono': '474086',
    'Susiswo': '548895',
    'Suwanda': '739722',
    'Syamsul Bahri': '145236',
    'Tae Rongxun': '207172',
    'Widia Hartiningsih,Sh': '621825',
    'Wilfridus Nong Very': '790053',
    'Wolgam Simtoma Doka Goa': '953577',
    'Yoo Jae Kwan': '885627',
    'Yoseph Dominikus Resi': '972137',
    'Yulianety Patabang': '378352',
    'Yustus Rahawarin': '272410',
    'Yusuf Abdul Ghofur': '763789',
}

master_key = "presdir"

# 로그인 정보 입력
st.sidebar.title("리더십 설문 결과")
password = st.sidebar.text_input("비밀번호를 입력하세요", type="password")

# 로그인 사용자 이름 초기화
user_name = None

# 비밀번호 검증
if password == PASSWORD or password == master_key or password in password_dic.values():
    if password in password_dic.values():
        # 일반 사용자로 로그인한 경우 해당 사용자의 이름 찾기
        user_name = next((name for name, pw in password_dic.items() if pw == password), None)
        st.sidebar.success(f"{user_name}님으로 로그인되었습니다!")
    elif password == PASSWORD or password == master_key:
        # 관리자 계정으로 로그인한 경우
        st.sidebar.success("관리자 계정으로 로그인되었습니다!")

    # 엑셀 파일 불러오기 (설문 데이터)
    file_path = '설문최종문서.xlsx'
    data = pd.read_excel(file_path, sheet_name='Sheet1')

    # 문항 내용 엑셀 파일 불러오기
    question_file_path = '설문문항.xlsx'
    question_data = pd.read_excel(question_file_path)

    # 상향 평가 문항 (Q1~Q13)과 자가 평가 문항 (SQ1~SQ13) 필터링
    peer_questions = question_data[question_data['문항번호'].str.startswith('Q')]
    self_questions = question_data[question_data['문항번호'].str.startswith('SQ')]

    # "Average" 제외한 이름 필터링 및 평균 점수 기준으로 정렬
    data_filtered = data[data['Name'] != 'Average']
    data_filtered['Average Score'] = data_filtered.loc[:, 'Q1':'Q13'].mean(axis=1)
    data_filtered = data_filtered[['Name', 'Average Score']].sort_values(by='Average Score', ascending=False)
    data_filtered['Rank'] = range(1, len(data_filtered) + 1)
    total_people = len(data_filtered)

    # 사용자 접근 제한 설정
    if user_name:
        # 일반 사용자일 때: 본인만 볼 수 있도록 데이터 필터링 및 블러 처리
        st.sidebar.write("### 본인 점수 (다른 인원은 비공개)")
        filtered_data = data_filtered.copy()
        filtered_data['Name'] = filtered_data.apply(
            lambda row: row['Name'] if row['Name'] == user_name else "****", axis=1
        )
        filtered_data['Average Score'] = filtered_data.apply(
            lambda row: row['Average Score'] if row['Name'] == user_name else "****", axis=1
        )
        filtered_data['Rank'] = filtered_data.apply(
            lambda row: row['Rank'] if row['Name'] == user_name else "****", axis=1
        )
        # 스타일 적용: 'Average Score' 열에만 소수점 두 자리 표시
        styled_data = filtered_data.set_index(filtered_data.columns[2]).style.format(
            {"Average Score": lambda x: "{:.2f}".format(x) if isinstance(x, (int, float)) else x}
            )

        st.sidebar.dataframe(styled_data, use_container_width=True)
        
        # 본인 데이터 요약 정보 표시
        individual_data = data[data['Name'] == user_name]
        selected_name = user_name  # 이름 선택 고정
        
    else:
        # 관리자일 때: 전체 데이터 표시하며, 인덱스 숨김 처리 및 검색 가능한 선택 박스
        st.sidebar.write("### 인원별 평균 점수 순위")
        selected_name = st.sidebar.selectbox("이름을 선택하여 요약페이지를 보세요", data_filtered['Name'], key="name_select", index=0)

        # 선택한 이름을 강조한 데이터프레임 생성
        def highlight_row(s):
            return ['background-color: yellow' if s['Name'] == selected_name else '' for _ in s]

        # 강조된 행 표시
        st.sidebar.dataframe(data_filtered.set_index(data_filtered.columns[2]).style.format({"Average Score": "{:.2f}"}).apply(highlight_row, axis=1).set_properties(**{'text-align': 'center'}).set_table_styles([{'selector': 'th', 'props': [('text-align', 'center')]}]),use_container_width=True)
        
        # 선택한 이름에 해당하는 데이터 추출
        individual_data = data[data['Name'] == selected_name]

    # 전체 데이터 기반으로 사용자의 순위 및 상위/하위 % 계산
    user_rank = data_filtered[data_filtered['Name'] == selected_name]['Rank'].values[0]
    user_percentile = (user_rank / total_people) * 100
    percentile_label = "상위" 
    st.write(f"## Summary - {selected_name} ({percentile_label} {int(abs(user_percentile))}%)")

    # 개인 요약 정보 및 분석 페이지 표시
    st.write(f"**Area:** {individual_data['area'].values[0]}")
    st.write(f"**Department:** {individual_data['department'].values[0]}")
    st.write(f"**Posisi:** {individual_data['posisi'].values[0]}")

    # Q1~Q13, SQ1~SQ13 점수 추출
    peer_evaluation = individual_data.loc[:, 'Q1':'Q13'].values.flatten()
    self_evaluation = individual_data.loc[:, 'SQ1':'SQ13'].values.flatten()

    # Plotly를 사용한 반응형 그래프 생성
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=list(range(1, 14)), y=peer_evaluation, mode='markers+lines', name="Upward Evaluation (Q1-Q13)", marker=dict(color='blue'), hovertemplate='Peer Score: %{y}<extra></extra>'))
    average_data = data[data['Name'] == 'Average'].iloc[0].loc['Q1':'Q13'].values
    fig.add_trace(go.Scatter(x=list(range(1, 14)), y=average_data, mode='markers+lines', name="Average (Q1-Q13)", marker=dict(color='green'), hovertemplate='Average Score: %{y}<extra></extra>'))
    fig.add_trace(go.Scatter(x=list(range(1, 14)), y=self_evaluation, mode='markers+lines', name="Self Evaluation (SQ1-SQ13)", marker=dict(color='red'), hovertemplate='Self Score: %{y}<extra></extra>'))
    fig.update_layout(title=f"Evaluation Scores for {selected_name}", xaxis_title="Question Number", yaxis_title="Score", legend_title="Evaluation Type", hovermode="x")

    # Streamlit에 Plotly 그래프 표시
    st.plotly_chart(fig)
    
    #문항 컨테이너 생성
    question_container = st.empty()
    
    # 사이드바에 문항 내용 보기 버튼 추가
    #st.sidebar.header("문항 내용 보기")
    if st.sidebar.button("상향 평가 문항 보기"):
        with question_container:
            st.write("### 상향 평가 문항 내용")
            st.dataframe(peer_questions.set_index(peer_questions.columns[0]).rename(columns={"문항번호": "문항 번호", "평가문항id": "인니어 내용", "평가문항kr": "번역본"}), use_container_width=True)

    if st.sidebar.button("자가 평가 문항 보기"):
        with question_container:
            st.write("### 자가 평가 문항 내용")
            st.dataframe(self_questions.set_index(self_questions.columns[0]).rename(columns={"문항번호": "문항 번호", "평가문항id": "인니어 내용", "평가문항kr": "번역본"}), use_container_width=True)

    # 각 문항별 자가평가, 상향평가, 평균, 평균과 상향평가의 차이 계산
    question_numbers = [f"Q{i}" for i in range(1, 14)]
    evaluation_data = {
        "Self": self_evaluation,
        "Upward": peer_evaluation,
        "Average": average_data,
        "Avg-Up": average_data - peer_evaluation
    }
    evaluation_df = pd.DataFrame(evaluation_data, index=question_numbers).T
    st.write("### 각 문항별 점수 비교")
    st.dataframe(evaluation_df.style.format("{:.2f}"), use_container_width=True)

    # 정성 평가 구분 선택 박스 추가
    st.sidebar.header("정성 평가 구분 선택")
    evaluation_type = st.sidebar.radio("정성 평가 구분을 선택하세요:", ["자가 평가", "상향 평가"])

    # 선택된 평가 구분에 따른 코멘트 출력 함수
    def display_comments(comments):
        for q, text in comments.items():
            st.write(f"**{q}**: {text if pd.notna(text) else 'No response provided'}")

    # 정성 피드백 추가
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
        st.write("### Upward Evaluation Comments")
        display_comments(peer_comments)

else:
    st.sidebar.error("올바른 비밀번호를 입력하세요.")
