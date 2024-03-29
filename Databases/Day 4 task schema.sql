CREATE DATABASE Day4Task;
USE Day4Task;

CREATE TABLE Article (ID INT PRIMARY KEY AUTO_INCREMENT, Title VARCHAR(15) NOT NULL, Text VARCHAR(15) NOT NULL,
PublishStatus ENUM('yes', 'no')DEFAULT NULL, Topic VARCHAR(30) DEFAULT NULL, Author VARCHAR(25) DEFAULT NULL, 
PublicationDate DATE DEFAULT NULL);

CREATE TABLE Topic (Name VARCHAR(30) PRIMARY KEY, Description VARCHAR(30) DEFAULT NULL);

CREATE TABLE Author (Username VARCHAR(25) PRIMARY KEY, DisplayName TEXT);

CREATE TABLE Course (ShortName VARCHAR(20) PRIMARY KEY, FullName TEXT);

CREATE TABLE Relevant_For (ArticleID INT, Course VARCHAR(20), PRIMARY KEY(ArticleID, Course));


ALTER TABLE Article ADD FOREIGN KEY (Topic) REFERENCES Topic (Name);
ALTER TABLE Article ADD FOREIGN KEY (Author) REFERENCES Author (Username);
ALTER TABLE Relevant_For ADD FOREIGN KEY (ArticleID) REFERENCES Article (ID);
ALTER TABLE Relevant_For ADD FOREIGN KEY (Course) REFERENCES Course (ShortName);



ALTER TABLE Topic ADD FOREIGN KEY (Name) REFERENCES Article (Topic);
ALTER TABLE Author ADD FOREIGN KEY (Username) REFERENCES Article (Author);
ALTER TABLE Course ADD FOREIGN KEY (Name) REFERENCES Article (Topic);

