-- Drop and create `challenges` table
DROP TABLE IF EXISTS `challenges`;
CREATE TABLE IF NOT EXISTS `challenges` (
  `id` int(255) NOT NULL AUTO_INCREMENT,
  `rules` longtext NOT NULL,
  `startdate` datetime NOT NULL,
  `added_by` varchar(255) NOT NULL,
  `timestamp` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `status` varchar(255) NOT NULL,
  `enddate` datetime NOT NULL,
  `players` varchar(255) NOT NULL,
  `plays` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- Drop and create `challenge_registration` table
DROP TABLE IF EXISTS `challenge_registration`;
CREATE TABLE IF NOT EXISTS `challenge_registration` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `challengeID` varchar(255) NOT NULL,
  `userID` varchar(255) NOT NULL,
  `timestamp` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `status` varchar(255) NOT NULL,
  `score` varchar(255) NOT NULL,
  `starttime` varchar(255) NOT NULL,
  `endtime` varchar(255) NOT NULL,
  `end_date` varchar(255) NOT NULL,
  `win_status` varchar(255) NOT NULL,
  `duel_id` varchar(255) NOT NULL,
  `my_cards` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- Drop and create `duel` table
DROP TABLE IF EXISTS `duel`;
CREATE TABLE IF NOT EXISTS `duel` (
  `id` int(255) NOT NULL AUTO_INCREMENT,
  `challenge_id` varchar(255) NOT NULL,
  `player_one` varchar(255) NOT NULL,
  `player_two` varchar(255) NOT NULL,
  `status` varchar(255) NOT NULL,
  `winner` varchar(255) NOT NULL,
  `end_date` datetime(6) NOT NULL,
  `start_date` datetime(6) NOT NULL,
  `player_one_ready` varchar(255) NOT NULL,
  `player_two_ready` varchar(255) NOT NULL,
  `player_one_complete` varchar(255) NOT NULL,
  `player_two_complete` varchar(255) NOT NULL,
  `play_type` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=1271 DEFAULT CHARSET=latin1;

-- Drop and create `kadi_plays` table
DROP TABLE IF EXISTS `kadi_plays`;
CREATE TABLE IF NOT EXISTS `kadi_plays` (
  `id` int(255) NOT NULL AUTO_INCREMENT,
  `players` varchar(255) NOT NULL,
  `next_to_play` varchar(255) NOT NULL,
  `prev_to_play` varchar(255) NOT NULL,
  `plays` longtext NOT NULL,
  `winner` varchar(255) NOT NULL,
  `play_direction` varchar(255) NOT NULL,
  `play_status` varchar(255) NOT NULL,
  `cardless_status` varchar(255) NOT NULL,
  `kadi_status` varchar(255) NOT NULL,
  `last_change_time` varchar(255) NOT NULL,
  `last_play` longtext NOT NULL,
  `duel_id` varchar(255) NOT NULL,
  `playing` varchar(255) NOT NULL,
  `ready_cards` varchar(255) NOT NULL,
  `players_ready` varchar(255) NOT NULL DEFAULT '0',
  `game_end` varchar(255) NOT NULL DEFAULT 'false',
  `play_type` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=448 DEFAULT CHARSET=latin1;

-- Drop and create `users` table
DROP TABLE IF EXISTS `users`;
CREATE TABLE IF NOT EXISTS `users` (
  `userID` int(11) NOT NULL AUTO_INCREMENT,
  `email` varchar(250) NOT NULL,
  `password` varchar(60) NOT NULL,
  `full_name` varchar(200) NOT NULL,
  PRIMARY KEY (`userID`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

