if __name__ == '__main__':
    N = int(input())
    myList = []

    for _ in range(N):
        inputList = input().split(' ')
        print(inputList)
        command = inputList.pop(0)
        print(command)
        print('userinput : {}'.format(inputList))
        if len(inputList) > 0:
            if command == "insert":
                eval('myList.{0}({1}, {2})'.format(command, inputList[0], inputList[1]))
                print('Log : {}'.format(myList))
            if command == 'remove' and inputList[0] not in myList:
                print('Element not in list')
            else:
                eval('myList.{}({})'.format(command, inputList[0]))
                print('Log : {}'.format(myList))
        elif command == 'print':
            print(myList)
        else:
            eval('myList.{}()'.format(command))
            print('Log : {}'.format(myList))
