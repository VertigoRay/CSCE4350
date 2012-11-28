-- userprofile.sql
-- PROFILE.SQL - rating, billing, address, userprofile, user
-- USER TABLE -- --verified 
INSERT INTO auth_user (username, first_name, last_name, email, password, date_joined) VALUES
    ('bmarley','Bob','Marley','bob@marley.com','qwe123','2009-5-4 04:13:54'),
	('cworley','Chris','Worley','cworley@unt.edu','123456','2009-6-5 04:13:54'),
	('jmills','Jimi','Mills','jmills@unt.edu','123456','2009-9-11 04:13:54'),
	('jbrhoads','Jacob','Rhoads','jbrhoads@email.com','qwe123','2009-7-23 04:13:54'),
	('stingray','Misagh','Piller','ray@email.com','qwe123','2010-2-8 04:13:54'),
	('superfox27','Daniel','Stuart','dstu@dstu.net','qwe123','2011-7-2 04:13:54'),
	('puppetmaster','Jay','Connor','jay@puppet.org','qwe123','2011-11-20 04:13:54'),
	('deathmaker','Randy','Madden','randy@realtor.com','qwe123','2012-10-2 04:13:54'),
	('redant','Drew','Porath','drew@internet.com','qwe123','2012-7-4 04:13:54'),
	('nowrath','Frank','Reynolds','frank@cool.net','qwe123','2012-7-5 04:13:54'),
	('stronghold','Chris','Valgren','valg@gmail.com','qwe123','2012-7-4 04:13:54'),
	('laggynewbie','Nick','Zdanuk','nickz@gmail.com','qwe123','2012-7-20 04:13:54')
;

-- USERPROFILE table
INSERT INTO	profile_userprofile (user_id, phone) VALUES
	(2, '9401234567'),
	(3, '9405654498'),
	(4, '9405654498'),
	(5, '9405654498'),
	(6, '9405654498'),
	(7, '8178441234'),
	(8, '8178441235'),
	(9, '8178441236'),
	(10, '8178441237'),
	(11, '8178441238'),
	(12, '8178441239'),
	(13, '8178441230')
;