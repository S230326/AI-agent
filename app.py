# 분류 모델 웹앱 만들기

import streamlit as st

# 1. 기계학습 모델 파일 로드

import joblib
model = joblib.load('AI_agent_model.pkl') 
# 2. 모델 설명
st.title('비행 만족도 예측 에이전트')
st.subheader('~수많은 훈련 데이터로 학습시켰습니다!!~')
col1, col2,col3 = st.columns( 3 )      # 몇 개의 컬럼으로 나눌까?
with col1:
      st.subheader('모델 설명 ')
      st.write(' - 기계학습 알고리즘 : 로지스틱 회귀 ')
      st.write(' - 학습 데이터 출처 : https://www.kaggle.com/')
      st.write(' - 훈련    데이터 : 103904건')
      st.write(' - 테스트 데이터 : 25976건')
      st.write(' - 모델 정확도 : 0.46')

# 3. 데이터시각화
with col2:
      st.subheader('데이터시각화1')
      st.image('bitmap.PNG' )   # 이미지 불러오기
with col3:
      st.subheader('데이터시각화2')
      st.image('image.png')    # 이미지 불러오기

# 4. 모델 활용
st.subheader('모델 활용')
st.write('**** 다음의 항목을 입력하세요.. 인공지능이 당신의 여행의 만족 여부 예측 결과를 알려드립니다!')

a = st.number_input(' 어떤 종류의 여정인가요?(개인적인 여행이면 0, 비즈니스 여행이면 1로 입력해주세요)  ', value=0)   # 사용자 입력
b = st.number_input(' 어떤 좌석에 탑승하셨나요?(이코노미면 0, 이코노미 플러스면 1, 비즈니스면 2로 입력해주세요) ', value=0)
c = st.number_input(' 비행 중 오락 시설이 있나요?(만족도를 1~5까지 입력해주세요) ', value=0)
if st.button('만족/불만족 분류'):              # 사용자가 '합불분류' 버튼을 누르면
        input_data = [[ a, b, c ]]          # 사용자가 입력한 a,b,c 를 input_data에 저장하고
        p = model.predict(input_data)      # model이 분류한 값을 p에 저장한다
        if p[0] == 1 :
              st.success('인공지능 예측 결과는 만족입니다')
        else:
              st.success('인공지능 예측 결과는 불만족입니다')
