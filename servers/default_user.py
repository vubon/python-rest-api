"""
 This is default user for authentication testing purpose
"""
import base64


class DefaultUser:

    key = ''

    def set_auth(self, username, password):
        """
        By this method we will get a base64 has key
        :param username:
        :param password:
        :rtype: str
        """
        self.key = base64.b64encode(
            bytes('%s:%s' % (username, password), 'utf-8')).decode('ascii')

    def get_auth_key(self):
        """
        By this method will get user key
        :return: a string
        :rtype: str
        """
        return self.key


def user_data():
    """
    If you want to change you can change and use same username password
    when you want to create recipe item, delete recipe, update recipe.
    :return: a key
    :rtype: str
    """
    user = DefaultUser()
    # username and password
    user.set_auth('vubon', '123456')
    return user.get_auth_key()

