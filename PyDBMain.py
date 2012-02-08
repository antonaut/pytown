#!/usr/bin/python

import pgdb
import pg
from DBContext import DBContext
from gui import PyDBWin

class PyDBMain(DBContext, object):
    """ Hej"""

    def __init__(self,debug=False):
        super(PyDBMain,self).__init__()
        self.debug=debug
    
        
    def run(self):        
        super(PyDBMain,self).run()
        #self.window = PyDBWin()
        #self.window.main()

    def safe_input(self,str):
        return pgdb.escape_string(raw_input(str))
        
    def safe_query(self, format_str, *args):
        try:
            query = format_str.format(*args)
            self.cur.execute(query)
        except pg.DatabaseError as e:
            if self.debug:
                print e
            print "An error occurred. Please try again."
            self.conn.rollback()
        else:
            self.conn.commit()


    def input_columns(self,str):
        """list comprehension building a list ready to be reduced into a string."""        
        columns = [x.strip() + str for x in self.safe_input("Choose column(s): ").split(",")]
        columns[len(columns)-1] = columns[len(columns)-1][0:len(columns[len(columns)-1])-len(str)]
        return reduce(lambda a,b:a+b,columns)


    def input_values(self):
        def parse(str):
            if str.isdigit():
                return str.strip() + ", "
            return "'" + str.strip() + "', "
            
        values = [parse(x) for x in self.safe_input("Choose value(s): ").split(",")]
        values[len(values)-1] = values[len(values)-1][0:len(values[len(values)-1])-2]
        return reduce(lambda a,b:a+b,values)


    def select(self):
        try:
            super(PyDBMain,self).select()
        except pg.DatabaseError as e:
            if self.debug:
                print e
            print "An error occurred. Please try again."
            self.conn.rollback()
        else:
            self.conn.commit()

            
    def remove(self):
        """Removes tuples.
        Will query the user for the information required to identify a tuple.
        If the filter field is left blank, no filters will be used."""
        table = self.safe_input("Choose table: ")
        filters = raw_input("Apply filters: ")

        self.safe_query("DELETE FROM {0}{1};", table, "" if filters == "" else " WHERE {0}".format(filters))

      
    def insert(self):
        """inserts tuples.
        Will query the user for the information required to create tuples."""
        table = self.safe_input("Choose table: ")
        columns = self.input_columns(", ")
        values = self.input_values()

        self.safe_query("INSERT INTO {0}({1}) VALUES({2});",table, columns, values)


    def update(self):
        """updates tuples.
        Will query the user for the information required to identify and update tuples.
        If the filter field is left blank, no filters will be used."""
        table = self.safe_input("Choose table: ")
        values = raw_input("Choose value(s): ")
        filters = raw_input("Apply filters: ")

        self.safe_query("UPDATE {0} SET {1}{2};",table, values, "" if filters == "" else " WHERE {0}".format(filters))
                  
        

if __name__== "__main__":
    pydb = PyDBMain(debug=True)
    pydb.run()
