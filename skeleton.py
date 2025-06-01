import matplotlib.pyplot as plt
import pandas as pd
from pandas.errors import ParserError

print('그래프 작성을 돕는 프로그램입니다')

try:
    file_name = input('파일명을 적어주세요(확장자 .csv): ')     #확장자 다른 오류, 없는파일 오류 잡아야함
    data = pd.read_csv(file_name, encoding = 'utf-8')
    fig, ax = plt.subplots()

except FileNotFoundError:
    print('폴더 내에 존재하지 않는 파일입니다.')
except ParserError:
    print('파일의 형식이 틀렸습니다.')

else:
    while True:
        type_graph = input('그래프 양식을 정해주세요\n막대/꺾은선/원\n: ')

        if type_graph == '막대':
            ax.bar()
            break

        elif type_graph == '꺾은선':
            ax.plot()
            break

        elif type_graph == '원':
            break

        else:
            print('막대, 꺾은선, 원 중에서 골라주세요!')