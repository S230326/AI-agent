# 1. 시작

import streamlit as st


# 2. 모델 설명
import joblib
model = joblib.load('AI_agent_model(1).pkl') 

st.title('비행 만족도 예측 에이전트')
st.subheader('〰10만 건의 훈련 데이터로 학습시켰습니다!!〰')
col1, col2,col3 = st.columns( 3 )      
with col1:
      st.subheader('모델 설명 ')
      st.write(' - 기계학습 알고리즘 : 로지스틱 회귀 ')
      st.write(' - 학습 데이터 출처 : https://www.kaggle.com/')
      st.write(' - 훈련    데이터 : 103904건')
      st.write(' - 테스트 데이터 : 25976건')
      st.write(' - 모델 정확도 : 0.8')
      

# 3. 데이터시각화
with col2:
      st.subheader('데이터시각화1')
      st.image('bitmap.PNG' )   
with col3:
      st.subheader('데이터시각화2')
      st.image('image.png')   

# 4. 모델 활용
st.subheader('모델 활용')
st.write('**** 다음의 항목을 입력하세요.. 인공지능이 당신의 여행의 만족 여부 예측 결과를 알려드립니다!')

a = st.number_input(' 어떤 종류의 여정인가요?(비즈니스 여행이면 0, 개인적인 여행이면 1로 입력해주세요)  ', value=0)   
b = st.number_input(' 어떤 좌석에 탑승하셨나요?(이코노미면 0, 이코노미 플러스면 1, 비즈니스면 2로 입력해주세요) ', value=0)
c = st.number_input(' 비행 중 오락 시설이 있나요?(만족도를 1~5까지 입력해주세요) ', value=0)
if st.button('만족/불만족 분류'):             
        input_data = [[ a, b, c ]]         
        p = model.predict(input_data)     
        if p[0] == 1 :
              st.success('인공지능 예측 결과는 만족입니다')
        else:
              st.success('인공지능 예측 결과는 불만족입니다')
import streamlit as st

# 상태 초기화
if 'toggle_state' not in st.session_state:
    st.session_state.toggle_state = False  # 초기 상태: False

# 버튼 클릭 시 상태 변경
def toggle_action():
    st.session_state.toggle_state = not st.session_state.toggle_state  # 상태를 반전

# 버튼 UI
if st.session_state.toggle_state:
    st.button("이 모델의 상업적 활용에 관한 정보", on_click=toggle_action)  # 상태가 True일 때 버튼 텍스트는 "취소"
            st.write('이 모델을 상업적으로 사용하려면 gimpo.s230326@ggh.goe.go.kr에 연락주세요')
else:
    st.button("이 모델의 상업적 활용에 관한 정보", on_click=toggle_action)  # 상태가 False일 때 버튼 텍스트는 "실행"



