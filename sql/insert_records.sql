# Insert Transaction data
INSERT INTO Transaction(Transaction_Id,Payement_Status,Currency,Payement_Amount,Payement_Method)
VALUES.
TS001	Paid	USD	10887	Amazon Gift Card	
TS002	Paid	EURO	98889	Credit Card	
TS003	Paid	USD	6757	Amazon Gift Card	
TS004	Paid	INR	677666	Debit Card	
TS005	Paid	INR	8777	Debit Card	
TS006	Paid	INR	9888	Debit Card	
TS007	Paid	INR	98887	Debit Card	
TS008	Invoiced	EURO	98887	Debit Card	
TS009	Invoiced	EURO	9754	Debit Card	
TS010	Invoiced	EURO	566888	Credit Card	
TS011	Invoiced	USD	655	Credit Card	
TS012	Invoiced	USD	677	Credit Card	
TS013	Invoiced	USD	677	Credit Card	
TS014	Invoiced	USD	677	Credit Card	
TS015	Invoiced	USD	677	Credit Card	
TS016	Invoiced	USD	677	Credit Card	

# Insert orders data
INSERT INTO order(Order_Id,Order_Date,Product_Id,	Customer_Id,Transaction_Id,order_description)
VALUES
ORD001	8/1/2022	P001	CUS001	TS001	Online
ORD002	8/19/2022	P002	CUS002	TS002	Online
ORD003	7/22/2022	P003	CUS003	TS003	Online
ORD004	8/22/2022	P004	CUS004	TS004	Online
ORD005	2/1/2022	P005	CUS005	TS005	Online
ORD006	3/17/2022	P006	CUS006	TS006	Online
ORD007	4/29/2022	P007	CUS007	TS007	Online
ORD008	10/18/2022	P008	CUS008	TS008	Online
ORD009	2/3/2022	P009	CUS009	TS009	Online
ORD010	3/10/2022	P010	CUS010	TS010	Online
ORD011	9/27/2022	P011	CUS011	TS011	Online
ORD012	11/16/2022	P012	CUS012	TS012	Online
