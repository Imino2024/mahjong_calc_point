import streamlit as st
from decimal import ROUND_HALF_DOWN, Decimal

st.title('点数計算')
st.write('Mリーグルールをベースとした点数計算を行います！')

first, second, third, fourth = st.columns(4)

def calc_point(page, rank):
    point_dict = {2 : 10, 3 : -10, 4 : -20}
    page.subheader(str(rank)+'位')
    point = page.number_input('点数を入力してください', key = str(rank))
    point = Decimal(point).quantize(Decimal('1E3'), rounding=ROUND_HALF_DOWN)           # 5捨6入
    point = (point - 30000)/1000 + point_dict[rank]
    page.header(str(point) + '点')
    return point

# 2-4位の計算
fourth_point = calc_point(fourth, 4)
third_point = calc_point(third, 3)
second_point = calc_point(second, 2)

first_point = abs(fourth_point + third_point + second_point)
first.subheader('1位')
first.write('1位は点数入力の必要がありません')
first.write('\n')
first.header(str(first_point) + '点')

