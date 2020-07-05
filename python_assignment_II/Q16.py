# Imagine you are creating a Super Mario game. You need to define
# a class to represent Mario. What would it look like? If you aren't
# familiar with SuperMario, use your own favorite video or board game
# to model a player.

# I am not familiar with SuperMario game, So I'll be creating class for Tommy (character in GTA Vice City)

class GTA_Character:
    name = 'Tommy'

    def __init__(self):
        hair_type_list = ['bald', 'normal', 'long', 'curly']
        hair_color_list = ['black', 'golden', 'red', 'bleached', 'orange']
        beard_type_list = ['clean', 'normal', 'french', 'circle', 'horseshoe', 'garibaldi']
        beard_color_list = ['black', 'bleached', 'red']
        skin_color_list = ['yellow', 'black', 'brown']
        face_orientation_list = ['normal', 'anger', 'smailey']

        self.hair_type = hair_type_list[0]
        self.hair_color = hair_color_list[0]
        self.beard_type = beard_type_list[0]
        self.beard_color = beard_color_list[0]
        self.skin_color = skin_color_list[0]
        self.is_fat = False
        self.face_orientation = face_orientation_list[0]
        self.health = 100
        self.is_alive = True


    def get_character(self):
        '''
        this method will return the properties of 'Tommy'

        :return: Dictionay -> which contains attributes of character('Tommy')
        '''
        character = {}
        character['name'] = self.name
        character['hair_color'] = self.hair_color
        character['hair_type'] = self.hair_type
        character['beard_type'] = self.beard_type
        character['beard_color'] = self.beard_color
        character['skin_color'] = self.skin_color
        character['is_fat'] = self.is_fat
        character['face_orientation'] = self.face_orientation
        character['health'] = self.health
        character['is_alive'] = self.is_alive

        return character

    def update_character_properties(self,
                                    hair_color=None,
                                    hair_type=None,
                                    beard_type=None,
                                    beard_color=None,
                                    skin_color=None,
                                    is_fat=None,
                                    face_orientation=None):
        '''
        user can ubdate following properties of Tommy

        :param hair_color: String
        :param hair_type: String
        :param beard_type: String
        :param beard_color: String
        :param is_fat: Boolean
        :param face_orientation: String
        :return: Boolean
        '''
        if hair_type:
            self.hair_type = hair_type
        if hair_color:
            self.hair_color = hair_color
        if beard_type:
            self.beard_type = beard_type
        if beard_color:
            self.beard_color = beard_color
        if skin_color:
            self.skin_color = skin_color
        if is_fat:
            self.is_fat = is_fat
        if face_orientation:
            self.face_orientation = face_orientation

        return True


# instatiating a character
gaurav = GTA_Character()
tommy = gaurav.get_character()
print(tommy['hair_type'])

# updating hair property of character
gaurav.update_character_properties(
    hair_type='curly'
)
tommy = gaurav.get_character()
print(tommy['hair_type'])