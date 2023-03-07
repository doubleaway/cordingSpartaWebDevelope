first_name='charin'
last_name='Y'
a=2
b='a'
#형변환
b=str(a)

text='abcdefgefe'
#길이
print(len(text))
print(text[3:7])
#복사
print(text[:])
print(first_name+last_name)
print(b)

#문자열 자르기
myEmail='abc@naver.com'

result=myEmail.split('@')[1].split('.')[0]

print(result)

#test1 앞에 3글자만
testTxt='sparta'
result2=testTxt[:3]
print(result2)

#test2 앞 번호만 나오게
phone='02-123-1234'
result3=phone.split('-')[0]
print(result3)
