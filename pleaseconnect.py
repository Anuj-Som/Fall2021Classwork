from pymodm import connect, MongoModel, fields

connect("mongodb+srv://User1:Password@cluster0.a532e.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")

class User(MongoModel):
    name=fields.CharField()


x = User(name="Braden")
x.save()

