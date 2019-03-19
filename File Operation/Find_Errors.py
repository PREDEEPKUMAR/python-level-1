import re

pattern = 'ERROR'

with open('Phone_ValidationLog.txt', 'r') as fo:
    lines = fo.read().splitlines()
    with open('ERROR_LOG.txt', 'a') as eer:
        for line in lines:
            match = re.search(pattern, line)
            if match:
                eer.write(line + '\n')