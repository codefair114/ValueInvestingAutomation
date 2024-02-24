import os

class EMAIL:
    ADMIN_EMAIL = os.getenv("ADMIN_EMAIL")
    SUBJECT_SEC_FETCH_SUCCESS = 'Updating companies data successful'
    BODY_SEC_FETCH_SUCCESS = 'The update of the companies data from sec was successful.'
    SUBJECT_SEC_FETCH_FAIL = 'Error updating companies data'
    BODY_SEC_FETCH_FAIL = 'There was an error updating the companies data.'
    DEFAULT_ARGS = {
        'owner': 'airflow',
        'email_on_failure': True,
        'email_on_success': True,
        'email': ADMIN_EMAIL,
        'email_on_retry': False,
        'retries': 1,
    }