import streamlit as st


from PIL import Image # 위에 올리는게 좋다

import pandas as pd

import matplotlib.pyplot as plt


# 체질량 지수 구하는 앱 
# 몸무게 , 키 입력 받기

# Using object notation

add_selectbox = st.sidebar.selectbox(
    "목차",
    ("체질량 계산기", "갭 마인더", "마이 페이지")  
)
#3개의 페이지를 만들어보자 if 구문 활용해서 각 해당 영역에 맞는 코드 작성 


if add_selectbox =="체질량 계산기":
    st.write("체질량 계산기 확인해보자 ")
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
#픽사베이 사이트 들어가서 원하는 이미지 다운로드 받고 그 이미지 파일 파이썬 폴더에 저장 그리고 그 이름 복사해서 이미지 함수open 파일 업로드

    image = Image.open('vegetables-1085063_1280.jpg')

    st.image(image, caption='야채를 많이 먹자')

    
elif add_selectbox=="갭 마인더":
        st.write("하하하")
        data=pd.read_csv('gapmindercsv.csv')
        st.write(data)
        
        year = st.slider('년도를 선택하세요', 1952,2007,1952,5)
        st.write("year ",year )
        
        data=data[data['year']==year]

        colors=[]

        for x in data['continent']:
            if x=='Asia':
                  colors.append('tomato')
            elif x=='Europe':
                  colors.append('blue')
            elif x=='Africa':
                    colors.append('olive')
            elif x=='Americas':
                 colors.append('green')
            else:
                 colors.append('orange')            

        data['colors']=colors

        fig, ax = plt.subplots()  
        ax.scatter(data['gdpPercap'],data['lifeExp'],s=data['pop']*0.00002, color=data['colors'])  #스캐터 그램으로 표현하고 싶고 data 중에서 gdp 열 사용하고 싶다 =x 축 y= data 중 기대수명 사용하고싶다
        ax.set_title("How does gdp per capital relate to life expectancy")
        ax.set_xlabel("gdp per capital")
        ax.set_ylabel("life expectancy")
        st.pyplot(fig)




elif add_selectbox=='마이 페이지':
        st.write("여기는 마이페이지입니다")


# 판다스 matplotlib 도 