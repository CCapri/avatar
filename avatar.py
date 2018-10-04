### 
### Author: Nick Polucci
### Description: Create an avatar or use a preset one. Presets: Jeff, Adam, and Chris.
###              Type "custom" if you want a custom avatar.
###

def jeff():
    hatStyles('both')
    face('True', '0')
    torso('=', 2)
    legs(2, '#HHH#')
    return()

def adam():
    hatStyles('right')
    face('False', '*')
    print('      |-X-|')
    torso('T', 3)
    legs(3, '<|||>')
    return()
    
def chris():
    hatStyles('front')
    face('True', 'U')
    print('      |-X-|')
    torso('W', 1)
    legs(4, '<>-<>')
    return()
    
def hatStyles(hatStyle):
# Prints out certain hatstyles based on user input
    print('')
    if hatStyle.lower() == 'left':
        print('''       ~-~       
     /-~-~-\\     
 ___/_______\\    ''')
    if hatStyle.lower() == 'right':
        print('''       ~-~       
     /-~-~-\     
    /_______\___ ''')
    if hatStyle.lower() == 'both':
        print('''       ~-~       
     /-~-~-\     
 ___/_______\___ ''')
    if hatStyle.lower() == 'front':
        print('''       ~-~       
     /-~-~-\     
    /_______\    ''')

def face(hair, eyeCharacter):
# Prints a basic face, changing with hair and eye character inputs
    if hair == 'True':
        print('    |"""""""|')
    if hair == 'False':
        print('    |\'\'\'\'\'\'\'|')
    print('    | {0}   {0} |'.format(eyeCharacter))
    print('    |   V   |')
    print('    |  ~~~  |')
    print('     \_____/')

def torso(armCharacter, torsoLength):
# Prints arms and torso, changing with arm character and torso length inputs
    print(' 0{0}{0}{0}{0}|---|{0}{0}{0}{0}0'.format(armCharacter))
    while torsoLength != 0:
        print('      |-X-|')
        torsoLength -= 1
    print('      HHHHH')

def legs(legLength, shoe):
# Prints out legs, changing with legLength and shoe inputs
    while legLength != 0:
        #while 
        if legLength >= 1:
            print('     /// \\\\\\') # 5 blank
        if legLength >= 2:
            print('    ///   \\\\\\') # 4 blank
        if legLength >= 3:
            print('   ///     \\\\\\') 
        if legLength == 4:
            print('  ///       \\\\\\')
        legLength = 0
    print('{0}       {0}'.format(shoe))
    
def legs(legLength, shoe):
    while legLength != 0:
        print(' ')

def customPrint():
# Asks all questions and assigns them to variables which are used as parameters for each function.
    hatStyle = input('Hat style ? \n')
    eyeCharacter = input('Character for eyes ? \n')
    hair = input('Shaggy hair (True/False) ? \n')
    armCharacter = input('Arm style ? \n')
    torsoLength = int(input('Torso length ? \n'))
    legLength = int(input('Leg length (1-4) ? \n'))
    shoe = input('Shoe look ? \n')
    # Prints out the custom character
    hatStyles(hatStyle)
    face(hair, eyeCharacter)
    torso(armCharacter, torsoLength)
    legs(legLength, shoe)
    return()
    
    
def main():
    print('----- AVATAR -----')
    character = ''
    while character.lower() != 'jeff' and character.lower() != 'adam' \
    and character.lower() != 'chris' and character.lower() != 'custom' \
    and character.lower() != 'exit':
        character = input('Select an Avatar or create your own:\n')
    if character.lower() == 'jeff':
        jeff()
    elif character.lower() == 'adam':
        adam()
    elif character.lower() == 'chris':
        chris()
    elif character.lower() == 'exit':
        return()
    elif character.lower() == 'custom':
        print('Answer the following questions to create a custom avatar')
        customPrint()

main()
