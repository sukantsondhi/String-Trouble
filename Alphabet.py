
string = "aabccb"


def solution(string):

    # Converting string to list S
    S = []
    S[:0] = string

    length = len(S)
    count = 0

    for alphabet in range(0, length + 3):

        if(S[alphabet] == "a"):
            
            if (alphabet < (length - 1)):
                if (S[alphabet + 1] != "b" ):
                    S.insert((alphabet + 1),"b")
                    count += 1
                    length += 1


        if((S[alphabet] == "b")):

            if (alphabet <= (length - 1)):
                if (S[alphabet + 1] != "c"):
                    S.insert((alphabet + 1),"c")
                    count += 1
                    length += 1
            

        if(S[alphabet] == "c"):
            
            if (alphabet < (length - 1)):
                if (S[alphabet + 1] != "a"):
                    S.insert((alphabet + 1),"a")
                    count += 1
                    length += 1

            else:
                break


    return print(f"Number of alphabets to be added to the string are: {count}")

print(solution(string))
