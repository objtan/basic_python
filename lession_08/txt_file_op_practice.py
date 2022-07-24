# 1. Write a program to read an entire the sample.txt file
print('===================================== 1 ======================================')
with open('sample.txt', mode='rt', encoding='utf-8') as fileObject:
    data = fileObject.read()
    print(data)

# 2. Write a program to read an first/last n line of the sample.txt file with n and first/last are arguments come from keyboard.
print('===================================== 2 ======================================')
def first_line(filename,n):
    with open(filename,'rt', encoding='utf-8') as fileObject:
        for line in range(n):
            line = fileObject.readline() # in ra dong dau tien cua van ban
            print(line)                  # sau do dung vong for de lay ra so dong muon lay
        # for line in (fileObject.readlines() [:n]): # fileObject.readlines() se lay ra mang trong sample.txt
        #     print(line)                            #  ap dung lay n phan tu trong mang
# first_line('sample.txt',3)


def last_line(filename,n):
    with open(filename,'rt', encoding='utf-8') as fileObject:
        # for line in (fileObject.readlines()[-n:]):
        #     print(line)
        line = (fileObject.readlines()[-n:])
        print(line)
# last_line('sample.txt',3)

# 3. Write a program to read line by line os the sample.txt file and store them in a list. Sort the list by length of each line.
print('===================================== 3 ======================================')
#Hàm sorted() không thay đổi list ban đầu mà tạo ra một list mới được sắp xếp lại từ list ban đầu.
#Phương thức sort() không tạo ra list mới mà chỉ sắp xếp lại chính list ban đầu.

def sort_list(filename):
    with open(filename,'rt', encoding='utf-8') as fileObject:
        new_list=fileObject.readlines() 
        sort_len=sorted(new_list,key=len)
        print(sort_len)
# sort_list('sample.txt')

# 4. Write a program to append a line to the sample.txt file with line is argument come from keyboard. 
# Print the length of file and the line with longest length.
print('===================================== 4 ======================================')
def append_file(filename, text):
    # Open the file in append & read mode ('a+')
    with open(filename, 'a+') as fileObject:
        # Move read cursor to the start of file.
        fileObject.seek(0)
        # If file is not empty then append '\n'
        data = fileObject.read()
        if len(data) > 0 :
            fileObject.write("\n")
        # Append text at the end of file
        fileObject.write(text)
        with open(filename, 'rt') as fileObject:
            file_len=fileObject.read()           
            print(f'File length: {len(file_len)}')
        with open(filename, 'rt') as fileObject:    
            lines=fileObject.readlines()
            sort_len=sorted(lines,key=len)
            print(sort_len[-1])

# text = input('Enter a text: ')
# append_file('sample.txt', text) 

# 5. Write a program to count frequency of each word in the sample.txt file.
print('===================================== 5 ======================================')
def word_count(filename):
    # Tao mot tu dien trong
    word_dict = dict()
    with open(filename, 'rt') as fileObject:
        data = fileObject.readlines()
        # Lap qua tung dong cua tep
        for line in data:
            # xoa khoang trang va ky tu dong moi trong tep
            line = line.strip()
            # chuyen het thanh chu thuong
            line = line.lower()
            # Tách từ sau khi da xoa het khoang trang, va chuyen sang chu thuong
            words = line.split()
            # Lặp lại từng từ trong dòng từng từ trong từ:
            # Kiểm tra xem từ đã có trong từ điển chưa
            for word in words:
                if word in word_dict:
                    word_dict[word] += 1
                else:
                    word_dict[word] = 1
    word_dict = sorted(word_dict.items(), key=lambda item: item[1], reverse=True)
    print(word_dict)
    # for key in list(word_dict.keys()):
    #     print(key,word_dict[key])

    #     lines = fileObject.readlines()
    #     for line in lines:
    #         for word in line.split(' '):
    #             if word not in word_dict:
    #                 word_dict[word] = 1
    #             else:
    #                 word_dict[word] += 1
    # word_dict = sorted(word_dict.items(), key=lambda item: item[1], reverse=True)
    # print(word_dict)

# word_count('sample.txt')

# 6. Write a program to remove a line which line number is a argument from the keyboard.
print('===================================== 6 ======================================')
def delete_line(filename, n):
    with open(filename, 'r') as f:
        lines = f.readlines()
    with open(filename, 'w') as f:
        for idx, line in enumerate(lines):
            if idx != n:
                f.write(line)
# n = int(input('Enter the line number: '))
# delete_line('sample.txt', n)
# -------------------

# 6. Write a program to store the below content in a file name sample_w.txt:
def write_file(filename, text):
    with open(filename, 'w') as fw: 
        fw.write(text)

text='''While CMR portrays extreme competency in capturing all data types, here are specific means through which it benefits your enterprise -

1. Automation Scope Expansion
CMR lets you leverage 85% of the untapped and unstructured data prevalent in your organization, implying that you receive enhanced results by automating deeper processes as well as more complex data.

2. Greater accuracy with data certainty
CMR offers a better capture rate with over 80% accuracy of consistently capturing information. CMR lets you promote the level of data certainty to attain a higher percentage of straight-through processing.'''

# text = "\n".join([s for s in text.split("\n") if s])
# write_file('sample_w.txt', text)
