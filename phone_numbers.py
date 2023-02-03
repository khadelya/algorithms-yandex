def get_number(num):
    new = ""
    for x in num:
        if x.isdigit():
            new += x
    return new


with open("input.txt", "r") as file:
    contents = file.read().split()
    ans = ""
    code = "495"
    new, num1, num2, num3 = [get_number(x) for x in contents]
    num = [num1, num2, num3]
    if len(new) == 11:
        for n in num:
            if len(n) == 11 and n[1:] == new[1:]:
                ans += "YES\n"
            elif len(n) == 7 and code + n == new[1:]:
                ans += "YES\n"
            else:
                ans += "NO\n"
    elif len(new) == 7:
        for n in num:
            if len(n) == 11 and n[1:] == code + new:
                ans += "YES\n"
            elif len(n) == 7 and n == new:
                ans += "YES\n"
            else:
                ans += "NO\n"
    else:
        print("Wrong new number")

with open("output.txt", "w") as file:
    file.write(ans)
