class Category:
    def __init__(self,
                 parent,
                 name: str,
                 color: str,
                 type: str):
        '''
        Args:
            parent::Wallet
                Wallet object that this Category object belongs to, each Wallet has it's own list of categories
            name::str
                Name of this category
            color::str
                Color assigned to this category, can be either a HEX code or represented by word (ex. 'green')
                This parameter is not validated at any point, make sure a correct value is passed
            type::str
                Entry type that this category belongs to
                String has to be equal to one of these: 'income', 'expense' or 'both'
        '''

        self.parent = parent
        self.name: str = name
        self.color: str = color
        self.type: str = type

        self.children: list[Category] = [] # A list of subcategories