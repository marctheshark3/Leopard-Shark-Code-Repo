CREATE TABLE IF NOT EXISTS Receipts_Table_1 (
    `id` INT,
    `customer_id` INT,
    `validation_type` VARCHAR(5) CHARACTER SET utf8,
    `total` NUMERIC(5, 2),
    `processing_state` VARCHAR(15) CHARACTER SET utf8,
    `validations` VARCHAR(14) CHARACTER SET utf8,
    `capture_lat` INT,
    `capture_long` INT,
    `created_at` DATETIME,
    `store_id` INT,
    `retailer_id` INT,
    `turk_submit_count` INT,
    `invalid_receipt` INT,
    `ref_number` VARCHAR(14) CHARACTER SET utf8,
    `appr_code` INT,
    `receipt_code` VARCHAR(23) CHARACTER SET utf8,
    `cashier` VARCHAR(10) CHARACTER SET utf8,
    `payment_trans_id` INT,
    `phone_data` VARCHAR(54) CHARACTER SET utf8,
    `verified_total` INT,
    `pending_acceptance_at` DATETIME,
    `pending_credit_at` DATETIME,
    `store_number` INT,
    `receipt_scan_content` INT,
    `fraud_type` VARCHAR(5) CHARACTER SET utf8,
    `Column_26` INT
);
INSERT INTO Receipts_Table_1 VALUES
    (962404,4162,'ocr',NULL,'invalid_receipt','ocr_unmatched',NULL,NULL,'2013-06-26 19:23:00',NULL,1,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'1.7.0:android:VS840 4G_4.0.4',NULL,NULL,NULL,NULL,NULL,NULL,NULL),
    (1521609,4162,'turk',121.32,'complete','turk_matched',NULL,NULL,'2013-09-08 03:47:00',2789,1,3,NULL,'0',NULL,'90 15 155 124','Jan D',NULL,'1.8:ios:iPhone3,1_6.1.3',1,NULL,NULL,NULL,NULL,NULL,NULL),
    (1927574,4162,'turk',5.39,'complete','turk_matched',NULL,NULL,'2013-10-18 18:32:00',116386,57,1,NULL,NULL,42614,NULL,'Ashley',NULL,'2.0:ios:iPhone3,1_7.0',1,NULL,NULL,NULL,NULL,'fraud',NULL),
    (1927689,4162,'turk',4.63,'complete','turk_matched',NULL,NULL,'2013-10-18 18:53:00',116386,57,1,NULL,NULL,85214,NULL,'Anndstasia',NULL,'2.0:ios:iPhone3,1_7.0',1,NULL,NULL,NULL,NULL,NULL,NULL),
    (2046635,4162,'turk',52.28,'complete','turk_matched',NULL,NULL,'2013-10-29 01:29:00',1979,3,1,NULL,NULL,NULL,'2-3301-2225-0077-5923-8',NULL,NULL,'2.0:ios:iPhone3,1_7.0',1,NULL,NULL,NULL,NULL,NULL,NULL),
    (2099520,4162,'turk',10.54,'complete','turk_matched',NULL,NULL,'2013-11-02 18:34:00',2789,1,1,NULL,'2700',NULL,'90 17 8 179','Jacob K',NULL,'2.0.0:android:VS840 4G_4.0.4',1,NULL,NULL,NULL,NULL,NULL,NULL),
    (2392982,4162,'turk',9.69,'complete','turk_matched',NULL,NULL,'2013-11-18 01:20:00',116386,57,1,NULL,NULL,NULL,NULL,'Troi',NULL,'2.0:ios:iPhone3,1_7.0.3',1,NULL,NULL,NULL,NULL,NULL,NULL),
    (3089652,4162,'turk',11.25,'complete','turk_matched',NULL,NULL,'2013-12-21 02:20:00',NULL,87,1,NULL,NULL,NULL,NULL,NULL,NULL,'2.0.6:ios:iPhone3,1_7.0.3',NULL,NULL,NULL,NULL,NULL,NULL,NULL),
    (3993876,4162,'ocr',15,'complete',NULL,NULL,NULL,'2014-01-26 20:22:00',NULL,3,NULL,NULL,NULL,NULL,'Feb-28',NULL,NULL,'2.0.6:ios:iPhone6,1_7.0.4',NULL,NULL,NULL,NULL,NULL,NULL,NULL),
    (4368961,4162,'turk',58.71,'complete','turk_matched',NULL,NULL,'2014-02-12 04:18:00',NULL,3,1,NULL,NULL,NULL,NULL,NULL,NULL,'2.0.6:ios:iPhone6,1_7.0.4',1,NULL,NULL,NULL,NULL,NULL,NULL),
    (4414820,4162,'turk',76.57,'complete','turk_matched',NULL,NULL,'2014-02-14 19:11:00',NULL,1,2,1,'84313',NULL,NULL,NULL,NULL,'2.0.6:ios:iPhone6,1_7.0.4',1,NULL,NULL,NULL,NULL,NULL,NULL),
    (5608076,4162,'turk',NULL,'complete','turk_matched',NULL,NULL,'2014-04-01 15:02:00',NULL,87,2,NULL,NULL,NULL,'337000010022',NULL,NULL,'2.1:ios:iPhone6,1_7.1',NULL,NULL,NULL,NULL,NULL,NULL,NULL),
    (5807279,4162,'turk',58.95,'complete','turk_matched',NULL,NULL,'2014-04-09 02:17:00',NULL,3,1,NULL,NULL,NULL,NULL,NULL,NULL,'2.1:ios:iPhone6,1_7.1',1,NULL,NULL,NULL,NULL,NULL,NULL),
    (6702789,4162,'turk',78.26,'complete','turk_matched',NULL,NULL,'2014-05-13 02:41:00',177738,99,1,NULL,NULL,NULL,NULL,NULL,NULL,'2.3.2:ios:iPhone6,1_7.1.1',1,NULL,NULL,NULL,NULL,NULL,NULL),
    (7026469,4162,'turk',74.01,'complete','turk_matched',NULL,NULL,'2014-05-24 01:48:00',2789,1,1,NULL,'0',NULL,'90 12 201 159','Rosa 9',NULL,'2.3.2:ios:iPhone6,1_7.1.1',1,NULL,NULL,NULL,NULL,'fraud',NULL),
    (7158589,4162,'turk',65.83,'complete','turk_matched',NULL,NULL,'2014-05-28 03:22:00',177738,99,1,NULL,NULL,454435,'C0214 #0684','Sara',NULL,'2.3.2:ios:iPhone6,1_7.1.1',1,NULL,NULL,NULL,NULL,NULL,NULL),
    (7591023,4162,'turk',59.67,'complete','turk_matched',NULL,NULL,'2014-06-11 00:57:00',NULL,3,2,NULL,NULL,NULL,'Feb-61',NULL,NULL,'2.4:ios:iPhone6,1_7.1.1',1,NULL,NULL,NULL,NULL,NULL,NULL),
    (8172736,4162,'turk',10.33,'complete','turk_matched',NULL,NULL,'2014-06-28 01:05:00',227080,115,2,NULL,NULL,NULL,NULL,NULL,NULL,'2.4.3:ios:iPhone6,1_7.1.1',1,NULL,NULL,NULL,NULL,NULL,NULL),
    (8558039,4162,'admin',11.71,'complete','turk_unmatched',NULL,NULL,'2014-07-08 21:19:00',55614,28,5,NULL,'95000 89 045 2',8358,NULL,'O7',NULL,'2.4.3:ios:iPhone6,1_7.1.1',1,NULL,NULL,NULL,NULL,NULL,NULL),
    (8631339,4162,'turk',57.6,'complete','turk_matched',NULL,NULL,'2014-07-10 02:24:00',NULL,99,1,NULL,NULL,NULL,NULL,NULL,NULL,'2.4.3:ios:iPhone6,1_7.1.1',1,NULL,NULL,NULL,NULL,NULL,NULL),
    (9615734,4162,'turk',65.23,'complete','turk_matched',NULL,NULL,'2014-08-03 18:03:00',NULL,99,2,NULL,NULL,NULL,NULL,NULL,NULL,'2.5.1:ios:iPhone6,1_7.1.2',1,NULL,NULL,NULL,NULL,NULL,NULL),
    (10320949,4162,'turk',89.06,'complete','turk_matched',NULL,NULL,'2014-08-19 03:49:00',NULL,1,1,NULL,'0',NULL,NULL,NULL,NULL,'2.5.1:ios:iPhone6,1_7.1.2',1,NULL,NULL,NULL,NULL,NULL,NULL),
    (12309037,4162,'turk',45.02,'complete','turk_matched',NULL,NULL,'2014-10-06 14:30:00',NULL,99,1,NULL,NULL,NULL,NULL,NULL,NULL,'3.0:ios:iPhone6,1_7.1.2',1,NULL,NULL,NULL,NULL,NULL,NULL),
    (13686045,4162,'admin',78.04,'complete','turk_matched',NULL,NULL,'2014-11-05 04:00:00',177738,99,1,NULL,NULL,NULL,NULL,NULL,NULL,'3.1:ios:iPhone6,1_8.1',1,NULL,NULL,NULL,NULL,NULL,NULL),
    (14121859,4162,'turk',104.63,'complete','turk_matched',NULL,NULL,'2014-11-14 13:54:00',12420,4,2,NULL,'431700036679',NULL,NULL,'2377',NULL,'3.1:ios:iPhone6,1_8.1',1,NULL,NULL,NULL,NULL,NULL,NULL),
    (14485500,4162,'turk',80.54,'complete','turk_matched',NULL,NULL,'2014-11-20 19:32:00',177738,99,1,NULL,NULL,NULL,NULL,NULL,NULL,'3.1.1:ios:iPhone6,1_8.1',1,NULL,NULL,NULL,NULL,NULL,NULL),
    (16587993,4162,'turk',50.82,'complete','turk_matched',NULL,NULL,'2014-12-24 23:06:00',NULL,188,1,NULL,NULL,NULL,NULL,NULL,NULL,'3.1.2:ios:iPhone6,1_8.1.2',1,NULL,NULL,NULL,NULL,NULL,NULL),
    (16986705,4162,'turk',31.38,'complete','turk_matched',NULL,NULL,'2015-01-01 01:49:00',NULL,188,5,NULL,NULL,NULL,NULL,NULL,NULL,'3.2:ios:iPhone6,1_8.1.2',1,NULL,NULL,NULL,NULL,NULL,NULL),
    (23129620,4162,'turk',106.54,'complete','turk_matched',NULL,NULL,'2015-03-29 16:44:00',177738,99,5,NULL,NULL,NULL,NULL,NULL,NULL,'3.4:ios:iPhone6,1_8.1.3',1,NULL,NULL,NULL,NULL,NULL,NULL),
    (23708211,4162,'tlog',87,'complete',NULL,NULL,NULL,'2015-04-05 11:30:00',NULL,129,NULL,NULL,'121752',NULL,'4/4/15 16:15',NULL,NULL,'0.1:online:RetailerTransactionProcessor::LinkshareBase',1,'2015-03-07 00:00:00','2015-04-19 11:30:00',NULL,NULL,NULL,NULL),
    (24724329,4162,'turk',47.46,'complete','turk_matched',NULL,NULL,'2015-04-17 02:52:00',NULL,2,1,NULL,NULL,NULL,NULL,NULL,NULL,'3.4:ios:iPhone6,1_8.1.3',1,NULL,NULL,NULL,NULL,NULL,NULL),
    (21661223,5354610,'turk',27.04,'complete','turk_matched',NULL,NULL,'2015-03-09 23:56:00',22929,1,1,NULL,NULL,NULL,NULL,'Rgan S',NULL,'3.3:ios:iPhone6,1_7.1.1',1,NULL,NULL,NULL,NULL,NULL,NULL),
    (23322944,5354610,'turk',23.77,'complete','turk_matched',NULL,NULL,'2015-04-01 04:40:00',NULL,1,1,NULL,NULL,NULL,'40Pm 87',NULL,NULL,'3.3:ios:iPhone6,1_7.1.1',1,NULL,NULL,NULL,NULL,NULL,NULL),
    (25206462,5354610,'turk',51.29,'complete','turk_matched',NULL,NULL,'2015-04-22 04:07:00',28872,2,1,NULL,NULL,NULL,NULL,NULL,NULL,'3.3:ios:iPhone6,1_7.1.1',1,NULL,NULL,1,NULL,'fraud',NULL);
