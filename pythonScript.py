import os
import re

def main():
    counters = {}

    for filename in os.listdir('.'):
        if not os.path.isfile(filename):
            continue

        match = re.match(r'^(\d+)\.([^.]+)$', filename)
        if match:
            number = int(match.group(1))
            ext = match.group(2)
            if ext not in counters or number >= counters[ext]:
                counters[ext] = number + 1

    for filename in os.listdir('.'):
        if filename.startswith('.'):
            continue

        if not os.path.isfile(filename):
            continue

        if filename.endswith('.py'):
            continue

        if re.match(r'^\d+\.[^.]+$', filename):
            continue

        parts = filename.split('.')
        if len(parts) > 1:
            extension = parts[-1]
        else:
            extension = filename   

        if extension not in counters:
            counters[extension] = 1

        new_name = f"{counters[extension]}.{extension}"

        while os.path.exists(new_name):
            counters[extension] += 1
            new_name = f"{counters[extension]}.{extension}"

        os.rename(filename, new_name)

        counters[extension] += 1

    print("Done.")

if __name__ == "__main__":
    main()