with open("quotes.txt", "r", encoding = "utf-8") as file:
    data  = file.read()
    print(data)

author = input("Хто написав ці рядки? ")

with open("quotes.txt", "a", encoding = "utf-8") as file:
    file.write(author + "\n")


while True:
    answer = input("Хочете добавити ще цитати(так/ні)")
    answer = answer.lower()

    if answer == "так":
        quote = input("Введіть цитату:")
        author = input("Введіть цитату:")

        file = open("quotes.txt", "a", encoding = "utf-8")
        file.write(quote + "\n")
        file.write("(" + author + ")" + "\n")
        file.close()

    else:
        break

print("зчитуємо фінальний файл:")
with open("quotes.txt", "r", encoding = "utf-8") as file:
    data  = file.read()
    print(data)