# 5.3.1 모듈 임포트하기
#import report as wr
from report import get_description as do_it
# main program
#description = report.get_description()
#description = wr.get_description()
description = do_it()
print("Today's weather: ", description)