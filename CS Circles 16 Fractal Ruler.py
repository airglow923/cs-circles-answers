def ruler(n):
    if n == 1:
        print('-')
    else:
        ruler(n - 1)
        print(n * '-')
        ruler(n - 1)
