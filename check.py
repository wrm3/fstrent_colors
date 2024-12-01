import os

for root, dirs, files in os.walk('.'):
    for file in files:
        print(os.path.join(root, file))
        if file.endswith('.py'):
            with open(os.path.join(root, file), 'rb') as f:
                try:
                    f.read().decode('ascii')
                except UnicodeDecodeError as e:
                    print(f"Non-ASCII character in {file}: {e}")