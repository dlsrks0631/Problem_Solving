def solution(triangles):
    for i in range(1, len(triangles)):
        for j in range(len(triangles[i])):
            if j == 0:
                triangles[i][j] = triangles[i][j] + triangles[i-1][j]
            elif j == len(triangles[i]) - 1:
                triangles[i][j] = triangles[i][j] + triangles[i-1][j-1]
            else:
                triangles[i][j] = triangles[i][j] + max(triangles[i-1][j-1], triangles[i-1][j])

    return max(triangles[-1])