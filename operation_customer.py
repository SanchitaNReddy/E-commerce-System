# Name: Sanchita Reddy
# Student ID: 33483086
# Creation Date: May 29, 2023
# Last Modified:
# Description: This program contains all the operations related to customer operations

import re
from operation_user import UserOperation
import pandas as pd
from model_user import User
from operation_order import OrderOperation
from model_customer import Customer


class CustomerOperation:
    def validate_email(self, user_email: str) -> bool:
        """


        Parameters
        ----------
        user_email : str
            DESCRIPTION.

        Returns
        -------
        bool
            DESCRIPTION.

        """
        # regex patter to match the validations - username@domain.address
        pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
        if re.match(pattern, user_email):
            return True
        return False

    def validate_mobile(self, user_mobile: str) -> bool:
        """


        Parameters
        ----------
        user_mobile : str
            DESCRIPTION.

        Returns
        -------
        bool
            DESCRIPTION.

        """
        # checking to ensure the number is 10 digits
        if len(user_mobile) != 10:
            return False
        # ensuring it is all digits
        if not user_mobile.isdigit():
            return False
        # ensuring the number starts with 04 or 03
        if not (user_mobile.startswith("04") or user_mobile.startswith("03")):
            return False
        return True

    def register_customer(
        self, user_name: str, user_password: str, user_email: str, user_mobile: str
    ):
        """


        Parameters
        ----------
        user_name : str
            DESCRIPTION.
        user_password : str
            DESCRIPTION.
        user_email : str
            DESCRIPTION.
        user_mobile : str
            DESCRIPTION.

        Returns
        -------
        bool
            DESCRIPTION.

        """
        # importing user class object
        user_obj = UserOperation()

        # validating by calling the created methods
        if not user_obj.validate_username(user_name):
            return False
        if not user_obj.validate_password(user_password):
            return False
        if not self.validate_email(user_email):
            return False
        if not self.validate_mobile(user_mobile):
            return False
        if user_obj.check_username_exist(user_name):
            return False

        # generating unique user_id
        user_id = user_obj.generate_unique_user_id()
        # capturing time of registration
        user_register_time = user_obj.current_time()
        # encrypting password
        encrypted_password = user_obj.encrypt_password(user_password)
        # creating an boject of customer
        new_user = Customer(
            user_id=user_id,
            user_name=user_name,
            user_password=encrypted_password,
            user_register_time=user_register_time,
            user_email=user_email,
            user_mobile=user_mobile,
        )
        # creating dataframes to append
        new_df = pd.DataFrame(new_user.__dict__, index=[0])
        existing_df = new_user.read_file_df()
        # writing in main file
        updated_df = new_user.append_df(existing_df, new_df)
        new_user.write_file_df(updated_df)
        return True

    def update_profile(self, logged_in_user, attribute_name: str, value: str) -> bool:
        logged_in_user = logged_in_user.__dict__
        # perform validations
        if attribute_name == "user_email":
            if not self.validate_email(value):
                return False
        if attribute_name == "user_mobile":
            if not self.validate_mobile(value):
                return False
        if attribute_name == "user_password":
            if not UserOperation().validate_password(value):
                return False
            value = UserOperation().encrypt_password(value)

        # Writing the attribute in the df
        logged_in_user[attribute_name] = value

        # Writing this value in the user.txt file
        user_profile_df = pd.DataFrame([logged_in_user])
        old_df = User().read_file_df()
        old_df = old_df[old_df["user_name"] != logged_in_user["user_name"]]
        updated_df = pd.concat([old_df, user_profile_df], ignore_index=True)
        User().write_file_df(updated_df)
        return True

    def delete_customer(self, cust_id: str) -> bool:
        """


        Parameters
        ----------
        cust_id : str
            DESCRIPTION.

        Returns
        -------
        bool
            DESCRIPTION.

        """
        # validating cutomer ID argument
        valid_df = User().search_user(cust_id, user_name=False, user_id=True)
        if valid_df.empty:
            return False
        else:
            old_df = User().read_file_df()
            old_df = old_df[old_df["user_id"] != cust_id].copy()
            User().write_file_df(old_df)
            return True

    def show_customer_list(self, page_no: str):
        def create_cust_obj(row):
            return Customer(**row["cust_dict"])

        page_size = 10

        user_file_df = User().read_file_df()
        cust_file_df = user_file_df[user_file_df["user_role"] == "customer"].copy()
        # converting df to a dictionary
        cust_df_dict = cust_file_df.to_dict("records")

        cust_df = pd.DataFrame()
        cust_df["cust_dict"] = cust_df_dict
        cust_df["customer_obj"] = cust_df.apply(create_cust_obj, axis=1)

        cust_df = cust_df.drop("cust_dict", axis=1)
        cust_df["page_num"] = (cust_df.index // page_size) + 1

        final_df = cust_df[cust_df["page_num"] == int(page_no)]

        return_list = final_df["customer_obj"].to_list()
        max_pages = cust_df["page_num"].max()

        return_tup = (return_list, page_no, max_pages)
        return return_tup

    def delete_all_customers(self):
        """


        Returns
        -------
        bool
            DESCRIPTION.

        """
        data_frame = User().read_file_df()
        cust_file_df = data_frame[data_frame["user_role"] == "customer"].copy()
        updated_data_frame = data_frame.drop(cust_file_df.index)
        User().write_file_df(updated_data_frame)
        return True

    def cust_generate_single_customer_consumption_figure(self, cust_id: str):
        if OrderOperation().generate_single_customer_consumption_figure(cust_id):
            return True
        else:
            return False

    def cust_generate_all_customers_consumption_figure(self):
        OrderOperation().generate_all_customers_consumption_figure()

    def cust_generate_all_top_10_best_sellers_figure(self):
        OrderOperation().generate_all_top_10_best_sellers_figure()

    pass
