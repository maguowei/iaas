import re

with open('./execute.txt') as f:
    mark_str = data = f.read()


def convert2code(mark_str) -> list:
    r = re.compile(r'`{1,3}(.*?)`{1,3}', re.DOTALL)
    code_data = r.findall(mark_str)
    codes = []

    for code in code_data:
        code = code.lstrip('bash').strip()
        codes.append(code)
    return codes


if __name__ == '__main__':
    data = convert2code(mark_str)
    # print(data)
    for d in data:
        print(d.strip())
