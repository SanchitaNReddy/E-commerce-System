# Name: Sanchita Reddy
# Student ID: 33483086
# Creation Date: May 29, 2023
# Last Modified:
# Description: This program contains all the operations related to a user

import pandas as pd


class User:

    user_file = "data/users.txt"
    time_format = "%d-%m-%Y_%H:%M:%S"

    def __init__(
        self,
        user_id="u_0000000001",
        user_name="sanch",
        user_password="^^^Y!J#2$2%6&X(1)M*$$$",
        user_register_time="00-00-0000_00:00:00",
        user_role="customer",
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
            DESCRIPTION. The default is "customer".

        Returns
        -------
        None.

        """

        self.user_id = user_id
        self.user_name = user_name
        self.user_password = user_password
        self.user_register_time = user_register_time
        self.user_role = user_role

    def __str__(self):
        """

        Returns
        -------
        user_string : TYPE
            DESCRIPTION.

        """
        user_string = str(self.__dict__)
        return user_string

    def read_file_df(self):
        """


        Returns
        -------
        user_data : TYPE
            DESCRIPTION.

        """
        # Method to read the user file
        try:
            with open(self.user_file, "r") as file:
                user_data = file.readlines()
                # Converting list of string to list of dictionaries
                user_data = [eval(line) for line in user_data]
                # converting the list of dictionaries to a data frame for data handling
                df = pd.DataFrame(user_data)
                return df
        except:
            data_frame = pd.DataFrame()
            return data_frame

    def append_df(self, old_df: pd.DataFrame, df: pd.DataFrame) -> pd.DataFrame:
        """


        Parameters
        ----------
        old_df : pd.DataFrame
            DESCRIPTION.
        df : pd.DataFrame
            DESCRIPTION.

        Returns
        -------
        new_df : TYPE
            DESCRIPTION.

        """
        try:
            new_df = pd.concat([df, old_df], ignore_index=True)
            return new_df
        except:
            return None

    def write_file_df(self, df: pd.DataFrame):
        """


        Parameters
        ----------
        df : pd.DataFrame
            DESCRIPTION.

        Returns
        -------
        bool
            DESCRIPTION.

        """
        # Updating the data frame to the file
        try:
            with open(self.user_file, "w") as file:
                final_df = df.fillna("None")
                for i, row in final_df.iterrows():
                    each_row = str(row.to_dict()) + "\n"
                    file.write(each_row)
            return True
        except:
            return None

    def search_user(
        self, user_detail: str, user_name: bool, user_id: bool
    ) -> pd.DataFrame():
        try:
            data_frame = self.read_file_df()
            # retrieving only the values required
            if user_name:
                if user_detail in data_frame["user_name"].values:
                    user_record = data_frame.loc[data_frame["user_name"] == user_detail]
                    return user_record
            if user_id:
                if user_detail in data_frame["user_id"].values:
                    user_record = data_frame.loc[data_frame["user_id"] == user_detail]
                    return user_record
            return pd.DataFrame()
        except:
            df = pd.DataFrame()
            return df
