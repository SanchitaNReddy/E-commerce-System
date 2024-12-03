# Name: Sanchita Reddy
# Student ID: 33483086
# Creation Date: May 29, 2023
# Last Modified:
# Description: This program contains all the order related operations

import pandas as pd
import time


class Order:

    order_id = "order_id"
    user_id = "user_id"
    order_time_stamp = "order_time"
    pro_id = "pro_id"
    order_file = "data/orders.txt"

    def __init__(
        self,
        order_id="o_10001",
        user_id="u_0000000001",
        pro_id="0000000",
        order_time_stamp="00-00-0000_00:00:00",
    ):
        """


        Parameters
        ----------
        order_id : TYPE, optional
            DESCRIPTION. The default is "o_00000".
        user_id : TYPE, optional
            DESCRIPTION. The default is "u_0000000001".
        product_id : TYPE, optional
            DESCRIPTION. The default is "0000000".
        order_time_stamp : TYPE, optional
            DESCRIPTION. The default is "00-00-0000_00:00:00".

        Returns
        -------
        None.

        """
        self.order_id = order_id
        self.user_id = user_id
        self.pro_id = pro_id
        self.order_time_stamp = order_time_stamp

    def __str__(self):
        """


        Returns
        -------
        order_string : TYPE
            DESCRIPTION.

        """
        order_string = self.__dict__
        return order_string

    def read_file_df(self):
        """


        Returns
        -------
        user_data : TYPE
            DESCRIPTION.

        """
        # Method to read the user file
        try:
            with open(Order.order_file, "r") as file:
                order_data = file.readlines()
                # Converting list of string to list of dictionaries
                order_data = [eval(line) for line in order_data]
                # converting the list of dictionaries to a data frame for data handling
                df = pd.DataFrame(order_data)
                return df
        except:
            data_frame = pd.DataFrame()
            return data_frame

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
            final_df = df.fillna("None")
            with open(Order.order_file, "w") as file:
                for i, row in final_df.iterrows():
                    each_row = str(row.to_dict()) + "\n"
                    # print(each_row)
                    file.write(each_row)
            return True
        except:
            return None

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

    def current_order_time(self):
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

    def search_order(
        self, order_detail: str, order_id: bool, user_id: bool
    ) -> pd.DataFrame():
        try:
            data_frame = self.read_file_df()
            # retrieving only the values required
            if order_id:
                if order_detail in data_frame[Order.order_id].values:
                    user_record = data_frame.loc[
                        data_frame[Order.order_id] == order_detail
                    ]
                    return user_record
            if user_id:
                if order_detail in data_frame[Order.user_id].values:
                    user_record = data_frame.loc[
                        data_frame[Order.user_id] == order_detail
                    ]
                    return user_record
            return pd.DataFrame()
        except:
            df = pd.DataFrame()
            return df

    pass
