class Person(object):
    def __init__(self, firstname, lastname, age, birthdate, gender):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.birthdate = birthdate
        self.gender = gender


class FamilyMember(Person):
    __MemberCount = 0

    def __init__(self, firstname, lastname, age, birthdate, gender, role, job):
        Person.__init__(self, firstname, lastname, age, birthdate, gender)
        self.role = role
        self.job = job
        FamilyMember.__MemberCount += 1

    def displaymembercount(self):
        print self.__MemberCount, "Family Members"


class Family(object):

    def __init__(self, familyname):
        self.familyname = familyname
        self.members = []

    def displaymembers(self):

        for person in self.members:
            print "Name:", person.firstname, person.lastname, "  age:", person.age, " Birthdate:", person.birthdate,  "  role:", person.role, " job:", person.job

    def RightToVote(self):
        count = 0
        for person in self.members:
            if person.age > 18:
                count += 1
                print person.firstname, "has the right to vote"
        print "Total ", count, " people have the right to vote"


class InvitedIndividualPartyMembers(Person):

    def __init__(self, firstname, lastname, age, birthdate, gender, attendancestatus, arrivingtime, leavingtime, thingsheshelikes):
        Person.__init__(self, firstname, lastname, age, birthdate, gender)
        self.attendancestatus = attendancestatus
        self.arrivingtime = arrivingtime
        self.leavingtime = leavingtime
        self.thingsheshelikes = thingsheshelikes


class InvitedFamilyPartyMembers(Family):

    def __init__(self, familyname, attendancestatus, arrivingtime, leavingtime, thingstheylike):
        Family.__init__(self, familyname)
        self.attendancestatus = attendancestatus
        self.arrivingtime = arrivingtime
        self.leavingtime = leavingtime
        self.thingstheylike = thingstheylike


class Birthdayparty():

    def __init__(self, celebrant, startingtime, endingtime, place):
        self.celebrant = celebrant
        self.startingtime = startingtime
        self.endingtime = endingtime
        self.place = place
        self.indvpartymembers = []
        self.familypartymembers = []

    def DisplaypartyInfo(self):

        n = 0
        print "Celebrant name:", self.celebrant.firstname, " age:", self.celebrant.age,\
            "Starting time:", self.startingtime, "Ending time", self.endingtime, "Place:", self.place
        print ""
        for family in self.familypartymembers:
            if family.attendancestatus == "yes":
                for person in family.familyname.members:
                    if person.age >= 18:
                        n += 1
        for person in self.indvpartymembers:
            if person.age >= 18:
                n += 1
        print n, "people are attending the party"
        print ""

    def Displayattendingfamilies(self):

        print "The attending guests are :"
        for family in self.familypartymembers:
            if family.attendancestatus == "yes":
                print family.familyname.familyname, ":", "  They like:", family.thingstheylike,",    arriving on:", family.arrivingtime
                print "Family members:"
                for person in family.familyname.members:
                    if person.age >= 18:
                        print "  ", person.firstname, person.lastname, person.age, "yearsold"
                    if person.age < 18:
                        print "  ", person.firstname, person.lastname, "Not allowed, age is:", person.age
                print ""
            if family.attendancestatus == "no":
                print family.familyname.familyname, "Wont be able to attend"

    def DisplayAttendingIndviduals(self):
        print""
        print "Other guests:"
        for person in self.indvpartymembers:
            if person.attendancestatus == "yes":
                if person.age >=18:
                    print person.firstname, person.lastname,"    ", person.age, "yearsold", ",   likes:", person.thingsheshelikes, ",  arriving on:", person.arrivingtime
                if person.age < 18:
                    print person.firstname, person.lastname, "Not allowed, age is:", person.age
            if person.attendancestatus == "no":
                print person.firstname, person.lastname, "wont be able to attend"






def main():
    f1m1 = FamilyMember("Anahit", "Ghazarian", 21, "1997-2-22", "Male", "son", "Student")
    f1m2 = FamilyMember("Garik", "Ghazarian", 50, "1964-3-18", "Male", "father", "Company Owner")
    f1m3 = FamilyMember("Anna", "Ghazarian", 17, "2000-3-18", "Female", "daughter", "student")
    f1m4 = FamilyMember("Mary", "Gurghikian", 48, "1970-3-18", "Female", "mother", "housewife")
    f1 = Family("GhazarianFamily")
    f1.members.append(f1m1)
    f1.members.append(f1m2)
    f1.members.append(f1m3)
    f1.members.append(f1m4)

    f2m1 = FamilyMember("Sam", "Rhods", 32, "1976-2-18", "Male", "father", "Company Owner")
    f2m2 = FamilyMember("Mary", "jane", 25, "1996-3-23", "Female", "mother", "housewife")
    f2m3 = FamilyMember("Suzan", "Rhods", 10, "2008-5-23", "Female", "daughter", "student")
    f2 = Family("RhodsFamily")
    f2.members.append(f2m1)
    f2.members.append(f2m2)
    f2.members.append(f2m3)

    f3m1 = FamilyMember("Serj", "Sarkisian", 32, "1976-2-18", "Male", "father", "Manager")
    f3m2 = FamilyMember("Mary", "Sarkisian", 25, "1996-3-23", "Female", "mother", "housewife")
    f3 = Family("Sarkisian Family")
    f3.members.append(f3m1)
    f3.members.append(f3m2)


    pm1 = InvitedIndividualPartyMembers("Spiderman", "Spidermanyan", 21, "2012-12-22", "Male", "yes", "18:30", "23:30", "dancing and smoking")
    pm2 = InvitedIndividualPartyMembers("Superman", "Supermanyan", 121, "1898-12-22", "Male", "no", "", "", "sleeping and eating")
    pm3 = InvitedIndividualPartyMembers("Batman", "Batmanyan", 17, "2001-9-5", "Female", "yes", "18:30", "23:30", "dancing, smoking, drinking")

    pf1 = InvitedFamilyPartyMembers(f1, "yes", "17:45", "20:00", "Drinking and Celebrating")
    pf2 = InvitedFamilyPartyMembers(f2, "yes", "18:25", "19:40", "Talking and Eating")
    pf3 = InvitedFamilyPartyMembers(f3, "no", "18:25", "19:40", "Smoking")

    Party = Birthdayparty(f1m1, "19:00", "1:00", "La Plaza")

    Party.indvpartymembers.append(pm1)
    Party.indvpartymembers.append(pm2)
    Party.indvpartymembers.append(pm3)
    Party.familypartymembers.append(pf1)
    Party.familypartymembers.append(pf2)
    Party.familypartymembers.append(pf3)


    Party.DisplaypartyInfo()
    Party.Displayattendingfamilies()
    Party.DisplayAttendingIndviduals ()

    #f1m1.displaymembercount()
    #f1.displaymembers()
    #f1.RightToVote()

main()
