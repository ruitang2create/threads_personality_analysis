from threads import Threads

threads = Threads()

def get_id_from_username(username : str) -> int:
    """
    Get the user ID from the given username.

    Parameters:
        username (str): The username of the user.

    Returns:
        int: The ID of the user.
    """
    return threads.public_api.get_user_id(username=username)

def fetch_user_info(username: str) -> dict:
    user_id = get_id_from_username(username)
    user_dict = threads.public_api.get_user(id=user_id)
    return user_dict

def fetch_user_threads(username: str)-> dict:
    user_id = get_id_from_username(username)
    response = threads.public_api.get_user_threads(id=user_id)
    return response
