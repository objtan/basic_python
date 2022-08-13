-- MySQL dump 10.13  Distrib 8.0.29, for Win64 (x86_64)
--
-- Host: localhost    Database: assignment_info_manage
-- ------------------------------------------------------
-- Server version	8.0.29

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `student`
--

DROP TABLE IF EXISTS `student`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `student` (
  `Student_ID` varchar(7) NOT NULL DEFAULT '0',
  `Name` varchar(255) NOT NULL,
  `DoB` date DEFAULT NULL,
  `Sex` enum('Female','Male','Gay') DEFAULT NULL,
  `Address` varchar(255) DEFAULT NULL,
  `Mobile_Number` varchar(50) DEFAULT NULL,
  `Email` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`Student_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `student`
--

LOCK TABLES `student` WRITE;
/*!40000 ALTER TABLE `student` DISABLE KEYS */;
INSERT INTO `student` VALUES ('PT0001','Nguyen Van Thang','2001-07-09','Male','Ha Noi','0123456789','nguyenvanthang@gmail.com'),('PT0002','Nguyen Viet Phuong','2001-07-09','Male','Ha Nam','0123456789','nguyenvietphuong@gmail.com'),('PT0003','Nguyen Manh Tan','2001-07-09','Male','Ha Tinh','0123456789','nguyenmanhtan@gmail.com'),('PT0004','Nguyen Viet Hieu','2001-07-09','Male','Thai Binh','0123456789','nguyenviethieu@gmail.com'),('PT0005','Ngo Manh Hung','2001-07-09','Male','Nam Dinh','0123456789','ngomanhhung@gmail.com'),('PT0006','Nguyen Tien Su','2001-07-09','Male','Thai Nguyen','0123456789','nguyentiensu@gmail.com'),('PT0007','Nguyen Viet Hoai Bao','2001-07-09','Male','Ha Noi','0123456789','ngoviethoaibao@gmail.com'),('PT0008','Pham Manh Ninh','2001-07-09','Male','Hai Duong','0123456789','phammanhninh@gmail.com'),('PT0009','Tran Anh Tuan','2001-07-09','Male','Hung Yen','0123456789','trananhtuan@gmail.com'),('PT0010','Nguyen Ngoc Son','2001-07-09','Male','Bac Giang','0123456789','nguyenngocson@gmail.com'),('PT0011','Pham Van Si','2001-07-09','Male','Nhat Ban','0123456789','phanvansi@gmail.com'),('PT0012','Phan Tan Sinh','2001-07-09','Male','Han Quoc','0123456789','phantansinh@gmail.com'),('PT0013','Dang Dinh Nam','2001-07-09','Male','Da Nang','0123456789','dangdinhnam@gmail.com'),('PT0014','Vo Tan Quynh','2001-07-09','Male','Quang Ngai','0123456789','votanquynh@gmail.com'),('PT0015','Nguyen Thi Ly','2001-07-09','Female','Thai Binh','0123456789','nguyenthily@gmail.com'),('PT0016','Le Ba Kham','2001-07-09','Male','Hai Phong','0123456789','lebakham@gmail.com'),('PT0017','Pham Thi Huong Giang','2001-07-09','Female','Ha Noi','0123456789','phamthihuongiang@gmail.com'),('PT0018','Nguyen Nhat Le','2001-07-09','Female','Bac Ninh','0123456789','nguyennhatle@gmail.com'),('PT0019','Nguyen Phuong Thao','2001-07-09','Female','Lang Son','0123456789','nguyenphuongthao@gmail.com'),('PT0020','Bui Hong Dao','2001-07-09','Male','Yen Bai','0123456789','buihongdao@gmail.com');
/*!40000 ALTER TABLE `student` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-08-13 23:59:25
