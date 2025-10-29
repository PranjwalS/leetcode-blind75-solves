def existHelper(board, i, j, word):
    if not word:
        return True
    prev = board[i][j]
    found = False
    board[i][j]='#'
    rows, cols = len(board), len(board[0])
    if i<rows-1 and board[i+1][j]==word[0]:
        found |= existHelper(board, i+1, j, word[1:])
    
    if i>0 and board[i-1][j]==word[0]:
        found |=  existHelper(board, i-1, j, word[1:])
    
    if j>0 and board[i][j-1] == word[0]:
        found |= existHelper(board, i, j-1, word[1:])
    
    if j<cols-1 and board[i][j+1] == word[0]:
        found |= existHelper(board, i, j+1, word[1:])
    
    board[i][j]=prev
    return found

            
            
            
def exist(board, word):
    arr =[]
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j]==word[0]:
                arr.append(existHelper(board, i, j, word[1:]))
    return True if True in arr else False



board = [["C","A","A"],["A","A","A"],["B","C","D"]]
word = "AAB"
print(exist(board, word))