def pascalTirangle(numRows):
    if numRows <= 0:
        return [[]]
    if numRows == 1:
        return [[1]]
    result = [[1]]
    for i in range(numRows-1):
        previous = result[-1]
        current = [1]
        for j in range(len(previous)-1):
            current.append(previous[j] + previous[j+1])
        current.append(1)
        result.append(current)
    return result

numRows = 5
triangle = pascalTirangle(numRows)
for li in triangle:
    print(li)