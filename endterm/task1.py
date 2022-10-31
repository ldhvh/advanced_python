import psycopg2

conn = psycopg2.connect(
   database="postgres", user='postgres', password='7554anH8447kqV', host='127.0.0.1', port= '5432'
)
conn.autocommit = True

cursor = conn.cursor()

sql = ("""
        CREATE TABLE onlineshop.Products (     ProductID int,     Price int,     UnitsNum int,     Name varchar(255),     Descr varchar(255) )

        """,
        """ CREATE TABLE onlineshop.Blog (     BlogID int,     Title varchar(255),     IntroTxt varchar(255),     Txt varchar(255),     AuthorName varchar(255),     PublDate DATE )

        """,
        """
        CREATE TABLE onlineshop.Blog (     BlogID int,     Title varchar(255),     IntroTxt varchar(255),     Txt varchar(255),     AuthorName varchar(255),     PublDate DATE )

        """,
        """
        INSERT into onlineshop.blog(BlogID,Title,IntroTxt,Txt,AuthorName,PublDate) values ('1','title','intro','txt','leila','2003-10-31'),('2','title2','intro2','txt','leil','2005-10-31'),('3','title3','intro3','txt','lei','2006-10-31'),('4','title4','intro4','txt','le','2004-10-31'),('5','title5','intro5','txt','l','2009-10-31'),('6','title6','intro6','txt','ll','2008-10-31')

        """);

cursor.execute(sql)
print("Done........")

conn.close()