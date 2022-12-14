# Create a dictionary with the cypher values for each variable name
cypher = {
    'width': '๐',
    'height': '๐',
    'steps': 'โฒ๏ธ',
    'sampler': '๐งช',
    'model': '๐งซ',
    'cfg_scale': '๐งญ',
    'number_of_images': '๐จ๏ธ',
    'clip_guidance': '๐'
}

# Create a dictionary with the cypher values for each variable value
value_cypher = {
    512: 'โซ',
    576: 'โช',
    640: '๐ ',
    704: '๐ก',
    768: '๐ข',
    832: '๐ต',
    896: '๐ฃ',
    960: '๐ค',
    1024: 'โฌ',
    'k_lms': 'โฌ',
    'k_euler': '๐ฅ',
    'k_euler_ancestral': '๐ฆ',
    'k_dpm_2': '๐ง',
    'k_dpm_2_ancestral': '๐จ',
    'k_heun': '๐ฉ',
    'k_dpmpp_2s_ancestral': '๐ช',
    'k_dpmpp_2m': '๐ซ',
    'ddim': '๐',
    'plms': '๐ฆ',
    14: '๐ด',
    15: '๐ฅ',
    20: '๐ง',
    21: '๐จ',
    0: '๐ฉ',
    1: '๐ช',
    2: '๐ซ',
    3: '๐',
    4: '๐',
    5: '๐',
    6: '๐',
    7: '๐',
    8: '๐',
    9: '๐',
    25  : '๐',
    30  : '๐',
    35  : '๐',
    40  : '๐',
    45  : '๐',
    50  : '๐',
    55  : '๐',
    60  : '๐ ',
    65  : '๐ก๏ธ',
    70  : '๐ค๏ธ',
    75  : '๐ฅ๏ธ',
    80  : '๐ฆ๏ธ',
    85  : '๐ง๏ธ',
    90  : '๐จ๏ธ',
    95  : '๐ฉ๏ธ',
    100 : '๐ช๏ธ',
    105 : '๐ซ๏ธ',
    110 : '๐ฌ๏ธ',
    115 : '๐ญ',
    120 : '๐ฎ',
    125 : '๐ฏ',
    130 : '๐ฐ',
    135 : '๐ฑ',
    140 : '๐ฒ',
    145 : '๐ณ',
    150 : '๐ด',
    True: '๐ธ',
    False:  '๐ท'
}

# Define the variables
width = 768
height = 768
steps = 30
sampler = 'k_dpm_2_ancestral'
model = 21
cfg_scale = 7
number_of_images = 4
clip_guidance = True

# Encode the variable names and values using the cypher dictionaries
SHORT_CODE = ''
for variable, value in locals().copy().items():
    if variable == 'cypher' or variable == 'value_cypher':
        continue
    if isinstance(value, dict):
        continue
    if value not in value_cypher:
        continue
    encoded_name = cypher[variable]
    encoded_value = value_cypher[value]
    SHORT_CODE += f'{encoded_name}{encoded_value}'

# Print the short code
print(SHORT_CODE)
