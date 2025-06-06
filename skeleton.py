import matplotlib.pyplot as plt
import pandas as pd
from pandas.errors import ParserError

print('그래프 생성기입니다!')

file_type = input("불러올 파일 종류를 선택해주세요 (csv / xlsx): ")
file_name = input("파일 이름을 확장자까지 적어주세요 (예: data.csv): ")

try:
    if file_type == 'csv':
        try:
            data = pd.read_csv(file_name, encoding='utf-8')
        except
    elif file_type == 'xlsx':
        try:
            data = pd.read_excel(file_name)
        except
    else:
        print("지원하지 않는 파일 형식입니다. csv 또는 xlsx만 입력해주세요.")
        exit()

except FileNotFoundError:
    print("폴더 내에 존재하지 않는 파일입니다.")
    exit()

while True:
    graph_type = input('그래프 양식을 정해주세요. \n막대/꺾은선/원\n: ')
    if graph_type in ['막대', '꺾은선', '원']:
        break
    else:
        print('막대, 꺾은선, 원 중에서 골라주세요!')

#막대, 꺾은선, 원 모두 plt로 처리하는게 어떨까요?
if graph_type == '막대':
    ax.bar()

elif graph_type == '꺾은선':
    ax.plot()

elif graph_type == '원':
    plt.pie(data[y_col], labels=data[x_col], autopct='%1.1f%%')
    plt.title(title)

plt.tight_layout()
plt.show()
