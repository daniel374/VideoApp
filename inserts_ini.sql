SELECT * FROM appinit.users;

insert into appinit.users (name_usr, email_usr) values ("daniel", "dani374@hotmail.com");

--
SELECT * FROM appinit.videos;

INSERT INTO `appinit`.`videos` (`name_vd`, `date_vd`, `url_vd`, `id_autor_vd`) VALUES ('3 AUTOS de LUJO USADOS MUY BARATOS', now(), './static/videos/3_AUTOS_de_LUJO_USADOS_MUY_BARATOS!.mp4',1);

UPDATE `appinit`.`videos` SET `url_vd` = './static/videos/3_AUTOS_de_LUJO_USADOS_MUY_BARATOS!.mp4' WHERE (`id_vd` = '1');

ALTER TABLE `appinit`.`videos` 
CHANGE COLUMN `name_vd` `name_vd` VARCHAR(128) NOT NULL ;
 -- 

SELECT * FROM appinit.thumbnails;

INSERT INTO `appinit`.`thumbnails` (`name_thn`, `url_thn`, `description_thn`, `date_thn`, `id_video_thn`) VALUES ('3 AUTOS de LUJO USADOS MUY BARATOS', './static/images/thumbnail/3_AUTOS_de_LUJO_USADOS_MUY_BARATOS!.jpg', '--',now(), '1');

UPDATE `appinit`.`thumbnails` SET `url_thn` = './static/images/thumbnail/3_AUTOS_de_LUJO_USADOS_MUY_BARATOS!.jpg' WHERE (`id_thn` = '1');

ALTER TABLE `appinit`.`thumbnails` 
CHANGE COLUMN `name_thn` `name_thn` VARCHAR(128) NOT NULL ;


-- 
ALTER TABLE `appinit`.`comments` 
ADD COLUMN `date_cmt` DATETIME NOT NULL DEFAULT now() AFTER `id_comment_cmt`;
