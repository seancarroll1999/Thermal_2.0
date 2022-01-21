CREATE TABLE PRINT(
	PRINT_ID INT NOT NULL auto_increment,
    FUNCTION_ID INT NOT NULL,
    DATA LONGTEXT NOT NULL,
    SENDER VARCHAR(50),
    ATTRIBUTES TEXT,
    PRIMARY KEY (PRINT_ID)
)