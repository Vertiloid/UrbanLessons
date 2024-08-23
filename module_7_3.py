class WordsFinder:
    def __init__(self, *args):
        self.file_names = args
    def get_all_words(self):
        all_words = {}
        for current_files in self.file_names:   #перебираем файлы
            with open(current_files) as file:
                content = file.read()
                current_word = ''
                list_words = []
                for current_symbol in range(0, len(content)):    #перебираем содержимое файла
                    #пробел, перенос строки или табуляция считается признаком конца слова
                    if (content[current_symbol] == ' ' or content[current_symbol] == '\n' or
                            content[current_symbol] == '\t') and len(current_word) > 0:
                        if current_word == '-': #если дефис обрамлёный пробелами или пробел за дефисом в начале файла
                                                #избавляемся от дефиса
                            current_word = ''
                        else:
                            list_words.append(current_word.lower())
                            current_word = ''
                    else:
                        if not any((content[current_symbol] == ',', content[current_symbol] == '.',
                                    content[current_symbol] == '=', content[current_symbol] == '!',
                                    content[current_symbol] == '?', content[current_symbol] == ';',
                                    content[current_symbol] == ':')):
                            current_word += content[current_symbol]  #собираем слово по буквам
            all_words[current_files] = list_words
        return all_words
    def find(self, word):
        output = {}
        for name, words in self.get_all_words().items():
            for i in range(0, len(words)):
                if word == words[i]:
                    output[name] = i + 1
                    break
        return output

    def count(self, word):
        output = {}
        for name, words in self.get_all_words().items():
            output[name] = 0
            for i in range(0, len(words)):
                if word == words[i]:
                    output[name] += 1
        return output



fw = WordsFinder('products.txt', 'test.txt', 'test_file.txt', 'Mother Goose - Monday’s Child.txt',
                 'Rudyard Kipling - If.txt', 'Walt Whitman - O Captain! My Captain!.txt')
print(fw.get_all_words())
print(fw.find('text'))
print(fw.count('text'))

