#!/usr/bin/python
import pgdb

class Books:

	def __len__(self):
		return len(self._books)

	def __getitem__(self, key):
		return self._books[key]

	def __setitem__(self, key, value):
		self._books[key] = value

	def __delitem__(self, key):
		del self._books[key]['book_id']
		del self._books[key]

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
		
		self._books = {}
		Book.cur = self.conn.cursor()
		self.cur.execute("SELECT book_id FROM books")
		for x in self.cur.fetchall():
			book_id = x[0]
			self._books[book_id] = Book(self.cur, book_id)

	def find(self, title):
		self.cur.execute("SELECT tile, stock FROM books NATURAL JOIN editions NATURAL JOIN stock WHERE title='" + pgdb.escape_string(title) + "';")

	def update_stock(self, title, stock):
		self.cur.execute("UPDATE stock SET stock='" + pgdb.escape_string(stock) + "' WHERE title='" + pgdb.escape_string(title) + "';")

	def get_all(self):
		d = {'title':[], 'stock':[]}
		self.cur.execute("SELECT title, stock FROM books NATURAL JOIN editions NATURAL JOIN stock;")
		for x in self.cur.fetchall():
			d['title'].append(x[0])
			d['stock'].append(x[1])
		return d

class Book:
	_data = None
	cur = None
	id = None
	
	def __init__(self, cur, book_id):
		self.id = str(book_id)
		self._data = {'book_id': book_id, 'title': None, 'author_id': None, 'subject_id': None}
	
	def __getattr__(self, name):
		if(self._data == None):
			return None
		if(self._data[name] == None):
			self.cur.execute("SELECT " + str(name) + " FROM books WHERE book_id=" + self.id)
			tmp = self.cur.fetchone()
			self._data[name] = tmp[0] if tmp != None else None
		return self._data[name]

	def __setattr__(self, name, value):
		self.cur.execute("UPDATE books SET " + str(name) + "=" + str(value) + " WHERE book_id=" + self.id)

	def __delattr__(self, name):
		if(name == 'book_id'):
			self.cur.execute("DELETE FROM books WHERE book_id=" + self.id)
		else:
			self[name] = None




