# import sys
# sys.path.insert(0,'C:\PyCharm\programming_study\introducing_python\chapter5\sources\daily.py')
# sys.path.insert(0,'C:\PyCharm\programming_study\introducing_python\chapter5\sources\weekly.py')
from sources import daily, weekly

print("daily forecast: ", daily.forecast())
print("Weeky forecast:")
for number, outlook in enumerate(weekly.forecast(), 1):
    print(number, outlook)
