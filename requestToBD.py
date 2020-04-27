#! /usr/bin/env python
# -*- coding: utf-8 -*-
import sqlite3
conn = sqlite3.connect("db.sqlite3")
cursor = conn.cursor()


"""
    cursor.execute("""
"""CREATE TABLE albums
                  (title text, artist text, release_date text,
                   publisher text, media_type text)
               """
""")



for row in cursor.execute("SELECT rowid, * FROM albums ORDER BY artist"):
    print(row)

"""

"""INSERT INTO albums
                  VALUES ('Glow', 'Andy Hunter', '7/24/2012',
                  'Xplore Records', 'MP3')
                  ,

    ('',
     'task01',
     ''),

('',
     'task01',
     ''),

('',
     'task01',
     ''),

('',
     'task01',
     ''),

('',
     'task01',
     ''),
    
('',
     '',
     '')
                  
                  
                  select * from sqlite_master
where type = 'table'
                  
                  """



#Данные для заполнения базы данных
albums = [
    ('ТУФЛИ ELLEN',1,6200,
     'Очаровательные красные туфли Ellen сделаны из натуральной лаковой кожи и декорированы элегантным минималистичным '
     'бантом. Эти туфли станут идеальным завершением праздничного образа. Носить можно с платьями и юбками.',
     1,'2019-01-08 17:49:08.700715','2019-09-27 12:30:33.119037',),

('Сапожки из овчины EMU Australia',1,3300,
     'Новинка этого сезона модель Fox - это сапожки из овчины с аппликацией, изображающей мордочку лисы. Ребенок будет рад весело'
     'му преображению с помощью удобной обуви! Мягкие и теплые внутри сапожки устойчивы к неблагоприятным погодным условиям и вод'
     'онепроницаемы снаружи. Они отлично подойдут для прогулок и игр на улице и в сырую, и в морозную погоду.',
     1,'2019-01-08 17:49:08.700715','2019-09-27 12:30:33.119037'),
('БОТИНКИ JANE',1,3900,
     'Идеальный выбор для маленькой модницы - это элегантные и утонченные ботиночки Jane. Они изготовлены из модного твида голубого'
     ' цвета с носиком из мягкой натуральной кожи и декорированы изящной лентой в цвет обуви. Мы рекомендуем носить их как с джинсами, так и c элегантным платьем.',
     1,'2019-01-08 17:49:08.700715','2019-09-27 12:30:33.119037' ),
('БОТИНКИ JANE',1,1400,
     'Детские кроссовки Retro V от Fila отлично завершат образ в спортивном стиле и гарантируют комфорт во время прогулок.',
     1,'2019-01-08 17:49:08.700715','2019-09-27 12:30:33.119037'),


]




#Очистка таблицы
#cursor.execute("DELETE FROM products_product")
#conn.commit()

#Внос данных и сохранения
#cursor.executemany("INSERT INTO products_product VALUES (NULL,?,?,?,?,?,?,?)", albums)
#conn.commit()

#Проверка
for row in cursor.execute("select * from products_product"):
    print(row)


albums2 = [
    (8,'products_images/1.jpg',True,True,8,8,),

(9,'products_images/2.jpg',True,True,9,9,),
(10,'products_images/3.jpg',True,True,10,10,),
(11,'products_images/4.jpg',True,True,11,11,),


]

#Очистка таблицы
#cursor.execute("DELETE FROM products_productimage")
#conn.commit()

#Внос данных и сохранения
#cursor.executemany("INSERT INTO products_productimage VALUES (NULL,?,?,?,?,?,?)", albums2)
#conn.commit()

#Проверка
for row in cursor.execute("select * from products_productimage"):
    print(row)
