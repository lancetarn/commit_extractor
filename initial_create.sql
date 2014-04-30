CREATE TABLE `svnfile` (
	svnfile_id INTEGER PRIMARY KEY AUTOINCREMENT,
	filename TEXT,
	product TEXT,
    UNIQUE (`filename`, `product`) ON CONFLICT IGNORE
);

CREATE TABLE `revision` (
	revision_id INTEGER PRIMARY KEY,
	time TEXT
);

CREATE TABLE `revision_svnfile` (
	revision_id INTEGER,
	svnfile_id INTEGER,
	PRIMARY KEY ( `revision_id`, `svnfile_id` ) ON CONFLICT IGNORE,
	FOREIGN KEY ( `svnfile_id` ) REFERENCES `svnfile` ( `svnfile_id` ) ON DELETE CASCADE,
	FOREIGN KEY ( `revision_id` ) REFERENCES `revision` ( `revision_id` ) ON DELETE CASCADE
);
