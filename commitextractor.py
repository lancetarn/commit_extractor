
from ConfigParser import SafeConfigParser

class CommitExtractor(object):

    def parse_config(self, cnf_file):
        cnf = SafeConfigParser()
        cnf.read(cnf_file)
        self.db_cnf = dict(cnf.items("db"))
        self.svn_cnf = dict(cnf.items("svn"))
