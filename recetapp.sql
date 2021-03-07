BEGIN TRANSACTION;
DROP TABLE IF EXISTS unidades; 
CREATE TABLE IF NOT EXISTS `unidades` (
	`id`	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
	`nombre`	TEXT NOT NULL,
	`abreviacion`	TEXT NOT NULL
);
DROP TABLE IF EXISTS tiendas; 
CREATE TABLE IF NOT EXISTS `tiendas` (
	`id`	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
	`nombre`	TEXT NOT NULL,
	`horario`	TEXT
);
DROP TABLE IF EXISTS recetas; 
CREATE TABLE IF NOT EXISTS `recetas` (
	`id`	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
	`nombre`	TEXT NOT NULL,
	`tiempo`	INTEGER,
	`vegano`	INTEGER DEFAULT 0
);
DROP TABLE IF EXISTS ingredientes; 
CREATE TABLE IF NOT EXISTS `ingredientes` (
	`id`	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
	`nombre`	TEXT NOT NULL,
	`tiendas_id`	INTEGER,
	FOREIGN KEY(`tiendas_id`) REFERENCES `tiendas`(`id`) ON UPDATE CASCADE ON DELETE CASCADE
);
DROP TABLE IF EXISTS recetas_ingredientes; 
CREATE TABLE IF NOT EXISTS `recetas_ingredientes` (
	`id`	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
	`recetas_id`	INTEGER NOT NULL,
	`ingredientes_id`	INTEGER NOT NULL,
	`cantidad`	REAL,
	`unidades_id`	INTEGER,

	
	FOREIGN KEY(`ingredientes_id`) REFERENCES `ingredientes`(`id`) ON UPDATE CASCADE ON DELETE CASCADE,
	FOREIGN KEY(`recetas_id`) REFERENCES `recetas`(`id`) ON UPDATE CASCADE ON DELETE CASCADE,
	FOREIGN KEY(`unidades_id`) REFERENCES `unidades`(`id`) ON UPDATE CASCADE ON DELETE CASCADE
);

INSERT INTO tiendas VALUES (1, "Verdulería", "Lunes a Viernes 10:00 a 20:00, Sábado 10:00 a 18:00");
INSERT INTO tiendas VALUES (2, "Dietética", "Lunes a Viernes 10:00 a 20:00, Sábado 10:00 a 18:00");
INSERT INTO tiendas VALUES (3, "Chino", "Lunes a Domingo 90:00 a 22:00");
INSERT INTO tiendas VALUES (4, "Supermercado", "Lunes a Viernes 10:00 a 21:00, Sábado 10:00 a 18:00");

INSERT INTO unidades VALUES (1, "gramos", "g");
INSERT INTO unidades VALUES (2, "mililitros", "ml");
INSERT INTO unidades VALUES (3, "unidades", "u");
INSERT INTO unidades VALUES (4, "kilogramos", "kg");
INSERT INTO unidades VALUES (5, "cucharadas", "cds");
INSERT INTO unidades VALUES (6, "pizca", "pzc");

INSERT INTO recetas VALUES (1, "Ensalada de tomates y paltas", 10, 1);

INSERT INTO ingredientes VALUES (1, "choclo", 4);
INSERT INTO ingredientes VALUES (2, "tomates", 4);
INSERT INTO ingredientes VALUES (3, "palta", 1);
INSERT INTO ingredientes VALUES (4, "cebolla morada", 1);
INSERT INTO ingredientes VALUES (5, "agua", NULL);
INSERT INTO ingredientes VALUES (6, "tahini", 2);
INSERT INTO ingredientes VALUES (7, "levadura de queso", 2);
INSERT INTO ingredientes VALUES (8, "limón", 1); 
INSERT INTO ingredientes VALUES (9, "sal", 2);

INSERT INTO recetas_ingredientes VALUES (1, 1, 1, 140, 1);
INSERT INTO recetas_ingredientes VALUES (2, 1, 2, 4, 3);
INSERT INTO recetas_ingredientes VALUES (3, 1, 3, 2, 3);
INSERT INTO recetas_ingredientes VALUES (4, 1, 4, 1, 3);
INSERT INTO recetas_ingredientes VALUES (5, 1, 5, 65, 2);
INSERT INTO recetas_ingredientes VALUES (6, 1, 6, 4, 5);
INSERT INTO recetas_ingredientes VALUES (7, 1, 7, 2, 5);
INSERT INTO recetas_ingredientes VALUES (8, 1, 8, 1, 5);
INSERT INTO recetas_ingredientes VALUES (9, 1, 9, NULL, NULL);




COMMIT;
