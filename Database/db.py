import mariadb
import connection

conn = connection.db_connection()

cursor = conn.cursor()

sql_delete_list = """DROP TABLE IF EXISTS beerlist;"""
sql_delete_beer = """DROP TABLE IF EXISTS beer;"""
sql_delete_user = """DROP TABLE IF EXISTS user;"""

sql_query = """CREATE table `beer`(
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    percentageAlcohol VARCHAR(5) NOT NULL,
    category VARCHAR(100) NOT NULL,
    stock INT NOT NULL,
    image VARCHAR(300) NOT NULL);"""

sql_querybis = """CREATE table `user`(
    id INT PRIMARY KEY AUTO_INCREMENT,
    pseudo VARCHAR(100) NOT NULL,
    mail VARCHAR(300) NOT NULL,
    password VARCHAR(100) NOT NULL);"""

sql_querybis_bis = """CREATE table `beerlist`(
id INT PRIMARY KEY AUTO_INCREMENT,
user_id INT NOT NULL,
beer_id INT NOT NULL,
quantite INT NOT NULL,
FOREIGN KEY (user_id) REFERENCES user(id),
FOREIGN KEY (beer_id) REFERENCES beer(id));"""

sql_beer = """INSERT INTO beer(name,percentageAlcohol,category, stock, image) VALUES 
('Heineken','3.2','Blonde', 10,'https://stmau.com/commande/wp-content/uploads/2020/11/biere-heineken.jpg'), 
('1664','5.5','Blonde', 15,'https://www.beertime.fr/media/6592/sans-titre-3.jpg'),
('Leffe Ruby','4.1','Fruit', 30,'https://leffe.com/img/beers/packshot_leffe_ruby.png'),
('Chouffe','9.2','Blonde', 5,'https://vandb-vandb-fr-storage.omn.proximis.com/Imagestorage/imagesSynchro/0/0/c37951080e47237284ca7e72fc2f85b2a9ccf5ee_4585BBO032022_1.png');"""

sql_user = """INSERT INTO user(pseudo,mail,password) VALUES('test','test@test.com','test');"""

cursor.execute(sql_delete_list)
cursor.execute(sql_delete_beer)
cursor.execute(sql_delete_user)
cursor.execute(sql_query)
cursor.execute(sql_querybis)
cursor.execute(sql_querybis_bis)
cursor.execute(sql_beer)
cursor.execute(sql_user)
conn.commit()
conn.close()