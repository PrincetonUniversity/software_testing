"""software_testing/02_unittest/examples/sizes.py"""
class Big:

    def __init__(self, mysize):
        self.mysize = mysize

    def check(self):
        return self.mysize > 75


class Medium:

    def __init__(self, mysize):
        self.mysize = mysize

    def check(self):
        return 25 < self.mysize <= 75


class Small:

    def __init__(self, mysize):
        self.mysize = mysize

    def check(self):
        return self.mysize <= 25
