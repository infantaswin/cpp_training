#!/usr/bin/env python3

import mysql.connector
from mysql.connector import errorcode

cnx =mysql.connector.connect(host='localhost', user='apin_admin', passwd='AceDemicProgress@2017', db='apin')
cursor = cnx.cursor()

DB_NAME = 'apin'

TABLES = {}

"""# Primary storage table for articles"""
TABLES['Article'] = (
	" CREATE TABLE `Article` ("
	"  `ArtID` INT (9) NOT NULL AUTO_INCREMENT,"
	"  `PubmedID` INT (8) NOT NULL UNIQUE,"
	"  `Year` YEAR NOT NULL,"
	"  `JournalName` VARCHAR (120) NOT NULL,"
	"  `ArticleTitle` VARCHAR (225) NOT NULL,"
	"  `ArticleAbstract` VARCHAR (1500) NOT NULL,"
	"  `AuthorShort` VARCHAR (120)	NOT NULL,"
	"  `OpenAccess` ENUM('True', 'False'),"
	"  `DocumentLink`  VARCHAR (225),"
	"  `Issue` INT (4),"	
	"  `Volume` INT (4),"
	"  `PageNo` INT (4),"
	"   PRIMARY KEY (`ArtID`), UNIQUE KEY (`PubmedID`)"
	")  ENGINE=InnoDB")

"""# First degree connection of primary articles"""
TABLES['Citation'] = (
	" CREATE TABLE `Citation` ("
	"  `CiteID` INT (12) NOT NULL AUTO_INCREMENT,"
	"  `PubmedID` INT (8) NOT NULL,"
	"  `CitedBy`  VARCHAR (1000),"
	"  `CitingInThis` VARCHAR (250),"
	"   PRIMARY KEY (`CiteID`)"
	")  ENGINE=InnoDB")

"""# Secondary storage table for related articles"""
TABLES['RelatedArticles'] = (
	" CREATE TABLE `RelatedArticles` ("
	"  `RelatedID` INT (12) NOT NULL AUTO_INCREMENT,"
	"  `PubmedID` INT (8) NOT NULL UNIQUE,"
	"  `Year` YEAR NOT NULL,"
	"  `JournalName` VARCHAR (120),"
	"  `ArticleTitle` VARCHAR (225),"
	"  `ArticleAbstract` VARCHAR (1500),"
	"  `AuthorShort` VARCHAR (120),"
	"  `Issue` INT (20),"
	"  `Volume` INT (8),"
	"  `PageNo` INT (8),"
	"   PRIMARY KEY (`RelatedID`)"
	")  ENGINE=InnoDB")

"""# Primary storage table for authors"""
TABLES['Author'] = (
	" CREATE TABLE `Author` ("
	"  `ScholarID` INT (8) NOT NULL AUTO_INCREMENT,"
	"  `PubmedIDS` VARCHAR (1000),"
	"  `user_id` VARCHAR(16),"
	"  `FirstName` VARCHAR (40) NOT NULL,"
	"  `MidleNames` VARCHAR (120),"
	"  `LastName` VARCHAR (10) NOT NULL,"
	"  `AuthorImgLink` VARCHAR (225),"
	"  `EmailID`  VARCHAR (65),"
	"  `LinkedIN` VARCHAR (225),"
	"  `GoogleScholar` VARCHAR (225),"
	"  `ORCID` VARCHAR (10),"
	"  `GroupID` VARCHAR (11) NOT NULL,"
	"   PRIMARY KEY (`ScholarID`), UNIQUE KEY `ScholarID` (`ScholarID`)"
    ")  ENGINE=InnoDB")

"""# Primary Group table and Additional information for authors"""
TABLES['RGroup'] = (
	" CREATE TABLE `RGroup` ("
	"  `GroupID` INT (8) NOT NULL AUTO_INCREMENT,"
	"  `GroupName` VARCHAR (120),"
	"  `GroupShortName` VARCHAR (12),"
	"  `InstituteID` VARCHAR (12) NOT NULL,"
	"  `InstituteName` VARCHAR (80),"
	"   PRIMARY KEY (`GroupID`), UNIQUE KEY (`GroupID`)"
    ")  ENGINE=InnoDB")

"""#Primary Institute table and additional information for Groups and authors"""
TABLES['Institute'] = (
    	" CREATE TABLE `Institute` ("
	"  `InstituteID` INT (12) NOT NULL AUTO_INCREMENT,"
	"  `InstituteName` VARCHAR (80),"
	"  `InstituteAcronym` VARCHAR (10),"
	"  `InstituteAddress` VARCHAR (80),"
	"  `InstituteCity` VARCHAR (40),"
	"  `InstituteState` VARCHAR (40),"
	"  `InstituteCountry` VARCHAR (24),"
	"   PRIMARY KEY (`InstituteID`), UNIQUE KEY (`InstituteID`)"
    ")  ENGINE=InnoDB")


TABLES['users'] = (
	" CREATE TABLE `users` ("
	"  `user_id` VARCHAR(16) NOT NULL,"
	"  `user_email` VARCHAR(90) NOT NULL,"
	"  `password`	VARCHAR(20) NOT NULL,"
	"  `ScholarID` INT (8),"
	"   PRIMARY KEY (`user_id`), UNIQUE KEY (`user_id`)"
	")  ENGINE=InnoDB")


def create_database(cursor):
	'''
	parse databse list for a given article 
	'''
	try:
		cursor.execute(
            "CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format(DB_NAME))
	except mysql.connector.Error as err:
		print("Failed creating database: {}".format(err))
		exit(1)

try:
    cnx.database = DB_NAME
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_BAD_DB_ERROR:
        create_database(cursor)
        cnx.database = DB_NAME
    else:
        print(err)
        exit(1)

for name, ddl in TABLES.items():
    try:
        print("Creating table {}: ".format(name), end='')
        cursor.execute(ddl)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
            print("already exists.")
        else:
            print(err.msg)
    else:
        print("OK")

cursor.close()
cnx.close()
# TODO Not install mysql

