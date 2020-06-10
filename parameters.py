# author Guido Schillaci
# Scuola Superiore Sant'Anna, Pisa, Italy
# guido.schillaci@santannapisa.it

import os
import pickle

class Parameters:

    def __init__(self):
        self.dictionary = {
            # directories
            'directory_main': '',
            'directory_data': '',
            'directory_results': '',
            'directory_plots': '',

            # debugging
            'verbosity_level': 1,
            'show_plots': True,

            # design of experiments
            'dimensions':2,
        }

    def get(self, key_name):
        if key_name in self.dictionary.keys():
            return self.dictionary[key_name]
        else:
            print('Trying to access parameters key: '+ key_name+ ' which does not exist')

    def set(self, key_name, key_value):
        if key_name in self.dictionary.keys():
            print('Setting parameters key: ', key_name, ' to ', str(key_value))
            self.dictionary[key_name] = key_value
        else:
            print('Trying to modify parameters key: '+ key_name+ ' which does not exist')

    def save(self):
        pickle.dump(self.dictionary, open(os.path.join(self.get('directory_main'), 'parameters.pkl'), 'wb'),  protocol=2) # protcolo2 for compatibility with python2
        # save also as plain text file
        with open(os.path.join(self.get('directory_main'), 'parameters.txt'), 'w') as f:
            print(self.dictionary, file=f)
