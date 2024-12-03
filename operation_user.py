# Name: Sanchita Reddy
# Student ID: 33483086
# Creation Date: May 29, 2023
# Last Modified:
# Description: This program contains all the operations related to user operations

import time
from model_user import User
import random
import pandas as pd
from model_customer import Customer
from model_admin import Admin


class UserOperation:
    def generate_unique_user_id(self) -> str:
        """


        Returns
        -------
        str
            DESCRIPTION.

        """
        # importing user class object
        user = User()
        # using the read_file_df function to get a data frame
        data_frame = user.read_file_df()

        if data_frame.empty:
            return "u_" + str(random.randint(1000000000, 9999999999))

        data_array = pd.Series(data_frame["user_id"])

        while True:
            new_user_id = "u_" + str(random.randint(1000000000, 9999999999))
            # ensuring the generated user_id does not exist
            if new_user_id not in data_array.values:
                return new_user_id

    def encrypt_password(self, user_password: str) -> str:
        """


        Parameters
        ----------
        user_password : TYPE
            DESCRIPTION.

        Returns
        -------
        str
            DESCRIPTION.

        """
        # the length of encrypted password should be doubled
        encryp_pass_len = len(user_password) * 2
        random_string = "".join(
            random.choices(
                "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789",
                k=encryp_pass_len,
            )
        )

        # combining random string and the password input
        encrypted_password = ""
        char_index = 0
        for char in user_password:
            encrypted_password += (
                random_string[char_index] + random_string[char_index + 1] + char
            )
            char_index += 2

        # Adding the prefix and suffix
        encrypted_password = "^^" + encrypted_password + "$$"
        return encrypted_password

    def decrypt_password(self, encrypted_password: str) -> str:
        """


        Parameters
        ----------
        encrypted_password : TYPE
            DESCRIPTION.

        Returns
        -------
        str
            DESCRIPTION.

        """
        try:
            encrypted_password = encrypted_password[2:-2]

            decrypted_password = ""
            char_index = 0
            while char_index < len(encrypted_password):
                decrypted_password += encrypted_password[char_index + 2]
                char_index += 3

            return decrypted_password
        except:
            return False

    def check_username_exist(self, user_name: str) -> bool:
        """


        Parameters
        ----------
        user_name : str
            DESCRIPTION.

        Returns
        -------
        bool
            DESCRIPTION.

        """
        # importing user class object
        user = User()
        # using the read_file_df function to get a data frame
        try:
            data_frame = user.read_file_df()
            data_array = pd.Series(data_frame["user_name"])
            # validating the existance of user_name
            if user_name is not None:
                if user_name in data_array.values:
                    return True
            return False
        except:
            return False

    def validate_username(self, user_name: str) -> bool:
        """


        Parameters
        ----------
        user_name : str
            DESCRIPTION.

        Returns
        -------
        bool
            DESCRIPTION.

        """
        # ensuring the length is atleast 5 chars
        if len(user_name) < 5:
            return False
        # ensuring that it is either alphabets or underscore
        for char in user_name:
            if not (char.isalpha() or char == "_"):
                return False
        return True

    def validate_password(self, user_password: str) -> bool:
        """


        Parameters
        ----------
        user_password : str
            DESCRIPTION.

        Returns
        -------
        bool
            DESCRIPTION.

        """
        # ensuring the length is atleast 5 chars
        if len(user_password) < 5:
            return False

        # variables to check for intersect of the conditions
        alpha_flag = False
        digit_flag = False

        for char in user_password:
            if char.isalpha():
                alpha_flag = True
            elif char.isdigit():
                digit_flag = True
        return alpha_flag and digit_flag

    def current_time(self):
        """


        Returns
        -------
        time_format : TYPE
            DESCRIPTION.

        """
        current_time = time.time()
        time_struct = time.localtime(current_time)
        time_format = time.strftime("%d-%m-%Y_%H:%M:%S", time_struct)
        return time_format

    def login(self, user_name: str, user_password: str):
        """


        Parameters
        ----------
        user_name : str
            DESCRIPTION.
        user_password : str
            DESCRIPTION.

        Returns
        -------
        TYPE
            DESCRIPTION.

        """
        user = User()
        data_frame = user.read_file_df()
        # retrieving only the values required
        if user_name in data_frame["user_name"].values:
            user_record = data_frame.loc[data_frame["user_name"] == user_name]
            decrypted_password = self.decrypt_password(
                user_record["user_password"].item()
            )
            if user_password == decrypted_password:
                # getting a return based on the type of user
                user_role = user_record["user_role"].item()
                if user_role == "customer":
                    return Customer(
                        user_record["user_id"].item(),
                        user_record["user_name"].item(),
                        user_record["user_password"].item(),
                        user_record["user_register_time"].item(),
                        user_record["user_role"].item(),
                        user_record["user_email"].item(),
                        user_record["user_mobile"].item(),
                    )
                elif user_role in ("admin", "primary admin"):
                    return Admin(
                        user_record["user_id"].item(),
                        user_record["user_name"].item(),
                        user_record["user_password"].item(),
                        user_record["user_register_time"].item(),
                        user_record["user_role"].item(),
                    )
        return user

    pass
