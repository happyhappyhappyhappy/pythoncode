from main.say import Foo, Hoge


def test_foo_say():
    assert Foo().say() == 'foo'


def test_foo_say2():
    assert Foo().say2() == 'foo'


def test_hoge_say1():
    assert Hoge().say() == 'hoge'


def test_hoge_say2():
    assert Hoge().say() == 'hoge2'
