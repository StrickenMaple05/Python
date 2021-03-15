class RomanNumerals:

    to_roman_dict = {
        1: "I",
        5: "V",
        10: "X",
        50: "L",
        100: "C",
        500: "D",
        1000: "M",
        5000: "",
        10000: "",
    }

    from_roman_dict = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }

    @staticmethod
    def translate_to_roman(digit, capacity):
        dict_get = RomanNumerals.to_roman_dict.get
        one = dict_get(10 ** capacity)
        digit = int(digit)
        return {
            0 <= digit <= 3: one * digit,
            4 <= digit <= 8: one * max(0, 5 - digit) +
                             dict_get(5 * 10 ** capacity) +
                             one * max(0, digit - 5),
            digit == 9: one + dict_get(10 ** (capacity + 1))
        }[True]

    @staticmethod
    def translate_from_roman(digit):
        return RomanNumerals.from_roman_dict.get(digit)

    @staticmethod
    def to_roman(number):
        translate = RomanNumerals.translate_to_roman
        if number >= 4000:
            return ""
        answer = ""
        digits = list(str(number))
        length = len(digits)
        for i in reversed(range(length)):
            answer = translate(digits[i], length - i - 1) + answer
        return answer

    @staticmethod
    def from_roman(number):
        translate = RomanNumerals.translate_from_roman
        if len(number) == 0:
            return 0
        answer = 0
        current_ = translate(number[0])
        for i in range(1, len(number)):
            next_ = translate(number[i])
            answer += current_ if current_ >= next_ else -current_
            current_ = next_
        answer += translate(number[len(number) - 1])
        return answer


print(RomanNumerals.to_roman(2999))
print(RomanNumerals.from_roman("MMCMXCIX"))
