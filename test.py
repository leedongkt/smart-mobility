import streamlit as st


from PIL import Image # 위에 올리는게 좋다



# 체질량 지수 구하는 앱 
# 몸무게 , 키 입력 받기




st.write("# 체질량 계산기")

st.info('체질량 지수는 자신의 몸무게를 키의 제곱으로 나눈 값입니다', icon="ℹ️")

height = st.number_input('키를 입력하세요. (cm)',100,200,170,5) #받는 값 숫자임  #최소 100 최대 200  현재 값 170 설정 클릭 할 때마다 스텝 5
st.write('키: ', height,'cm')

weight = st.number_input('몸무게를  입력하세요. (kg)',30,150,60,5) #받는 값 숫자임  #최소 100 최대 200  현재 값 170 설정 클릭 할 때마다 스텝 5
st.write('몸무게: ', weight,'kg')

bmi=weight/((height/100)**2)

if st.button('계산'):
    
    st.balloons()
    
    st.write("당신의 체질량 지수는",round(bmi,2),'입니다')
    if bmi>=25:
        
        st.error('위험하다 !!', icon="🚨")
    elif bmi>=23:
        
        st.warning('과체중이다 !', icon="⚠️")
    elif bmi>=20:
        
        st.info('정상이다 !', icon="ℹ️")
    elif bmi>=18.5:
        
        st.success('저체중이다 ! ', icon="✅")
    
    

# 이미지 다운로드 받는 법 


image = Image.open('vegetables-1085063_1280.jpg')

st.image(image, caption='야채를 많이 먹자')

