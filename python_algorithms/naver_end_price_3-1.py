from collections import namedtuple
# 문제 3-1
#
# 2015년 9월 초의 네이버 종가는 표 3.2와 같습니다.
# 09/07의 종가를 리스트의 첫 번째 항목으로 입력해서 naver_end_price라는 이름의 리스트를 만들어보세요.
naver_end_price = [474500, 461500, 501000, 500500, 488500]
# 3-1
print(naver_end_price)
# 3-2
print(max(naver_end_price))
# 3-3
print(min(naver_end_price))
# 3-4
print(max(naver_end_price)-min(naver_end_price))
# 3-5
print(naver_end_price[2])
# 3-6
naver_end_price2 = {"월":474500, "화":461500, "수":501000, "목":500500, "금":488500}
print(naver_end_price2, "\n type : ", type(naver_end_price2))
#print(naver_end_price2.get("월"))
# 3-7
print(naver_end_price2.get("수"))

# tuple로 변환
naver_days = tuple(naver_end_price2.keys())
print(naver_days)
print(naver_end_price2.values())
list_price = list(naver_end_price2.values())
list_date = ["09/07", "09/08", "09/09", "09/10", "09/11"]
print(list_date)

dict_naver_price = {naver_days[0]:list_price[0]+list_date[0]}
print(dict_naver_price)