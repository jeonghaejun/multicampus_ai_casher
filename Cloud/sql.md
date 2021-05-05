

```sql
create DATABASE multicampus;
```



### item_info

```mysql
CREATE TABLE Item_info(
	Item_id VARCHAR(20) PRIMARY KEY,
	Name VARCHAR(50) NOT NULL,
	Price INT(20) NOT NULL,
	Qty INT(20) NOT NULL,
	Category VARCHAR(30) NOT NULL 
)charset = utf8;

```



### item_image

```mysql
CREATE TABLE Item_image(
	Image_ID INT(10) auto_increment NOT NULL PRIMARY KEY,
	Item_ID VARCHAR(20),
	URL VARCHAR(100),
	FOREIGN KEY(Item_ID) REFERENCES Item_info(Item_ID) 
)charset = utf8;

```





### sales_history

```mysql
CREATE TABLE Sales_history(
	Sales_ID INT(20) AUTO_INCREMENT NOT NULL primary key,
	Credit_ID VARCHAR(50) NOT NULL,
	DATE TIMESTAMP DEFAULT NOW(),
	History LONGTEXT
	)charset = utf8;
```



### error_detection

```mysql
CREATE TABLE Error_detection(
	Error_ID INT(20) AUTO_INCREMENT NOT NULL PRIMARY KEY ,
	Wrong_item_ID varchar(20) NOT NULL,
	Selected_ID VARCHAR(20),
	ErrorIMG_ID INT(15) NOT NULL,
	FOREIGN KEY(Wrong_item_ID) REFERENCES Item_info(Item_ID),
	FOREIGN KEY(Selected_ID) REFERENCES Item_info(Item_ID),
	FOREIGN KEY(ErrorIMG_ID) REFERENCES Item_image(Image_ID)	
)charset = utf8;
```

