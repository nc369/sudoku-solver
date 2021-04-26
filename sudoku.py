#sudoku
import numpy as np

a = np.zeros((9,9))

def InputSudoku(board,row,col,no):
    """
    

    Parameters
    ----------
    board : ndarray
        sudoku board as an np array of shape (9,9)
    row : int
        row in which value is to be inserted (indexing starts from 1)
    col : int
        column in which value is to be inserted (indexing starts from 1)
    no : int
        the value to be inserted.

    Returns
    -------
    None.

    """
    board[row][col]=int(no)
    return(board)
    
def SetupSudoku():
    """
    Sets up the sudoku board to be solved.
    Asked the user to input values of the sudoku alongs with its coordinates.
    The coordinates for both row and column are indexed starting from 1.

    Returns
    -------
    ndarray
        returns the sudoku board that needs to be solved

    """
    
    board = np.zeros((9,9))
    value=0
    while value!=1:
        v=int(input("Enter 1 if this is the last value otherwise 0:"))
    
        x=int(input("Enter row:"))
        y=int(input("Enter collum:"))
        z=float(input("Enter value:"))
        board=InputSudoku(board,x-1,y-1,z)
        print("value inserted")
        value=v
    
    return(board)

    
b=np.array([[8,0,0,     0,0,0,      0,0,0],
            [0,0,3,     6,0,0,      0,0,0],
            [0,7,0,     0,9,0,      2,0,0],
            
            [0,5,0,     0,0,7,      0,0,0],
            [0,0,0,     0,4,5,      7,0,0],
            [0,0,0,     1,0,0,      0,3,0],
            
            [0,0,1,     0,0,0,      0,6,8],
            [0,0,8,     5,0,0,      0,1,0],
            [0,9,0,     0,0,0,      4,0,0]])
  
    
def IdCol(a,x,y):
    """
    

    Parameters
    ----------
    a : ndarray
        sudoku board as an np array of shape (9,9)
    x : int
        index of row (indexing starts from 1)
    y : int
        index of collumn (indexing starts from 1)

    Returns
    -------
    ndarray
        returns the column of a

    """
    z=a[:,y-1]
    return(z)
    
def IdRow(a,x,y):
    """
    

    Parameters
    ----------
    a : ndarray
        sudoku board as an np array of shape (9,9)
    x : int
        index of row (indexing starts from 1)
    y : int
        index of collumn (indexing starts from 1)

    Returns
    -------
    ndarray
        returns the row of a

    """
    z=a[x-1]
    return(z)
    
def IdTinySquare(a,x,y):
    """
    

    Parameters
    ----------
    a : ndarray
        sudoku board as an np array of shape (9,9)
    x : int
        index of row (indexing starts from 1)
    y : int
        index of collumns (indexing starts from 1)

    Returns
    -------
    ndarray
        returns smaller square corresponding to the coordinates (x,y)

    """
    if x<=3:
        if y<=3:
            z=a[:3,:3]
        elif 3<y<=6:
            z=a[:3,3:6]
        else:
            z=a[:3,6:]
    elif 3<x<=6:
        if y<=3:
            z=a[3:6,0:3]
        elif 3<y<=6:
            z=a[3:6,3:6]
        else:
            z=a[3:6,6:]
    else:
        if y<=3:
            z=a[6:,0:3]
        elif 3<y<=6:
            z=a[6:,3:6]
        else:
            z=a[6:,6:]
            
    return(z)




def ReadNonZero(k):
    """
    

    Parameters
    ----------
    k : ndim array
        1 dim or 2 dim array whose non zero elements are to be read

    Returns
    -------
    list of non zero elements in a

    """
    l=[]
    if len(k)==3:
        for i in range(3):
            for j in range(3):
                if k[i][j]!=0:
                    v=k[i][j]
                    l.append(v)
    else:
        for i in range(len(k)):
            if k[i]!=0:
                v=k[i]
                l.append(v)
    return(l)
        

def ReadZeros(a):
    """
    

    Parameters
    ----------
    a : ndarray
        sudoku board as an np array of shape (9,9)

    Returns
    -------
    list
        contains len 2 arrays where each array cooresponds to coordinates to a non zero element in a

    """
    place=[]
    for i in range(9):
        for j in range(9):
            if a[i][j]==0:
                place.append([i,j])
    return(place)
    





def solveSudoku(a):
    """
    

    Parameters
    ----------
    a : ndarray
        sudoku board as an np array of shape (9,9)

    Returns
    -------
    ntuple
        If sudoku is solveable, return the solved sudoku puzzle and the number of steps taken
    
    None
        If the sudoku is unsolveable

    """
    

    place=ReadZeros(a)
    
    
    j=0
    steps=0 
    count=1  #tracks the number inputted in blank space
    
    while j<len(place):
        steps=steps+1
        k=place[j]
        done=0
        
        if j==-1:
            return None # can not be solved
            break
        
        if count==10:  #if count increases to 10
            a[k[0]][k[1]]=0
            j=j-1
            m=place[j]
            count=a[m[0]][m[1]]
            continue
        
        
        #take the pos and find the row
        l=IdRow(a,k[0]+1,k[1]+1)
        # check if there is any value in row = input
        l=ReadNonZero(l)
       
        for i in range(len(l)):
            if l[i]==count:
                count=count+1
                done=done+1
                break
        if done==1:
            continue
        
        
        #take the pos and find the col
        l=IdCol(a,k[0]+1,k[1]+1)
        # check if there is any value in row = input
        l=ReadNonZero(l)
        for i in range(len(l)):
            if l[i]==count:
                count=count+1
                done=done+1
                break
        if done==1:
           continue   
            
            
        #take the pos and find the tiny square
        l=l=IdTinySquare(a,k[0]+1,k[1]+1)
        # check if there is any value in row = input
        l=ReadNonZero(l)
        for i in range(len(l)):
            if l[i]==count:
                count=count+1
                done=done+1
                break
        if done==1:
            continue
        
        a[k[0]][k[1]]=count
        count=1
        j=j+1
    
    return(a,steps)
    

def sudoku(a):
    a=SetupSudoku(a)
    a=solveSudoku(a)
    return(a)
    


print(solveSudoku(b))
    
    

    
