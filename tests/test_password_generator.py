from src import password_generator


def test_password_generator():
    password = password_generator.PasswordGenerator().generate(10)
    assert password_generator.PasswordGenerator().validate(password)
