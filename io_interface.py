# Name: Sanchita Reddy
# Student ID: 33483086
# Creation Date: May 29, 2023
# Last Modified:
# Description: This program contains all the input/output related operations


class IOInterface:
    def get_user_input(self, message: str, num_of_args: str) -> list:
        """


        Parameters
        ----------
        message : str
            DESCRIPTION.
        num_of_args : str
            DESCRIPTION.

        Returns
        -------
        list
            DESCRIPTION.

        """
        # Taking user input and split to differenciate num of agrs and get it as a list

        # user_input = input(message).split()
        # user_input = ""
        num_of_args = int(num_of_args)
        user_input = input(message).split()
        if not user_input:
            user_input = [""] * int(num_of_args)
        else:
            user_input = user_input[:num_of_args] + [""] * max(
                0, int(num_of_args) - len(user_input)
            )
        return user_input

    def main_menu(self) -> str:
        """


        Returns
        -------
        str
            DESCRIPTION.

        """
        print(
            """
------------------------- Main Menu ----------------------------
1. Login
2. Register
3. Quit
----------------------------------------------------------------
"""
        )

    def admin_menu(self, logged_in_user) -> str:
        """


        Returns
        -------
        str
            DESCRIPTION.

        """
        user_profile = logged_in_user.__dict__
        user = user_profile["user_name"]
        print(
            f"""
Hello {user},
Please select your choice from the below
------------------------- Admin Menu ---------------------------
1. Products menu - Search/Add/Delete products
2. User menu - Search/Add/Delete users
3. Orders menu - Search/Add/Delete orders
4. Statistics and figures
5. Generate test data
6. Logout
----------------------------------------------------------------
"""
        )

    def customer_menu(self, logged_in_user) -> str:
        """


        Returns
        -------
        str
            DESCRIPTION.

        """
        user_profile = logged_in_user.__dict__
        user = user_profile["user_name"]
        print(
            f"""
Hello {user},
Please select options fro the menu to access the submenu
----------------------- Customer Menu --------------------------
1. Profile Menu - Show profile/ Edit profile
2. Products Menu - Show products/ Get product by product ID
3. Manage orders
4. Generate all consumption figures
5. Logout
----------------------------------------------------------------
"""
        )

    def print_error_message(self, error_source: str, error_message: str) -> str:
        """


        Parameters
        ----------
        error_source : str
            DESCRIPTION.
        error_message : str
            DESCRIPTION.

        Returns
        -------
        str
            DESCRIPTION.

        """
        print("Error in {}: {}".format(error_source.__qualname__, error_message))

    def print_message(self, message: str) -> str:
        """


        Parameters
        ----------
        message : str
            DESCRIPTION.

        Returns
        -------
        str
            DESCRIPTION.

        """
        print(message)

    def print_object(self, target_object: str) -> None:
        string_obj = target_object.__str__()
        print(string_obj)

    def show_profile(self, logged_in_user: dict):
        """


        Parameters
        ----------
        logged_in_user : dict
            DESCRIPTION.

        Returns
        -------
        None.

        """
        # taking the dict of the user who has logged in
        user_profile = logged_in_user.__dict__
        user_id = user_profile["user_id"]
        user_name = user_profile["user_name"]
        registered_time = user_profile["user_register_time"]
        user_email = user_profile["user_email"]
        user_mobile = user_profile["user_mobile"]
        print(
            f"""
Dear {user_name},
  -------------------- Your Profile ------------------------
  Username: {user_name}
  User ID: {user_id}
  Email: {user_email}
  Phone: {user_mobile}
  Active since: {registered_time}
  ----------------------------------------------------------
"""
        )

    def show_list(self, object_list: list, user_role: str, list_type: str):
        # customer cannot view a customer list
        if user_role == "customer" and list_type == "customer":
            list_message = "You are not authored to view this list"
            self.print_message(list_message)
        else:
            data = object_list[0]
            page_no = object_list[1]
            total_pages = object_list[2]
            final_list_message = f"""
                ------------------ {list_type} Profile ------------------
                Page {page_no} of {total_pages} pages 
                """
            self.print_message(final_list_message)

            for item in data:
                self.print_object(item)

    pass
