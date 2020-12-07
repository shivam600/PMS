-- MySQL Administrator dump 1.4
--
-- ------------------------------------------------------
-- Server version	5.0.33-community-nt


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;


--
-- Create schema pms
--

CREATE DATABASE IF NOT EXISTS pms;
USE pms;

--
-- Definition of table `admin`
--

DROP TABLE IF EXISTS `admin`;
CREATE TABLE `admin` (
  `adminid` varchar(45) NOT NULL,
  `adminname` varchar(45) NOT NULL,
  `password` varchar(45) NOT NULL,
  PRIMARY KEY  (`adminid`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `admin`
--

/*!40000 ALTER TABLE `admin` DISABLE KEYS */;
INSERT INTO `admin` (`adminid`,`adminname`,`password`) VALUES 
 ('100','Vicky Kumar','123');
/*!40000 ALTER TABLE `admin` ENABLE KEYS */;


--
-- Definition of table `dailyreport`
--

DROP TABLE IF EXISTS `dailyreport`;
CREATE TABLE `dailyreport` (
  `transactionid` int(10) unsigned NOT NULL auto_increment,
  `doctorid` int(10) unsigned NOT NULL,
  `patientid` varchar(45) NOT NULL,
  `currentdate` varchar(45) NOT NULL,
  `currenttime` varchar(45) NOT NULL,
  `temprature` varchar(45) NOT NULL,
  `bloodpressure` varchar(45) NOT NULL,
  `ecgstatus` varchar(45) NOT NULL,
  PRIMARY KEY  (`transactionid`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `dailyreport`
--

/*!40000 ALTER TABLE `dailyreport` DISABLE KEYS */;
INSERT INTO `dailyreport` (`transactionid`,`doctorid`,`patientid`,`currentdate`,`currenttime`,`temprature`,`bloodpressure`,`ecgstatus`) VALUES 
 (1,3,'1','','','','','');
/*!40000 ALTER TABLE `dailyreport` ENABLE KEYS */;


--
-- Definition of table `doctors`
--

DROP TABLE IF EXISTS `doctors`;
CREATE TABLE `doctors` (
  `doctorid` int(10) unsigned NOT NULL auto_increment,
  `doctorname` varchar(45) NOT NULL,
  `dob` varchar(20) NOT NULL,
  `gender` varchar(45) NOT NULL,
  `address` varchar(45) NOT NULL,
  `states` varchar(45) NOT NULL,
  `city` varchar(45) NOT NULL,
  `mobileno` varchar(45) NOT NULL,
  `email` varchar(45) NOT NULL,
  `hospitalcity` varchar(45) NOT NULL,
  `specialization` varchar(45) NOT NULL,
  `degrees` varchar(45) NOT NULL,
  `password` varchar(45) NOT NULL,
  `image` varchar(100) NOT NULL,
  PRIMARY KEY  (`doctorid`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `doctors`
--

/*!40000 ALTER TABLE `doctors` DISABLE KEYS */;
INSERT INTO `doctors` (`doctorid`,`doctorname`,`dob`,`gender`,`address`,`states`,`city`,`mobileno`,`email`,`hospitalcity`,`specialization`,`degrees`,`password`,`image`) VALUES 
 (2,'Dr MQ Khan','1990-09-16','Male','Patel Nagar','Gujrat','Ahemdabad','67676767676','pd@cc.com','AIIMS Ahemdabad','Neurology','MBBS','1.jpg','1.jpg'),
 (3,'Dr GK Kumar','1990-09-09','Male','Vikas Nagar','Madhya Pradesh','Bhopal','9876987676','gk@cc.com','AIIMS Bhopal','Orthopedic','MBBS MS','123','1.jpg');
/*!40000 ALTER TABLE `doctors` ENABLE KEYS */;


--
-- Definition of table `patients`
--

DROP TABLE IF EXISTS `patients`;
CREATE TABLE `patients` (
  `doctorsid` int(10) unsigned NOT NULL,
  `patientid` int(10) unsigned NOT NULL auto_increment,
  `patientname` varchar(45) NOT NULL,
  `dob` varchar(45) NOT NULL,
  `gender` varchar(45) NOT NULL,
  `address` varchar(45) NOT NULL,
  `states` varchar(45) NOT NULL,
  `city` varchar(45) NOT NULL,
  `email` varchar(45) NOT NULL,
  `mobileno` varchar(45) NOT NULL,
  `admitfor` varchar(45) NOT NULL,
  `bloodgroup` varchar(45) NOT NULL,
  `admittime` varchar(45) NOT NULL,
  `roomno` varchar(45) NOT NULL,
  `bedno` varchar(45) NOT NULL,
  `status` varchar(45) NOT NULL,
  `image` varchar(45) NOT NULL,
  `password` varchar(45) NOT NULL,
  PRIMARY KEY  (`patientid`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `patients`
--

/*!40000 ALTER TABLE `patients` DISABLE KEYS */;
INSERT INTO `patients` (`doctorsid`,`patientid`,`patientname`,`dob`,`gender`,`address`,`states`,`city`,`email`,`mobileno`,`admitfor`,`bloodgroup`,`admittime`,`roomno`,`bedno`,`status`,`image`,`password`) VALUES 
 (3,1,'Mohan Das','2019-09-18','male','sa','Bihar','Patna','gg@gmai.com','8888888888','ddd','A+','23:59','1','1','yes','1.jpg','123'),
 (3,2,'Mohan Das','2019-09-18','male','sa','Bihar','Patna','gg@gmai.com','8888888888','ddd','A+','23:59','1','1','yes','1.jpg','123');
/*!40000 ALTER TABLE `patients` ENABLE KEYS */;




/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
