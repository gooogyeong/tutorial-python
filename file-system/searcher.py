import sys
from pathlib import Path
import re

# dir_path='.'
# keyword='bacon'
dir_path=sys.argv[1]
keyword=sys.argv[2]

# print(os.listdir(dir_path)))
path = Path(dir_path)
# print(list(path.glob('*.txt'))) # [PosixPath('sonnet.txt'), PosixPath('hello_world.txt'), PosixPath('bacon.txt')]

for text_file in list(path.glob('*.txt')):
    content = text_file.read_text()
    # print(content)
    search_result=re.search(keyword, content)
    # print(search_result)
    CHIGHLIGHT = '\033[104m'
    CEND = '\033[0m'
    sub = re.sub(keyword, CHIGHLIGHT + keyword + CEND, content)
    print(sub)
    # content=sub
    # print(sub)