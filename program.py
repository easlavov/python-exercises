import sys

def main():
    d = {1:3, 2:5, 3:15}
    d[-2] = 22
    sort = sorted(d)
    print sorted(d.items())

if __name__ == '__main__':
    main()
    