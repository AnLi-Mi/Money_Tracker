CREATE TABLE spendings (
	id integer, 
    purchase_date date, 
    amount float NOT NULL, 
    category varchar(255) NOT NULL, 
    notes varchar(255), 
    for_whom varchar(255) NOT NULL, 
    who_paid varchar(255) NOT NULL,
    PRIMARY KEY (id),
    CHECK (for_whom = 'Anna' OR for_whom = 'Craig' OR for_whom = 'common')
    );