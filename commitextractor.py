
import svn_broker
import db_broker
from ConfigParser import SafeConfigParser

class CommitExtractor(object):

    def __init__(self):
        pass

    def __parse_config(self, cnf_file):
        cnf = SafeConfigParser()
        cnf.read(cnf_file)
        self.db_cnf = dict(cnf.items("db"))
        self.svn_cnf = dict(cnf.items("svn"))

    def init_svn_client(self):
        pass

