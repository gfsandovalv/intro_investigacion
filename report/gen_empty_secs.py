sections_names = ['abstract',
                  'introduction',
                  'theoretical framework',
                  'statement of the tentative problem',
                  'objectives',
                  'methodology',
                  'time line',
                  'resources']

prefix = '/home/gabo/Documents/unal/Semestres/2022-2/intro_investigacion/reports/preproyecto/secs/'
for section_name in sections_names:
    file_path = prefix + section_name.replace(" ", '_')
    with open(file_path + '.tex', 'w+') as file:
        file.write('\section{' + section_name.capitalize() + '}')