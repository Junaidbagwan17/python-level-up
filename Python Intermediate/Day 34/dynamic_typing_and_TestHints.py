my_age : int
my_name: str
height: float
is_human : bool

my_age = 12 # it is dynamic typing and help you to know what age should dtype must be


def police_check(age:int) -> bool:
    if age > 18:
        can_drive = True
    else:
        can_drive =  False
    return can_drive


if police_check(21):
    print("No need to Pay fine, but sure other docs are clear")
else:
    print("pay fine")