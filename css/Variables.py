

def get_variables(key_word):
    dict_variables = {
        "page-width" : "900",
        "page-height" : "3100",
        "profile-height" : "200",
        "profile-width" : "200",
        "resume-title-height" : "150",
        "left-box-width" : "235",
        "right-box-width" : "500"
    }
    return dict_variables.get(key_word, "key_word not found")