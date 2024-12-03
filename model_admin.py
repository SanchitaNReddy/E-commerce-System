# Name: Sanchita Reddy
# Student ID: 33483086
# Creation Date: May 29, 2023
# Last Modified:
# Description: This program contains all the operations related to a admin

from model_user import User


class Admin(User):
    def __init__(
        self,
        user_id="u_0000000001",
        user_name="sanch",
        user_password="^^^Y!J#2$2%6&X(1)M*$$$",
        user_register_time="00-00-0000_00:00:00",
        user_role="admin",
    ):
        """


        Parameters
        ----------
        user_id : TYPE, optional
            DESCRIPTION. The default is "u_0000000001".
        user_name : TYPE, optional
            DESCRIPTION. The default is "sanch".
        user_password : TYPE, optional
            DESCRIPTION. The default is "^^^Y!J#2$2%6&X(1)M*$$$".
        user_register_time : TYPE, optional
            DESCRIPTION. The default is "00-00-0000_00:00:00".
        user_role : TYPE, optional
            DESCRIPTION. The default is "admin".

        Returns
        -------
        None.

        """
        # Inheriting the initialized variables
        super().__init__(
            user_id, user_name, user_password, user_register_time, user_role
        )

    def __str__(self):
        """


        Returns
        -------
        TYPE
            DESCRIPTION.

        """
        # Inheriting the string method from User class
        return super().__str__()

    pass
