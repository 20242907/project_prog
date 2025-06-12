import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import pandas as pd
from pandas.errors import ParserError
import platform

def set_korean_font():
    os_name = platform.system()

    if os_name == 'Windows':
        plt.rcParams['font.family'] = 'Malgun Gothic'
    elif os_name == 'Darwin':
        font_path = '/System/Library/Fonts/Supplemental/AppleGothic.ttf'
        font_prop = fm.FontProperties(fname=font_path)
        plt.rcParams['font.family'] = font_prop.get_name()
    else:
        plt.rcParams['font.family'] = 'NanumGothic'

set_korean_font()


print('그래프 생성기입니다!')

while True:
    file_path = input("불러올 파일 이름 또는 전체 경로를 입력해주세요. (e.g. data.csv 또는 /Users/...): ")

    if file_path.endswith('.csv'):
        try:
            data = pd.read_csv(file_path, encoding='utf-8')
            break
        except FileNotFoundError:
            print('폴더 내에 존재하지 않는 파일입니다.')
        except ParserError:
            print('지원하지 않는 파일 형식입니다. csv 파일이 맞는지 확인해주세요.')

    elif file_path.endswith('.xlsx'):
        try:
            data = pd.read_excel(file_path)
            break
        except FileNotFoundError:
            print("폴더 내에 존재하지 않는 파일입니다.")
        except ParserError:
            print('지원하지 않는 파일 형식입니다. xlsx파일이 맞는지 확인해주세요.')

    else:
        print("지원하지 않는 파일 형식입니다. csv 또는 xlsx만 입력해주세요.")

while True:
    graph_type = input('그래프 양식을 정해주세요. \n막대/꺾은선/원\n: ')
    if graph_type in ['막대', '꺾은선', '원']:
        break
    else:
        print('막대, 꺾은선, 원 중에서 골라주세요!')


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
    ax.plot(data[x_col], data[y_col], marker='o') 

elif graph_type == '원':
    if pd.api.types.is_numeric_dtype(data[y_col]):
        plt.pie(data[y_col], labels=data[x_col], autopct='%1.1f%%')
        plt.title(title)
    else:
        counts = data.groupby(x_col)[y_col].count()
        plt.pie(counts, labels=counts.index, autopct='%1.1f%%')
        plt.title(title)

if graph_type in ['막대', '꺾은선']:
    ax.set_xlabel(x_col)
    ax.set_ylabel(y_col)
    ax.set_title(title)
    ax.tick_params(axis='x', rotation=45)       #이름 길면 겹치길래 살짝 돌렸어요

print("\n[그래프 요약 정보]")
if graph_type == '원':
    if pd.api.types.is_numeric_dtype(data[y_col]):
        total = data[y_col].sum()
        max_label = data.loc[data[y_col].idxmax(), x_col]
        print(f"총합: {total}")
        print(f"가장 큰 값: {max_label} ({data[y_col].max()})")
    else:
        counts = data.groupby(x_col)[y_col].count()
        most_common = counts.idxmax()
        print(f"가장 많이 등장한 {x_col}: {most_common} ({counts.max()}개)")

else:
    print(f"{y_col} 평균: {data[y_col].mean():.2f}")
    print(f"{y_col} 최대값: {data[y_col].max()} (↖ {data.loc[data[y_col].idxmax(), x_col]})")
    print(f"{y_col} 최소값: {data[y_col].min()} (↘ {data.loc[data[y_col].idxmin(), x_col]})")


plt.tight_layout()
plt.show()
