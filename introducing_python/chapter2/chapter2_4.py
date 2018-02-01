# 2.4 연습문제
# 2.1 1 시간은 몇 초 인가? 대화식 인터프리터를 사용해서 계산해보라. 1시간은 60분이고, 1분은 60초다. 이 둘을 곱한다.
# 2.2 계산한 결과를 seconds_per_hour 변수에 저장하라.
seconds_per_hour = 60 * 60
print("seconds_per_hour:",seconds_per_hour)
# 2.3 1일은 몇 초인가? Seconds_per_hour 변수를 사용하라.
# 2.4 계산한 결과를 seconds_per_day 변수에 저장하라.
seconds_per_day = seconds_per_hour * 24
print("seconds_per_day:", seconds_per_day)
# 2.5 부동소수점(/) 나눗셈을 사용해서 seconds_per_day 를 seconds_per_hour 로 나누어라.
result=seconds_per_day / seconds_per_hour
print("result :", result)
# 2.6 정수(//) 나눗셈을 사용해서 seconds_per_day 를 seconds_per_hour 로 나누어라. 이전 문제의 부동소수점 결과에서 본 .0 이 있는가?
result = seconds_per_day // seconds_per_hour
print("result : ", result)