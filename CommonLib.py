def reverse(Number):
    Reverse = 0

    while(Number > 0):
        Reminder = Number %10
        Reverse = (Reverse *10) + Reminder
        Number = Number // 10

    return (Reverse)

def isParlindrom(num):

    reverse_num = reverse(num)
    if num == reverse_num:
        return True

    return False

