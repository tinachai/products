#檢查檔案在不在電腦裡
import os #operating system 透過載入模組(os)來進行isfile功能，檢查檔案在不在

#讀取檔案
products = []
if os.path.isfile('products.csv'):  #檢查檔案在不在 (絕對路徑 相對路徑 path模組)
	print('find the file')
	with open('products.csv', 'r') as f: #開始讀取檔案
		for line in f:
			if 'name,price' in line:
				continue
			name,  price = line.strip().split(',') #先把換行的符號去掉(strip),再進行切割
			products.append([name, price])
	print(products)
else:
	print('cannot find the file')

#讓使用者輸入
while True:
	name = input('Enter the product name: ')
	if name == 'q':
		break
	price = input('Enter the product price: ')
	products.append([name, price])
print(products)

#印出所有購買紀錄
for p in products:
	print(p[0], 'The price is', p[1])

#寫入檔案
with open('products.csv', 'w') as f:
	f.write('name,price\n')
	for p in products:
		f.write(p[0] + ',' + p[1] + '\n')