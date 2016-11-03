# RamblerTask

If you run Django server then use:

* from RamblerTask.development import *

in RamblerTask/settings.py else use:

* from RamblerTask.production import *


## API

* Get class:

URL: "calc_pickle/"

TYPE: only POST

REQUEST DATA: JSON {"f1": x1, "f2": x2, "f3": x3, "f4": x4} where type(xi) is float or integer. You can also pass strings convertable to float.

RETURN: JSON {"class": <string result of .pickle execution>} in case of success. If something went wrong JSON {"error": <error message>} would be returned.

* Change pickle file

URL: "change_pickle/"
TYPE: only GET;
REQUEST DATA: <pickle> - name of the file without extension (for example "svm_iris_model" for "RamblerTask/pickles/svm_iris_model.pickle")
RETURN: JSON {} in case of success. If something went wrong JSON {"error": <error message>} would be returned.

* Visualization

URL: "/"
TYPE: GET
REQUEST DATA: Empty
RETURN: http page

Each error message will be shown in top right corner of the page until click on it. If request to "calc_pickle/" after click on "Get class" is OK then you will see green message with predicted "class" in top right corner for 2.5 seconds.
