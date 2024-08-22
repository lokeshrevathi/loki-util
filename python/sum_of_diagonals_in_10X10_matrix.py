#sum_of_diagonals_in_10X10_matrix
def sumDiagonals(s: str) -> int:
    sum = 0
    rows = s.split("\n")
    print(len(rows))
    i = 0
    while i < len(rows):
        vals = [j for j in rows[i].split(" ") if j != '' and j != ' '] #rows[i].split(" ")
        print(vals)
        sum = sum + int(vals[i])
        i += 1
    return sum

if __name__ == "__main__":
    s = open("C:/Users/lokesh.subramaniyan/Documents/python/ip.txt", "+r").read()
    print(sumDiagonals(s))