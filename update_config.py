import sys

# Usage: python update_config.py <parameter> <value>
def update_config(param, value):
    with open('config.py', 'r') as f:
        lines = f.readlines()
    with open('config.py', 'w') as f:
        for line in lines:
            if line.strip().startswith(param + ' ='):
                f.write(f"{param} = {repr(value)}\n")
            else:
                f.write(line)

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('Usage: python update_config.py <parameter> <value>')
        sys.exit(1)
    update_config(sys.argv[1], sys.argv[2])
    print(f"Updated {sys.argv[1]} in config.py.")
