from translate import Translator
translator = Translator(to_lang="es")
try:
    with open("text.txt", "r") as file:
        text = file.read()
        translation = translator.translate(text)
        print(translation)
except FileNotFoundError as err:
    print("File is not existing")
    raise err