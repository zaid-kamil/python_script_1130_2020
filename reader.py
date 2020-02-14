def read_file(path):
    f = open(path)
    data = f.read()
    f.close()
    return data

# testing function 1
# data=read_file('data/Richardson_Clarissa.txt')
# print(data[:200])

def count_word_occurance(file,word):
    data = read_file(file).lower()
    result = data.count(word)
    return result


# testing function 2
# file = 'data/Richardson_Clarissa.txt'
# print("hello = ",count_word_occurance(file,'hello'))
# print(count_word_occurance(file,'there'))
# print(count_word_occurance(file,'olive'))

def count_vowels(file):
    vowels = 'aeiou'
    data = read_file(file).lower()
    results={}
    for item in vowels:
        size= data.count(item)
        results[item]=size
    return results

# testing function 3
# file = 'data/Richardson_Clarissa.txt'
# print('total vowels are',count_vowels(file))

# print('total vowels in file 2',count_vowels('data/Sterne_Sentimental.txt'))
# print(count_vowels(file))

