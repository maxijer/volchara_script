from main import run

while True:
    text = input('volchara > ')
    result, error = run("<stdin>", text)
    if error:
        print(error.as_string())
    else:
        print(result)
