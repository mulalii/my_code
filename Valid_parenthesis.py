class Solution:
    def isValid(self, s: str) -> bool:
        
        i_parser = s[0: :2]
        j_parser = s[1: :2]

        i = 0
        j = 0
        max_ = len(j_parser)

        char_array = []

        while i < max_:
            while j < max_:
                if '(' in i_parser and ')' in j_parser:
                    char_array.append(i_parser[i])
                    char_array.append(j_parser[j])

                elif '[' in i_parser and ']' in j_parser:
                    char_array.append(i_parser[i])
                    char_array.append(j_parser[j])

                elif '{' in j_parser and '}' in j_parser:
                    char_array.append(i_parser[i])
                    char_array.append(j_parser[j])

                else:
                    return False

                j+=1
                i+=1

        if len(char_array) % 2 != 0:
            return False

        if len(char_array) != len(char_array):
            return False

        return True  
