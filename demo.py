favorite_places = {
    'jen': ['beijing', 'shanghai'],
    'sarah': ['paris'],
    'edward': ['london'],
    'phil': ['new york'],
}

for name,places in favorite_places.items():
    '''if len(languages)<2:
        print(name.title() + '\'s favorite languages is:' +'\t\n'+language)
        '''
  #  else:
    print(name.title()+ '\'s favorite places are:')
    for place in places:
            print('\t'+place)