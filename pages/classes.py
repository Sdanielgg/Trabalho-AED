class User():
    def __init__(self,Username,Password,Admin,Views,AlbumsCreated,AlbumsCommentsNumber):
        self.Username= Username
        self.Password=Password
        self.Admin=Admin
        self.Views=Views
        self.AlbumsCreated=AlbumsCreated
        self.AlbumsCommentsNumber=AlbumsCommentsNumber


class Album():
    def __init__(self,Views,Comments,):
        self.Views=Views
        
#sub classe de admin? com os metodos aqui para nao sobrecarregar a classe de user?
class Admin():
    def __init__(self):




