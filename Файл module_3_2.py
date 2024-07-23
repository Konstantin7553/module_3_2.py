def send_mail(message, recipient, sender="university.help@gmail.com"):
    def is_valid_email(email):
        return "@" in email and (email.endswith(".com") or email.endswith(".ru")
                                 or email.endswith(".net"))

    if not is_valid_email(recipient) or not is_valid_email(sender):
        print(f"Невозможно отправить письмо с адреса <{sender}> на адрес <{recipient}")
        return
    if sender == recipient:
        print("Нельзя отправить письмо самому себе!")
        return
    if sender == "university.help@gmail.com":
        print(f"Письмо успешно отправлено с адреса <{sender}> на адрес <{recipient}>.")

    else:
        print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса <{sender}> на адрес <{recipient}>.")


send_mail("Это сообщение для прверки связи", "vasyok1337@gmail.com")
send_mail("Вы видите это сообщение как лучший студент курса!", "urban.fan@mail.ru",
          sender="urban.info@gmail.com")
send_mail("Пожалуйста, исправьте задание", "urban.student@mail.ru",
          sender="urban.teacher@mail.uk")
send_mail("Напоминаю самому себе о вебинаре", "urban.teacher@mail.ru",
          sender="urban.teacher@mail.ru")
