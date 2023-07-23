class File:
    def __init__(self, file_name):

        self.header = ''
        self.numbers = ''
        self.tail = ''

        header_start_flag = True
        number_start_flag = False
        tail_start_flag = False
        for i in range(len(file_name)):
            c = file_name[i]
            if header_start_flag:
                if ord('0') <= ord(c) <= ord('9'):
                    number_start_flag = True
                    header_start_flag = False
                    self.numbers += c
                else:
                    self.header += c
            elif number_start_flag:
                if ord('0') <= ord(c) <= ord('9') and len(self.numbers) < 5:
                    self.numbers += c
                else:
                    number_start_flag = False
                    tail_start_flag = True
                    self.tail += c
            elif tail_start_flag:
                self.tail += c

        print(self.header, self.numbers, self.tail)


def solution(files):
    answer = []

    for file_name in files:
        answer.append(File(file_name))




    return answer


input1 = ["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]
input2 = ["F-5 Freedom Fighter", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat"]
solution(input2)
