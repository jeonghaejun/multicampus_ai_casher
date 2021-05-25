

```sql
create DATABASE multicampus;
```



### item_info

```mysql
CREATE TABLE Item_info(
	Item_id INT(10) auto_increment PRIMARY KEY NOT NULL,
	Product_name VARCHAR(50) NOT NULL,
	Price INT(20) NOT NULL,
	Qty INT(20) NOT NULL,
	Category VARCHAR(30) NOT NULL 
)charset = utf8;

ALTER TABLE Item_info AUTO_INCREMENT=10000;
```



### item_image

```mysql
CREATE TABLE Item_image(
	Image_id INT(10) auto_increment NOT NULL PRIMARY KEY,
	Item_id JSON,
	Img_url VARCHAR(100),
	FOREIGN KEY(Item_id) REFERENCES Item_info(Item_id) 
)charset = utf8;

```





### sales_history

```mysql
CREATE TABLE Sales_history(
	Sales_id INT(20) AUTO_INCREMENT NOT NULL primary key,
	User_phonenum VARCHAR(50) NOT NULL,
	DATE TIMESTAMP DEFAULT NOW(),
	History JSON
	)charset = utf8;
```



### error_detection

```mysql
CREATE TABLE Error_detection(
	Error_id INT(20) AUTO_INCREMENT NOT NULL PRIMARY KEY ,
	Errorimg_id INT(15) NOT NULL,
    Outcome TINYINT(1) NOT NULL,
    Result_info JSON NOT NULL,
	FOREIGN KEY(Errorimg_id) REFERENCES Item_image(Image_id)	
)charset = utf8;
```

db테이블에 탄산/물 이런거 추가..?



### stock_code

```mysql
CREATE TABLE Stock_code(
	Item_id INT(20) NOT NULL PRIMARY KEY ,
    Barcode VARCHAR(20) NOT NULL,
    Product_name VARCHAR(50) NOT NULL,
    Price INT(20) NOT NULL,
	FOREIGN KEY(Item_id) REFERENCES Item_info(Item_id)
)charset = utf8;
```

