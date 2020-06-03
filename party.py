import numpy
import db


class Party:
    def __init__(self, kod, name, char):
        self.kod = kod
        self.name = name
        self.char = char
        self.countVoters = 0

    def __init__(self, ):
        pass

    def get_max_Party(self):
        count = db.cursor.execute(
            "select [nameParty],[charParty] from [dbo].[Party] where[countVoters] = (select   max([countVoters]) from [dbo].[Party])"
        ).fetchone()

        print("המפלגה עם מספר הקולות הגבוה ביותר הינה {} - {}".format(count[1], count[0]))
        # numpy.array()


if __name__ == '__main__':
    p = Party()
    p.get_max_Party()
