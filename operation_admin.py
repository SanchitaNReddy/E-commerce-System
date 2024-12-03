# Name: Sanchita Reddy
# Student ID: 33483086
# Creation Date: May 29, 2023
# Last Modified:
# Description: This program contains all the operations related to admin operations


from operation_user import UserOperation
from operation_customer import CustomerOperation
from model_admin import Admin
import pandas as pd
from model_user import User
from model_customer import Customer
from opreation_product import ProductOperation


class AdminOperation:
    def register_primary_admin(self) -> bool:
        user_obj = UserOperation()
        cust_obj = CustomerOperation()
        user_id = "u_0000000001"
        user_name = "primary_admin"
        user_password = "primaryadmin123"
        user_role = "admin"

        # validating by calling the created methods
        if not user_obj.validate_username(user_name):
            return False
        if not user_obj.validate_password(user_password):
            return False
        if user_obj.check_username_exist(user_name):
            return False
        # capturing time of registration
        user_register_time = user_obj.current_time()
        # encrypting password
        encrypted_password = user_obj.encrypt_password(user_password)
        # creating an boject of customer
        new_user = Admin(
            user_id=user_id,
            user_name=user_name,
            user_password=encrypted_password,
            user_register_time=user_register_time,
            user_role=user_role,
        )
        # creating dataframes to append
        new_df = pd.DataFrame(new_user.__dict__, index=[0])
        existing_df = new_user.read_file_df()
        # writing in main file
        updated_df = new_user.append_df(existing_df, new_df)
        new_user.write_file_df(updated_df)

        return True

    def register_admin(self, user_name: str, user_password: str):
        """


        Parameters
        ----------
        user_name : str
            DESCRIPTION.
        user_password : str
            DESCRIPTION.

        Returns
        -------
        bool
            DESCRIPTION.

        """
        # importing user class object
        user_obj = UserOperation()
        cust_obj = CustomerOperation()

        # validating by calling the created methods
        if not user_obj.validate_username(user_name):
            return False
        if not user_obj.validate_password(user_password):
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
        new_user = Admin(
            user_id=user_id,
            user_name=user_name,
            user_password=encrypted_password,
            user_register_time=user_register_time,
        )
        # creating dataframes to append
        new_df = pd.DataFrame(new_user.__dict__, index=[0])
        existing_df = new_user.read_file_df()
        # writing in main file
        updated_df = new_user.append_df(existing_df, new_df)
        new_user.write_file_df(updated_df)

        return True

    def add_customer(self, user_name: str, user_email: str, user_mobile: str) -> dict:
        """


        Parameters
        ----------
        user_name : str
            DESCRIPTION.
        user_email : str
            DESCRIPTION.
        user_mobile : str
            DESCRIPTION.

        Returns
        -------
        dict
            DESCRIPTION.

        """
        user_password = "password123"
        # calling the register customer function from CustomerOperation class
        return CustomerOperation().register_customer(
            user_name, user_password, user_email, user_mobile
        )

    def show_customer(self, cust_input: str, page_no: bool, cust_id: bool) -> tuple:
        """


        Parameters
        ----------
        cust_input : TYPE
            DESCRIPTION.
        page_no : bool
            DESCRIPTION.
        cust_id : bool
            DESCRIPTION.

        Returns
        -------
        tuple
            DESCRIPTION.

        """
        # To show all customers, the entire list pased on the page number
        if page_no:
            cust_list = CustomerOperation().show_customer_list(cust_input)
            return cust_list

        # show a single customer based on the customer id
        if cust_id:
            df = User().search_user(cust_input, user_name=False, user_id=True)
            # converting df to tuple to keep the output consistent
            if not df.empty:
                customer_dict = df.to_dict("records")[0]
                customer = Customer(**customer_dict)
                # return customer object as a tuple
                return ([customer], "0", "0")
        return ([], "0", "0")

    def delete_cust_admin(self, cust_id: str) -> bool:
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
        CustomerOperation().delete_customer(cust_id)
        return True

    def delete_all_cust_admin(self) -> bool:
        """


        Returns
        -------
        bool
            DESCRIPTION.

        """
        CustomerOperation().delete_all_customers()
        return True

    def delete_admin(self, user_id: str) -> bool:
        """


        Parameters
        ----------
        user_id : str
            DESCRIPTION.

        Returns
        -------
        bool
            DESCRIPTION.

        """
        if user_id != "u_0000000001":
            valid_df = User().search_user(user_id, user_name=False, user_id=True)
            if valid_df.empty:
                return False
            else:
                old_df = User().read_file_df()
                old_df = old_df[old_df["user_id"] != user_id].copy()
                User().write_file_df(old_df)
                return True

    def add_admin(self, user_name: str) -> bool:
        user_password = "password123"
        self.register_admin(user_name, user_password)
        return True

    def ad_generate_category_figure(self):
        ProductOperation().generate_category_figure()

    def ad_generate_discount_figure(self):
        ProductOperation().generate_discount_figure()

    def ad_generate_likes_count_figure(self):
        ProductOperation().generate_likes_count_figure()

    def ad_generate_discount_likes_count_figure(self):
        ProductOperation().generate_discount_likes_count_figure()

    pass
