# Import
from colorama import Fore

# Code
if True:
    # Constants
    if True:
        _error = Fore.RED
        _warn = Fore.YELLOW
        _output = Fore.BLUE
        _input = Fore.GREEN
        _origin = Fore.RESET
        _return = "\n"
        inputquote = f"{_return}{_input}Input needed in program: {_return}>>> "
        _ = ["ERR"] * 5

    # Functions
    def copy(l):
        return list([copy(_) for _ in l]) if type(l) == list else l

    def unzip(test_list):
        return ["".join([i for i, j in test_list]), [j for i, j in test_list]]

    def filtered(original, keep):
        return unzip(
            list(
                filter(
                    lambda x: x[0] in keep, list(zip(original, range(0, len(original))))
                )
            )
        )

    # Class
    class Code:
        def __init__(self, code):
            self.code = code

        def clean_code(self):
            # print(self.code.split('#')[::2])
            return "".join(self.code.split("#")[::2])

        def get_code(self):
            return self.clean_code()

        def get_other_half(self, index):
            character = self.get_code()[index]
            l1, l2 = "([{<,./", ")]}>;:\\"
            if character in l2:
                search = self.get_code()[:index][::-1]
                search_for = l1[l2.index(character)]
            else:
                search = self.get_code()[index::][1::]
                search_for = l2[l1.index(character)]
            new_code, indexes_ = filtered(search, [character, search_for])
            eliminate = f"{character}{search_for}"
            while eliminate in new_code:
                i = new_code.index(eliminate)
                new_code = new_code[:i] + new_code[i:][1:][1:]
                indexes_ = indexes_[:i] + indexes_[i:][1:][1:]
            answer = indexes_[new_code.index(search_for)]
            if character in l2:
                return index - (answer + 1)
            return answer + 1 + index

        def get_loop_end(self, index):
            search = self.get_code()
            character = self.get_code()[index]
            _____ = character
            l1, l2 = "([{<,./", ")]}>;:\\"
            new_code, indexes_ = filtered(search, l1 + l2 + character)
            eliminates = [l1[i] + l2[i] for i in range(len(l1))]
            _nc, _ind = copy(new_code), copy(indexes_)
            _nc = _nc[: _ind.index(index)] + _nc[_ind.index(index) + 1 :]
            _ind = _ind[: _ind.index(index)] + _ind[_ind.index(index) + 1 :]
            while _____ in _nc:
                _nc = _nc[: _nc.index(_____)] + _nc[_nc.index(_____) + 1 :]
                _ind = _ind[: _nc.index(_____)] + _ind[_nc.index(_____) + 1 :]
            for ind in indexes_:
                if ind not in _ind + [index]:
                    new_code = (
                        new_code[: indexes_.index(ind)]
                        + new_code[indexes_.index(ind) + 1 :]
                    )
                    indexes_ = (
                        indexes_[: indexes_.index(ind)]
                        + indexes_[indexes_.index(ind) + 1 :]
                    )
            while any([eliminate in new_code for eliminate in eliminates]):
                for eliminate in eliminates:
                    if eliminate in new_code:
                        i = new_code.index(eliminate)
                        new_code = new_code[:i] + new_code[i:][1:][1:]
                        indexes_ = indexes_[:i] + indexes_[i:][1:][1:]
            return indexes_[new_code.index(_____) + 2]

        def execute(
            self,
            cells=[0],
            cursor=[0],
            copied=None,
            portals={},
            functions={},
            sace=True,
            scc=True,
        ):
            # sace  : Show Actual Commands Executed
            # scc   : Show Current Cells
            pointer = 0
            code = self.get_code()
            if scc:
                #
                print(f"{_warn}{_return}Current cells: {cells}", end=_return)
            while pointer < len(code):
                digit = code[pointer]
                if sace:
                    #
                    print(f"{_warn}{_return}Executing: {digit}", end=_return)
                location = f'cells{"".join(([f"[{i}]" for i in cursor]))}'
                if digit == "Q":
                    print(f"{_warn}{_return*2}Process finished by exit code 'q'")
                    return _
                elif digit == "q":
                    # Equivalent: break
                    return cells, cursor, copied, portals, functions
                elif digit == "'":
                    #
                    print("\t", end="")
                elif digit == '"':
                    #
                    print("\n", end="")
                elif digit == "O":
                    value = eval(location)
                    if isinstance(value, int):
                        print(f"{_output}{value}", end="")
                    else:
                        print(
                            f"{_error}"
                            f"{_return}"
                            f"Location {cursor} has "
                            f"value {value}, "
                            f"type {type(value)}, "
                            f"and cannot be directly output. {_return}"
                            f"ERR listout"
                        )
                        return _
                elif digit == "o":
                    values = eval(location)
                    if isinstance(values, int):
                        value = values
                        try:
                            print(f"{_output}{chr(value)}", end="")
                        except ValueError:
                            print(
                                f"{_error}"
                                f"{_return}"
                                f"Location {cursor} has "
                                f"value {value}, "
                                f"not in range(0x110000), "
                                f"and thus caused error: {_return}"
                                f"ValueError: chr() arg not in range(0x110000){_return}"
                                f"ERR chroutrange"
                            )
                            return _
                    else:
                        index = 0
                        for value in values:
                            try:
                                print(f"{_output}{chr(value)}", end="")
                            except ValueError:
                                print(
                                    f"{_error}"
                                    f"{_return}"
                                    f"Location {cursor} has "
                                    f"value {values}, "
                                    f"of which index {index} "
                                    f"has value {value}, "
                                    f"not in range(0x110000), "
                                    f"and thus caused error: {_return}"
                                    f"ValueError: chr() arg not in range(0x110000){_return}"
                                    f"ERR chroutrange"
                                )
                                return _
                            else:
                                index += 1
                elif digit == "+":
                    value = eval(location)
                    try:
                        exec(f"{location}+=1")
                    except TypeError:
                        print(
                            f"{_error}"
                            f"{_return}"
                            f"Location {cursor} has "
                            f"value {value}, "
                            f"type {type(value)}, "
                            f"cannot be added one, "
                            f"and thus caused error: {_return}"
                            f'TypeError: can only concatenate list (not "int") to list{_return}'
                            f"ERR list+"
                        )
                        return _
                elif digit == "-":
                    value = eval(location)
                    try:
                        exec(f"{location}-=1")
                    except TypeError:
                        print(
                            f"{_error}"
                            f"{_return}"
                            f"Location {cursor} has "
                            f"value {value}, "
                            f"type {type(value)}, "
                            f"cannot be subtracted one, "
                            f"and thus caused error: {_return}"
                            f"TypeError: unsupported operand type(s) for -=: 'list' and 'int'{_return}"
                            f"ERR list-"
                        )
                        return _
                elif digit == "0":
                    # Easy
                    exec(f"{location}=0")
                elif digit == "a":
                    if cursor[-1] == 0:
                        print(
                            f"{_error}"
                            f"{_return}"
                            f"Location {cursor} has "
                            f"final value 0, "
                            f"cannot be subtracted one. "
                            f"i.e. cannot go left {_return}"
                            f"ERR pos0-"
                        )
                        return _
                    cursor[-1] -= 1
                    location = f'cells{"".join(([f"[{i}]" for i in cursor]))}'
                elif digit == "d":
                    cursor[-1] += 1
                    location = f'cells{"".join(([f"[{i}]" for i in cursor]))}'
                    try:
                        eval(location)
                    except IndexError:
                        location = f'cells{"".join(([f"[{i}]" for i in cursor[:-1]]))}'
                        exec(f"{location}.append(0)")
                elif digit == "s":
                    value = eval(location)
                    if isinstance(value, int):
                        exec(f"{location}=[0]")
                    cursor.append(0)
                elif digit == "w":
                    c = cursor[:]
                    cursor = cursor[:-1]
                    if not cursor:  # cursor==[]
                        print(
                            f"{_error}"
                            f"{_return}"
                            f"Location {c} has "
                            f"only one value, "
                            f"cannot be recursed. "
                            f"i.e. cannot go up {_return}"
                            f"ERR posoriginup"
                        )
                        return _
                elif digit == "i":
                    # Simple
                    exec(f"{location}={[ord(char) for char in input(inputquote)]}")
                elif digit == "I":
                    in_ = input(inputquote)
                    try:
                        int(in_)
                    except:
                        print(
                            f"{_error}"
                            f"{_return}"
                            f"Input has "
                            f"value {in_}, "
                            f"cannot be integerized. "
                            f"i.e. cannot store data {_return}"
                            f"and thus caused error: {_return}"
                            f"ValueError: invalid literal for int() with base 10: '{in_}'{_return}"
                            f"ERR badin"
                        )
                        return _
                    exec(f"{location}={in_}")
                elif digit == "c":
                    # Thought easy
                    copied = eval(f"copy({location})")
                elif digit == "v":
                    # Thought easy
                    if copied != None:  # Prevent 0 => False
                        exec(f"{location}={copied}")
                    else:
                        print(
                            f"{_error}"
                            f"{_return}"
                            f"Nothing was copied "
                            f"and thus caused error: {_return}"
                            f"NameError: name 'copied' is not defined{_return}"
                            f"ERR nocopy"
                        )
                        return _
                elif digit == "p":
                    pointer += 1
                    name = code[pointer]
                    portals[name] = copy(cursor)
                elif digit == "P":
                    pointer += 1
                    name = code[pointer]
                    try:
                        cursor = copy(portals[name])
                    except KeyError:
                        print(
                            f"{_error}"
                            f"{_return}"
                            f"Nothing called {name} was defined "
                            f"and thus caused error: {_return}"
                            f"KeyError: {name}{_return} "
                            f"ERR nodefport"
                        )
                        return _
                    location = f'cells{"".join(([f"[{i}]" for i in cursor]))}'
                    try:
                        eval(location)
                    except Exception as e:
                        print(
                            f"{_error}"
                            f"{_return}"
                            f"Portal exception: {_return}"
                            f"{e}{_return}"
                            f"Debug details: {_return}"
                            f"name: {name}{_return}"
                            f"cells: {cells}{_return}"
                            f"cursor: {cursor}{_return}"
                            f"portals: {portals}{_return}"
                            f"ERR port{name}"
                        )
                        return _
                elif digit == "f":
                    pointer += 1
                    name = code[pointer]
                    c = code[pointer:]
                    __ = c[1 : c.index("f")]
                    functions[name] = __
                    pointer += c.index("f")
                elif digit == "F":
                    pointer += 1
                    name = code[pointer]
                    try:
                        f = functions[name]
                    except KeyError:
                        print(
                            f"{_error}"
                            f"{_return}"
                            f"Nothing called {name} was defined "
                            f"and thus caused error: {_return}"
                            f"KeyError: {name}{_return} "
                            f"ERR nodeffunc"
                        )
                        return _
                    cells, cursor, copied, portals, functions = Code(f).execute(
                        cells, cursor, copied, portals, functions
                    )
                    if cells == "ERR":
                        return _
                elif digit in "([{<,./":
                    dictionary = dict(
                        zip(
                            list("([{<,./"),
                            [
                                lambda x: x == 0,
                                lambda x: x != 0,
                                lambda x: x > 0,
                                lambda x: x < 0,
                                lambda x: x >= 0,
                                lambda x: x <= 0,
                                lambda x: True,
                            ],
                        )
                    )
                    if not dictionary[digit](eval(location)):
                        try:
                            pointer = self.get_other_half(pointer)
                        except ValueError:
                            print(
                                f"{_error}"
                                f"{_return}"
                                f"Unpaired 'bracket' '{digit}' {_return}"
                                f"caused error: {_return}"
                                f"ValueError: substring not found {_return}"
                                f"ERR nopair{digit}"
                            )
                            return _
                elif digit == "l":
                    # Easy
                    try:
                        pointer = self.get_other_half(pointer + 1) - 1
                    except ValueError:
                        print(
                            f"{_error}"
                            f"{_return}"
                            f"Unpaired 'bracket' '{digit}' {_return}"
                            f"caused error: {_return}"
                            f"ValueError: substring not found {_return}"
                            f"ERR nopair{digit}"
                        )
                        return _
                elif digit == "|":
                    pointer = self.get_loop_end(pointer)
                elif digit == "_":
                    pointer = self.get_other_half(self.get_loop_end(pointer)) - 1
                pointer += 1
                if scc:
                    #
                    print(f"{_warn}{_return}Current cells: {cells}", end=_return)
            return cells, cursor, copied, portals, functions

    # More Functions
    def bf2bfp(code):
        return (
            filtered(code, ",.<>+-[]")[0]
            .replace(",", "iscwv")
            .replace(".", "o")
            .replace(">", "d")
            .replace("<", "a")
            .replace("]", "l]")
        )

    # More Constants
    ___ = bf2bfp(
        """
    ++++++++[>+>++>+++>++++>+++++>++++++>+++++++>++++++++>+++++++++>++++++++++>+++++++++++>++++++++++++>+++++++++++++>++++++++++++++>+++++++++++++++>++++++++++++++++<<<<<<<<<<<<<<<<-]>>>>>>>>>.<<<<<<<<<>>>>>>>>>>>>>---.+++<<<<<<<<<<<<<>>>>>>>>>>>>>>----.++++<<<<<<<<<<<<<<>>>>>>>>>>>>>>----.++++<<<<<<<<<<<<<<>>>>>>>>>>>>>>-.+<<<<<<<<<<<<<<>>>>>>----.++++<<<<<<>>>>.<<<<>>>>>>>>>>>>++.--<<<<<<<<<<<<>>>>>>>>>>>>>>++.--<<<<<<<<<<<<<<>>>>>>>>>>>>+.-<<<<<<<<<<<<>>>>>>>>>>>>>+.-<<<<<<<<<<<<<>>>>>>>>>>>>>>--.++<<<<<<<<<<<<<<>>>>>>>>>>>>>--.++<<<<<<<<<<<<<>>>>>++.--<<<<<>>>>>>>>>>>>+++.---<<<<<<<<<<<<>>>>>>>>>>>>>+++.---<<<<<<<<<<<<<>>>>.<<<<>>>>>>>>>>>>>>>----.++++<<<<<<<<<<<<<<<>>>>>>>>>>>>>>-.+<<<<<<<<<<<<<<>>>>.<<<<>>>>>>>>>>>>++.--<<<<<<<<<<<<>>>>>>>>>>>>>>++.--<<<<<<<<<<<<<<>>>>>>>>>>>>+.-<<<<<<<<<<<<>>>>>>>>>>>>>+.-<<<<<<<<<<<<<>>>>>>>>>>>>>>--.++<<<<<<<<<<<<<<>>>>>>>>>>>>>--.++<<<<<<<<<<<<<>>>>>++.--<<<<<>>>>>>>>>>>>+++.---<<<<<<<<<<<<>>>>>>>>>>>>>+++.---<<<<<<<<<<<<<>>>>>+++.---<<<<<>>>>.<<<<>>>>>>>>>>>>>>>-.+<<<<<<<<<<<<<<<>>>>>>>>>>>>>>-.+<<<<<<<<<<<<<<>>>>>>>>>>>>>>++.--<<<<<<<<<<<<<<>>>>>>>>>>>>>>----.++++<<<<<<<<<<<<<<>>>>>>>>>>>>>----.++++<<<<<<<<<<<<<>>>>+.-<<<<>>>>+.-<<<<>>>>+.-<<<<>>>>.<<<<.
    """
    )
    badinput = """
    ++++++++[>+>++>+++>++++>+++++>++++++>+++++++>++++++++>+++++++++>++++++++++>+++++++++++>++++++++++++>+++++++++++++>++++++++++++++>+++++++++++++++>++++++++++++++++<<<<<<<<<<<<<<<<-]>>>>>>>>>>>+.-<<<<<<<<<<<>>>>>>>>>>>>>>-.+<<<<<<<<<<<<<<>>>>>>>>>>>>>>>---.+++<<<<<<<<<<<<<<<>>>>.<<<<>>>>>>>>>>>>>----.++++<<<<<<<<<<<<<>>>>>>>>>>>>>+.-<<<<<<<<<<<<<>>>>>>>>>>>>>----.++++<<<<<<<<<<<<<>>>>.<<<<>>>>>>>>>>>>>>--.++<<<<<<<<<<<<<<>>>>>>>>>>>>>>-.+<<<<<<<<<<<<<<>>>>>>>>>>>>>>>----.++++<<<<<<<<<<<<<<<>>>>.<<<<>>>>>>>>>>>>>---.+++<<<<<<<<<<<<<>>>>>>>>>>>>>>--.++<<<<<<<<<<<<<<>>>>>>>>>>>>>>>----.++++<<<<<<<<<<<<<<<>>>>>>>>>>>>>---.+++<<<<<<<<<<<<<>>>>>>>>>>>>>>++.--<<<<<<<<<<<<<<>>>>.<<<<>>>>>>>>>>>>+.-<<<<<<<<<<<<>>>>.<<<<>>>>>>>>>>>>>>>--.++<<<<<<<<<<<<<<<>>>>>>>>>>>>+.-<<<<<<<<<<<<>>>>>>>>>>>>>>----.++++<<<<<<<<<<<<<<>>>>>>>>>>>>>+.-<<<<<<<<<<<<<>>>>>>>>>>>>>----.++++<<<<<<<<<<<<<>>>>.<<<<>>>>>>>>>>>>+++.---<<<<<<<<<<<<>>>>>>>>>>>>>>-.+<<<<<<<<<<<<<<>>>>>>>>>>>>>----.++++<<<<<<<<<<<<<>>>>>>>>>>>>>---.+++<<<<<<<<<<<<<>>>>>>--.++<<<<<<>>>>.<<<<.
    """

    # Main Function
    def main():
        print(_return * 5)
        i = input(
            f"{_input}Run default bf program translated to bf+: {_warn}d {_return}"
            f"{_input}Run custom bf program translated to bf+: {_warn}c {_return}"
            f"{_input}Run custom bf+ program: {_warn}p {_return}"
            f"{_input}Translate bf program to bf+: {_warn}t {_return}"
        )
        __ = (
            ___
            if i == "d"
            else (
                open(input(f"{_input}" f"Code file? \n" f">>> ")).read()
                if i == "p"
                else (
                    bf2bfp(open(input(f"{_input}" f"Code file? \n" f">>> ")).read())
                    if i == "c"
                    else(
                        print(bf2bfp(open(input(f"{_input}" f"Code file? \n" f">>> ")).read())) or quit()
                        if i=='t'
                        else bf2bfp(badinput))
                )
            )
        )
        print(_return * 5)
        Code(__).execute(scc=False, sace=False)
        print(_return * 5)

    if True:
        main()

    # try:
    #   IdIa{[-d+a]}[+d-a]dd++++++++++oaO
    # (Adds two numbers by input)
    _

    # Even More Functions
    def runbf(code):
        Code(bf2bfp(code)).execute(scc=False, sace=False)

    def runbfp(code):
        Code(code).execute(scc=False, sace=False)

    def str2bf(string):
        __ = ""
        for char in string:
            __ += "+" * ord(char)
            __ += ".[-]"
        return __

    def str2bfp(string):
        return bf2bfp(str2bf(string))


# End of File


# 427 lines!!!

# /pA+-----------,|;+++++++++++cdvdvdpBaa[d[-d+al]va-l]PBO0PA"l\

# /pA+--,|;++cdvpBdva[d[-d+a]va]PBOPA"l\

