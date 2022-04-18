default_path = "password.txt"

if True:  # Functions

    def get_common_passwords(path=default_path):
        return [i.strip() for i in open(path, "r").readlines()]

    def get_password_total_num(path=default_path):
        return len(get_common_passwords(path))

    def simplify(text):
        answer = (
            text.strip()
            .replace(" ", "")
            .replace("_", "")
            .replace("-", "")
            .replace(".", "")
            .lower()
        )
        if answer:
            return answer
        else:
            return "this is not included in any password 2893ytugihou1fyuigyho1u90gy8uhi2fjhiju9gytguhifehovuf289hioevw"

    def inside(part, whole):
        return simplify(part) in simplify(whole)

    def is_same(one, another):
        return inside(one, another) and inside(another, one)

    def conclude():
        pass

    def yes_or_no(input):
        if "q" in input.lower().strip():
            quit()
        return "y" in input.lower().strip()

    def is_easy(text):
        bad = False
        common_phrases = [
            "123",
            "abc",
            "qwe",
            "gwe",
            "qaw",
            "waq",
            "!@#",
            "111",
            "222",
            "333",
            "444",
            "555",
            "666",
            "777",
            "888",
            "999",
            "000",
            "987",
            "258",
            "147",
            "369",
            "qaz",
            "zaq",
            "ewq",
            "ewg",
            "*&^",
            "^%$",
            "pass",
            "word",
            "admin",
            "login",
            "ice",
            "day",
            "q1w",
            "w1q",
            "q2w",
            "w2q",
            "g2w",
            "w2g",
            "g1w",
            "w1g",
            "qaz",
            "zaq",
            "gaz",
            "zag",
        ]
        for index, common_phrase in enumerate(common_phrases):
            if inside(common_phrase, text):
                print(
                    f'Sorry, common phrase #{index}: "{common_phrase}" is in password "{text}". '
                    f"Password is too easy. "
                )
                bad = True
        if not bad:
            print(f'\nYour password "{text}" passed EASYTEST. ')
        else:
            print(f'\nYour password "{text}" failed EASYTEST. ')
        conclude()
        return not bad

    def is_short(text, threshold=6):
        length = len(text)
        if length <= threshold:
            print(
                f'Sorry, your password "{text}" has length {length}, too short (≤{threshold}). '
                f"Password is too short. "
            )
            print(f'\nYour password "{text}" failed SHORTTEST. ')
        else:
            print(f'\nYour password "{text}" passed SHORTTEST. ')
        conclude()

    def is_common(text, path=default_path, test_up_to=10000000000):
        bad = False
        for index, common_password in enumerate(
            get_common_passwords(path)[:test_up_to]
        ):
            if is_same(common_password, text):
                print(
                    f'Sorry, password "{text}" is the #{index} common password. '
                    f"Password is too common. "
                )
                bad = True
            elif inside(text, common_password):
                print(
                    f'Sorry, password "{text}" is in the #{index} common password: "{common_password}". '
                    f"Password is too common. "
                )
                bad = True
        if not bad:
            print(f'\nYour password "{text}" passed COMMONTEST. ')
        else:
            print(f'\nYour password "{text}" failed COMMONTEST. ')
        conclude()

    def generate_password(web):
        website = simplify(web.split(".")[0].split("//")[-1].split("/")[0])
        for from_, to in zip(list("asioz"), list("@$102")):
            website = website.replace(from_, to)
        web1 = website[::2].lower()
        web2 = website[1::2].upper()
        output = ""
        if len(web1) == len(web2):
            _ = zip(web1, web2)
        else:
            _ = zip(web1, web2 + " ")
        for a, b in _:
            output += a + b
        print(f'Generated password for {web}: "{output.strip()}"')
        return output.strip()


def all_tests(text, path=default_path):
    is_easy(text)
    is_short(text)
    is_common(text, path)


def main():
    if yes_or_no(input("Generate password? \n>>> ")):
        _ = generate_password(input("Website name? \n>>> "))
        if yes_or_no(input("Check generated password? \n>>> ")):
            all_tests(_, default_path)
    if yes_or_no(input("Check your own password? \n>>> ")):
        all_tests(input("Password? \n>>> "), default_path)
    main()


main()
