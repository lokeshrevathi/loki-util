#letter_combinations
def letterCombinations(digits: str) -> list:
    letters = [["a","b","c"], ["d","e","f"], ["g","h","i"], ["j","k","l"], ["m","n","o"],["p","q","r","s"], ["t","u","v"], ["w","x","y","z"]]
    combinations = []
    for i in str:
        for j in letters[int(i) + 2]:
            