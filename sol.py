if __name__ == '__main__':
    info = list(map(int, input().split()))
    B, L, D = info[0], info[1], info[2]

    B_scores = list(map(int, input().split()))

    L_info = {}
    for i in range(L):
        l = list(map(int, input().split()))
        L_info[i] = [[l[0], l[1], l[2]], [], []]
        books = list(map(int, input().split()))
        books = sorted(books, key=lambda x: B_scores[x])
        b_sum = 0
        for b in books:
            b_sum += B_scores[b]
        L_info[i][1] = books
        L_info[i][2] = b_sum

    print(B, L, D)
    print(B_scores)
    print(L_info)



