
class SvnFile(object):

    def __init__(self):
        self.filename = None
        self.product = None
        self.id = None

    def set_filename(self, name):
        if not isinstance(name, basestring) or name == '':
            raise BadFilenameError()

        self.filename = name

    def set_product(self, product):
        if not isinstance(product, basestring) or product == '':
            raise BadProductError()

        self.product = product

    def set_id(self, id):
        id = int(id)
        if id < 0:
            raise ValueError('ID must be positive')
        self.id = id


    def get_id(self):
        return self.id

    def get_filename(self):
        return self.filname

    def get_product(self):
        return self.product



class BadFilenameError(Exception):
    pass

class BadProductError(Exception):
    pass
