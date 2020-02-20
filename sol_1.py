if __name__ == '__main__':
    info = list(map(int, input().split()))
    B, L, D = info[0], info[1], info[2]
    print(D)

    B_scores = list(map(int, input().split()))

    L_info = {}
    for i in range(L):
        nj, tj, mj = map(int, input().split())
        L_info[i] = [[nj, tj, mj], [], []]

        books = list(map(int, input().split()))
        books = sorted(books, key=lambda x: B_scores[x], reverse=True)

        hd = D - tj
        scan_bks = mj*hd
        if scan_bks < len(books):
            books = books[0:scan_bks]
        b_sum = 0
        for b in books:
            b_sum += B_scores[b]
        L_info[i][1] = books
        L_info[i][2] = b_sum


    L_order = [l for l in range(L)]
    L_order = sorted(L_order, key=lambda x: L_info[x][2], reverse=True)

    # seen_b = set()
    # for l in L_order:
    #     bks = L_info[l][1]
    #     if(len(bks)) is 0: continue
    #     bks = list(set(bks)-seen_b)

    #     for b in bks: seen_b.add(b)
    #     L_info[l][1] = bks


    # n_l = [c for c in L_order if len(L_info[c][1]) is not 0]
    # print(len(n_l))
    # for l in L_order:
    #     n_b = len(L_info[l][1])
    #     if n_b is 0: continue
    #     print(l, n_b)
    #     for b in L_info[l][1]:
    #         print(b, end=' ')
    #     print()





