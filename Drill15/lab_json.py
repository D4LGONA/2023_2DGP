import json

numbers = [1,2,3,4]
# numbers라는 리스트를 json 포맷으로 변경
numbers_string = json.dumps(numbers)
print(numbers_string)

values_string = '{"x": 10, "y": 20, "size": 4.5}'
values = json.loads(values_string) # 여기서 s는 string
print(type(values))
print(values)

# f = open()과 같음
with open('zombie_data.json', 'r') as f: # f에 제대로 들어왓을때만 실행, 파일 close 안해도됨
    zombie_data_list = json.load(f) # 알아서 파싱 해준다
    print(zombie_data_list)
