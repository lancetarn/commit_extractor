
import sqlite3

class DbBroker(object):
    LAST_REV_TABLE = 'last_rev'
    REV_TABLE = 'rev'
    SVNFILE_TABLE = 'svnfile'
    REV_FILE_TABLE = 'rev_svnfile'

    def __init__(self, db_name, db_user = None, db_pass = None):
        self.db_name = db_name
        self.db_user = db_user
        self.db_pass = db_pass
        self.conn = None

    def connect(self):
        self.conn = sqlite3.connect(self.db_name)
        self.conn.row_factory = sqlite3.Row
        self.cursor = self.conn.cursor()

    @property
    def get_last_rev(self):
        """
        Retrieves the latest rev that has been entered into the db
        """
        sql = 'SELECT last_rev_id FROM %s' % DbBroker.LAST_REV_TABLE
        row = self.cursor.execute(sql).fetchone()
        return row['last_rev_id']

    def set_last_rev(self, rev):
        sql = 'UPDATE %s SET last_rev_id = %d' % (DbBroker.LAST_REV_TABLE, rev)
        self.cursor.execute(sql)

    def insert_rev_files(self, rev, time, svnfiles):
        self.insert_rev(rev, time)
        ids = self.insert_svnfiles(rev, svnfiles)
        self.associate_files(rev, ids)
        self.set_last_rev(rev)

    def insert_svnfiles(self, svnfiles):
        """
        Takes a list of SvnFile objects and adds new entries to the database
        """
        # File_dict will eventually contain only new files
        filenames = []
        file_dict = {}
        for f in svnfiles:
            file_dict[f.filename] = f.product
            filenames.append(f.filename)

        existing_files = self.get_files_by_name(filenames)

        # Make list of existing ids while paring file_dict down for insert
        ids = []
        for existing in existing_files:
            del file_dict[existing['filename']]
            ids.append(existing['svnfile_id'])

        if file_dict:
            print file_dict
            self.insert_files(file_dict)

        # Get the ids out...
        new_ids = self.get_ids_from_filenames(file_dict.keys())

        return ids.extend(new_ids)


    def associate_revs(self, rev_id, file_ids):
        values = [ (rev_id, file_id) for file_id in file_ids ]
        sql = "INSERT INTO %s VALUES ( ?, ? )" % (DbBroker.REV_FILE_TABLE)
        self.cursor.executemany(sql, values)
        self.conn.commit()


    def set_last_rev(self, rev_id):
        sql = "INSERT INTO %s VALUES ( ? )" % (DbBroker.LAST_REV_TABLE)
        self.cursor.execute(sql, rev_id)
        self.conn.commit()


    def get_files_by_name(self, filenames):
        sql = 'SELECT * FROM %s WHERE filename IN ( %s )' % (DbBroker.SVNFILE_TABLE, self.make_placeholders(filenames))
        self.cursor.execute(sql, filenames)
        existing_files = self.cursor.fetchall()
        return existing_files


    def insert_files(self, file_dict):
        sql = 'INSERT INTO %s (filename, product) VALUES (?,?)' % (DbBroker.SVNFILE_TABLE)
        self.cursor.executemany(sql, file_dict.items())
        self.conn.commit()


    def get_ids_from_filenames(self, filenames):
        sql = 'SELECT svnfile_id FROM %s WHERE filename IN ( %s )' % (DbBroker.SVNFILE_TABLE, self.make_placeholders(filenames))
        # Makes a list of tuples
        ids = [ id for id in self.cursor.execute(sql, filenames)]
        if ids:
            # Unpacks tuples into a list of ints
            ids = zip(*ids)[0]
        print ids
        return ids


    def make_placeholders(self, value_list):
        return ', '.join('?'*len(value_list))
