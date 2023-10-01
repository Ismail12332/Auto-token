def expanded_form(num):
    a = 0
    b = 0
    x = 0
    if num > 100:
        a += num % 10
        b += num / 10
        c = int(b) * 10
        x = num - (int(a) + int(b))
        return f"{c} + {x} + {a}"

    if 100 < num > 1000:
        a += num % 100
        b += num / 100
        c = int(b) * 10
        x = num - (a + b)
        return f"{c} + {x} + {a}"
    
    
    if 1000 > num > 10000:
        a += num % 1000
        b += num / 1000
        c = int(b) * 10

        return f"{c} + {a}"


    
wer = expanded_form(344)
print(wer)