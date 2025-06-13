#Daily Challenge: Dictionaries
# Demande un mot à l'utilisateur
word = input("Enter a word: ")

# Convertit tout en minuscules pour ignorer la casse
word = word.lower()

# Dictionnaire pour stocker les lettres et leurs positions
letter_indexes = {}

# Parcourrir chaque caractère et son index
for index, letter in enumerate(word):
    # Vérifie que c'est une lettre alphabétique
    if letter.isalpha():
        if letter in letter_indexes:
            letter_indexes[letter].append(index)
        else:
            letter_indexes[letter] = [index]

# Affiche le résultat
print(letter_indexes)

     

#DC Gold : Solve The Matrix
# La matrice de départ
matrix = [
    ['7', 'i', 'i'],
    ['T', 's', 'x'],
    ['h', '%', '?'],
    ['i', ' ', '#'],
    ['s', 'M', ' '],
    ['$', 'a', ' '],
    ['#', 't', '%'],
    ['^', 'r', '!']
]

# Lire les colonnes de haut en bas et concaténer les caractères
message = ''
rows = len(matrix)
cols = len(matrix[0])

for col in range(cols):
    for row in range(rows):
        message += matrix[row][col]

# Nettoyer manuellement : on ajoute une lettre, on remplace les symboles entre deux lettres par un espace
final_message = ''
i = 0
while i < len(message):
    if message[i].isalpha():
        final_message += message[i]
        i += 1
    else:
        # On regarde s'il y a une lettre après un ou plusieurs symboles
        j = i
        while j < len(message) and not message[j].isalpha():
            j += 1
        # S'il y a bien une lettre après les symboles, on ajoute un espace
        if i > 0 and j < len(message):
            final_message += ' '
        i = j

print(final_message)