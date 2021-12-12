import os
import re
for file in os.listdir():
    if re.match("input.*\.txt", file):
        os.remove(file)
