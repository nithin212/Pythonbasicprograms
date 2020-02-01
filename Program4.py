def replace_adv(ch):
    first_ch=ch[0]
    ch=ch.replace(first_ch,"$")
    cha=first_ch+ch[1:]
    return cha

print(replace_adv("return"))
