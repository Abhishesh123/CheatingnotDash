-- MySQL dump 10.13  Distrib 5.7.29, for Linux (x86_64)
--
-- Host: localhost    Database: CheatingNot_test1
-- ------------------------------------------------------
-- Server version	5.7.29-0ubuntu0.18.04.1

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
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=153 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can view log entry',1,'view_logentry'),(5,'Can add permission',2,'add_permission'),(6,'Can change permission',2,'change_permission'),(7,'Can delete permission',2,'delete_permission'),(8,'Can view permission',2,'view_permission'),(9,'Can add group',3,'add_group'),(10,'Can change group',3,'change_group'),(11,'Can delete group',3,'delete_group'),(12,'Can view group',3,'view_group'),(13,'Can add user',4,'add_user'),(14,'Can change user',4,'change_user'),(15,'Can delete user',4,'delete_user'),(16,'Can view user',4,'view_user'),(17,'Can add content type',5,'add_contenttype'),(18,'Can change content type',5,'change_contenttype'),(19,'Can delete content type',5,'delete_contenttype'),(20,'Can view content type',5,'view_contenttype'),(21,'Can add session',6,'add_session'),(22,'Can change session',6,'change_session'),(23,'Can delete session',6,'delete_session'),(24,'Can view session',6,'view_session'),(25,'Can add anonymous',7,'add_anonymous'),(26,'Can change anonymous',7,'change_anonymous'),(27,'Can delete anonymous',7,'delete_anonymous'),(28,'Can view anonymous',7,'view_anonymous'),(29,'Can add discount',8,'add_discount'),(30,'Can change discount',8,'change_discount'),(31,'Can delete discount',8,'delete_discount'),(32,'Can view discount',8,'view_discount'),(33,'Can add height',9,'add_height'),(34,'Can change height',9,'change_height'),(35,'Can delete height',9,'delete_height'),(36,'Can view height',9,'view_height'),(37,'Can add hobbies',10,'add_hobbies'),(38,'Can change hobbies',10,'change_hobbies'),(39,'Can delete hobbies',10,'delete_hobbies'),(40,'Can view hobbies',10,'view_hobbies'),(41,'Can add occupation',11,'add_occupation'),(42,'Can change occupation',11,'change_occupation'),(43,'Can delete occupation',11,'delete_occupation'),(44,'Can view occupation',11,'view_occupation'),(45,'Can add push notification msg',12,'add_pushnotificationmsg'),(46,'Can change push notification msg',12,'change_pushnotificationmsg'),(47,'Can delete push notification msg',12,'delete_pushnotificationmsg'),(48,'Can view push notification msg',12,'view_pushnotificationmsg'),(49,'Can add users',13,'add_users'),(50,'Can change users',13,'change_users'),(51,'Can delete users',13,'delete_users'),(52,'Can view users',13,'view_users'),(53,'Can add weight',14,'add_weight'),(54,'Can change weight',14,'change_weight'),(55,'Can delete weight',14,'delete_weight'),(56,'Can view weight',14,'view_weight'),(57,'Can add users notification',15,'add_usersnotification'),(58,'Can change users notification',15,'change_usersnotification'),(59,'Can delete users notification',15,'delete_usersnotification'),(60,'Can view users notification',15,'view_usersnotification'),(61,'Can add userprofile videos',16,'add_userprofilevideos'),(62,'Can change userprofile videos',16,'change_userprofilevideos'),(63,'Can delete userprofile videos',16,'delete_userprofilevideos'),(64,'Can view userprofile videos',16,'view_userprofilevideos'),(65,'Can add userprofile images',17,'add_userprofileimages'),(66,'Can change userprofile images',17,'change_userprofileimages'),(67,'Can delete userprofile images',17,'delete_userprofileimages'),(68,'Can view userprofile images',17,'view_userprofileimages'),(69,'Can add user privacy',18,'add_userprivacy'),(70,'Can change user privacy',18,'change_userprivacy'),(71,'Can delete user privacy',18,'delete_userprivacy'),(72,'Can view user privacy',18,'view_userprivacy'),(73,'Can add user auth',19,'add_userauth'),(74,'Can change user auth',19,'change_userauth'),(75,'Can delete user auth',19,'delete_userauth'),(76,'Can view user auth',19,'view_userauth'),(77,'Can add super like',20,'add_superlike'),(78,'Can change super like',20,'change_superlike'),(79,'Can delete super like',20,'delete_superlike'),(80,'Can view super like',20,'view_superlike'),(81,'Can add reports',21,'add_reports'),(82,'Can change reports',21,'change_reports'),(83,'Can delete reports',21,'delete_reports'),(84,'Can view reports',21,'view_reports'),(85,'Can add preferences',22,'add_preferences'),(86,'Can change preferences',22,'change_preferences'),(87,'Can delete preferences',22,'delete_preferences'),(88,'Can view preferences',22,'view_preferences'),(89,'Can add otp',23,'add_otp'),(90,'Can change otp',23,'change_otp'),(91,'Can delete otp',23,'delete_otp'),(92,'Can view otp',23,'view_otp'),(93,'Can add nopes',24,'add_nopes'),(94,'Can change nopes',24,'change_nopes'),(95,'Can delete nopes',24,'delete_nopes'),(96,'Can view nopes',24,'view_nopes'),(97,'Can add match',25,'add_match'),(98,'Can change match',25,'change_match'),(99,'Can delete match',25,'delete_match'),(100,'Can view match',25,'view_match'),(101,'Can add like',26,'add_like'),(102,'Can change like',26,'change_like'),(103,'Can delete like',26,'delete_like'),(104,'Can view like',26,'view_like'),(105,'Can add hi',27,'add_hi'),(106,'Can change hi',27,'change_hi'),(107,'Can delete hi',27,'delete_hi'),(108,'Can view hi',27,'view_hi'),(109,'Can add heart',28,'add_heart'),(110,'Can change heart',28,'change_heart'),(111,'Can delete heart',28,'delete_heart'),(112,'Can view heart',28,'view_heart'),(113,'Can add block',29,'add_block'),(114,'Can change block',29,'change_block'),(115,'Can delete block',29,'delete_block'),(116,'Can view block',29,'view_block'),(117,'Can add accessories',30,'add_accessories'),(118,'Can change accessories',30,'change_accessories'),(119,'Can delete accessories',30,'delete_accessories'),(120,'Can view accessories',30,'view_accessories'),(121,'Can add paytm payment status',31,'add_paytmpaymentstatus'),(122,'Can change paytm payment status',31,'change_paytmpaymentstatus'),(123,'Can delete paytm payment status',31,'delete_paytmpaymentstatus'),(124,'Can view paytm payment status',31,'view_paytmpaymentstatus'),(125,'Can add plan details',32,'add_plandetails'),(126,'Can change plan details',32,'change_plandetails'),(127,'Can delete plan details',32,'delete_plandetails'),(128,'Can view plan details',32,'view_plandetails'),(129,'Can add plans',33,'add_plans'),(130,'Can change plans',33,'change_plans'),(131,'Can delete plans',33,'delete_plans'),(132,'Can view plans',33,'view_plans'),(133,'Can add wallet',34,'add_wallet'),(134,'Can change wallet',34,'change_wallet'),(135,'Can delete wallet',34,'delete_wallet'),(136,'Can view wallet',34,'view_wallet'),(137,'Can add user daily dose',35,'add_userdailydose'),(138,'Can change user daily dose',35,'change_userdailydose'),(139,'Can delete user daily dose',35,'delete_userdailydose'),(140,'Can view user daily dose',35,'view_userdailydose'),(141,'Can add purchase request',36,'add_purchaserequest'),(142,'Can change purchase request',36,'change_purchaserequest'),(143,'Can delete purchase request',36,'delete_purchaserequest'),(144,'Can view purchase request',36,'view_purchaserequest'),(145,'Can add plan purched by user',37,'add_planpurchedbyuser'),(146,'Can change plan purched by user',37,'change_planpurchedbyuser'),(147,'Can delete plan purched by user',37,'delete_planpurchedbyuser'),(148,'Can view plan purched by user',37,'view_planpurchedbyuser'),(149,'Can add accessories details',38,'add_accessoriesdetails'),(150,'Can change accessories details',38,'change_accessoriesdetails'),(151,'Can delete accessories details',38,'delete_accessoriesdetails'),(152,'Can view accessories details',38,'view_accessoriesdetails');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (1,'pbkdf2_sha256$150000$ajplym0NLEyV$X3NjLrRlctMDTO40JmWEBnjJ6ya7DxgKy/gQpMeX1lQ=','2020-04-19 16:27:31.361591',1,'abhimishra','','','abhi@gmail.com',1,1,'2020-04-19 16:27:04.132034'),(2,'pbkdf2_sha256$150000$E2s0HSLXDk9f$ghm0VfqwLUTETiKBwjfYcfGA6JJnNBwpUlznRGC1tLI=',NULL,1,'Abhishesh','Abhishesh','mishra','abhishesh@cheatingnot.com',0,1,'2020-04-19 17:05:07.000000');
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=27 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (1,'2020-04-19 17:02:18.238651','1','Love guru',1,'[{\"added\": {}}]',11,1),(2,'2020-04-19 17:02:31.909870','1','174',1,'[{\"added\": {}}]',9,1),(3,'2020-04-19 17:02:44.158219','1','coding',1,'[{\"added\": {}}]',10,1),(4,'2020-04-19 17:03:01.619437','1','67',1,'[{\"added\": {}}]',14,1),(5,'2020-04-19 17:05:07.791855','2','Abhishesh',1,'[{\"added\": {}}]',4,1),(6,'2020-04-19 17:05:37.639240','2','Abhishesh',2,'[{\"changed\": {\"fields\": [\"first_name\", \"last_name\", \"email\"]}}]',4,1),(7,'2020-04-19 17:05:48.841300','2','Abhishesh',2,'[{\"changed\": {\"fields\": [\"is_superuser\"]}}]',4,1),(8,'2020-04-19 17:25:30.552010','1','Gold',1,'[{\"added\": {}}]',33,1),(9,'2020-04-19 17:26:14.678315','1','Gold - 3',1,'[{\"added\": {}}]',32,1),(10,'2020-04-19 17:26:49.593809','1','Gold',1,'[{\"added\": {}}]',30,1),(11,'2020-04-19 17:27:14.217718','1','Gold - 3',1,'[{\"added\": {}}]',38,1),(12,'2020-04-19 17:28:09.528414','1','8744865366',1,'[{\"added\": {}}]',7,1),(13,'2020-04-19 17:28:28.342109','1','500',1,'[{\"added\": {}}]',8,1),(14,'2020-04-19 17:30:19.052944','0a614350-8c3a-4fa3-be22-47c11d42dd6f','abhishesh mishra',1,'[{\"added\": {}}]',13,1),(15,'2020-04-19 17:31:11.055794','1','hey plz purchage  hey mssg',1,'[{\"added\": {}}]',12,1),(16,'2020-04-19 18:53:07.271622','e306ba18-81a9-446c-8bcd-2ea89c16069f','abhishesh',1,'[{\"added\": {}}]',13,1),(17,'2020-04-21 17:07:16.248916','1','PlanPurchedByUser object (1)',1,'[{\"added\": {}}]',37,1),(18,'2020-04-22 13:25:58.220116','1','abhishesh mishra',1,'[{\"added\": {}}]',25,1),(19,'2020-04-24 18:01:04.472685','1','abhishesh mishra',1,'[{\"added\": {}}]',25,1),(20,'2020-04-24 18:01:13.516029','2','abhishesh mishra',1,'[{\"added\": {}}]',25,1),(21,'2020-04-24 18:03:40.219209','2c51705a-43a3-42eb-9d2a-161f7e4dc8c3','Shyam',1,'[{\"added\": {}}]',13,1),(22,'2020-04-24 18:04:58.158088','2','PlanPurchedByUser object (2)',1,'[{\"added\": {}}]',37,1),(23,'2020-04-24 18:26:35.740951','2','Plus',1,'[{\"added\": {}}]',33,1),(24,'2020-04-24 18:27:15.186551','3','super likes plan',1,'[{\"added\": {}}]',33,1),(25,'2020-04-24 18:29:10.887024','2','Plus - 6',1,'[{\"added\": {}}]',32,1),(26,'2020-04-24 18:43:53.698515','3','PlanPurchedByUser object (3)',1,'[{\"added\": {}}]',37,1);
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=39 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(3,'auth','group'),(2,'auth','permission'),(4,'auth','user'),(5,'contenttypes','contenttype'),(6,'sessions','session'),(30,'subscription','accessories'),(38,'subscription','accessoriesdetails'),(31,'subscription','paytmpaymentstatus'),(32,'subscription','plandetails'),(37,'subscription','planpurchedbyuser'),(33,'subscription','plans'),(36,'subscription','purchaserequest'),(35,'subscription','userdailydose'),(34,'subscription','wallet'),(7,'userprofile','anonymous'),(29,'userprofile','block'),(8,'userprofile','discount'),(28,'userprofile','heart'),(9,'userprofile','height'),(27,'userprofile','hi'),(10,'userprofile','hobbies'),(26,'userprofile','like'),(25,'userprofile','match'),(24,'userprofile','nopes'),(11,'userprofile','occupation'),(23,'userprofile','otp'),(22,'userprofile','preferences'),(12,'userprofile','pushnotificationmsg'),(21,'userprofile','reports'),(20,'userprofile','superlike'),(19,'userprofile','userauth'),(18,'userprofile','userprivacy'),(17,'userprofile','userprofileimages'),(16,'userprofile','userprofilevideos'),(13,'userprofile','users'),(15,'userprofile','usersnotification'),(14,'userprofile','weight');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2020-04-19 14:28:06.950967'),(2,'auth','0001_initial','2020-04-19 14:28:09.803689'),(3,'admin','0001_initial','2020-04-19 14:28:23.370659'),(4,'admin','0002_logentry_remove_auto_add','2020-04-19 14:28:25.722079'),(5,'admin','0003_logentry_add_action_flag_choices','2020-04-19 14:28:25.788664'),(6,'contenttypes','0002_remove_content_type_name','2020-04-19 14:28:27.571226'),(7,'auth','0002_alter_permission_name_max_length','2020-04-19 14:28:27.806152'),(8,'auth','0003_alter_user_email_max_length','2020-04-19 14:28:27.996258'),(9,'auth','0004_alter_user_username_opts','2020-04-19 14:28:28.069421'),(10,'auth','0005_alter_user_last_login_null','2020-04-19 14:28:28.876699'),(11,'auth','0006_require_contenttypes_0002','2020-04-19 14:28:28.932695'),(12,'auth','0007_alter_validators_add_error_messages','2020-04-19 14:28:29.007568'),(13,'auth','0008_alter_user_username_max_length','2020-04-19 14:28:29.201267'),(14,'auth','0009_alter_user_last_name_max_length','2020-04-19 14:28:29.389741'),(15,'auth','0010_alter_group_name_max_length','2020-04-19 14:28:29.556654'),(16,'auth','0011_update_proxy_permissions','2020-04-19 14:28:29.632811'),(17,'sessions','0001_initial','2020-04-19 14:28:30.267383'),(18,'userprofile','0001_initial','2020-04-19 14:28:42.816712'),(19,'subscription','0001_initial','2020-04-19 14:29:18.879998');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('vde76vwe34xiznumzblzvtvw7ny21u2p','MzY0ODM0ZGY2MzhhMTM0MzRlZjM1ZGYxNzliMzg2OTQwZjZjOWU2Zjp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJjYjJhMmYwNTNiOWNiZDM3MjgxNjZiMmJjZWMxZmE0NmEyODc4ZGVjIn0=','2020-05-03 16:27:31.434578');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `subscription_accessories`
--

DROP TABLE IF EXISTS `subscription_accessories`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `subscription_accessories` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `accessories_description` longtext,
  `is_active` tinyint(1) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `subscription_accessories`
--

LOCK TABLES `subscription_accessories` WRITE;
/*!40000 ALTER TABLE `subscription_accessories` DISABLE KEYS */;
INSERT INTO `subscription_accessories` VALUES (1,'Gold','Like swipe',1,'2020-04-19 17:26:49.592860'),(2,'Plus',NULL,0,'2020-04-30 18:12:43.639102'),(3,'abhishesh',NULL,1,'2020-04-30 18:16:33.047172');
/*!40000 ALTER TABLE `subscription_accessories` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `subscription_accessoriesdetails`
--

DROP TABLE IF EXISTS `subscription_accessoriesdetails`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `subscription_accessoriesdetails` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `price` decimal(6,2) NOT NULL,
  `validity` varchar(10) NOT NULL,
  `description` longtext NOT NULL,
  `remaining_hi` int(11) NOT NULL,
  `remaining_hearts` int(11) NOT NULL,
  `remaining_boosts` int(11) NOT NULL,
  `remaining_talktime` int(11) NOT NULL,
  `remaining_superlikes` int(11) NOT NULL,
  `wallet_percentage` double NOT NULL,
  `discount_percentage` double NOT NULL,
  `accessories_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `subscription_accesso_accessories_id_b4c1dc70_fk_subscript` (`accessories_id`),
  CONSTRAINT `subscription_accesso_accessories_id_b4c1dc70_fk_subscript` FOREIGN KEY (`accessories_id`) REFERENCES `subscription_accessories` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `subscription_accessoriesdetails`
--

LOCK TABLES `subscription_accessoriesdetails` WRITE;
/*!40000 ALTER TABLE `subscription_accessoriesdetails` DISABLE KEYS */;
INSERT INTO `subscription_accessoriesdetails` VALUES (1,200.00,'3','gold plan',0,0,0,0,0,0,0,1);
/*!40000 ALTER TABLE `subscription_accessoriesdetails` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `subscription_paytmpaymentstatus`
--

DROP TABLE IF EXISTS `subscription_paytmpaymentstatus`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `subscription_paytmpaymentstatus` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `order_id` varchar(30) NOT NULL,
  `txn_id` varchar(100) NOT NULL,
  `txn_type` varchar(30) NOT NULL,
  `bank_txn_id` varchar(100) NOT NULL,
  `bank_name` varchar(50) NOT NULL,
  `resp_code` int(11) NOT NULL,
  `payment_mode` varchar(10) NOT NULL,
  `gatway_name` varchar(30) NOT NULL,
  `mid` varchar(100) NOT NULL,
  `resp_msg` longtext NOT NULL,
  `txn_amount` decimal(6,2) NOT NULL,
  `refund_amount` decimal(6,2) NOT NULL,
  `status` varchar(12) NOT NULL,
  `txn_date` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `order_id` (`order_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `subscription_paytmpaymentstatus`
--

LOCK TABLES `subscription_paytmpaymentstatus` WRITE;
/*!40000 ALTER TABLE `subscription_paytmpaymentstatus` DISABLE KEYS */;
/*!40000 ALTER TABLE `subscription_paytmpaymentstatus` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `subscription_plandetails`
--

DROP TABLE IF EXISTS `subscription_plandetails`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `subscription_plandetails` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `price` decimal(6,2) NOT NULL,
  `validity` int(11) NOT NULL,
  `description` longtext NOT NULL,
  `hi` int(11) NOT NULL,
  `hearts` int(11) NOT NULL,
  `likes` int(11) NOT NULL,
  `boosts` int(11) NOT NULL,
  `talktime` int(11) NOT NULL,
  `superlikes` int(11) NOT NULL,
  `wallet_percentage` double NOT NULL,
  `discount_percentage` double NOT NULL,
  `video_enabled` tinyint(1) NOT NULL,
  `audio_enabled` tinyint(1) NOT NULL,
  `sees_control` tinyint(1) NOT NULL,
  `interested_profile` tinyint(1) NOT NULL,
  `hide_ads` tinyint(1) NOT NULL,
  `profile_control` tinyint(1) NOT NULL,
  `stickers` tinyint(1) NOT NULL,
  `scrach_enable` tinyint(1) NOT NULL,
  `e_greetings_enable` tinyint(1) NOT NULL,
  `plan_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `subscription_plandet_plan_id_23b82c65_fk_subscript` (`plan_id`),
  CONSTRAINT `subscription_plandet_plan_id_23b82c65_fk_subscript` FOREIGN KEY (`plan_id`) REFERENCES `subscription_plans` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `subscription_plandetails`
--

LOCK TABLES `subscription_plandetails` WRITE;
/*!40000 ALTER TABLE `subscription_plandetails` DISABLE KEYS */;
INSERT INTO `subscription_plandetails` VALUES (1,500.00,3,'3month vailidity',0,0,0,0,0,0,0,0,1,0,1,0,0,1,1,0,0,1),(2,1000.00,6,'6 months validity',20,20,20,20,20,20,10,1,0,0,1,0,0,1,1,1,1,2);
/*!40000 ALTER TABLE `subscription_plandetails` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `subscription_planpurchedbyuser`
--

DROP TABLE IF EXISTS `subscription_planpurchedbyuser`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `subscription_planpurchedbyuser` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `plan_id` varchar(10) DEFAULT NULL,
  `plan_name` varchar(30) DEFAULT NULL,
  `accessories_id` varchar(10) DEFAULT NULL,
  `accessories_name` varchar(30) DEFAULT NULL,
  `paytm_txn_id` varchar(40) DEFAULT NULL,
  `order_id` varchar(30) NOT NULL,
  `paytm_amount` decimal(6,2) NOT NULL,
  `cashback_amount` decimal(6,2) NOT NULL,
  `wallet_amount` decimal(6,2) NOT NULL,
  `discount_amount` decimal(6,2) NOT NULL,
  `plan_price_amount` decimal(6,2) NOT NULL,
  `plan_purched_at` datetime(6) NOT NULL,
  `user_id` char(32) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `order_id` (`order_id`),
  KEY `subscription_planpur_user_id_7fe90600_fk_userprofi` (`user_id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `subscription_planpurchedbyuser`
--

LOCK TABLES `subscription_planpurchedbyuser` WRITE;
/*!40000 ALTER TABLE `subscription_planpurchedbyuser` DISABLE KEYS */;
INSERT INTO `subscription_planpurchedbyuser` VALUES (1,'1','Vip','1','2','234567','23',100.00,0.00,0.00,0.00,100.00,'2020-04-21 17:07:16.171265','0a6143508c3a4fa3be2247c11d42dd6f'),(2,'2','Plus','2','likes','234567sdfg','24',1000.00,0.00,0.00,0.00,100.00,'2020-04-24 18:04:58.156985','2c51705a43a342eb9d2a161f7e4dc8c3'),(3,'3','Super','23','super likes','234567sdfg3456','345',1000.00,0.00,0.00,0.00,1000.00,'2020-04-24 18:43:53.697298','e306ba1881a9446c8bcd2ea89c16069f');
/*!40000 ALTER TABLE `subscription_planpurchedbyuser` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `subscription_plans`
--

DROP TABLE IF EXISTS `subscription_plans`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `subscription_plans` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `plan_description` longtext,
  `is_active` tinyint(1) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `subscription_plans`
--

LOCK TABLES `subscription_plans` WRITE;
/*!40000 ALTER TABLE `subscription_plans` DISABLE KEYS */;
INSERT INTO `subscription_plans` VALUES (1,'Gold','gold plan',1,'2020-04-19 17:25:30.550605'),(2,'Plus','Plus plan having 20 likes heart etc',1,'2020-04-24 18:26:35.740002'),(3,'super likes plan','super likes plan',0,'2020-04-24 18:27:15.185431');
/*!40000 ALTER TABLE `subscription_plans` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `subscription_purchaserequest`
--

DROP TABLE IF EXISTS `subscription_purchaserequest`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `subscription_purchaserequest` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `plan_id` varchar(10) DEFAULT NULL,
  `plan_name` varchar(30) DEFAULT NULL,
  `accessories_id` varchar(10) DEFAULT NULL,
  `accessories_name` varchar(30) DEFAULT NULL,
  `order_id` varchar(30) NOT NULL,
  `paytm_amount` decimal(6,2) NOT NULL,
  `cashback_amount` decimal(6,2) NOT NULL,
  `wallet_amount` decimal(6,2) NOT NULL,
  `discount_amount` decimal(6,2) NOT NULL,
  `plan_price_amount` decimal(6,2) NOT NULL,
  `plan_request_at` datetime(6) NOT NULL,
  `user_id` char(32) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `order_id` (`order_id`),
  KEY `subscription_purchas_user_id_a3ad8999_fk_userprofi` (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `subscription_purchaserequest`
--

LOCK TABLES `subscription_purchaserequest` WRITE;
/*!40000 ALTER TABLE `subscription_purchaserequest` DISABLE KEYS */;
/*!40000 ALTER TABLE `subscription_purchaserequest` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `subscription_userdailydose`
--

DROP TABLE IF EXISTS `subscription_userdailydose`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `subscription_userdailydose` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `plan_name` varchar(50) DEFAULT NULL,
  `remaining_hi` int(11) NOT NULL,
  `remaining_likes` int(11) NOT NULL,
  `remaining_hearts` int(11) NOT NULL,
  `remaining_boosts` int(11) NOT NULL,
  `remaining_talktime` int(11) NOT NULL,
  `remaining_superlikes` int(11) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `is_expired` tinyint(1) NOT NULL,
  `plan_expire_at` datetime(6) DEFAULT NULL,
  `payment_token` varchar(60) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `plan_id` int(11) DEFAULT NULL,
  `user_id` char(32) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`),
  KEY `subscription_userdai_plan_id_d899c97a_fk_subscript` (`plan_id`),
  CONSTRAINT `subscription_userdai_plan_id_d899c97a_fk_subscript` FOREIGN KEY (`plan_id`) REFERENCES `subscription_plandetails` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `subscription_userdailydose`
--

LOCK TABLES `subscription_userdailydose` WRITE;
/*!40000 ALTER TABLE `subscription_userdailydose` DISABLE KEYS */;
INSERT INTO `subscription_userdailydose` VALUES (5,'Basic',5,100,5,5,5,5,1,0,'2020-04-26 17:30:19.048055','','2020-04-19 17:30:19.048449','2020-04-19 17:30:19.048464',1,'0a6143508c3a4fa3be2247c11d42dd6f'),(6,'Basic',5,100,5,5,5,5,1,0,'2020-04-26 18:53:07.265440','','2020-04-19 18:53:07.267524','2020-04-19 18:53:07.267569',1,'e306ba1881a9446c8bcd2ea89c16069f'),(7,'Basic',5,100,5,5,5,5,1,0,'2020-05-01 18:03:40.035827','','2020-04-24 18:03:40.037659','2020-04-24 18:03:40.037717',1,'2c51705a43a342eb9d2a161f7e4dc8c3');
/*!40000 ALTER TABLE `subscription_userdailydose` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `subscription_wallet`
--

DROP TABLE IF EXISTS `subscription_wallet`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `subscription_wallet` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `wallet_amount` decimal(6,2) NOT NULL,
  `referral_amount` decimal(6,2) NOT NULL,
  `last_updated` datetime(6) NOT NULL,
  `user_id` char(32) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `subscription_wallet`
--

LOCK TABLES `subscription_wallet` WRITE;
/*!40000 ALTER TABLE `subscription_wallet` DISABLE KEYS */;
INSERT INTO `subscription_wallet` VALUES (1,1000.00,0.00,'2020-04-19 17:30:19.049346','0a6143508c3a4fa3be2247c11d42dd6f'),(2,1000.00,0.00,'2020-04-19 18:53:07.269349','e306ba1881a9446c8bcd2ea89c16069f'),(3,1000.00,0.00,'2020-04-24 18:03:40.216290','2c51705a43a342eb9d2a161f7e4dc8c3');
/*!40000 ALTER TABLE `subscription_wallet` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `userprofile_anonymous`
--

DROP TABLE IF EXISTS `userprofile_anonymous`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `userprofile_anonymous` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `phone_no` varchar(12) DEFAULT NULL,
  `country_code` varchar(4) DEFAULT NULL,
  `email` varchar(254) DEFAULT NULL,
  `auth_token` varchar(100) NOT NULL,
  `app_version` double NOT NULL,
  `device_id` varchar(30) NOT NULL,
  `device_type` varchar(10) DEFAULT NULL,
  `fcm_token` varchar(200) NOT NULL,
  `create_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `userprofile_anonymous`
--

LOCK TABLES `userprofile_anonymous` WRITE;
/*!40000 ALTER TABLE `userprofile_anonymous` DISABLE KEYS */;
INSERT INTO `userprofile_anonymous` VALUES (1,'8744865366','+91','abhishesh@cheatingnot.com','124',1,'123','234','3','2020-04-19 17:28:09.527606','2020-04-19 17:28:09.527646');
/*!40000 ALTER TABLE `userprofile_anonymous` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `userprofile_block`
--

DROP TABLE IF EXISTS `userprofile_block`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `userprofile_block` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `blocked_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `blocked_id` char(32) NOT NULL,
  `blocked_by_id` char(32) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `userprofile_block_blocked_id_a314d254_fk_userprofile_users_id` (`blocked_id`),
  KEY `userprofile_block_blocked_by_id_07c31987_fk_userprofile_users_id` (`blocked_by_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `userprofile_block`
--

LOCK TABLES `userprofile_block` WRITE;
/*!40000 ALTER TABLE `userprofile_block` DISABLE KEYS */;
/*!40000 ALTER TABLE `userprofile_block` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `userprofile_discount`
--

DROP TABLE IF EXISTS `userprofile_discount`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `userprofile_discount` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `cashback_percentage` decimal(6,2) NOT NULL,
  `referral_amount` decimal(6,2) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `userprofile_discount`
--

LOCK TABLES `userprofile_discount` WRITE;
/*!40000 ALTER TABLE `userprofile_discount` DISABLE KEYS */;
INSERT INTO `userprofile_discount` VALUES (1,500.00,20.00);
/*!40000 ALTER TABLE `userprofile_discount` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `userprofile_heart`
--

DROP TABLE IF EXISTS `userprofile_heart`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `userprofile_heart` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `heart_count` int(11) NOT NULL,
  `create_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `heart_to_id` char(32) NOT NULL,
  `user_id` char(32) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `userprofile_heart_heart_to_id_ef3a093d_fk_userprofile_users_id` (`heart_to_id`),
  KEY `userprofile_heart_user_id_96ff4971_fk_userprofile_users_id` (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `userprofile_heart`
--

LOCK TABLES `userprofile_heart` WRITE;
/*!40000 ALTER TABLE `userprofile_heart` DISABLE KEYS */;
/*!40000 ALTER TABLE `userprofile_heart` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `userprofile_height`
--

DROP TABLE IF EXISTS `userprofile_height`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `userprofile_height` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `height` varchar(20) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `userprofile_height`
--

LOCK TABLES `userprofile_height` WRITE;
/*!40000 ALTER TABLE `userprofile_height` DISABLE KEYS */;
INSERT INTO `userprofile_height` VALUES (1,'174','2020-04-19 17:02:31.908735','2020-04-19 17:02:31.908796');
/*!40000 ALTER TABLE `userprofile_height` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `userprofile_hi`
--

DROP TABLE IF EXISTS `userprofile_hi`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `userprofile_hi` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `hi_count` int(11) NOT NULL,
  `create_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `hi_to_id` char(32) NOT NULL,
  `user_id` char(32) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `userprofile_hi_hi_to_id_9d44974c_fk_userprofile_users_id` (`hi_to_id`),
  KEY `userprofile_hi_user_id_5464c65c_fk_userprofile_users_id` (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `userprofile_hi`
--

LOCK TABLES `userprofile_hi` WRITE;
/*!40000 ALTER TABLE `userprofile_hi` DISABLE KEYS */;
/*!40000 ALTER TABLE `userprofile_hi` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `userprofile_hobbies`
--

DROP TABLE IF EXISTS `userprofile_hobbies`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `userprofile_hobbies` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `hobbies` varchar(200) DEFAULT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `userprofile_hobbies`
--

LOCK TABLES `userprofile_hobbies` WRITE;
/*!40000 ALTER TABLE `userprofile_hobbies` DISABLE KEYS */;
INSERT INTO `userprofile_hobbies` VALUES (1,'coding','2020-04-19 17:02:44.157221','2020-04-19 17:02:44.157274');
/*!40000 ALTER TABLE `userprofile_hobbies` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `userprofile_like`
--

DROP TABLE IF EXISTS `userprofile_like`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `userprofile_like` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `create_at` datetime(6) NOT NULL,
  `liked_id` char(32) NOT NULL,
  `user_id` char(32) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `userprofile_like_liked_id_d5079f1e_fk_userprofile_users_id` (`liked_id`),
  KEY `userprofile_like_user_id_fee31b32_fk_userprofile_users_id` (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `userprofile_like`
--

LOCK TABLES `userprofile_like` WRITE;
/*!40000 ALTER TABLE `userprofile_like` DISABLE KEYS */;
/*!40000 ALTER TABLE `userprofile_like` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `userprofile_match`
--

DROP TABLE IF EXISTS `userprofile_match`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `userprofile_match` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `create_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `user_id` char(32) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `userprofile_match_user_id_72620e73_fk_userprofile_users_id` (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `userprofile_match`
--

LOCK TABLES `userprofile_match` WRITE;
/*!40000 ALTER TABLE `userprofile_match` DISABLE KEYS */;
/*!40000 ALTER TABLE `userprofile_match` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `userprofile_match_matches`
--

DROP TABLE IF EXISTS `userprofile_match_matches`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `userprofile_match_matches` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `match_id` int(11) NOT NULL,
  `users_id` char(32) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `userprofile_match_matches_match_id_users_id_a06df9f6_uniq` (`match_id`,`users_id`),
  KEY `userprofile_match_ma_users_id_577945e7_fk_userprofi` (`users_id`),
  CONSTRAINT `userprofile_match_ma_match_id_db944952_fk_userprofi` FOREIGN KEY (`match_id`) REFERENCES `userprofile_match` (`id`),
  CONSTRAINT `userprofile_match_ma_users_id_577945e7_fk_userprofi` FOREIGN KEY (`users_id`) REFERENCES `userprofile_users` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `userprofile_match_matches`
--

LOCK TABLES `userprofile_match_matches` WRITE;
/*!40000 ALTER TABLE `userprofile_match_matches` DISABLE KEYS */;
/*!40000 ALTER TABLE `userprofile_match_matches` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `userprofile_nopes`
--

DROP TABLE IF EXISTS `userprofile_nopes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `userprofile_nopes` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `create_at` datetime(6) NOT NULL,
  `nope_id` char(32) NOT NULL,
  `user_id` char(32) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `userprofile_nopes_nope_id_0d88e96c_fk_userprofile_users_id` (`nope_id`),
  KEY `userprofile_nopes_user_id_773e4a1e_fk_userprofile_users_id` (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `userprofile_nopes`
--

LOCK TABLES `userprofile_nopes` WRITE;
/*!40000 ALTER TABLE `userprofile_nopes` DISABLE KEYS */;
/*!40000 ALTER TABLE `userprofile_nopes` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `userprofile_occupation`
--

DROP TABLE IF EXISTS `userprofile_occupation`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `userprofile_occupation` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `occupation` varchar(30) NOT NULL,
  `create_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `userprofile_occupation`
--

LOCK TABLES `userprofile_occupation` WRITE;
/*!40000 ALTER TABLE `userprofile_occupation` DISABLE KEYS */;
INSERT INTO `userprofile_occupation` VALUES (1,'Love guru','2020-04-19 17:02:18.237966','2020-04-19 17:02:18.238003');
/*!40000 ALTER TABLE `userprofile_occupation` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `userprofile_otp`
--

DROP TABLE IF EXISTS `userprofile_otp`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `userprofile_otp` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `otp` varchar(10) DEFAULT NULL,
  `otp_expire_at` datetime(6) DEFAULT NULL,
  `create_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`),
  CONSTRAINT `userprofile_otp_user_id_94a5f34a_fk_userprofile_anonymous_id` FOREIGN KEY (`user_id`) REFERENCES `userprofile_anonymous` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `userprofile_otp`
--

LOCK TABLES `userprofile_otp` WRITE;
/*!40000 ALTER TABLE `userprofile_otp` DISABLE KEYS */;
/*!40000 ALTER TABLE `userprofile_otp` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `userprofile_preferences`
--

DROP TABLE IF EXISTS `userprofile_preferences`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `userprofile_preferences` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `gender` varchar(10) DEFAULT NULL,
  `age_from` int(11) DEFAULT NULL,
  `age_to` int(11) DEFAULT NULL,
  `distance_min` varchar(10) DEFAULT NULL,
  `distance_max` varchar(10) DEFAULT NULL,
  `distance_no_limit` tinyint(1) NOT NULL,
  `preferences_update_percentage` int(11) NOT NULL,
  `age_no_limit` tinyint(1) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `user_id` char(32) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `userprofile_preferences`
--

LOCK TABLES `userprofile_preferences` WRITE;
/*!40000 ALTER TABLE `userprofile_preferences` DISABLE KEYS */;
INSERT INTO `userprofile_preferences` VALUES (5,'Both',18,50,NULL,'50',0,0,0,'2020-04-19 17:30:19.044801','2020-04-24 21:07:53.479225','0a6143508c3a4fa3be2247c11d42dd6f'),(6,'Both',18,50,NULL,'50',0,0,0,'2020-04-19 18:53:07.054296','2020-04-28 18:37:50.287616','e306ba1881a9446c8bcd2ea89c16069f'),(7,'Both',18,50,NULL,'50',0,0,0,'2020-04-24 18:03:39.937451','2020-04-24 18:03:39.940389','2c51705a43a342eb9d2a161f7e4dc8c3');
/*!40000 ALTER TABLE `userprofile_preferences` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `userprofile_pushnotificationmsg`
--

DROP TABLE IF EXISTS `userprofile_pushnotificationmsg`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `userprofile_pushnotificationmsg` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `notification_type` int(11) NOT NULL,
  `msg_title` varchar(60) NOT NULL,
  `msg_body` longtext NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `userprofile_pushnotificationmsg`
--

LOCK TABLES `userprofile_pushnotificationmsg` WRITE;
/*!40000 ALTER TABLE `userprofile_pushnotificationmsg` DISABLE KEYS */;
INSERT INTO `userprofile_pushnotificationmsg` VALUES (1,1,'hey','hey plz purchage  hey mssg','2020-04-19 17:31:11.054287');
/*!40000 ALTER TABLE `userprofile_pushnotificationmsg` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `userprofile_reports`
--

DROP TABLE IF EXISTS `userprofile_reports`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `userprofile_reports` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `reason` varchar(256) NOT NULL,
  `report_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `reported_id` char(32) NOT NULL,
  `reported_by_id` char(32) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `userprofile_reports_reported_id_36b90adc_fk_userprofile_users_id` (`reported_id`),
  KEY `userprofile_reports_reported_by_id_8353e81b_fk_userprofi` (`reported_by_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `userprofile_reports`
--

LOCK TABLES `userprofile_reports` WRITE;
/*!40000 ALTER TABLE `userprofile_reports` DISABLE KEYS */;
/*!40000 ALTER TABLE `userprofile_reports` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `userprofile_superlike`
--

DROP TABLE IF EXISTS `userprofile_superlike`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `userprofile_superlike` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `superlike_count` int(11) NOT NULL,
  `create_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `superliked_id` char(32) NOT NULL,
  `user_id` char(32) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `userprofile_superlik_superliked_id_9c872901_fk_userprofi` (`superliked_id`),
  KEY `userprofile_superlike_user_id_2d1ce5d7_fk_userprofile_users_id` (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `userprofile_superlike`
--

LOCK TABLES `userprofile_superlike` WRITE;
/*!40000 ALTER TABLE `userprofile_superlike` DISABLE KEYS */;
/*!40000 ALTER TABLE `userprofile_superlike` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `userprofile_userauth`
--

DROP TABLE IF EXISTS `userprofile_userauth`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `userprofile_userauth` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `auth_token` varchar(100) NOT NULL,
  `session_id` varchar(100) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `user_id` char(32) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `userprofile_userauth`
--

LOCK TABLES `userprofile_userauth` WRITE;
/*!40000 ALTER TABLE `userprofile_userauth` DISABLE KEYS */;
/*!40000 ALTER TABLE `userprofile_userauth` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `userprofile_userprivacy`
--

DROP TABLE IF EXISTS `userprofile_userprivacy`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `userprofile_userprivacy` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `age` tinyint(1) NOT NULL,
  `showme` tinyint(1) NOT NULL,
  `aboutme` tinyint(1) NOT NULL,
  `sharephotos` tinyint(1) NOT NULL,
  `occupation` tinyint(1) NOT NULL,
  `create_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `user_id` char(32) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `userprofile_userprivacy`
--

LOCK TABLES `userprofile_userprivacy` WRITE;
/*!40000 ALTER TABLE `userprofile_userprivacy` DISABLE KEYS */;
INSERT INTO `userprofile_userprivacy` VALUES (5,0,0,0,0,0,'2020-04-19 17:30:19.046633','2020-04-24 21:07:53.544777','0a6143508c3a4fa3be2247c11d42dd6f'),(6,0,0,0,0,0,'2020-04-19 18:53:07.261977','2020-04-28 18:37:50.418721','e306ba1881a9446c8bcd2ea89c16069f'),(7,0,0,0,0,0,'2020-04-24 18:03:39.943189','2020-04-24 18:03:40.033315','2c51705a43a342eb9d2a161f7e4dc8c3');
/*!40000 ALTER TABLE `userprofile_userprivacy` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `userprofile_userprofileimages`
--

DROP TABLE IF EXISTS `userprofile_userprofileimages`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `userprofile_userprofileimages` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `profilepics` varchar(100) NOT NULL,
  `is_profile` tinyint(1) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `user_id` char(32) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `userprofile_userprof_user_id_d8226bcc_fk_userprofi` (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `userprofile_userprofileimages`
--

LOCK TABLES `userprofile_userprofileimages` WRITE;
/*!40000 ALTER TABLE `userprofile_userprofileimages` DISABLE KEYS */;
/*!40000 ALTER TABLE `userprofile_userprofileimages` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `userprofile_userprofilevideos`
--

DROP TABLE IF EXISTS `userprofile_userprofilevideos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `userprofile_userprofilevideos` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `profilevideos` varchar(100) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `user_id` char(32) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `userprofile_userprof_user_id_cf8315b0_fk_userprofi` (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `userprofile_userprofilevideos`
--

LOCK TABLES `userprofile_userprofilevideos` WRITE;
/*!40000 ALTER TABLE `userprofile_userprofilevideos` DISABLE KEYS */;
/*!40000 ALTER TABLE `userprofile_userprofilevideos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `userprofile_users`
--

DROP TABLE IF EXISTS `userprofile_users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `userprofile_users` (
  `id` char(32) NOT NULL,
  `name` varchar(30) NOT NULL,
  `email` varchar(254) NOT NULL,
  `phone_no` varchar(15) NOT NULL,
  `country_code` varchar(4) DEFAULT NULL,
  `dob` date NOT NULL,
  `gender` varchar(6) NOT NULL,
  `body_type` varchar(10) NOT NULL,
  `about_me` varchar(100) NOT NULL,
  `user_type` varchar(20) NOT NULL,
  `occupation` varchar(30) NOT NULL,
  `height` varchar(20) NOT NULL,
  `weight` varchar(10) NOT NULL,
  `latitude` double NOT NULL,
  `longitude` double NOT NULL,
  `distance` double NOT NULL,
  `referral_code` varchar(10) NOT NULL,
  `priority` int(11) NOT NULL,
  `profile_verified` tinyint(1) NOT NULL,
  `active` tinyint(1) NOT NULL,
  `staff` tinyint(1) NOT NULL,
  `app_version` double DEFAULT NULL,
  `device_id` varchar(30) DEFAULT NULL,
  `device_type` varchar(10) DEFAULT NULL,
  `fcm_token` varchar(200) DEFAULT NULL,
  `profile_complete_percentage` int(11) NOT NULL,
  `profile_update_percentage` int(11) NOT NULL,
  `last_login` datetime(6) NOT NULL,
  `create_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `userprofile_users`
--

LOCK TABLES `userprofile_users` WRITE;
/*!40000 ALTER TABLE `userprofile_users` DISABLE KEYS */;
INSERT INTO `userprofile_users` VALUES ('0a6143508c3a4fa3be2247c11d42dd6f','abhishesh mishra','abhishesh@cheatingnot.com','8744865366','+91','1996-04-19','male','average','I m Dating King','xyz','Love guru','174','67',0,0,0,'1',1,1,1,1,1,'123','234','3',5,3,'2020-04-24 21:07:53.340189','2020-04-19 17:30:19.043897','2020-04-24 21:07:53.340213'),('2c51705a43a342eb9d2a161f7e4dc8c3','Shyam','shyam@cheatingn.com','9876543212','+91','1970-04-24','male','average','I m Dating Raja','xyz','Love Advisior','172','72',0,0,0,'1234567567',0,0,1,0,3,'1234567','234','3fghjk',9,5,'2020-04-24 18:03:39.935534','2020-04-24 18:03:39.935595','2020-04-24 18:03:39.935619'),('e306ba1881a9446c8bcd2ea89c16069f','abhishesh','abhishesh@jiyo.com','0998765456','+91','1996-04-19','male','average','I m Dating King','xyz','Love guru','174','67',4,0,0,'1234567',0,1,0,1,3,'12345678','2345678','sdfgh34567890',10,7,'2020-04-28 18:37:50.166949','2020-04-19 18:53:07.053114','2020-04-28 18:37:50.166971');
/*!40000 ALTER TABLE `userprofile_users` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `userprofile_usersnotification`
--

DROP TABLE IF EXISTS `userprofile_usersnotification`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `userprofile_usersnotification` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `img` varchar(200) DEFAULT NULL,
  `action` varchar(200) DEFAULT NULL,
  `msg_title` varchar(200) DEFAULT NULL,
  `msg_body` varchar(200) DEFAULT NULL,
  `create_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `friend_user_id` char(32) NOT NULL,
  `user_id` char(32) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `userprofile_usersnot_friend_user_id_b7491480_fk_userprofi` (`friend_user_id`),
  KEY `userprofile_usersnot_user_id_df30596d_fk_userprofi` (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `userprofile_usersnotification`
--

LOCK TABLES `userprofile_usersnotification` WRITE;
/*!40000 ALTER TABLE `userprofile_usersnotification` DISABLE KEYS */;
/*!40000 ALTER TABLE `userprofile_usersnotification` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `userprofile_weight`
--

DROP TABLE IF EXISTS `userprofile_weight`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `userprofile_weight` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `weight` varchar(20) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `userprofile_weight`
--

LOCK TABLES `userprofile_weight` WRITE;
/*!40000 ALTER TABLE `userprofile_weight` DISABLE KEYS */;
INSERT INTO `userprofile_weight` VALUES (1,'67','2020-04-19 17:03:01.618059','2020-04-19 17:03:01.618127');
/*!40000 ALTER TABLE `userprofile_weight` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-05-01 10:50:07
