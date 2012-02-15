#!/usr/bin/python
import pgdb
import sys


class DBContext:
    """DBContext is a small interface to a database that simplifies SQL.
    Each function gathers the minimal amount of information required and executes the query."""

    def __init__(self): #PG-connection setup
        try:
            f = open("/afs/nada.kth.se/home/z/u1btp95z/Private/.psqlpw-nestor2.csc.kth.se",'r')
            self.password = f.readlines()[0].strip(' \n')
            f.close()

        except ValueError:
            sys.exit(1)


        params = {'host':'nestor2.csc.kth.se', 'user':'aerholt', 'database':'aerholt', 'password':self.password}
        self.conn = pgdb.connect(**params)
        self.menu = ["Select.", "Insert.", "Remove.", "Update.", "Exit"]
        self.cur = self.conn.cursor()

    def print_menu(self):
        """Prints a menu of all functions this program offers.  Returns the numerical correspondant of the choice made."""
        for i,x in enumerate(self.menu):
            print("%i. %s"%(i+1,x))
        return self.get_int()

    def get_int(self):
        """Retrieves an integer from the user.
        If the user fails to submit an integer, it will reprompt until an integer is submitted."""
        while True:
            try:
                choice = int(input("Choose: "))
                if 1 <= choice <= len(self.menu):
                    return choice
                print("Invalid choice.")
            except ValueError:
                print("That was not a number, genious.... :(")

    def select(self):
        """Finds and prints tuples.
        Will query the user for the information required to identify a tuple.
        If the filter field is left blank, no filter will be used."""
        table = raw_input("Choose table: ")
        #list comprehension building a list ready to be reduced into a string.
        columns = [x.strip() + " natural join " for x in raw_input("Choose column(s): ").split(",")]
        columns[len(columns)-1] = columns[len(columns)-1][0:len(columns[len(columns)-1])-14]
        filters = raw_input("Apply filters: ")
        query = """SELECT %s FROM %s%s;"""%(reduce(lambda a,b:a+b,columns), table, "" if filters == "" else " WHERE %s"%filters)
        self.cur.execute(query)
        self.print_answer()

    def remove(self):
        """Removes tuples.
        Will query the user for the information required to identify a tuple.
        If the filter field is left blank, no filters will be used."""
        pass

    def insert(self):
        """inserts tuples.
        Will query the user for the information required to create tuples."""
        pass
    
    def update(self):
        """updates tuples.
        Will query the user for the information required to identify and update tuples.
        If the filter field is left blank, no filters will be used."""
        pass
    
    def print_answer(self):
            print("\n".join([", ".join([str(a) for a in x]) for x in self.cur.fetchall()]))

    def run(self):
        """Main loop.
        Will divert control through the DBContext as dictated by the user."""
        actions = [self.select, self.insert, self.remove, self.update]
        while True:
            try:
                actions[self.print_menu()-1]()
                print
            except IndexError:
                self.cur.close()
                self.conn.close()
                exit()

if __name__ == "__main__":
    db = DBContext()
    db.run()
