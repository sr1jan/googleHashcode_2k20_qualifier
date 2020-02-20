if __name__ == '__main__':
    info = list(map(int, input().split()))
    B, L, D = info[0], info[1], info[2]

    B_scores = list(map(int, input().split()))

    L_info = {}
    seen_b = set()
    for i in range(L):
        l = list(map(int, input().split()))
        L_info[i] = [[l[0], l[1], l[2]], [], []]
        books = list(map(int, input().split()))
        books = list(set(books)-seen_b)
        books = sorted(books, key=lambda x: B_scores[x], reverse=True)
        for b in books: seen_b.add(b)
        b_sum = 0
        for b in books:
            b_sum += B_scores[b]
        L_info[i][1] = books
        L_info[i][2] = b_sum

    L_order = [l for l in range(L)]
    L_order = sorted(L_order, key=lambda x: (L_info[x][0][1], - L_info[x][2]))

    print(D, L_info[L_order[0]][0][1])
    # n_l = [c for c in L_order if len(L_info[c][1]) is not 0]
    # print(len(n_l))
    # for l in L_order:
    #     n_b = len(L_info[l][1])
    #     if n_b is 0: continue
    #     print(l, n_b)
    #     for b in L_info[l][1]:
    #         print(b, end=' ')
        # print()





