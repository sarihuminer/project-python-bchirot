import db
import numpy


class Party:
    def __init__(self, kod, name, char):
        self.kod = kod
        self.name = name
        self.char = char
        self.countVoters = 0

    #def __init__(self, ):
     #   pass

    def get_max_Party(self):
        count = db.cursor.execute(
            "select [nameParty],[charParty] from [dbo].[Party] where[countVoters] = (select   max([countVoters]) from [dbo].[Party])"
        ).fetchone()

        print("המפלגה עם מספר הקולות הגבוה ביותר הינה {} - {}".format(count[1], count[0]))
        # numpy.array()

    def get_all_Over_Parties(self):
        # 3.2% מכל הקולות
        db.cursor.execute('select [nameParty],[charParty], countVoters from [dbo].[Party]')
        results = db.cursor.fetchall()
        countVoters = [i[2] for i in results]
        Parties = [{i[0], i[1]} for i in results]
        arrayCountVoters = numpy.fromiter(countVoters, dtype=numpy.int32)
        # מציאת המקסימום של הקולות לאיזו מפלגה
        print(arrayCountVoters.max())
        indexOfMax = numpy.where(arrayCountVoters == numpy.amax(arrayCountVoters))
        # print('Returned tuple of arrays :', indexOfMax)
        print('List of Indices of maximum element :', end='\n')
        for p in indexOfMax[0]:
            print("אות מפלגה : {} שם מפלגה : {}".format(Parties[p][0], Parties[p][1]))


if __name__ == '__main__':
    p = Party()
    p.get_max_Party()
    p.get_all_Over_Parties()
