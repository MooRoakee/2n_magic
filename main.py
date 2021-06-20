ans = []
N = input('输入N:')
N = int(N)
c = [0] * N


def plus():
    c[len(c) - 1] += 1
    for i in range(len(c) - 1, -1, -1):
        if c[i] >= 2:
            c[i - 1] += c[i] // 2
            c[i] = c[i] % 2


def get_common_str_front(s1, s2):
    for i in range(len(s1)):
        flag = 0
        for j in range(len(s2)):
            if i + j < len(s1) and s1[i + j] != s2[j]:
                flag = 1
                break
        if flag == 1:
            pass
        else:
            return len(s1) - i

    return len(s1) - i - 1


def cal():
    for i in range(2 ** N):
        flag = 0
        if len(ans) == 0:
            for each in c:
                ans.append(each)

        else:
            if ''.join(str(each) for each in c) in ''.join(str(each) for each in ans) or ''.join(
                    str(each) for each in c) in ''.join(str(each) for each in ans[len(ans) // 2:len(ans)]) + ''.join(
                str(each) for each in ans[0:len(ans) // 2]):
                pass
            else:
                sub_len = get_common_str_front(''.join(str(each) for each in ans[len(ans) - len(c):len(ans)]),
                                               ''.join(str(each) for each in c))
                for each in c[sub_len:len(c)]:
                    ans.append(each)

        plus()

    print(ans)
    print(len(ans))


cal()
input('敲任意键退出...')
