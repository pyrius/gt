def ammo(n):
    cnt = 0
    while cnt < n:
        yield cnt
        cnt += 1


def req(size, ammo):
    while size > 0:
        size -= 1
        item = next(ammo)
        print(f"Here is the item {item}", item*10)


ammo_w = ammo(10)
size = 3
try:
    req(size, ammo_w)
except:
    print("done")
