class GridGen():
    rows, cols = (3, 3)
    resultsArr = [[0 for i in range(cols)] for j in range(rows)]
    resultsArr[0][0] = 0
    resultsArr[0][1] = 1
    resultsArr[0][2] = 2
    resultsArr[1][0] = 2
    resultsArr[1][1] = 0
    resultsArr[1][2] = 1
    resultsArr[2][0] = 1
    resultsArr[2][1] = 2
    resultsArr[2][2] = 0

GridGenerate()