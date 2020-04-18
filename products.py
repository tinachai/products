#檢查檔案在不在電腦裡
import os #operating system 透過載入模組(os)來進行isfile功能，檢查檔案在不在

def read_file(filename): #()內寫成參數 加參數
    products = []
    with open(filename, 'r') as f: #開始讀取檔案
        for line in f:
            if 'name,price' in line:
                continue
            name,  price = line.strip().split(',') #先把換行的符號去掉(strip),再進行切割
            products.append([name, price])
    return products #放在function 最後一行 回傳products清單 因為有append 加入新的東西進去       

#讓使用者輸入
def user_input(products):
    while True:
        name = input('Enter the product name: ')
        if name == 'q':
            break
        price = input('Enter the product price: ')
        products.append([name, price])
    print(products)
    return products #這樣才能重新存下來

#印出所有購買紀錄
def print_products(products):
    for p in products:
        print(p[0], 'The price is', p[1]) #沒有改變任何東西所以不用回傳(return)

#寫入檔案
def write_file(filename, products):
    with open(filename, 'w') as f:
        f.write('name,price\n')
        for p in products:
            f.write(p[0] + ',' + p[1] + '\n')

def main():
    filename = 'products.csv'
    if os.path.isfile(filename):  #檢查檔案在不在 (絕對路徑 相對路徑 path模組)
        print('find the file')
        products = read_file(filename) #有return 就可以存下來
    else:
        print('cannot find the file')
    products = user_input(products)
    print_products(products)
    write_file('products.csv', products)

main()
