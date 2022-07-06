-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Oct 31, 2020 at 10:21 AM
-- Server version: 10.4.11-MariaDB
-- PHP Version: 7.4.5

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `webproazad`
--

-- --------------------------------------------------------

--
-- Table structure for table `admin`
--

CREATE TABLE `admin` (
  `id` int(11) NOT NULL,
  `usr_name` varchar(55) NOT NULL,
  `pass` varchar(55) NOT NULL,
  `status` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `admin`
--

INSERT INTO `admin` (`id`, `usr_name`, `pass`, `status`) VALUES
(6, 'admin', 'c97fb691224b7e6989d8788fb8f70f84', 1);

-- --------------------------------------------------------

--
-- Table structure for table `administrator`
--

CREATE TABLE `administrator` (
  `id` int(11) NOT NULL,
  `fname` varchar(55) NOT NULL,
  `lname` varchar(55) NOT NULL,
  `title` varchar(255) NOT NULL,
  `shrt_desc` text NOT NULL,
  `long_desc` text NOT NULL,
  `position` varchar(55) NOT NULL,
  `email` varchar(55) NOT NULL,
  `address` varchar(400) NOT NULL,
  `profile_img` varchar(255) NOT NULL,
  `phn` varchar(11) NOT NULL,
  `interest` varchar(250) NOT NULL,
  `birthday` date NOT NULL,
  `website` varchar(255) NOT NULL,
  `web_name` varchar(255) NOT NULL,
  `linkedin` varchar(255) NOT NULL,
  `facebook` varchar(255) NOT NULL,
  `youtube` varchar(255) NOT NULL,
  `behance` varchar(255) NOT NULL,
  `resume` varchar(255) NOT NULL,
  `skype` varchar(255) NOT NULL,
  `twitter` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `administrator`
--

INSERT INTO `administrator` (`id`, `fname`, `lname`, `title`, `shrt_desc`, `long_desc`, `position`, `email`, `address`, `profile_img`, `phn`, `interest`, `birthday`, `website`, `web_name`, `linkedin`, `facebook`, `youtube`, `behance`, `resume`, `skype`, `twitter`) VALUES
(1, 'Azadul', 'Islam', 'Web', 'I am Azadul islam. I have 3+ years of experience in Web Development. You will get 100% full support of work assured until you are fully satisfied. I am highly experienced in 1. HTML5, CSS3 ,Sass , JavaScript &amp; Jquery, Bootstrap, wordpress customization, PHP, OOP and MySql (Database)  2. any psd/photo to html, css, bootstrap, demo import  3. demo import and customize with client requirement, page build with Elementor, SEO, login, registration 4. Graphic Design: A. Logo Design C. Favicon Design D. Adobe Illustrator E. Adobe Photoshop 5. Admin Panel, Controler Others', '<div>Hey,</div>\r\n<p>I am Azadul islam. I have 3+ years of experience in Webdesign and Web Development.</p>\r\n<p>You will get&nbsp;<strong><a title=\"Fiverr\" href=\"https://www.fiverr.com/mjhm12\" target=\"_blank\">100% full support</a></strong>&nbsp;of work assured until you are fully satisfied&nbsp;</p>\r\n<h2>My key skills are:</h2>\r\n<ul>\r\n<li>HTML5</li>\r\n<li>CSS3</li>\r\n<li>JavaScript&nbsp;</li>\r\n<li>Jquery</li>\r\n<li>Bootstrap</li>\r\n<li>SASS (SCSS)</li>\r\n<li>PHP</li>\r\n<li>OOP, PDO</li>\r\n<li>MySql</li>\r\n<li>Any sketch&nbsp;or PSD to HTML</li>\r\n<li>Demo import WordPress</li>\r\n<li>PHP Website Installation</li>\r\n<li>User panel with PHP, OOP, Mysql</li>\r\n<li>Admin Panel with PHP, OOP, Mysql</li>\r\n<li>Controller with PHP, OOP, Mysql</li>\r\n</ul>', 'Administrator', 'azadkh92558@gmail.com', 'Halsha (6400), Natore, Rajshahi, Dhaka', 'profile-200916061218.jpg', '01723026191', 'Coding, typing, Public speaking, Bike riding', '2012-03-14', 'https://webproazad.com', 'Web Pro Azad', 'https://www.linkedin.com/in/azadul-islam-78b8781b1/', 'https://web.facebook.com/profile.php?id=100056505368575', '', '', '', '', 'https://twitter.com/AzadKh10');

-- --------------------------------------------------------

--
-- Table structure for table `blog`
--

CREATE TABLE `blog` (
  `id` int(11) NOT NULL,
  `title` varchar(255) NOT NULL,
  `slg` varchar(255) NOT NULL,
  `image` varchar(255) NOT NULL,
  `category` tinyint(4) NOT NULL,
  `blg_dsc` text NOT NULL,
  `user` varchar(50) NOT NULL,
  `time` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `category`
--

CREATE TABLE `category` (
  `id` int(11) NOT NULL,
  `name` varchar(55) NOT NULL,
  `type` tinyint(4) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `category`
--

INSERT INTO `category` (`id`, `name`, `type`) VALUES
(2, 'Audio', 2),
(6, 'Video', 1);

-- --------------------------------------------------------

--
-- Table structure for table `gallery`
--

CREATE TABLE `gallery` (
  `id` int(11) NOT NULL,
  `gal_img` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `status` tinyint(4) NOT NULL,
  `time` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `gallery`
--

INSERT INTO `gallery` (`id`, `gal_img`, `name`, `status`, `time`) VALUES
(6, 'gallery-200916072539.jpg', 'gallery-200916072539', 1, '2020-09-16 17:20:28');

-- --------------------------------------------------------

--
-- Table structure for table `images`
--

CREATE TABLE `images` (
  `id` int(11) NOT NULL,
  `home_bg` varchar(225) NOT NULL,
  `logo_img` varchar(255) NOT NULL,
  `fav_icon` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `images`
--

INSERT INTO `images` (`id`, `home_bg`, `logo_img`, `fav_icon`) VALUES
(1, 'home-bg-20200913051006.jpeg', 'logo.png', 'icon-20200916070522.png');

-- --------------------------------------------------------

--
-- Table structure for table `portfolio`
--

CREATE TABLE `portfolio` (
  `id` int(11) NOT NULL,
  `title` varchar(255) NOT NULL,
  `port_desc` text NOT NULL,
  `port_img` varchar(55) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `portfolio`
--

INSERT INTO `portfolio` (`id`, `title`, `port_desc`, `port_img`) VALUES
(3, 'Full Admin panel', 'Full Admin panel', 'portfolio-200911065735.png'),
(4, 'This is title', 'adfasfd', 'portfolio-200917114549.png');

-- --------------------------------------------------------

--
-- Table structure for table `resume`
--

CREATE TABLE `resume` (
  `id` int(11) NOT NULL,
  `clnt` int(11) NOT NULL,
  `project` int(11) NOT NULL,
  `review` int(11) NOT NULL,
  `runing_pro` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `resume`
--

INSERT INTO `resume` (`id`, `clnt`, `project`, `review`, `runing_pro`) VALUES
(1, 12, 11, 12, 15);

-- --------------------------------------------------------

--
-- Table structure for table `review`
--

CREATE TABLE `review` (
  `id` int(11) NOT NULL,
  `clnt_name` varchar(55) NOT NULL,
  `clnt_cmnt` text NOT NULL,
  `clnt_cntry` varchar(55) NOT NULL,
  `clnt_rting` int(11) NOT NULL,
  `clnt_img` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `review`
--

INSERT INTO `review` (`id`, `clnt_name`, `clnt_cmnt`, `clnt_cntry`, `clnt_rting`, `clnt_img`) VALUES
(9, 'Azad', 'Awesome developer! I recommend because he is very professional, provide ongoing updates. Excellent work.', 'Bangladesh', 1, 'client-profile-200902054519.jpg'),
(10, 'Azad', 'Awesome developer! I recommend because he is very professional, provide ongoing updates. Excellent work.', 'Bangladesh', 1, 'client-profile-200902054636.jpg');

-- --------------------------------------------------------

--
-- Table structure for table `services`
--

CREATE TABLE `services` (
  `id` int(11) NOT NULL,
  `name` varchar(55) NOT NULL,
  `srv_desc` text NOT NULL,
  `image` varchar(55) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `services`
--

INSERT INTO `services` (`id`, `name`, `srv_desc`, `image`) VALUES
(6, 'Graphic Design', 'I will make all responsive designs. I know all clients love responsive design. my all work Responsive Design. As a developer we need to complete Complete Responsive design :)', 'service-200910064648.png'),
(7, 'It Support', 'I have experience in the Sector works. I know it is one going work. I have so many clients in It Sector work. All people love my work.', 'service-200910065634.png'),
(8, 'Responsive design', 'I will make all responsive designs. I know all clients love responsive design. my all work Responsive Design. As a developer we need to complete Complete Responsive design :)', 'service-200910065941.png'),
(9, 'Web Design', 'I am working with web design in the last 3 years. Now I have so much experience and I have completed so much design. I have so many clients to work with web design.', 'service-200910070748.png');

-- --------------------------------------------------------

--
-- Table structure for table `skille`
--

CREATE TABLE `skille` (
  `id` int(11) NOT NULL,
  `skl_name` varchar(55) NOT NULL,
  `skl_prcnt` varchar(55) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `skille`
--

INSERT INTO `skille` (`id`, `skl_name`, `skl_prcnt`) VALUES
(5, 'HMTL', '25');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `admin`
--
ALTER TABLE `admin`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `administrator`
--
ALTER TABLE `administrator`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `email` (`email`);

--
-- Indexes for table `blog`
--
ALTER TABLE `blog`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `category`
--
ALTER TABLE `category`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `gallery`
--
ALTER TABLE `gallery`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `images`
--
ALTER TABLE `images`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `portfolio`
--
ALTER TABLE `portfolio`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `resume`
--
ALTER TABLE `resume`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `review`
--
ALTER TABLE `review`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `services`
--
ALTER TABLE `services`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indexes for table `skille`
--
ALTER TABLE `skille`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `skl_name` (`skl_name`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `admin`
--
ALTER TABLE `admin`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `administrator`
--
ALTER TABLE `administrator`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `blog`
--
ALTER TABLE `blog`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `category`
--
ALTER TABLE `category`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `gallery`
--
ALTER TABLE `gallery`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `images`
--
ALTER TABLE `images`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `portfolio`
--
ALTER TABLE `portfolio`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `resume`
--
ALTER TABLE `resume`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `review`
--
ALTER TABLE `review`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT for table `services`
--
ALTER TABLE `services`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT for table `skille`
--
ALTER TABLE `skille`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
