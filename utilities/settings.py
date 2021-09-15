from pandas import set_option


def project_settings():
    set_option('display.max_columns', None)
    set_option('max_colwidth', None)
    set_option('max_rows', 25)
