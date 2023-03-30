autors = "autors.txt"
domains = "domains.txt"
names = "names.txt"
class Filejoyer:

    def __init__(self):
        self.autors = autors
        self.domains = domains
        self.names = names

    def domaination(self):
        with open(self.domains, 'r') as my_file:
            data = my_file.readlines()
            my_list = []
            for i in list(data):
                x = i.replace(".", "").replace("\n", "")
                my_list.append(x)

        return my_list

    def surnamation(self):
        with open(self.names, "r") as my_file:
            data = my_file.readlines()
            sur = []
            for i in list(data):
                x = i.split("\t")
                sur.append(x[1])

        return sur

    def dateination(self):
        with open(self.autors, "r") as my_file:
            data = my_file.readlines()
            my_list = []
            for i in list(data):
                x = i.split(" - ")
                if "\n" not in x[0]:
                    y = {"date": x[0]}
                    my_list.append(y)

        return my_list



joy = Filejoyer()

print(joy.surnamation())
