-- order.sql
-- SHOP.SQL - category, product, order
-- ORDER TABLE --
INSERT INTO `shop_order` (user_id, product_id, billing_id, status, statusinfo,mod_date, pub_date) VALUES
  (2,12,2,'sr','USPS: 9405511201080473337287',null,null),
	(2,15,2,'sr','UPS: 1Z2807700363847562',null,null),
	(3,18,3,'or',null,null,null),
	(3,21,3,'sr','Fedex: 9002901001300270295452',null,null),
	(3,24,3,'or',null,null,null),
	(4,27,4,'sr','USPS: 9405511201080432879465',null,null),
	(5,30,5,'pr',null,null,null),
	(6,33,6,'pr',null,null,null),
	(6,36,6,'os','Fedex: 9562901001300278763431',null,null),
	(7,3,1,'or',null,null, null),
	(7,6,1,'os','Fedex: 9102901001300272627875',null,null),
	(7,9,1,'os','UPS: 1Z2807700364791005',null,null)
;