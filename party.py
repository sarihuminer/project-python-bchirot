import db
import numpy


class Party:
    def __init__(self, kod=0, name=0, char=0):
        self.kod = kod
        self.name = name
        self.char = char
        self.countVoters = 0

    # def __init__(self, ):
    #   pass

    def get_max_Party(self):
        count = db.cursor.execute(
            "select [nameParty],[charParty],countVoters from [dbo].[Party] where[countVoters] = (select   max([countVoters]) from [dbo].[Party])"
        ).fetchone()

        print("המפלגה עם מספר הקולות הגבוה ביותר הינה {} - {}".format(count[1], count[0]))
        # numpy.array()
        return count[2]

    def get_all_Over_Parties(self):
        # 3.25% מכל הקולות

        db.cursor.execute('''
        select [nameParty],[charParty], countVoters 
        from [dbo].[Party]
        where CAST(countVoters AS float)/(select sum([countVoters])from [dbo].[Party])*100>=2.25''')
        results = db.cursor.fetchall()

        db.cursor.execute('select sum([countVoters]) from [dbo].[Party]')
        countVoters = [i[2] for i in results]
        Parties = [[i[0], i[1]] for i in results]
        arrayCountVoters = numpy.fromiter(countVoters, dtype=numpy.int32)
        # מציאת המקסימום של הקולות לאיזו מפלגה
        print(arrayCountVoters.max())
        indexOfMax = numpy.where(arrayCountVoters == numpy.amax(arrayCountVoters))
        # print('Returned tuple of arrays :', indexOfMax)
        print('List of Indices of maximum element :', end='\n')
        for p in indexOfMax[0]:
            print("שם מפלגה: {}  אות מפלגה: {}".format(Parties[p][0], Parties[p][1]))
        print(numpy.size(arrayCountVoters))
        return numpy.size(arrayCountVoters)

if __name__ == '__main__':
    p = Party()
    p.get_max_Party()
    p.get_all_Over_Parties()
