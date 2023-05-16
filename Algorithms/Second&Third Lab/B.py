def main():
    n = int(input())
    st = []
    sz = 0
    ans = 0
    while n:
        n -= 1
        x = int(input())
        if not sz:
            st.append(x)
            st.append(1)
            sz += 2
        elif st[sz - 2] != x:
            if st[sz - 1] > 2:
                ans += st[sz - 1]
                sz -= 2
            if not sz or st[sz - 2] != x:
                st.append(x)
                st.append(1)
                sz += 2
            else:
                st[sz - 1] += 1
        else:
            st[sz - 1] += 1
    if sz and st[sz - 1] > 2:
        ans += st[sz - 1]
    print(ans)


if __name__ == '__main__':
    main()