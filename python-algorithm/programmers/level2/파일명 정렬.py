import re


class File:
    def __init__(self, file_name):
        self.file_name = file_name
        self.header, self.number, self.tail = self.parse_file_name(file_name)

    def parse_file_name(self, file_name):
        match = re.match(r'([a-z\-_\s]+)(\d{1,5})(.*)', file_name, re.I)
        if match:
            return match.group(1).lower(), int(match.group(2)), match.group(3)
        else:
            return file_name, 0, ""


def solution(files):
    file_objects = [File(file_name) for file_name in files]
    file_objects.sort(key=lambda x: (x.header, x.number))
    return [file_obj.file_name for file_obj in file_objects]


def other_solution(files):
    # Regular expression pattern
    pattern = re.compile(r'([a-z\s.-]+)([0-9]{1,5})', re.IGNORECASE)

    print(pattern)

    # Sorting
    files.sort(key=lambda f: (match.group(1), int(match.group(2)))
    if (match := pattern.match(f.lower())) else (f, 0))

    return files


input1 = ["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]
input2 = ["F-5 Freedom Fighter", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat"]
print(solution(input2))
print(other_solution(input2))
