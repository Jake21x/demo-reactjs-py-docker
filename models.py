from exts import db


"""
class Dsm:
    id:int primary key
    storeid:text
    userid:text
    skuid:text
    begining_inventory:int
    delivery:int
    bad_order:int
    transfer_incoming:int
    transfer_outgoing:int
    withdrawal:int
    ending_inventory:int
    sku_status:text
    date_created:date
    date_updated:date
    date_synced:date
"""

class Dsm(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    storeid=db.Column(db.Text(), nullable=False)
    userid=db.Column(db.Text(), nullable=False)
    skuid=db.Column(db.Text(), nullable=False)
    begining_inventory=db.Column(db.Integer(), nullable=False)
    delivery=db.Column(db.Integer(), nullable=False)
    bad_order=db.Column(db.Integer(), nullable=False)
    transfer_incoming=db.Column(db.Integer(), nullable=False)
    transfer_outgoing=db.Column(db.Integer(), nullable=False)
    withdrawal=db.Column(db.Integer(), nullable=False)
    ending_inventory=db.Column(db.Integer(), nullable=False)
    sku_status=db.Column(db.Integer(), nullable=False)
    date_created=db.Column(db.Date(), nullable=False)
    date_updated=db.Column(db.Date(), nullable=False)
    date_synced=db.Column(db.Date(), default= 'now()')

    def __repr__(self):
        return f"<Dsm {self.skuid}>"
        
    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

"""
class User
    id:int primary key
    userid=db.Column(db.Text(), nullable=False)
    roleid=db.Column(db.Integer(), nullable=False)
    first_name=db.Column(db.Text(), nullable=False)
    last_name=db.Column(db.Text(), nullable=False)
    date_created=db.Column(db.Date(), default= 'now()')
    date_updated=db.Column(db.Date(), nullable=False)
"""

class User(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    userid=db.Column(db.Text(), nullable=False)
    roleid=db.Column(db.Integer(), nullable=False)
    first_name=db.Column(db.Text(), nullable=False)
    last_name=db.Column(db.Text(), nullable=False)
    address=db.Column(db.Text(), nullable=False)
    contact_number=db.Column(db.Text(), nullable=False)
    date_updated=db.Column(db.Date(), nullable=False)
    date_created=db.Column(db.Date(), default= 'now()')

    def __repr__(self):
        return f"<User {self.userid}>"
    
    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def update(self,roleid,first_name,last_name,address,contact_number,date_updated):
        self.name = roleid
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.contact_number = contact_number
        self.date_updated = date_updated 
        db.session.commit()

"""
class Store
     id:int primary key
"""
class Store(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    storeid=db.Column(db.Text(), nullable=False) 
    name=db.Column(db.Text(), nullable=False)
    area=db.Column(db.Text(), nullable=False)
    channel=db.Column(db.Text(), nullable=False)
    date_updated=db.Column(db.Date(), nullable=False)
    date_created=db.Column(db.Date(), default= 'now()')

    def __repr__(self):
        return f"<Store {self.name}>"
    
    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def update(self,name,area,channel,date_updated):
        self.name = name 
        self.area = area
        self.channel = channel
        self.date_updated = date_updated
        db.session.commit()


"""
class Sku
     id:int primary key
"""
class Sku(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    skuid=db.Column(db.Text(), nullable=False) 
    name=db.Column(db.Text(), nullable=False)
    category=db.Column(db.Text(), nullable=False)
    brand=db.Column(db.Text(), nullable=False)
    price_piece=db.Column(db.Text(), nullable=False)
    price_case=db.Column(db.Text(), nullable=False)
    date_updated=db.Column(db.Date(), nullable=False)
    date_created=db.Column(db.Date(), default= 'now()')
    
    def __repr__(self):
        return f"<Sku {self.name}>"

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def update(self,name,category,brand,price_piece,price_case,date_updated):
        self.name = name
        self.category = category
        self.brand = brand
        self.price_piece = price_piece
        self.price_case = price_case
        self.date_updated = date_updated
        db.session.commit()


"""
class Role
     id:int primary key
"""
class Role(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    roleid=db.Column(db.Text(), nullable=False) 
    name=db.Column(db.Text(), nullable=False)
    date_updated=db.Column(db.Date(), nullable=False)
    date_created=db.Column(db.Date(), default= 'now()')


    def __repr__(self):
        return f"<Role {self.name}>"

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def update(self,name,date_updated):
        self.name = name
        self.date_updated = date_updated
        db.session.commit()
