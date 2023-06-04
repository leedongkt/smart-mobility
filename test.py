print("hello world")
print(1+1)
import streamlit as st
st.write("# Hi welcome my APP")
st.write("반갑습니다 저는 이동현이라고 합니다")

if st.button("say hello"):
    st.write("Why hello there")    #버튼 누르면 참이라고 함 if = 참일 때 
else:
    st.write("Goodbye!")


option = st.selectbox(
    '좋아하는 동물은?',
    ('강아지', '고양이', '말','토끼','코끼리'))

st.write('내가 좋아하는 동물은:', option)   #option 클릭하면 내가 좋아하는 동물 뜨는거임    
st.write("내가 좋아하는 동물은 {}이다".format(option))


txt=st.text_area('자신을 소개해보세요','''

''')

st.write("내가 입력한 내용은:", txt)

age = st.slider('나이를 선택하세요?', 0, 130, 25)
st.write("내 나이는", age, '살입니다')