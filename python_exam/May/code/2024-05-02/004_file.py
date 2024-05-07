# 파일 처리 : 저장, 불러오기
save_file = open('save.txt', 'w', encoding='utf8')
print('테스트1 : 테스트', file=save_file)
print('테스트2 : 테스트2', file=save_file)
save_file.close()



