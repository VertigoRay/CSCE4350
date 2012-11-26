-- category.sql
-- CATEGORY TABLE --
-- MAIN CATEGORIES (pid_id=0) -- -- verified
INSERT INTO `shop_category` (pid_id, name) VALUES
  (0,'Books'),
	(0,'Music'),
	(0,'Movies'),
	(0,'Games'),
	(0,'Electronics'),
	(0,'Appliances'),
	(0,'Automotive'),
	(0,'Clothing'),
	(0,'Computers'),
	(0,'Furniture')
;

-- SUB-CATEGORY -- These can only be inserted once the main categories are entered.
-- BOOKS --
INSERT INTO `shop_category` (pid_id, name) VALUES
	((SELECT id FROM (SELECT * FROM shop_category) AS c1 WHERE c1.name='Books'),'Mystery'),
	((SELECT id FROM (SELECT * FROM shop_category) AS c1 WHERE c1.name='Books'),'History'),
	((SELECT id FROM (SELECT * FROM shop_category) AS c1 WHERE c1.name='Books'),'Romance'),
	((SELECT id FROM (SELECT * FROM shop_category) AS c1 WHERE c1.name='Books'),'Science'),
	((SELECT id FROM (SELECT * FROM shop_category) AS c1 WHERE c1.name='Books'),'Comics'),
	((SELECT id FROM (SELECT * FROM shop_category) AS c1 WHERE c1.name='Books'),'Fantasy'),
	((SELECT id FROM (SELECT * FROM shop_category) AS c1 WHERE c1.name='Books'),'Politics'),
	((SELECT id FROM (SELECT * FROM shop_category) AS c1 WHERE c1.name='Books'),'Paranormal'),
	((SELECT id FROM (SELECT * FROM shop_category) AS c1 WHERE c1.name='Books'),'Audiobooks'),
	((SELECT id FROM (SELECT * FROM shop_category) AS c1 WHERE c1.name='Books'),'Horror'),
	((SELECT id FROM (SELECT * FROM shop_category) AS c1 WHERE c1.name='Books'),'Health'),
	((SELECT id FROM (SELECT * FROM shop_category) AS c1 WHERE c1.name='Books'),'Philosophy')
;

-- SUB-CATEGORY --
-- MUSIC --
INSERT INTO `shop_category` (pid_id, name) VALUES
	((SELECT id FROM (SELECT * FROM shop_category) AS c1 WHERE c1.name='Music'),'Alternative'),
	((SELECT id FROM (SELECT * FROM shop_category) AS c1 WHERE c1.name='Music'),'Dubstep'),
	((SELECT id FROM (SELECT * FROM shop_category) AS c1 WHERE c1.name='Music'),'Electronica'),
	((SELECT id FROM (SELECT * FROM shop_category) AS c1 WHERE c1.name='Music'),'Classical'),
	((SELECT id FROM (SELECT * FROM shop_category) AS c1 WHERE c1.name='Music'),'Indy Rock'),
	((SELECT id FROM (SELECT * FROM shop_category) AS c1 WHERE c1.name='Music'),'Country'),
	((SELECT id FROM (SELECT * FROM shop_category) AS c1 WHERE c1.name='Music'),'K-Pop'),
	((SELECT id FROM (SELECT * FROM shop_category) AS c1 WHERE c1.name='Music'),'Jazz'),
	((SELECT id FROM (SELECT * FROM shop_category) AS c1 WHERE c1.name='Music'),'Latino'),
	((SELECT id FROM (SELECT * FROM shop_category) AS c1 WHERE c1.name='Music'),'Oldies'),
	((SELECT id FROM (SELECT * FROM shop_category) AS c1 WHERE c1.name='Music'),'Christian'),
	((SELECT id FROM (SELECT * FROM shop_category) AS c1 WHERE c1.name='Music'),'Rap'),
	((SELECT id FROM (SELECT * FROM shop_category) AS c1 WHERE c1.name='Music'),'Choral'),
	((SELECT id FROM (SELECT * FROM shop_category) AS c1 WHERE c1.name='Music'),'Acoustic')
;

-- SUB-CATEGORY --
-- MOVIES --
INSERT INTO `shop_category` (pid_id, name) VALUES
	((SELECT id FROM (SELECT * FROM shop_category) AS c1 WHERE c1.name='Movies'),'Action'),
	((SELECT id FROM (SELECT * FROM shop_category) AS c1 WHERE c1.name='Movies'),'Comedy'),
	((SELECT id FROM (SELECT * FROM shop_category) AS c1 WHERE c1.name='Movies'),'Family'),
	((SELECT id FROM (SELECT * FROM shop_category) AS c1 WHERE c1.name='Movies'),'History'),
	((SELECT id FROM (SELECT * FROM shop_category) AS c1 WHERE c1.name='Movies'),'Mystery'),
	((SELECT id FROM (SELECT * FROM shop_category) AS c1 WHERE c1.name='Movies'),'Science'),
	((SELECT id FROM (SELECT * FROM shop_category) AS c1 WHERE c1.name='Movies'),'Western'),
	((SELECT id FROM (SELECT * FROM shop_category) AS c1 WHERE c1.name='Movies'),'Animation'),
	((SELECT id FROM (SELECT * FROM shop_category) AS c1 WHERE c1.name='Movies'),'Horror'),
	((SELECT id FROM (SELECT * FROM shop_category) AS c1 WHERE c1.name='Movies'),'Biography'),
	((SELECT id FROM (SELECT * FROM shop_category) AS c1 WHERE c1.name='Movies'),'Drama'),
	((SELECT id FROM (SELECT * FROM shop_category) AS c1 WHERE c1.name='Movies'),'Romance'),
	((SELECT id FROM (SELECT * FROM shop_category) AS c1 WHERE c1.name='Movies'),'Adventure'),
	((SELECT id FROM (SELECT * FROM shop_category) AS c1 WHERE c1.name='Movies'),'Fantacy')
;

-- SUB-CATEGORY --
-- GAMES --
INSERT INTO `shop_category` (pid_id, name) VALUES
	((SELECT id FROM (SELECT * FROM shop_category) AS c1 WHERE c1.name='Games'),'PC'),
	((SELECT id FROM (SELECT * FROM shop_category) AS c1 WHERE c1.name='Games'),'Xbox'),
	((SELECT id FROM (SELECT * FROM shop_category) AS c1 WHERE c1.name='Games'),'Xbox 360'),
	((SELECT id FROM (SELECT * FROM shop_category) AS c1 WHERE c1.name='Games'),'Playstation 1'),
	((SELECT id FROM (SELECT * FROM shop_category) AS c1 WHERE c1.name='Games'),'Playstation 2'),
	((SELECT id FROM (SELECT * FROM shop_category) AS c1 WHERE c1.name='Games'),'Playstation 3'),
	((SELECT id FROM (SELECT * FROM shop_category) AS c1 WHERE c1.name='Games'),'Gamecube'),
	((SELECT id FROM (SELECT * FROM shop_category) AS c1 WHERE c1.name='Games'),'Nintendo 64'),
	((SELECT id FROM (SELECT * FROM shop_category) AS c1 WHERE c1.name='Games'),'Nintendo Wii '),
	((SELECT id FROM (SELECT * FROM shop_category) AS c1 WHERE c1.name='Games'),'Nintendo DS'),
	((SELECT id FROM (SELECT * FROM shop_category) AS c1 WHERE c1.name='Games'),'Gameboy Classic'),
	((SELECT id FROM (SELECT * FROM shop_category) AS c1 WHERE c1.name='Games'),'Gameboy Advance')
;

-- SUB-CATEGORY --
-- ELECTRONICS --
INSERT INTO `shop_category` (pid_id, name) VALUES
	((SELECT id FROM (SELECT * FROM shop_category) AS c1 WHERE c1.name='Electronics'),'Phones'),
	((SELECT id FROM (SELECT * FROM shop_category) AS c1 WHERE c1.name='Electronics'),'TVs'),
	((SELECT id FROM (SELECT * FROM shop_category) AS c1 WHERE c1.name='Electronics'),'DVD Players'),
	((SELECT id FROM (SELECT * FROM shop_category) AS c1 WHERE c1.name='Electronics'),'Blu-ray Players'),
	((SELECT id FROM (SELECT * FROM shop_category) AS c1 WHERE c1.name='Electronics'),'Game Consoles'),
	((SELECT id FROM (SELECT * FROM shop_category) AS c1 WHERE c1.name='Electronics'),'Audio Components'),
	((SELECT id FROM (SELECT * FROM shop_category) AS c1 WHERE c1.name='Electronics'),'GPS'),
	((SELECT id FROM (SELECT * FROM shop_category) AS c1 WHERE c1.name='Electronics'),'Tablets'),
	((SELECT id FROM (SELECT * FROM shop_category) AS c1 WHERE c1.name='Electronics'),'Cameras')
;

-- SUB-CATEGORY --
-- APPLIANCES --
INSERT INTO `shop_category` (pid_id, name) VALUES
	((SELECT id FROM (SELECT * FROM shop_category) AS c1 WHERE c1.name='Appliances'),'Refridgerators'),
	((SELECT id FROM (SELECT * FROM shop_category) AS c1 WHERE c1.name='Appliances'),'Range/Oven'),
	((SELECT id FROM (SELECT * FROM shop_category) AS c1 WHERE c1.name='Appliances'),'Dishwashers'),
	((SELECT id FROM (SELECT * FROM shop_category) AS c1 WHERE c1.name='Appliances'),'Washer/Dryers'),
	((SELECT id FROM (SELECT * FROM shop_category) AS c1 WHERE c1.name='Appliances'),'AC/Heating'),
	((SELECT id FROM (SELECT * FROM shop_category) AS c1 WHERE c1.name='Appliances'),'Microwaves')
;

-- SUB-CATEGORY --
-- AUTOMOTIVE --
INSERT INTO `shop_category` (pid_id, name) VALUES
	((SELECT id FROM (SELECT * FROM shop_category) AS c1 WHERE c1.name='Automotive'),'Paint'),
	((SELECT id FROM (SELECT * FROM shop_category) AS c1 WHERE c1.name='Automotive'),'Body'),
	((SELECT id FROM (SELECT * FROM shop_category) AS c1 WHERE c1.name='Automotive'),'Parts'),
	((SELECT id FROM (SELECT * FROM shop_category) AS c1 WHERE c1.name='Automotive'),'Cars'),
	((SELECT id FROM (SELECT * FROM shop_category) AS c1 WHERE c1.name='Automotive'),'Trucks'),
	((SELECT id FROM (SELECT * FROM shop_category) AS c1 WHERE c1.name='Automotive'),'Vans'),
	((SELECT id FROM (SELECT * FROM shop_category) AS c1 WHERE c1.name='Automotive'),'Hatchbacks'),
	((SELECT id FROM (SELECT * FROM shop_category) AS c1 WHERE c1.name='Automotive'),'Motorcycles')
;

-- SUB-CATEGORY --
-- CLOTHING --
INSERT INTO `shop_category` (pid_id, name) VALUES
	((SELECT id FROM (SELECT * FROM shop_category) AS c1 WHERE c1.name='Clothing'),'T-Shirts'),
	((SELECT id FROM (SELECT * FROM shop_category) AS c1 WHERE c1.name='Clothing'),'Mens Jeans'),
	((SELECT id FROM (SELECT * FROM shop_category) AS c1 WHERE c1.name='Clothing'),'Womens Jeans'),
	((SELECT id FROM (SELECT * FROM shop_category) AS c1 WHERE c1.name='Clothing'),'Button-up Shirts'),
	((SELECT id FROM (SELECT * FROM shop_category) AS c1 WHERE c1.name='Clothing'),'Polo'),
	((SELECT id FROM (SELECT * FROM shop_category) AS c1 WHERE c1.name='Clothing'),'Dresses'),
	((SELECT id FROM (SELECT * FROM shop_category) AS c1 WHERE c1.name='Clothing'),'Shoes'),
	((SELECT id FROM (SELECT * FROM shop_category) AS c1 WHERE c1.name='Clothing'),'Hats')
;

-- SUB-CATEGORY --
-- COMPUTERS --
INSERT INTO `shop_category` (pid_id, name) VALUES
	((SELECT id FROM (SELECT * FROM shop_category) AS c1 WHERE c1.name='Computers'),'Desktop'),
	((SELECT id FROM (SELECT * FROM shop_category) AS c1 WHERE c1.name='Computers'),'Laptop'),
	((SELECT id FROM (SELECT * FROM shop_category) AS c1 WHERE c1.name='Computers'),'Server'),
	((SELECT id FROM (SELECT * FROM shop_category) AS c1 WHERE c1.name='Computers'),'Netbook')
;

-- SUB-CATEGORY --
-- FURNITURE --
INSERT INTO `shop_category` (pid_id, name) VALUES
	((SELECT id FROM (SELECT * FROM shop_category) AS c1 WHERE c1.name='Furniture'),'Kitchen'),
	((SELECT id FROM (SELECT * FROM shop_category) AS c1 WHERE c1.name='Furniture'),'Living Room'),
	((SELECT id FROM (SELECT * FROM shop_category) AS c1 WHERE c1.name='Furniture'),'Bedroom'),
	((SELECT id FROM (SELECT * FROM shop_category) AS c1 WHERE c1.name='Furniture'),'Office'),
	((SELECT id FROM (SELECT * FROM shop_category) AS c1 WHERE c1.name='Furniture'),'Patio')
;