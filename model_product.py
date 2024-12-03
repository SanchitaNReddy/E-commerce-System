# Name: Sanchita Reddy
# Student ID: 33483086
# Creation Date: May 29, 2023
# Last Modified:
# Description: This program contains all the product related operations

from model_user import User
import pandas as pd


class Product(User):

    product_file = "data/products.txt"
    product_id = "pro_id"
    product_model = "pro_model"
    product_category = "pro_category"
    product_name = "pro_name"
    product_current_price = "pro_current_price"
    product_raw_price = "pro_raw_price"
    product_discount = "pro_discount"
    product_likes_count = "pro_likes_count"
    # variable to save the columns in the data frame
    df_file_save_columns = [
        product_id,
        product_model,
        product_category,
        product_name,
        product_current_price,
        product_raw_price,
        product_discount,
        product_likes_count,
    ]
    # variable to read the columns in the data frame
    df_file_read_columns = [
        "id",
        "model",
        "category",
        "name",
        "current_price",
        "raw_price",
        "discount",
        "likes_count",
    ]

    def __init__(
        self,
        product_id="0000000",
        product_model="",
        product_category="",
        product_name="",
        product_current_price="",
        product_raw_price="",
        product_discount="",
        product_likes_count="",
    ):
        """


        Parameters
        ----------
        product_id : TYPE, optional
            DESCRIPTION. The default is "0000".
        product_model : TYPE, optional
            DESCRIPTION. The default is "AB12".
        product_category : TYPE, optional
            DESCRIPTION. The default is "apparel".
        product_name : TYPE, optional
            DESCRIPTION. The default is "champion".
        product_current_price : TYPE, optional
            DESCRIPTION. The default is "12".
        product_raw_price : TYPE, optional
            DESCRIPTION. The default is "10".
        product_discount : TYPE, optional
            DESCRIPTION. The default is "10".
        product_likes_count : TYPE, optional
            DESCRIPTION. The default is "100".

        Returns
        -------
        None.

        """
        self.product_id = product_id
        self.product_model = product_model
        self.product_category = product_category
        self.product_name = product_name
        self.product_current_price = product_current_price
        self.product_raw_price = product_raw_price
        self.product_discount = product_discount
        self.product_likes_count = product_likes_count

    def __str__(self):
        product_string = str(self.__dict__)
        return product_string

    def read_file_df(self):
        """


        Returns
        -------
        user_data : TYPE
            DESCRIPTION.

        """
        # Method to read the user file
        try:
            with open(self.product_file, "r") as file:
                user_data = file.readlines()
                # Converting list of string to list of dictionaries
                user_data = [eval(line) for line in user_data]
                # converting the list of dictionaries to a data frame for data handling
                df = pd.DataFrame(user_data)
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
            with open(Product.product_file, "w") as file:
                for i, row in final_df.iterrows():
                    each_row = str(row.to_dict()) + "\n"
                    # print(each_row)
                    file.write(each_row)
            return True
        except:
            return None

    pass
