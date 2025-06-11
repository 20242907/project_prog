import matplotlib.pyplot as plt
import pandas as pd
from pandas.errors import ParserError

print('그래프 생성기입니다!')

file_type = input("불러올 파일 종류를 선택해주세요 (csv / xlsx): ")
file_name = input("파일 이름을 확장자까지 적어주세요 (예: data.csv): ")

if file_type == 'csv':
    try:
        data = pd.read_csv(file_name, encoding='utf-8')
    except FileNotFoundError:
        print('폴더 내에 존재하지 않는 파일입니다.')
        exit()
    except ParserError:
        print('지원하지 않는 파일 형식입니다. csv파일이 맞는지 확인해주세요.')
        exit()

elif file_type == 'xlsx':
    try:
        data = pd.read_excel(file_name)
    except FileNotFoundError:
        print("폴더 내에 존재하지 않는 파일입니다.")
        exit()
    except ParserError:
        print('지원하지 않는 파일 형식입니다. xlsx파일이 맞는지 확인해주세요.')
        exit()

else:
    print("지원하지 않는 파일 형식입니다. csv 또는 xlsx만 입력해주세요.")

while True:
    graph_type = input('그래프 양식을 정해주세요. \n막대/꺾은선/원\n: ')
    if graph_type in ['막대', '꺾은선', '원']:
        break
    else:
        print('막대, 꺾은선, 원 중에서 골라주세요!')

#그래프 제목, x축 이름, y축 이름 입력받으려고 넣었습니다
#data.columns는 기본 형식이 index라고 해서 list변환해뒀습니다다
while True:
    title = input('그래프의 제목을 입력해주세요: ')
    x_col = input('x축 기둥의 이름을 입력해주세요: ')
    y_col = input('y축 기둥의 이름을 입력해주세요: ')

    if x_col in list(data.columns):
        pass
    else:
        print('입력하신 x축 기둥이 파일 내에 존재하지 않습니다')
    
    if y_col in list(data.columns):
        break
    else:
        print('입력하신 y축 기둥이 파일 내에 존재하지 않습니다')


fig, ax = plt.subplots()

if graph_type == '막대':
    ax.bar(data[x_col], data[y_col])

elif graph_type == '꺾은선':
    ax.plot(data[x_col], data[y_col], marker='o')       #꺾은선 근본은 값 위에 점이 있어야 한다고 생각해서 마커 넣었는데 아닌 것 같으면 그냥 지워주세용

elif graph_type == '원':
    plt.pie(data[y_col], labels=data[x_col], autopct='%1.1f%%')
    plt.title(title)

ax.set_xlabel(x_col)
ax.set_ylabel(y_col)
ax.set_title(title)
ax.tick_params(axis='x', rotation=45)       #이름 길면 겹치길래 살짝 돌렸어요

plt.tight_layout()
plt.show()
