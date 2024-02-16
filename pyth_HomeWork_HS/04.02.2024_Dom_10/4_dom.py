# 4. Палиндром: Напишете рекурсивна функция, която проверява
# дали даден низ е палиндром (четене отпред назад и отзад
# напред дава еднакви резултати).

def is_palindrome(s):
    s = s.lower()  # Превръщаме всички букви в низа в малки, за да игнорираме главни/малки букви
    s = ''.join(c for c in s if c.isalnum())  # Премахваме всички символи, които не са букви или цифри

    if len(s) <= 1:
        return True
    elif s[0] == s[-1]:
        return is_palindrome(s[1:-1])
    else:
        return False

# Пример за извикване на функцията с низ "A man, a plan, a canal, Panama!"
result = is_palindrome("A man, a plan, a canal, Panama!")
print(result)
