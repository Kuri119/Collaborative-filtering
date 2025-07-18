import CollaberativeFiltering
import math


def rmse(matrix, m, n, target):
    print("Evaluate:")
    cnt = 0
    x = 0
    for movie in range(m):
        if matrix[movie][target] != -1:
            test = [[-1] * n for i in range(m)]
            for i in range(m):
                for j in range(n):
                    test[i][j] = matrix[i][j]
            test[movie][target] = -1
            predict, similarity = CollaberativeFiltering.getPredict(test, m,
                                                                    n, target, movie)

            print("Movie {} with:".format(movie), end=" ")
            print(similarity)
            if predict != -1:
                x += math.pow(matrix[movie][target] - predict, 2)
                cnt += 1
    if cnt != 0:
        result = math.sqrt(x/cnt)
    else:
        result = -1

    return result

