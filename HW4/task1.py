from sys import argv

name_script, production, rate_hour, bounty = argv


def salary(production=production, rate_hour=rate_hour, bounty=bounty):
    print(
        (int(production) * int(rate_hour)) + int(bounty)
    )


salary()
