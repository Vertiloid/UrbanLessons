def test_function():
    def inner_function():
        print("Я в области видимости функции test_function")

    inner_function()


test_function()
# inner_function()
# При вызове inner_function() происходит ошибка:
# NameError: name 'inner_function' is not defined.