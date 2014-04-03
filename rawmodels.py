
import sqlite3

class Commits:

    def __init__(self):
        self.db = sqlite3.connect("subvision.db")
        self.db.row_factory = sqlite3.Row
        self.cur = self.db.cursor()

    def getAll(self):
        sql = "SELECT * from SVNLog"
        self.cur.execute(sql)
        commit_list = []
        commits = self.cur.fetchall()
        for commit in commits:
            commit_list.append( self.getDictFromRow(commit))

        return commit_list

    def getDictFromRow(self, row):
        return dict(zip(row.keys(), row))


