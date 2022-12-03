
# Create a dictionary with the cypher values for each variable name
cypher = {
    'width': '📏',
    'height': '📐',
    'steps': '📊',
    'sampler': '📈',
    'model': '📉',
    'Cfg_Scale': '📆',
    'number_of_images': '📷',
    'CLIP_Guidance': '📸'
}

# Create a dictionary with the cypher values for each variable value
value_cypher = {
    512: '⚫',
    576: '⚪',
    640: '🟠',
    704: '🟡',
    768: '🟢',
    832: '🔵',
    896: '🟣',
    960: '🟤',
    1024: '⬜',
    'k_lms': '⬛',
    'k_euler': '🟥',
    'k_euler_ancestral': '🟦',
    'k_dpm_2': '🟧',
    'k_dpm_2_ancestral': '🟨',
    'k_heun': '🟩',
    'k_dpmpp_2s_ancestral': '🟪',
    'k_dpmpp_2m': '🟫',
    'ddim': '🔅',
    'plms': '🦚',
    14: '🔴',
    15: '🟥',
    20: '🟧',
    21: '🟨',
    0: '🟩',
    1: '🟪',
    2: '🟫',
    3: '🌑',
    4: '🌒',
    5: '🌓',
    6: '🌔',
    7: '🌕',
    8: '🌖',
    9: '🌗',
    True: '🔵',
    False: '⚪'
}

# Define the variables
width = 786
height = 786
steps = 30
sampler = 'k_euler_ancestral'
model = 21
Cfg_Scale = 7
number_of_images = 9
CLIP_Guidance = True

# Encode the variable names and values using the cypher dictionaries
short_code = ''
for variable, value in locals().copy().items():
    if variable == 'cypher' or variable == 'value_cypher':
        continue
    if isinstance(value, dict):
        continue
    if value not in value_cypher:
        continue
    encoded_name = cypher[variable]
    encoded_value = value_cypher[value]
    short_code += f'{encoded_name}{encoded_value}'

# Print the short code
print(short_code)