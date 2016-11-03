import os
import json
import pickle
import numpy as np
from django.conf import settings

PICKLE_SETTINGS = 'pickle.json'


class Pickle:
    def __init__(self):
        self.pickle_root = os.path.join(settings.BASE_DIR, 'RamblerTask', 'pickles')
        self.pickle_settings = os.path.join(self.pickle_root, PICKLE_SETTINGS)

    def set_new_pickle(self, pname):
        pname += '.pickle'
        if not os.path.exists(os.path.join(self.pickle_root, pname)):
            raise ValueError('Pickle file was not found, ensure you have uploaded it to "pickles" directory')
        with open(self.pickle_settings, 'w', encoding='utf8') as fp:
            json.dump({'name': pname}, fp, ensure_ascii=False)

    def calc_pickle(self, vals):
        vals = np.array(vals)
        vals.reshape(1, -1)
        try:
            with open(self.get_pickle(), 'rb') as fp:
                clf = pickle.load(fp)
            return str(clf.predict(vals)[0])
        except Exception as e:
            raise type(e)("Pickle failed with error: %s" % e)

    def get_pickle(self):
        if os.path.exists(self.pickle_settings):
            with open(self.pickle_settings, 'r', encoding='utf8') as fp:
                pickle_file = json.load(fp)['name']
        else:
            pickle_files = list(x for x in os.listdir(self.pickle_root) if os.path.splitext(x)[-1] == '.pickle')
            try:
                pickle_file = pickle_files[0]
            except IndexError:
                raise ValueError('Pickle file was not found, ensure you have uploaded it to "pickles" directory')
            self.set_new_pickle(pickle_file)
        return os.path.join(self.pickle_root, pickle_file)
