def read_file():
        filename = "/home/jyz/niv2-camp/jiangyaozu/test.txt"
        f = open(filename, "r")
        all_line = []
        for line in f.readlines():
            line=line.strip('\n')
            all_line.append(line)
        accounts = []
        i = 0
        while i < len(all_line)-4:
            accounts.append(all_line[i:i+4])
            i += 4
        print accounts
        return accounts

number_string_dict = {
        "     |  |": 1,
        " _  _||_ ": 2,
        " _  _| _|": 3,
        "   |_|  |": 4,
        " _ |_  _|": 5,
        " _ |_ |_|": 6,
        " _   |  |": 7,
        " _ |_||_|": 8,
        " _ |_| _|": 9,
        " _ | ||_|": 0
    }

def read_accounts():
        accounts = read_file()
        numbers = []
        for account in accounts:
            line_1 = account[0]
            line_2 = account[1]
            line_3 = account[2]
            characters = read_one_account((line_1, line_2, line_3))
            numbers.append(characters)
        return numbers

def read_one_account((line_1, line_2, line_3)):
        import pdb;pdb.set_trace()
        characters = list()
        for i in range(9):
            ch = (line_1[i*3:(i+1)*3] + line_2[i*3:(i+1)*3] + line_3[i*3:(i+1)*3])
            print ch
            characters.append(number_string_dict[ch])
        return characters

read_accounts()
