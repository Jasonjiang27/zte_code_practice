# f = open("/home/jyz/niv2-camp/jiangyaozu/test.txt", 'r')
#
# lines = f.readlines()
# total_lines = len(lines)
# numbers = [""] * (total_lines / 4)
# print numbers
# #import pdb;pdb.set_trace()
# # for i in range(total_lines / 4):
# #     print i
# #     numbers[i] = "1"
# print len(numbers)
# i=0
# while i < total_lines-3:
#     line_string = lines[i]
#     j = 0
#     while j < len(line_string)-2:
#         if j != "":
#             k = i / 4
#             if j%3 == 0:
#                 x = "a"
#             elif j%3 == 1:
#                 x = "b"
#             else:
#                 x = "c"
#         numbers[k] += x
#         j += 1
#     i += 4
# f.close()
#
# # number_string_dict = {
# #     1: ["f", "i"],
# #     2: ["b", "f", "e", "g", "h"],
# #     3: ["b", "e", "f", "h", "i"],
# #     4: ["d", "e", "f", "i"],
# #     5: ["b", "d", "e", "h", "i"],
# #     6: ["b", "d", "e", "g", "h", "i"],
# #     7: ["b", "f", "i"],
# #     8: ["b", "d", "e" ,"f", "g", "h", "i"],
# #     9: ["b", "d", "e" ,"f", "h", "i"],
# #     0: ["b", "d" ,"f", "g", "h", "i"]
# # }
# number_string_dict = {
#     1: "cc",
#     2: "bbcab",
#     3: "bbcbc",
#     4: "abcc",
#     5: "babbc",
#     6: "bababc",
#     7: "bcc",
#     8: "babcabc",
#     9: "babcbc",
#     0: "bacabc"
# }
#
# print numbers
class CheckNum(object):
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
    def read_file(self):
        f = open("/home/jyz/niv2-camp/jiangyaozu/test.txt", 'r')
        # for l in f.readlines():
        #     line = l.strip("\n")
        lines = f.readlines()
        i=0
        numbers = []
        total_lines = len(lines)
        while i < total_lines-3:
            line_string = lines[i]
            j = 0
            while j < len(line_string)-2:
                if j != "":
                    k = i / 4
                    if j%3 == 0 or j%3==2:
                        x = "|"
                    elif j%3 == 1:
                        x = "_"

                numbers[k] += x
                j += 1
            i += 4
        f.close()


    def read_one_account(self,(line_1, line_2, line_3)):
        characters = list()
        for i in range(9):
            ch = (line_1[i*3:(i+1)*3] + line_2[i*3:(i+1)*3] + line_3[i*3:(i+1)*3])
            characters.append(self.number_string_dict[ch])
        return characters

    def read_file(self):
        filename = "/home/jyz/niv2-camp/jiangyaozu/test.txt"
        f = open(filename, "r")
        lines = f.readlines()
        accounts = []
        i = 0
        while i < len(lines)-4:
            accounts.append(lines[i:i+4])
            i += 4
        print accounts
        return accounts

    def read_accounts(self):
        accounts = self.read_file()
        numbers = []
        for account in accounts:
            line_1 = account[0]
            line_2 = account[1]
            line_3 = account[2]
            characters = self.read_one_account((line_1, line_2, line_3))
            numbers.append(characters)
        return numbers

    def check_number(self, numbers):
        result = 0
        for i in range(9):
            result += int(numbers[i])*(9-i)
        return result % 11 == 0

    def get_numbers(self):
        return self.read_file()
