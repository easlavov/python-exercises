import sys

def repeat(s, count, exclaim):
    """
    Returns the string 's' repeated 'count' times.
    If exclaim is true, add exclamation marks.
    """

    result = s * count # can also use "s * 3" which is faster (Why?)
    if exclaim:
        result = result + '!!!'
    return result

def task(arg):
    s = 'Hello, %s!' % (arg)
    unic = (u'A unicode \u018e string \xf1').encode('utf-8')
    print unic

def task2(arg):
    tuple = (1, 2, 'hi')
    print tuple

def main():
    word = 'a'
    das = word[-1]
        
    task2('powerr')
    # task(sys.argv[1])
    # print repeat(sys.argv[1], 10, True)
    # print repeat(sys.argv[2], 3, False)

if __name__ == '__main__':
    main()