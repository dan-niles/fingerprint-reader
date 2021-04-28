-- phpMyAdmin SQL Dump
-- version 5.0.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Oct 16, 2020 at 09:37 AM
-- Server version: 10.4.11-MariaDB
-- PHP Version: 7.4.2

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `pyzk`
--

-- --------------------------------------------------------

--
-- Table structure for table `all_employee`
--

CREATE TABLE `all_employee` (
  `EmployeeID` int(11) NOT NULL,
  `EmployeeNo` varchar(255) NOT NULL,
  `DisplayNo` varchar(255) NOT NULL,
  `DisplayName` varchar(255) NOT NULL,
  `EmpTitle` varchar(255) NOT NULL,
  `CallingName` varchar(255) NOT NULL,
  `Surname` varchar(255) NOT NULL,
  `FullName` varchar(255) NOT NULL,
  `NIC_No` varchar(255) NOT NULL,
  `NIC_Date` varchar(255) NOT NULL,
  `Birthday` varchar(255) NOT NULL,
  `Gender` varchar(255) NOT NULL,
  `EmpType` varchar(255) NOT NULL,
  `EmpTypeDescription` varchar(255) NOT NULL,
  `CT_Code` varchar(255) NOT NULL,
  `CT_Name` varchar(255) NOT NULL,
  `DSG_Code` varchar(255) NOT NULL,
  `DSG_Name` varchar(255) NOT NULL,
  `HIE_CODE_1` varchar(255) NOT NULL,
  `HIE_CODE_2` varchar(255) NOT NULL,
  `DepartmentID` int(11) NOT NULL,
  `Department` varchar(255) NOT NULL,
  `HIE_CODE_3` varchar(255) NOT NULL,
  `Section` varchar(255) NOT NULL,
  `HIE_CODE_4` varchar(255) NOT NULL,
  `Team` varchar(255) NOT NULL,
  `ImageURL` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `all_employee`
--

INSERT INTO `all_employee` (`EmployeeID`, `EmployeeNo`, `DisplayNo`, `DisplayName`, `EmpTitle`, `CallingName`, `Surname`, `FullName`, `NIC_No`, `NIC_Date`, `Birthday`, `Gender`, `EmpType`, `EmpTypeDescription`, `CT_Code`, `CT_Name`, `DSG_Code`, `DSG_Name`, `HIE_CODE_1`, `HIE_CODE_2`, `DepartmentID`, `Department`, `HIE_CODE_3`, `Section`, `HIE_CODE_4`, `Team`, `ImageURL`) VALUES
(92, '000095', '00097', 'Kuhanandan Sathyaraaj 000814', 'Mr.', 'Saththiyaraj', 'Kuhanandan', 'Saththiyaraj Kuhanandan', '792182801V', '02/12/2014 00:00:00', '05/08/1979 00:00:00', '1', '000001', 'Permanent', '000013', '1_Non-Executive', '000102', 'Office Assistant Driver', '000001', '000014', 5, 'ICT', '000033', 'Administration', '000087', 'Administration', ''),
(117, '000120', '00122', 'Dumith Senevirathne 000435', 'Mr.', 'Dumith', 'Seneviratne', 'Hettiarachchige Don Dumith Eranda Seneviratne', '850563799V', '27/10/2008 00:00:00', '25/02/1985 00:00:00', '1', '000001', 'Permanent', '000014', '2_Non-Executive', '000247', 'Systems Administrator / Team Lead', '000001', '000014', 5, 'ICT', '000036', 'System Engineering', '000090', 'System Engineering', ''),
(148, '000151', '00154', 'Udaya Dimbulagedera 000982', 'Mr.', 'Udaya', 'Dimbulagedera', 'Dimbulagedara Udaya Kumara Dimbulagedera', '830163450V', '02/02/2011 00:00:00', '16/01/1983 00:00:00', '1', '000001', 'Permanent', '000004', '2_Executive', '000024', 'Assistant Manager -ICT', '000001', '000014', 5, 'ICT', '000034', 'ICT', '000088', 'ICT', 'img/00154.png'),
(218, '000223', '00227', 'Nilthara Isurunie 001152', 'Ms.', 'Nilthara', 'Isurunie', 'Herath Mudiyanselage Gamage Nilthara Isurunie', '945911018V', '22/07/2010 00:00:00', '31/03/1994 00:00:00', '0', '000001', 'Permanent', '000013', '1_Non-Executive', '000049', 'Front Office Assistant / Secretary', '000001', '000014', 5, 'ICT', '000033', 'Administration', '000087', 'Administration', ''),
(223, '000231', '00235', 'Chinthana Mendis 001174', 'Mr.', 'Chinthana', 'Mendis', 'Agampodi Chinthana Sameera Mendis', '882560295V', '25/10/2004 00:00:00', '12/09/1988 00:00:00', '1', '000001', 'Permanent', '000013', '1_Non-Executive', '000098', 'Network Administrator', '000001', '000014', 5, 'ICT', '000036', 'System Engineering', '000090', 'System Engineering', ''),
(301, '000313', '00322', 'Viraj Goonewardena 001303', 'Mr.', 'Viraj', 'Goonewardena', 'Viraj Prasanna Goonewardena', '812080407V', '03/07/2007 00:00:00', '26/07/1981 00:00:00', '1', '000001', 'Permanent', '000008', '6_Executive', '000241', 'HOD - ICT', '000001', '000014', 5, 'ICT', '000034', 'ICT', '000088', 'ICT', ''),
(330, '000343', '00352', 'Tharindu Rupasinghe 001341', 'Mr.', 'Tharindu', 'Rupasinghe', 'Hewa Bowalage Tharindu Deeptha Rupasinghe', '880490060V', '27/04/2004 00:00:00', '18/02/1988 00:00:00', '1', '000001', 'Permanent', '000014', '2_Non-Executive', '000246', 'Software Engineer / Team Lead', '000001', '000014', 5, 'ICT', '000035', 'Software Engineering', '000089', 'Software Engineering', ''),
(402, '000430', '00441', 'Poshila Lekamge 001455', 'Ms.', 'Poshila', 'Lekamge', 'Poshila Sachinthani Lekamge', '927441616V', '20/11/2008 00:00:00', '31/08/1992 00:00:00', '0', '000001', 'Permanent', '000013', '1_Non-Executive', '000174', 'Software Engineer', '000001', '000014', 5, 'ICT', '000035', 'Software Engineering', '000089', 'Software Engineering', ''),
(422, '000465', '00510', 'Nisansala Edirisinghe Gamage', 'Ms.', 'Indrani', 'Nisansala', 'Edirisinghe  Gamage Indrani Nisansala', '916721382V', '19/09/2007 00:00:00', '20/06/1991 00:00:00', '0', '000001', 'Permanent', '000013', '1_Non-Executive', '000174', 'Software Engineer', '000001', '000014', 5, 'ICT', '000035', 'Software Engineering', '000089', 'Software Engineering', ''),
(477, '000578', '00584', 'Iksuka Premaratne', 'Mr.', 'Iksuka', 'Premaratne', 'Purawedi Wickramage Iksuka Sonal Premaratne', '200012103658', '18/08/2017 00:00:00', '30/04/2000 00:00:00', '1', '000008', 'Trainee', '000001', 'Trainee', '000212', 'Trainee - ICT', '000001', '000014', 5, 'ICT', '000034', 'ICT', '000088', 'ICT', ''),
(481, '000584', '00536', 'Ashan Kaldera 001532', 'Mr.', 'Ashan', 'Kaldera', 'Kottaralalage Ashan Kaldera', '981800117V', '01/07/2014 00:00:00', '28/06/1998 00:00:00', '1', '000001', 'Permanent', '000013', '1_Non-Executive', '000252', 'ICT Technician', '000001', '000014', 5, 'ICT', '000034', 'ICT', '000088', 'ICT', ''),
(482, '000585', '00587', 'Dan Niles', 'Mr.', 'Dan', 'Niles', 'Dan Asher Niles', '200005402690', '10/11/2016 00:00:00', '23/02/2000 00:00:00', '1', '000001', 'Permanent', '000013', '1_Non-Executive', '000255', 'Trainee Software Developer', '000001', '000014', 5, 'ICT', '000034', 'ICT', '000088', 'ICT', 'img/00587.png'),
(554, '000672', '00678', 'Urashima Isuranthi', 'Ms.', 'Urashima', 'Isuranthi', 'Kottawaththa Waddage Urashima Isuranthi', '955390423V', '26/05/2011 00:00:00', '08/02/1995 00:00:00', '0', '000007', 'Casual', '000016', 'Casual', '000260', 'HRIS Assistant', '000001', '000014', 5, 'ICT', '000034', 'ICT', '000088', 'ICT', '');

-- --------------------------------------------------------

--
-- Table structure for table `login`
--

CREATE TABLE `login` (
  `ID` int(11) NOT NULL,
  `UserName` varchar(250) NOT NULL,
  `Password` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `login`
--

INSERT INTO `login` (`ID`, `UserName`, `Password`) VALUES
(1, 'udaya', 'udaya');

-- --------------------------------------------------------

--
-- Table structure for table `payments`
--

CREATE TABLE `payments` (
  `payment_id` int(11) NOT NULL,
  `DisplayNo` varchar(255) NOT NULL,
  `day_payment` int(11) NOT NULL,
  `ot_payment` int(11) NOT NULL,
  `total` int(11) NOT NULL,
  `comments` varchar(1255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `payments`
--

INSERT INTO `payments` (`payment_id`, `DisplayNo`, `day_payment`, `ot_payment`, `total`, `comments`) VALUES
(1, '00587', 100, 50, 200, ''),
(2, '00587', 200, 200, 200, ''),
(3, '00587', 200, 200, 200, ''),
(4, '00587', 50, 500, 200, ''),
(5, '00587', 100, 1000, 200, ''),
(6, '00587', 200, 300, 200, ''),
(7, '00587', 200, 200, 200, ''),
(8, '00587', 200, 400, 200, ''),
(9, '00587', 100, 500, 200, 'Test'),
(10, '00587', 0, 23, 200, ''),
(11, '00587', 23, 23, 200, ''),
(12, '00587', 123, 123, 200, ''),
(13, '00587', 600, 123, 200, '');

-- --------------------------------------------------------

--
-- Table structure for table `transactions`
--

CREATE TABLE `transactions` (
  `id` int(11) NOT NULL,
  `DisplayNo` varchar(255) NOT NULL,
  `Reason` varchar(255) NOT NULL,
  `Type` varchar(255) NOT NULL,
  `Value` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `transactions`
--

INSERT INTO `transactions` (`id`, `DisplayNo`, `Reason`, `Type`, `Value`) VALUES
(1, '00587', 'Test1', 'Debit', 100),
(2, '00587', 'Test2', 'Credit', 200),
(3, '00587', 'Test3', 'Debit', 400),
(4, '00587', 'Test4', 'Credit', 50),
(5, '00587', 'Test5', 'Credit', 800),
(6, '00587', 'Test6', 'Debit', 700),
(7, '00587', 'Test7', 'Debit', 150),
(8, '00587', 'Test8', 'Credit', 140),
(9, '00587', 'Test9', 'Debit', 40),
(10, '00154', 'Test1', 'Credit', 50),
(11, '00154', 'Test2', 'Debit', 80),
(12, '00154', 'Test3', 'Credit', 10),
(13, '00154', 'Test4', 'Debit', 200),
(14, '00154', 'Test5', 'Debit', 800),
(15, '00154', 'Test6', 'Credit', 700),
(16, '00154', 'Test7', 'Credit', 1000),
(17, '00154', 'Test8', 'Debit', 5000);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `all_employee`
--
ALTER TABLE `all_employee`
  ADD PRIMARY KEY (`EmployeeID`);

--
-- Indexes for table `login`
--
ALTER TABLE `login`
  ADD PRIMARY KEY (`ID`);

--
-- Indexes for table `payments`
--
ALTER TABLE `payments`
  ADD PRIMARY KEY (`payment_id`);

--
-- Indexes for table `transactions`
--
ALTER TABLE `transactions`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `all_employee`
--
ALTER TABLE `all_employee`
  MODIFY `EmployeeID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=566;

--
-- AUTO_INCREMENT for table `login`
--
ALTER TABLE `login`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `payments`
--
ALTER TABLE `payments`
  MODIFY `payment_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;

--
-- AUTO_INCREMENT for table `transactions`
--
ALTER TABLE `transactions`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=18;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
