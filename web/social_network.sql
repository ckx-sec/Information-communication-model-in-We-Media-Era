-- MySQL dump 10.13  Distrib 5.5.62, for Win64 (AMD64)
--
-- Host: localhost    Database: social_network
-- ------------------------------------------------------
-- Server version	8.0.25

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `t_news_content`
--

DROP TABLE IF EXISTS `t_news_content`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `t_news_content` (
  `id` varchar(100) DEFAULT NULL,
  `sort_id` varchar(100) DEFAULT NULL,
  `content` varchar(1000) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `t_news_content`
--

LOCK TABLES `t_news_content` WRITE;
/*!40000 ALTER TABLE `t_news_content` DISABLE KEYS */;
INSERT INTO `t_news_content` VALUES ('1','7','北京邮电大学专业录取分数线'),('2','4','最新！患者就医经验'),('3','2','基金选股青睐三主线 卖出银行煤炭有色'),('4','5','男篮备战克罗地亚，郭艾伦开小灶阿联单练'),('5','2','机构看好后市五大ETF集体净申购'),('6','1','洗车太勤会伤漆九大误区可能毁您爱车'),('7','6','雁荡山：首批国家重点风景名胜区之一'),('8','5','皇马恒大足校报名人数超10万'),('9','9','傅敏谈傅雷艺术收藏'),('10','8','历史密码：曹操杀华佗之迷'),('11','2','您认为国际油价近期会暴跌吗？石油随时面临抛售'),('12','2','交通部：出租汽车企业应推“员工制”'),('13','2','深港设计中心明年正式开张'),('14','2','资本新规推至明年实施，银行暂获喘息机会'),('15','2','积极把握波段性机会(组图)'),('16','2','官方：今年不扩大房地产税改革试点热'),('17','2','全国人大调研控烟立法'),('18','2','央行开展2000亿元MLF操作 利率持平'),('19','2','招商之后，国信、长城也出现“宕机”现象'),('20','2','1元诱导开通会员被续费8个月 风行电视被指欺诈？'),('21','2','车辆“锁电”后续航大幅缩水 车主直呼投诉举证难'),('22','2','起底退保黑产：投保人30%至60%退还保费被中介拿走'),('23','2','不平仓、不增保证金 青山集团与银团达成静默协议');
/*!40000 ALTER TABLE `t_news_content` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `t_news_sort`
--

DROP TABLE IF EXISTS `t_news_sort`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `t_news_sort` (
  `id` int DEFAULT NULL,
  `content` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `t_news_sort`
--

LOCK TABLES `t_news_sort` WRITE;
/*!40000 ALTER TABLE `t_news_sort` DISABLE KEYS */;
INSERT INTO `t_news_sort` VALUES (1,'汽车'),(2,'财经'),(3,'IT'),(4,'健康'),(5,'体育'),(6,'旅游'),(7,'教育'),(8,'军事'),(9,'文化'),(10,'娱乐'),(11,'时尚');
/*!40000 ALTER TABLE `t_news_sort` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `t_user`
--

DROP TABLE IF EXISTS `t_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `t_user` (
  `u_id` bigint unsigned NOT NULL AUTO_INCREMENT,
  `u_username` varchar(100) NOT NULL,
  `u_password` varchar(100) NOT NULL,
  `u_name` varchar(100) NOT NULL,
  `u_contact` varchar(100) NOT NULL,
  PRIMARY KEY (`u_id`),
  UNIQUE KEY `t_user_UN` (`u_username`)
) ENGINE=InnoDB AUTO_INCREMENT=49 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci COMMENT='用户';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `t_user`
--

LOCK TABLES `t_user` WRITE;
/*!40000 ALTER TABLE `t_user` DISABLE KEYS */;
INSERT INTO `t_user` VALUES (1,'admin','admin','admin22','admin3'),(12,'admin3','admin3','name','con'),(13,'user1','user1','name','con'),(14,'user2','user2','name','con'),(20,'user3','user3','name','contact'),(21,'user4','user4','name','contact'),(22,'114514','1919810','name','con'),(23,'user10','user10','1233','fdas1'),(31,'user11','user11','44','44'),(32,'user12','user12','4235','2345'),(33,'sad','sad123','asd','sad1'),(34,'dsftest','sd','dsag','asdf'),(42,'1131','113','name','con'),(43,'admin1','admin','admin','admin'),(46,'张岩','123','张岩1','123345'),(47,'admin2','admin2','admin22','13');
/*!40000 ALTER TABLE `t_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping routines for database 'social_network'
--
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-03-17 13:18:30
