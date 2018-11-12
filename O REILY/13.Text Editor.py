import copy


class Text:
    def __init__(self):
        self.text = ''
        self.font = ''

    def set_font(self, font):
        self.font = font

    def write(self, text):
        self.text += text

    def restore(self, text):
        self.text = text.text
        self.font = text.font

    def show(self):
        if (self.font != ''):
            font = '[' + self.font + ']'
        else:
            font = ''
        return '{}{}{}'.format(font, self.text, font)


class SavedText:
    def __init__(self):
        self.texts = {}
        self.last_version = 0

    def save_text(self, text):
        self.texts[self.last_version] = copy.copy(text)
        self.last_version += 1

    def get_version(self, version):
        return self.texts[version]


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing

    text = Text()
    saver = SavedText()

    text.write("At the very beginning ")
    saver.save_text(text)
    text.set_font("Arial")
    saver.save_text(text)
    text.write("there was nothing.")

    assert text.show() == "[Arial]At the very beginning there was nothing.[Arial]"

    text.restore(saver.get_version(0))
    assert text.show() == "At the very beginning "

    print("Coding complete? Let's try tests!")