from flask_app.config.mysqlconnection import connectToMySQL


class Ninja: 
    db = "dojos_and_ninjas_new"
    def __init__( self , data ):
        self.id = data['id']
        self.firstname = data['firstname']
        self.lastname = data['lastname']
        self.age = data['age']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.dojo_id = data['dojo_id']
    
    @classmethod
    def get_all_ninjas(cls):
        query = "SELECT * FROM ninjas;"
        results = connectToMySQL('dojos_and_ninjas_new').query_db(query)

        ninjas_Arr = []

        for elt in results:
            ninjas_Arr.append(cls(elt))

        return ninjas_Arr


    
    @classmethod
    def create_ninja (cls, data):

        query = "INSERT INTO ninjas ( firstname , lastname , age , created_at, updated_at, dojo_id ) VALUES ( %(first_name)s , %(last_name)s , %(age)s , NOW() , NOW(), %(dojo_id)s );"

        return connectToMySQL('dojos_and_ninjas_new').query_db( query, data )




    @classmethod
    def get_specific_ninja(cls, data):
        query = "SELECT * FROM ninjas WHERE dojo_id = %(dojo_id)s"

        results = connectToMySQL('dojos_and_ninjas_new').query_db(query, data)

        # print('new results:++', results)
        #return cls(results[0])
       
        #return results[0]
        
        ninja_Arr = []

        for elt in results:
            ninja_Arr.append(elt)

        return ninja_Arr
    

    