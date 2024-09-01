-- phpMyAdmin SQL Dump
-- version 2.11.6
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: Mar 18, 2024 at 04:36 PM
-- Server version: 5.0.51
-- PHP Version: 5.2.6

SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `2collaborationcloudpy`
--

-- --------------------------------------------------------

--
-- Table structure for table `calltb`
--

CREATE TABLE `calltb` (
  `id` bigint(20) NOT NULL auto_increment,
  `Name` varchar(250) NOT NULL,
  `Mobile` varchar(250) NOT NULL,
  `Email` varchar(250) NOT NULL,
  `Address` varchar(500) NOT NULL,
  `UserName` varchar(250) NOT NULL,
  `Password` varchar(250) NOT NULL,
  PRIMARY KEY  (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=3 ;

--
-- Dumping data for table `calltb`
--

INSERT INTO `calltb` (`id`, `Name`, `Mobile`, `Email`, `Address`, `UserName`, `Password`) VALUES
(1, 'san', '9486365535', 'sangeeth5535@gmail.com', 'No 16, Samnath Plaza, Madurai Main Road, Melapudhur', 'san', 'san'),
(2, 'pavi', '9486365535', 'sangeeth5535@gmail.com', 'No 16, Samnath Plaza, Madurai Main Road, Melapudhur', 'pavi', 'pavi');

-- --------------------------------------------------------

--
-- Table structure for table `colltb`
--

CREATE TABLE `colltb` (
  `id` bigint(20) NOT NULL auto_increment,
  `Name` varchar(250) NOT NULL,
  `Mobile` varchar(250) NOT NULL,
  `Email` varchar(250) NOT NULL,
  `Address` varchar(500) NOT NULL,
  `UserName` varchar(250) NOT NULL,
  `Password` varchar(250) NOT NULL,
  `Status` varchar(250) NOT NULL,
  `EncKey` varchar(250) NOT NULL,
  PRIMARY KEY  (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=7 ;

--
-- Dumping data for table `colltb`
--

INSERT INTO `colltb` (`id`, `Name`, `Mobile`, `Email`, `Address`, `UserName`, `Password`, `Status`, `EncKey`) VALUES
(1, 'san', '9486365535', 'sangeeth5535@gmail.com', 'No 16, Samnath Plaza, Madurai Main Road, Melapudhur', 'san', 'san', 'Active', 'f3b25f5b6c'),
(2, 'sangeeth', '9486365535', 'sangeeth5535@gmail.com', 'No 16, Samnath Plaza, Madurai Main Road, Melapudhur', 'sangeeth', 'sangeeth', 'Active', 'd454f3c2eb'),
(3, 'siddiq', '9486365535', 'sangeeth5535@gmail.com', 'No 16, Samnath Plaza, Madurai Main Road, Melapudhur', 'siddiq', 'siddiq', 'Active', '544a542aef'),
(4, 'priya', '9486365535', 'sangeeth5535@gmail.com', 'No 16, Samnath Plaza, Madurai Main Road, Melapudhur', 'priya', 'priya', 'Active', '64362aafd5'),
(5, 'sanc', '9486365535', 'sangeeth5535@gmail.com', 'No 16, Samnath Plaza, Madurai Main Road, Melapudhur', 'sanc', 'sanc', 'Active', '2b42f2dbc1'),
(6, 'pavi', '9486365535', 'sangeeth5535@gmail.com', 'No 16, Samnath Plaza, Madurai Main Road, Melapudhur', 'pavi', 'pavi', 'Active', 'ac5c4d64fa');

-- --------------------------------------------------------

--
-- Table structure for table `cuserfiletb`
--

CREATE TABLE `cuserfiletb` (
  `id` bigint(20) NOT NULL auto_increment,
  `FileId` varchar(250) NOT NULL,
  `OwnerName` varchar(250) NOT NULL,
  `Filename` varchar(250) NOT NULL,
  `PrKey` varchar(250) NOT NULL,
  `UserName` varchar(250) NOT NULL,
  `Status` varchar(250) NOT NULL,
  `Type` varchar(250) NOT NULL,
  `Email` varchar(500) NOT NULL,
  PRIMARY KEY  (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=3 ;

--
-- Dumping data for table `cuserfiletb`
--

INSERT INTO `cuserfiletb` (`id`, `FileId`, `OwnerName`, `Filename`, `PrKey`, `UserName`, `Status`, `Type`, `Email`) VALUES
(1, '1', 'san', '5301tamil8.txt', 'a2ace5bdbb', 'san', 'Approved', 'callcenter', 'sangeeth5535@gmail.com'),
(2, '2', 'pavi', '9321tamilmv77.txt', 'ad3234ddd2', 'pavi', 'Approved', 'callcenter', 'sangeeth5535@gmail.com');

-- --------------------------------------------------------

--
-- Table structure for table `filetb`
--

CREATE TABLE `filetb` (
  `id` bigint(10) NOT NULL auto_increment,
  `CollName` varchar(250) NOT NULL,
  `PatientName` varchar(250) NOT NULL,
  `DiseaseName` varchar(250) NOT NULL,
  `Date` varchar(250) NOT NULL,
  `Info` varchar(250) NOT NULL,
  `FileName` varchar(250) NOT NULL,
  `ENkey` varchar(500) NOT NULL,
  `Status` varchar(250) NOT NULL,
  `ServerUrl` varchar(250) NOT NULL,
  `EncryptUrl` varchar(250) NOT NULL,
  `UrlKey` varchar(250) NOT NULL,
  PRIMARY KEY  (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=3 ;

--
-- Dumping data for table `filetb`
--

INSERT INTO `filetb` (`id`, `CollName`, `PatientName`, `DiseaseName`, `Date`, `Info`, `FileName`, `ENkey`, `Status`, `ServerUrl`, `EncryptUrl`, `UrlKey`) VALUES
(1, 'san', 'san', 'fever', '2024-03-18', 'nill', '5301tamil8.txt', 'a2ace5bdbb', 'Encrypt', '', '', ''),
(2, 'pavi', 'pavi', 'covid', '2024-03-18', 'asfsd', '9321tamilmv77.txt', 'ad3234ddd2', 'urlEncrypt', 'http://127.0.0.1:5000/static/Encrypt/9321tamilmv77.txt', 'wQ7LGrrcJ44Xf+YKvZGC5IUOBZC7PHTXfKaXLh/CzMZgbVQAQq9th9CAE3yTXIgFcO+Fa6j6EptD5dcedKtKqh5fVcitMXd0hK+X/prYOi3SDVczgvZSZlWFgpsy+5WKOufixO5AWNG05T/00Um/ZVvp3ldNkNLvnJPQ6a8/sbk=', 'eebb9ead41cf5c809c6d8b6357326b210ebff0ce58c918e9d419affb7b6caafb');

-- --------------------------------------------------------

--
-- Table structure for table `patienttb`
--

CREATE TABLE `patienttb` (
  `id` bigint(20) NOT NULL auto_increment,
  `Name` varchar(250) NOT NULL,
  `Mobile` varchar(250) NOT NULL,
  `Email` varchar(250) NOT NULL,
  `Address` varchar(500) NOT NULL,
  `UserName` varchar(250) NOT NULL,
  `Password` varchar(250) NOT NULL,
  `Status` varchar(250) NOT NULL,
  `CName` varchar(250) NOT NULL,
  PRIMARY KEY  (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=6 ;

--
-- Dumping data for table `patienttb`
--

INSERT INTO `patienttb` (`id`, `Name`, `Mobile`, `Email`, `Address`, `UserName`, `Password`, `Status`, `CName`) VALUES
(1, 'san', '9486365535', 'sangeeth5535@gmail.com', 'No 16, Samnath Plaza, Madurai Main Road, Melapudhur', 'san', 'san', 'Active', ''),
(2, 'siddiq', '9486365535', 'sangeeth5535@gmail.com', 'No 16, Samnath Plaza, Madurai Main Road, Melapudhur', 'siddiq', 'siddiq', 'Active', ''),
(3, 'priya', '9486365535', 'sangeeth5535@gmail.com', 'No 16, Samnath Plaza, Madurai Main Road, Melapudhur', 'priya', 'priya', 'Active', ''),
(4, 'sanp', '9486365535', 'sangeeth5535@gmail.com', 'No 16, Samnath Plaza, Madurai Main Road, Melapudhur', 'sanp', 'sanp', 'Active', ''),
(5, 'pavi', '9486365535', 'sangeeth5535@gmail.com', 'No 16, Samnath Plaza, Madurai Main Road, Melapudhur', 'pavi', 'pavi', 'Active', '');

-- --------------------------------------------------------

--
-- Table structure for table `requesttb`
--

CREATE TABLE `requesttb` (
  `id` bigint(10) NOT NULL auto_increment,
  `PatinetName` varchar(250) NOT NULL,
  `Emailid` varchar(250) NOT NULL,
  `CollaName` varchar(250) NOT NULL,
  `CEmailid` varchar(250) NOT NULL,
  `Status` varchar(250) NOT NULL,
  PRIMARY KEY  (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=6 ;

--
-- Dumping data for table `requesttb`
--

INSERT INTO `requesttb` (`id`, `PatinetName`, `Emailid`, `CollaName`, `CEmailid`, `Status`) VALUES
(1, 'san', 'sangeeth5535@gmail.com', 'san', 'sangeeth5535@gmail.com', 'Accept'),
(2, 'siddiq', 'sangeeth5535@gmail.com', 'siddiq', 'sangeeth5535@gmail.com', 'Accept'),
(3, 'priya', 'sangeeth5535@gmail.com', 'priya', 'sangeeth5535@gmail.com', 'Accept'),
(4, 'sanp', 'sangeeth5535@gmail.com', 'sanc', 'sangeeth5535@gmail.com', 'Accept'),
(5, 'pavi', 'sangeeth5535@gmail.com', 'pavi', 'sangeeth5535@gmail.com', 'Accept');

-- --------------------------------------------------------

--
-- Table structure for table `researchtb`
--

CREATE TABLE `researchtb` (
  `id` bigint(20) NOT NULL auto_increment,
  `Name` varchar(250) NOT NULL,
  `Mobile` varchar(250) NOT NULL,
  `Email` varchar(250) NOT NULL,
  `Address` varchar(500) NOT NULL,
  `UserName` varchar(250) NOT NULL,
  `Password` varchar(250) NOT NULL,
  PRIMARY KEY  (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=2 ;

--
-- Dumping data for table `researchtb`
--

INSERT INTO `researchtb` (`id`, `Name`, `Mobile`, `Email`, `Address`, `UserName`, `Password`) VALUES
(1, 'san', '9486365535', 'sangeeth5535@gmail.com', 'No 16, Samnath Plaza, Madurai Main Road, Melapudhur', 'san', 'san');

-- --------------------------------------------------------

--
-- Table structure for table `usertb`
--

CREATE TABLE `usertb` (
  `id` bigint(20) NOT NULL auto_increment,
  `Name` varchar(250) NOT NULL,
  `Mobile` varchar(250) NOT NULL,
  `Email` varchar(250) NOT NULL,
  `Address` varchar(500) NOT NULL,
  `UserName` varchar(250) NOT NULL,
  `Password` varchar(250) NOT NULL,
  PRIMARY KEY  (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=2 ;

--
-- Dumping data for table `usertb`
--

INSERT INTO `usertb` (`id`, `Name`, `Mobile`, `Email`, `Address`, `UserName`, `Password`) VALUES
(1, 'san', '9486365535', 'sangeeth5535@gmail.com', 'No 16, Samnath Plaza, Madurai Main Road, Melapudhur', 'san', 'san');
