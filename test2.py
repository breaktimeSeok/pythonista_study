# 제너레이터 테스트

def get_natural_number():
	n=0
	while True:
		n += 1
		yield n
		
		
		
g = get_natural_number()
for _ in range(0, 10):
	print(next(g))

# enumerate 테스트

a = [1,2,3,2,45,2,5]

print(a)

print(list(enumerate(a)))

a = ['a1', 'b1', 'c1']


for i,v in enumerate(a):
	print(i, v)
