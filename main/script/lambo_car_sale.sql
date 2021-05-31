/*
 Navicat Premium Data Transfer

 Source Server         : localhost
 Source Server Type    : MySQL
 Source Server Version : 50712
 Source Host           : localhost:3306
 Source Schema         : lambo_car_sale

 Target Server Type    : MySQL
 Target Server Version : 50712
 File Encoding         : 65001

 Date: 26/05/2021 22:22:33
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for cars
-- ----------------------------
DROP TABLE IF EXISTS `cars`;
CREATE TABLE `cars`  (
  `car_id` int(11) NOT NULL AUTO_INCREMENT,
  `car_name` varchar(150) CHARACTER SET latin1 COLLATE latin1_swedish_ci NOT NULL,
  `car_brand` varchar(150) CHARACTER SET latin1 COLLATE latin1_swedish_ci NOT NULL,
  `color` varchar(50) CHARACTER SET latin1 COLLATE latin1_swedish_ci NOT NULL,
  `speed` int(3) NOT NULL,
  `price` int(20) NOT NULL,
  PRIMARY KEY (`car_id`) USING BTREE
) ENGINE = MyISAM AUTO_INCREMENT = 6 CHARACTER SET = latin1 COLLATE = latin1_swedish_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of cars
-- ----------------------------
INSERT INTO `cars` VALUES (1, 'Toyota corolla', 'Toyota', 'red', 100, 8050000);
INSERT INTO `cars` VALUES (2, 'Lamborghini Gallardo', 'Lamborghini', 'black', 240, 45000000);
INSERT INTO `cars` VALUES (3, 'Toyota Axio', 'Toyota', 'black', 90, 5500000);
INSERT INTO `cars` VALUES (4, 'Maruti Suzuki', 'Maruti', 'green', 60, 1600000);
INSERT INTO `cars` VALUES (5, 'Honda Swift', 'Honda', 'black', 60, 3500000);

-- ----------------------------
-- Table structure for contact_details
-- ----------------------------
DROP TABLE IF EXISTS `contact_details`;
CREATE TABLE `contact_details`  (
  `c_id` int(11) NOT NULL AUTO_INCREMENT,
  `c_address` varchar(250) CHARACTER SET latin1 COLLATE latin1_swedish_ci NOT NULL,
  `c_number` varchar(50) CHARACTER SET latin1 COLLATE latin1_swedish_ci NOT NULL,
  `c_email` varchar(100) CHARACTER SET latin1 COLLATE latin1_swedish_ci NOT NULL,
  PRIMARY KEY (`c_id`) USING BTREE
) ENGINE = MyISAM AUTO_INCREMENT = 2 CHARACTER SET = latin1 COLLATE = latin1_swedish_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of contact_details
-- ----------------------------
INSERT INTO `contact_details` VALUES (1, 'Lambo Colombo 4 address', '0770000001', 'Lambo@email.com');

SET FOREIGN_KEY_CHECKS = 1;
