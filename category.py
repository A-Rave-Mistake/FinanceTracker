class Category:
    def __init__(self,
                 parent,
                 name: str,
                 color: str):
        '''
        Args:
            parent::Wallet
                Wallet object that this Category object belongs to, each Wallet has it's own list of categories
            name::str
                Name of this category
            color::str
                Color assigned to this category, can be either a HEX code or represented by word (ex. 'green')
                This parameter is not validated at any point, make sure a correct value is passed
        '''

        self.parent = parent
        self.name = name
        self.color = color

        self.children: list[Category] = [] # A list of subcategories