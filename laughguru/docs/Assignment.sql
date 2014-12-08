-- phpMyAdmin SQL Dump
-- version 4.0.9
-- http://www.phpmyadmin.net
--
-- Host: 127.0.0.1
-- Generation Time: Nov 26, 2014 at 03:47 PM
-- Server version: 5.5.34
-- PHP Version: 5.4.22

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `mydb`
--
CREATE DATABASE IF NOT EXISTS `mydb` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
USE `mydb`;

-- --------------------------------------------------------

--
-- Table structure for table `content`
--

CREATE TABLE IF NOT EXISTS `content` (
  `idContent` int(11) NOT NULL,
  `Name` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`idContent`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `content`
--

INSERT INTO `content` (`idContent`, `Name`) VALUES
(1, 'English'),
(2, 'Math');

-- --------------------------------------------------------

--
-- Table structure for table `questions`
--

CREATE TABLE IF NOT EXISTS `questions` (
  `idQues` int(11) NOT NULL,
  `Question` varchar(45) NOT NULL,
  `Opt_A` varchar(45) NOT NULL,
  `Opt_C` varchar(45) DEFAULT NULL,
  `Opt_B` varchar(45) DEFAULT NULL,
  `Opt_D` varchar(45) DEFAULT NULL,
  `Opt_right` varchar(1) DEFAULT NULL,
  `Order_ques` int(11) DEFAULT NULL,
  `Content_idContent` int(11) NOT NULL,
  PRIMARY KEY (`idQues`,`Content_idContent`),
  KEY `fk_Questions_Content1` (`Content_idContent`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `questions`
--

INSERT INTO `questions` (`idQues`, `Question`, `Opt_A`, `Opt_C`, `Opt_B`, `Opt_D`, `Opt_right`, `Order_ques`, `Content_idContent`) VALUES
(1, 'What is 2 + 2?', '2', '4', '-1', '-1', 'A', 1, 2),
(2, 'What is 3 + 2?', '5', '4', '-1', '-1', 'A', 2, 2),
(3, 'What is 3 + 3?', '3', '6', '-1', '-1', 'B', 3, 2),
(4, 'A _____ of birds', 'Group', 'Flock', 'Pairs', 'Herd', 'B', 1, 1),
(5, 'A _____ of men', 'Group', 'Flock', 'Pairs', 'Herd', 'A', 2, 1),
(6, 'A _____ of cattle', 'Group', 'Flock', 'Pairs', 'Herd', 'D', 3, 1);

--
-- Constraints for dumped tables
--

--
-- Constraints for table `questions`
--
ALTER TABLE `questions`
  ADD CONSTRAINT `fk_Questions_Content1` FOREIGN KEY (`Content_idContent`) REFERENCES `content` (`idContent`) ON DELETE NO ACTION ON UPDATE NO ACTION;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
