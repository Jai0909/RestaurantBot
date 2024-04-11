/*
SQLyog Community Edition- MySQL GUI v7.01 
MySQL - 5.0.27-community-nt : Database - restaurant
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;

CREATE DATABASE /*!32312 IF NOT EXISTS*/`restaurant` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `restaurant`;

/*Table structure for table `addmenu` */

DROP TABLE IF EXISTS `addmenu`;

CREATE TABLE `addmenu` (
  `choosefile` varchar(255) NOT NULL,
  `menuname` varchar(50) NOT NULL,
  `price` varchar(50) NOT NULL,
  `category` varchar(50) NOT NULL,
  `id` int(255) NOT NULL auto_increment,
  PRIMARY KEY  (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `addmenu` */

insert  into `addmenu`(`choosefile`,`menuname`,`price`,`category`,`id`) values ('static/menuimages/img-01.jpg','drink 1','85','drinks',1),('static/menuimages/img-04.jpg','lunch 1','355','lunch',2),('static/menuimages1/img-03.jpg','drink 2','150','drinks',3),('static/menuimages/img-08.jpg','diner 1','550','dinner',4);

/*Table structure for table `addsupplier` */

DROP TABLE IF EXISTS `addsupplier`;

CREATE TABLE `addsupplier` (
  `image_file` varchar(50) NOT NULL,
  `suppliername` varchar(50) NOT NULL,
  `stype` varchar(50) NOT NULL,
  `mobileno` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `addsupplier` */

insert  into `addsupplier`(`image_file`,`suppliername`,`stype`,`mobileno`) values ('static/menuimages/stuff-img-02.jpg','Thomas','vegetables supplier','9856324756');

/*Table structure for table `bill` */

DROP TABLE IF EXISTS `bill`;

CREATE TABLE `bill` (
  `item_name` varchar(255) NOT NULL,
  `item_price` varchar(255) NOT NULL,
  `bill_datetime` datetime NOT NULL,
  `user_id` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `bill` */

insert  into `bill`(`item_name`,`item_price`,`bill_datetime`,`user_id`) values ('drink 1','85','2024-03-20 11:32:22',''),('lunch 1','355','2024-03-20 11:41:00',''),('diner 1','550','2024-04-02 15:45:58','OWN001'),('lunch 1','355','2024-04-02 15:47:03','OWN001'),('drink 1','85','2024-04-02 16:38:12','OWN001'),('drink 2','150','2024-04-02 16:49:23','OWN001'),('lunch 1','355','2024-04-02 17:48:39','EMP001'),('drink 1','85','2024-04-02 18:06:06','MAN001'),('diner 1','550','2024-04-02 18:37:38','MAN001'),('lunch 1','355','2024-04-02 18:44:20','MAN001'),('drink 2','150','2024-04-02 18:50:24','MAN001'),('diner 1','550','2024-04-02 19:18:20','MAN001'),('diner 1','550','2024-04-02 19:25:10','MAN001'),('lunch 1','355','2024-04-02 19:42:41','MAN001'),('drink 1','85','2024-04-02 20:03:57','MAN001');

/*Table structure for table `bills` */

DROP TABLE IF EXISTS `bills`;

CREATE TABLE `bills` (
  `item_name` varchar(255) NOT NULL default '',
  `item_price` varchar(255) NOT NULL default '',
  `bill_datetime` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `bills` */

insert  into `bills`(`item_name`,`item_price`,`bill_datetime`) values ('diner 1','550','2024-03-20 11:45:49'),('drink 1','85','2024-03-20 11:45:55'),('lunch 1','355','2024-03-20 11:45:58'),('drink 2','150','2024-03-20 11:46:01'),('lunch 1','355','2024-03-20 11:46:08'),('diner 1','550','2024-03-29 16:04:14'),('drink 2','150','2024-03-29 16:04:27'),('drink 1','85','2024-03-29 16:26:15'),('diner 1','550','2024-03-29 16:29:24'),('lunch 1','355','2024-04-01 10:41:33'),('drink 2','150','2024-04-01 10:41:37'),('drink 1','85','2024-04-01 11:05:35'),('diner 1','550','2024-04-01 11:05:42'),('drink 1','85','2024-04-01 11:05:45'),('drink 1','85','2024-04-01 11:53:47'),('drink 2','150','2024-04-01 16:28:09'),('lunch 1','355','2024-04-01 16:36:10'),('lunch 1','355','2024-04-01 17:22:57'),('diner 1','550','2024-04-01 17:32:14'),('drink 1','85','2024-04-01 17:55:41'),('diner 1','550','2024-04-01 19:07:30'),('drink 1','85','2024-04-02 11:24:35'),('diner 1','550','2024-04-02 15:10:05'),('lunch 1','355','2024-04-02 20:12:01'),('drink 1','85','2024-04-03 11:12:13'),('lunch 1','355','2024-04-03 14:58:09'),('drink 1','85','2024-04-03 18:43:16'),('diner 1','550','2024-04-03 18:55:51'),('drink 2','150','2024-04-03 19:00:13');

/*Table structure for table `empregister` */

DROP TABLE IF EXISTS `empregister`;

CREATE TABLE `empregister` (
  `name` varchar(255) NOT NULL,
  `user_id` varchar(255) NOT NULL default '',
  `password` varchar(50) NOT NULL,
  `person` varchar(255) NOT NULL default ''
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `empregister` */

insert  into `empregister`(`name`,`user_id`,`password`,`person`) values ('Reshma','EMP001','123','Employee'),('Rahul','EMP002','123456','Employee');

/*Table structure for table `managerlogin` */

DROP TABLE IF EXISTS `managerlogin`;

CREATE TABLE `managerlogin` (
  `user_id` varchar(50) NOT NULL,
  `password` varchar(50) NOT NULL,
  `person` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `managerlogin` */

insert  into `managerlogin`(`user_id`,`password`,`person`) values ('MAN001','456','Manager');

/*Table structure for table `ownerlogin` */

DROP TABLE IF EXISTS `ownerlogin`;

CREATE TABLE `ownerlogin` (
  `user_id` varchar(50) NOT NULL,
  `password` varchar(50) NOT NULL,
  `person` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `ownerlogin` */

insert  into `ownerlogin`(`user_id`,`password`,`person`) values ('OWN001','123','owner');

/*Table structure for table `registerusers` */

DROP TABLE IF EXISTS `registerusers`;

CREATE TABLE `registerusers` (
  `name` varchar(50) NOT NULL,
  `email` varchar(50) NOT NULL,
  `phone` varchar(50) NOT NULL,
  `user_id` varchar(50) NOT NULL default '',
  `password` varchar(50) NOT NULL,
  `person` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `registerusers` */

insert  into `registerusers`(`name`,`email`,`phone`,`user_id`,`password`,`person`) values ('jay','jay@gmail.com','7894561254','EMP001','123','Employee'),('jay','jay@gmail.com','7894561254','EMP001','123','Employee'),('aa','aa','456','EMP002','123456','Employee'),('sdsd','sdsd@gmail.com','9898999999','EMP003','123456','Employee'),('sss','sc@gmail.com','8600306078','EMP004','789','Employee');

/*Table structure for table `shifts` */

DROP TABLE IF EXISTS `shifts`;

CREATE TABLE `shifts` (
  `start_time` datetime default NULL,
  `end_time` datetime NOT NULL,
  `duration` time NOT NULL,
  `employee_id` varchar(255) default ''
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `shifts` */

insert  into `shifts`(`start_time`,`end_time`,`duration`,`employee_id`) values ('2024-03-18 16:16:23','2024-03-18 16:17:05','00:00:41','EMP001'),('2024-03-18 16:20:37','2024-03-18 16:21:21','00:00:43','EMP002'),('2024-03-18 16:37:59','2024-03-18 16:38:02','00:00:03','EMP002'),('2024-03-19 10:45:16','2024-03-19 10:54:13','00:08:57','EMP001'),('2024-04-01 17:00:04','2024-04-01 17:00:38','00:00:34','Employee'),('2024-04-01 17:14:41','2024-04-01 17:15:05','00:00:24','EMP002'),('2024-04-03 11:21:56','2024-04-03 11:22:01','00:00:05','EMP001'),('2024-04-03 11:37:15','2024-04-03 11:37:46','00:00:31','EMP001'),('2024-04-03 18:29:16','2024-04-03 18:29:51','00:00:35','EMP001');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
