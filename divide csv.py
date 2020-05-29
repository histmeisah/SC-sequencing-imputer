import csv
import os

def divide(path,row_number):
    with open(path,'r',newline='') as file:
        csvreader = csv.reader(file)
        a = next(csvreader)
        print(a)
        i = j = 1
        for row in csvreader:
            print(row)
            print(f'i is {i} , j is {j}')
            if i % row_number == 0:
                j += 1
                print(f"csv{j}生成成功")
            csv_path = os.path.join('/'.join(path.split('/')[:-1]),'result' +  str(j) + '.csv')
            print(csv_path)
            if not os.path.exists(csv_path):
                with open(csv_path, 'w', newline='') as file:
                    csvwriter = csv.writer(file)
                    csvwriter.writerow(['image_url'])
                    csvwriter.writerow(row)
                i += 1
            # 存在的时候就往里面添加
            else:
                with open(csv_path, 'a', newline='') as file:
                    csvwriter = csv.writer(file)
                    csvwriter.writerow(row)
                i += 1
