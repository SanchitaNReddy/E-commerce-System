# Name: Sanchita Reddy
# Student ID: 33483086
# Creation Date: May 29, 2023
# Last Modified:
# Description: This program contains all the main related operations

from model_user import User
from io_interface import IOInterface
from operation_customer import CustomerOperation
from operation_admin import AdminOperation
from operation_user import UserOperation
from opreation_product import ProductOperation
from operation_order import OrderOperation
import numpy as np

#%%
def register_primary_admin():
    """


    Returns
    -------
    None.

    """
    # ensuring the primary admin is created when not existing
    reg = AdminOperation().register_primary_admin()
    if reg:
        IOInterface().print_message("Primary Admin created")
    else:
        pass


def open_file():
    """


    Returns
    -------
    None.

    """
    try:
        with open(User().user_file, "r+") as file:
            register_primary_admin()
    except:
        with open(User().user_file, "w+") as file:
            # ensuring the primary admin is regiestered first without multiple primary admins
            register_primary_admin()


def register_user(customer=True):
    """


    Parameters
    ----------
    customer : TYPE, optional
        DESCRIPTION. The default is True.

    Returns
    -------
    None.

    """
    customer_login = """
Thank you for choosing to register.
Please provide the below details to complete your registration:
----------------------------------------------------------------
    1. Username
    2. Password
    3. Email ID
    4. Mobile
----------------------------------------------------------------
    Points to remember while registering:
    * The username should be atleast 5 characters long; 
        It should contain only letters or underscore.
    * The password should be atleast 5 characters long; 
        It should contain atleats one alphabet and one digit.
    * The mobile number should start with 03 0r 04.
    
    Please enter your details with a single space between them: 
    """
    if customer:
        reg_input = IOInterface().get_user_input(customer_login, 4)
        user_name = reg_input[0]
        user_password = reg_input[1]
        user_email = reg_input[2]
        user_mobile = reg_input[3]
        create_cust = CustomerOperation().register_customer(
            user_name, user_password, user_email, user_mobile
        )

        if create_cust == True:
            IOInterface().print_message("You have been registered successfully!\n")
        else:
            IOInterface().print_error_message(
                CustomerOperation().register_customer,
                "\nRegistration unsuccessful.\nPlease ensure that you are providing all the required details in the correct format.",
            )
            try_register = IOInterface().get_user_input(
                "Would you like to try registering again? (y/n): ", 1
            )
            if isinstance(try_register, list):
                try_register = try_register[0]
            try_register = try_register.strip()
            if try_register == "y":
                return register_user()


def login_control():
    """


    Returns
    -------
    None.

    """
    login_message = """
To login, please provide your Username and Password.
Please enter your credentials with a space between them: 
"""
    login_input = IOInterface().get_user_input(login_message, 2)
    user_name = login_input[0]
    user_password = login_input[1]
    logged_in_user = UserOperation().login(user_name, user_password)
    if logged_in_user.user_name != "sanch":
        IOInterface().print_message("You have logged in successfully!\n")
        if logged_in_user.user_role == "customer":
            return customer_control(logged_in_user)
        if logged_in_user.user_role == "admin":
            return admin_control(logged_in_user)
    else:
        IOInterface().print_error_message(UserOperation().login, "\nLogin unsuccessful")
        try_login = IOInterface().get_user_input(
            "Would you like to try and login again? (y/n): ", 1
        )
        if isinstance(try_login, list):
            try_login = try_login[0]
        try_login = try_login.strip()
        if try_login == "y":
            return login_control()
        else:
            main()


def customer_control(logged_in_user):
    """


    Returns
    -------
    bool
        DESCRIPTION.

    """
    # calling the customer menu
    # cust_input = ""
    IOInterface().customer_menu(logged_in_user)
    cust_list = [1, 2, 3, 4, 5]
    cust_input = IOInterface().get_user_input(
        "Please input your choice [1, 2, 3, 4 or 5]: ", 1
    )
    if isinstance(cust_input, list):
        cust_input = cust_input[0]
    cust_input = cust_input.strip()
    if cust_input.isdigit() and int(cust_input) in cust_list:
        if cust_input == "1":
            customer_profile_control(logged_in_user)
        if cust_input == "2":
            customer_product_menu(logged_in_user)
        if cust_input == "3":
            customer_order_menu(logged_in_user)
        if cust_input == "4":
            IOInterface().print_message(
                "There are 3 graphs populated for you.\n1. Your product consumption.\n"
            )
            user_profile = logged_in_user.__dict__
            user = user_profile["user_id"]
            if CustomerOperation().cust_generate_single_customer_consumption_figure(
                user
            ):
                IOInterface().print_message(
                    f"The bar char has been populated for {user}"
                )
            else:
                IOInterface().print_message(
                    f"The {user} does not have any orders or has not been registered.\n"
                )
            next_input = IOInterface().get_user_input(
                "Please press 'y' to view the next figure: ", 1
            )
            if isinstance(next_input, list):
                next_input = next_input[0]
            next_input = next_input.strip()
            if next_input == "y":
                CustomerOperation().cust_generate_all_customers_consumption_figure()
                IOInterface().print_message("2. Customer consumption for a year.")
                next_input = IOInterface().get_user_input(
                    "Please press 'y' to view the next figure: ", 1
                )
                if isinstance(next_input, list):
                    next_input = next_input[0]
                next_input = next_input.strip()
                CustomerOperation().cust_generate_all_top_10_best_sellers_figure()
                IOInterface().print_message("3. The top 10 best sellers")
                return customer_control(logged_in_user)
            else:
                IOInterface().print_message("Invalid input. Please try again.")
                return customer_control(logged_in_user)
        if cust_input == "5":
            return logout()
    else:
        IOInterface().print_message("Invalid input. Please try again.")
        return customer_control(logged_in_user)


def customer_profile_control(logged_in_user):
    """


    Returns
    -------
    None.

    """
    """
    try:
        del valid, prof_input
    except:
        pass
    """
    IOInterface().print_message(
        """
-------------------- Customer Profile Menu ---------------------
1. View profile
2. Update profile
3. Delete Profile
4. Go back to the menu
----------------------------------------------------------------
"""
    )
    prof_list = [1, 2, 3, 4]
    prof_input = IOInterface().get_user_input(
        "Please input your choice from the profile menu: ", 1
    )
    if isinstance(prof_input, list):
        prof_input = prof_input[0]
    prof_input = prof_input.strip()
    if prof_input.isdigit() and int(prof_input) in prof_list:
        if prof_input == "1":
            IOInterface().show_profile(logged_in_user)
            customer_profile_control(logged_in_user)
        if prof_input == "2":
            attribute_choice = """
Please select the attribute you would like to update:
1. Email
2. Mobile
3. Password
Enter your choice here: """
            attribute_input = IOInterface().get_user_input(attribute_choice, 1)
            value = input("Enter the updated value: ")
            update_list = [1, 2, 3]
            if isinstance(attribute_input, list):
                attribute_input = attribute_input[0]
            attribute_input = attribute_input.strip()
            if attribute_input.isdigit() and int(attribute_input) in update_list:
                if attribute_input == "1":
                    attribute_name = "user_email"
                if attribute_input == "2":
                    attribute_name = "user_mobile"
                if attribute_input == "3":
                    attribute_name = "user_password"
            update = CustomerOperation().update_profile(
                logged_in_user, attribute_name, value
            )
            if update:
                IOInterface().print_message("Changes have been saved!\n")
                return customer_control(logged_in_user)
            else:
                IOInterface().print_error_message(
                    CustomerOperation().update_profile,
                    "\nUpdate failed. Returning to main",
                )
                return customer_profile_control(logged_in_user)
        if prof_input == "3":
            user_profile = logged_in_user.__dict__
            user = user_profile["user_id"]
            delete_user = CustomerOperation().delete_customer(user)
            if delete_user:
                IOInterface().print_message("Your account has been deleted\n!")
                return main()
            else:
                IOInterface().print_error_message(
                    CustomerOperation().delete_customer,
                    "\nYour account could not be deleted!\n",
                )
                return main()
        if prof_input == "4":
            IOInterface().print_message("Going back to the menu\n")
            return customer_control(logged_in_user)
    else:
        IOInterface().print_message("Invalid input. Please try again\n")
        return customer_profile_control(logged_in_user)

    pass


def customer_product_menu(logged_in_user):
    """


    Returns
    -------
    None.

    """
    IOInterface().print_message(
        """
-------------------- Customer Product Menu ---------------------
1. Search product
2. Place an order
3. Go back to main menu
----------------------------------------------------------------
"""
    )
    prod_list = [1, 2, 3]
    prod_input = IOInterface().get_user_input(
        "Please input your choice from the profile menu: ", 1
    )
    if isinstance(prod_input, list):
        prod_input = prod_input[0]
    prod_input = prod_input.strip()
    if prod_input.isdigit() and int(prod_input) in prod_list:
        if prod_input == "1":
            search_prod_message = """ 
How would you like to search for products?
    1. By product ID
    2. By page number
    3. Keyword search
Please input your choice here: """
            search_prod_list = [1, 2, 3]
            search_prod_input = IOInterface().get_user_input(search_prod_message, 1)
            if isinstance(search_prod_input, list):
                search_prod_input = search_prod_input[0]
            search_prod_input = search_prod_input.strip()
            if (
                search_prod_input.isdigit()
                and int(search_prod_input) in search_prod_list
            ):
                if search_prod_input == "1":
                    s_input = IOInterface().get_user_input(
                        "Please input a product ID: ", 1
                    )
                    if isinstance(s_input, list):
                        s_input = s_input[0]
                    search_result = ProductOperation().get_product_by_id(s_input)
                    product = list(search_result)
                    if len(product[0]) == 0:
                        IOInterface().print_error_message(
                            ProductOperation().get_product_by_id,
                            "Unable to find the item. Please try again.\n",
                        )
                        return customer_product_menu(logged_in_user)
                    else:
                        IOInterface().show_list(
                            search_result, user_role="customer", list_type="product"
                        )
                        return customer_product_menu(logged_in_user)
                if search_prod_input == "2":
                    p_input = IOInterface().get_user_input(
                        "Please input the page number [1 - 7,450]: ", 1
                    )
                    if isinstance(p_input, list):
                        p_input = p_input[0]
                    p_input = p_input.strip()
                    page_result = ProductOperation().get_product_list(p_input)
                    page = list(page_result)
                    if len(page[0]) == 0:
                        IOInterface().print_error_message(
                            ProductOperation().get_product_list,
                            "Unable to find the item. Please try again.\n",
                        )
                        return customer_product_menu(logged_in_user)
                    else:
                        IOInterface().show_list(page_result, "customer", "product")
                        return customer_product_menu(logged_in_user)
                if search_prod_input == "3":
                    p_input = IOInterface().get_user_input(
                        "Please input the keyword you are searching for [Only slingle word key search]: ",
                        1,
                    )
                    if isinstance(p_input, list):
                        p_input = p_input[0]
                    p_input = p_input.strip()
                    page_result = ProductOperation().get_product_list_by_keyword(
                        p_input
                    )
                    page = list(page_result)
                    if len(page[0]) == 0:
                        IOInterface().print_error_message(
                            ProductOperation().get_product_list_by_keyword,
                            "Unable to find the item. Please try again.\n",
                        )
                        return customer_product_menu(logged_in_user)
                    else:
                        IOInterface().show_list(page_result, "customer", "product")
                        return customer_product_menu(logged_in_user)
            else:
                IOInterface().print_message("Invalid input. Please try again")
                return customer_product_menu(logged_in_user)
        if prod_input == "2":
            create_order_message = """
You will need to provide a product ID to place an order. To view products, please go back to the previous menu and choose the 'Search product' option.
Please input the product ID here: """
            create_order_input = IOInterface().get_user_input(create_order_message, 1)
            if isinstance(create_order_input, list):
                create_order_input = create_order_input[0]
            user_profile = logged_in_user.__dict__
            user_id = user_profile["user_id"]
            create_order = OrderOperation().create_order(user_id, create_order_input)
            if create_order:
                IOInterface().print_message("Your order has been successfully created.")
                return customer_control(logged_in_user)
            else:
                IOInterface().print_error_message(
                    OrderOperation().create_order,
                    "\nYour order could not be created. Please check your product ID again.",
                )
                return customer_control(logged_in_user)
        if prod_input == "3":
            IOInterface().print_message("Going back to the previous menu.")
            return customer_control(logged_in_user)
    else:
        IOInterface().print_message("Invalid input. Please try again")
        return customer_product_menu(logged_in_user)


def customer_order_menu(logged_in_user):
    cust_menu = """
Manage your orders:
    1. View your order history
    2. Delete orders
    3. Go back to previous menu
Please enter your choice here: """
    cust_list = [1, 2, 3]
    cust_input = IOInterface().get_user_input(cust_menu, 1)
    if isinstance(cust_input, list):
        cust_input = cust_input[0]
    cust_input = cust_input.strip()
    if cust_input.isdigit() and int(cust_input) in cust_list:
        if cust_input == "1":
            order_his_input = IOInterface().get_user_input(
                "Please enter the page number of orders: ", 1
            )
            if isinstance(order_his_input, list):
                order_his_input = order_his_input[0]
            order_his_input = order_his_input.strip()
            user_profile = logged_in_user.__dict__
            user_id = user_profile["user_id"]
            order_his = OrderOperation().get_order_list(user_id, order_his_input)
            if len(order_his[0]) == 0:
                IOInterface().print_error_message(
                    OrderOperation().get_order_list, "\nNo orders could be found\n"
                )
                return customer_order_menu(logged_in_user)
            else:
                page_list = list(order_his)
                IOInterface().show_list(
                    page_list, user_role="customer", list_type="order"
                )
                return customer_order_menu(logged_in_user)
        if cust_input == "2":
            order_del_input = IOInterface().get_user_input(
                "Please enter the order ID to delete: ", 1
            )
            if isinstance(order_del_input, list):
                order_del_input = order_del_input[0]
            order_del_input = order_del_input.strip()
            delete_order = OrderOperation().delete_order(order_del_input)
            if delete_order:
                IOInterface().print_message("The order has been deleted.")
                return customer_order_menu(logged_in_user)
            else:
                IOInterface().print_error_message(
                    OrderOperation().delete_order,
                    "\nYour order has not been deleted. Try again.\n",
                )
                return customer_order_menu(logged_in_user)
        if cust_input == "3":
            IOInterface().print_message("Going back to the previous menu.")
            return customer_control(logged_in_user)
    else:
        IOInterface().print_message("Invalid input. Please try again")
        return customer_order_menu(logged_in_user)


def admin_control(logged_in_user):
    ad_list = [1, 2, 3, 4, 5, 6, 7, 8]
    IOInterface().admin_menu(logged_in_user)
    ad_input = IOInterface().get_user_input("Please input your choice [1 - 8]: ", 1)
    if isinstance(ad_input, list):
        ad_input = ad_input[0]
    ad_input = ad_input.strip()
    if ad_input.isdigit() and int(ad_input) in ad_list:
        if ad_input == "1":
            admin_product_menu(logged_in_user)
        if ad_input == "2":
            admin_customer_menu(logged_in_user)
        if ad_input == "3":
            admin_order_menu(logged_in_user)
        if ad_input == "4":
            IOInterface().print_message(
                "Here are the updated statistical figures for you...\nCategory figures"
            )
            AdminOperation().ad_generate_category_figure()
            next_input = IOInterface().get_user_input(
                "Please press 'y' to view the next figure: ", 1
            )
            if isinstance(next_input, list):
                next_input = next_input[0]
            next_input = next_input.strip()
            if next_input == "y":
                IOInterface().print_message(
                    "The next graph shows the product discount trends..."
                )
                AdminOperation().ad_generate_discount_figure()
                next_input = IOInterface().get_user_input(
                    "Please press 'y' to view the next figure: ", 1
                )
                if isinstance(next_input, list):
                    next_input = next_input[0]
                next_input = next_input.strip()
                if next_input == "y":
                    IOInterface().print_message(
                        "The next graph shows the product discount trends along with like responses from customers..."
                    )
                    AdminOperation().ad_generate_discount_likes_count_figure()
                    next_input = IOInterface().get_user_input(
                        "Please press 'y' to view the next figure: ", 1
                    )
                    if isinstance(next_input, list):
                        next_input = next_input[0]
                    next_input = next_input.strip()
                    if next_input == "y":
                        IOInterface().print_message(
                            "The final graph shows the customer likes trends..."
                        )
                        AdminOperation().ad_generate_likes_count_figure()
                        return admin_control(logged_in_user)

            else:
                IOInterface().print_message("Going back to the menu")
                return admin_control(logged_in_user)
        if ad_input == "5":
            gen_input = IOInterface().get_user_input(
                "Are you sure you would like to generate the test data?\nIt will re-write your existing data/nPlease select (y/n): ",
                1,
            )
            if isinstance(gen_input, list):
                gen_input = gen_input[0]
            gen_input = gen_input.strip()
            if gen_input == "y":
                OrderOperation().generate_test_data()
                IOInterface().print_message(
                    "The test data has been successfully generated."
                )
                return admin_control(logged_in_user)
            else:
                IOInterface().print_message(
                    "The test data could not be generated. Please try again."
                )
                return admin_control(logged_in_user)
        if ad_input == "6":
            return logout()
        else:
            IOInterface().print_message("Invalid input. Please try again")
            try_login = IOInterface().get_user_input(
                "Would you like to try and login again? (y/n): ", 1
            )
            if isinstance(try_login, list):
                try_login = try_login[0]
            try_login = try_login.strip()
            if try_login == "y":
                return admin_control(logged_in_user)
            else:
                return main()


def admin_product_menu(logged_in_user):
    """


    Returns
    -------
    None.

    """
    print(
        """
Hello admin,
Please select your choice from the below
-------------------- Admin Product Menu ------------------------
1. Search products
2. Delete products
3. Load products
4. Back to main menu
----------------------------------------------------------------
"""
    )
    prod_list = [1, 2, 3, 4]
    admin_prod_input = IOInterface().get_user_input(
        "Please share your choice here: ", 1
    )
    if isinstance(admin_prod_input, list):
        admin_prod_input = admin_prod_input[0]
    admin_prod_input = admin_prod_input.strip()
    if admin_prod_input.isdigit() and int(admin_prod_input) in prod_list:
        if admin_prod_input == "1":
            search_message = """
How would you like to view products:
    1. By product ID
    2. By page number
Please choose one option here [1, 2]: """
            search_list = [1, 2]
            search_input = IOInterface().get_user_input(search_message, 1)
            if isinstance(search_input, list):
                search_input = search_input[0]
            search_input = search_input.strip()
            if search_input.isdigit() and int(search_input) in search_list:
                if search_input == "1":
                    s_input = IOInterface().get_user_input(
                        "Please input a product ID: ", 1
                    )
                    if isinstance(s_input, list):
                        s_input = s_input[0]
                    search_result = ProductOperation().get_product_by_id(s_input)
                    search_list = list(search_result)
                    if len(search_list[0]) == 0:
                        IOInterface().print_error_message(
                            ProductOperation().get_product_by_id,
                            "Unable to find the item. Please try again.",
                        )
                        return admin_product_menu(logged_in_user)
                    else:
                        IOInterface().show_list(
                            search_list, user_role="admin", list_type="product"
                        )
                        return admin_product_menu(logged_in_user)
                if search_input == "2":
                    p_input = IOInterface().get_user_input(
                        "Please input the page number [1 - 7,450]: ", 1
                    )
                    if isinstance(p_input, list):
                        p_input = p_input[0]
                    p_input = p_input.strip()
                    page_result = ProductOperation().get_product_list(p_input)
                    page_list = list(page_result[0])
                    IOInterface().show_list(page_result, "admin", "product")
                    return admin_product_menu(logged_in_user)
                    if len(page_list) == 0:
                        IOInterface().print_error_message(
                            ProductOperation().get_product_list,
                            "\nUnable to find the item. Please try again.",
                        )
                        return admin_product_menu(logged_in_user)
            else:
                IOInterface().print_message("Invalid input. Please try again")
                return admin_product_menu(logged_in_user)
        if admin_prod_input == "2":
            delete_message = """
How would you like to delete products:
1. By product ID
2. By all products
Please choose one option here [1, 2]: """
            delete_list = [1, 2]
            delete_input = IOInterface().get_user_input(delete_message, 1)
            if isinstance(delete_input, list):
                delete_input = delete_input[0]
            delete_input = delete_input.strip()
            if delete_input.isdigit() and int(delete_input) in delete_list:
                if delete_input == "1":
                    id_input = IOInterface().get_user_input(
                        "Please input the product ID you would like to delete: ", 1
                    )
                    if isinstance(id_input, list):
                        id_input = id_input[0]
                    id_input = id_input.strip()
                    delete_row = ProductOperation().delete_product(id_input)
                    if delete_row:
                        IOInterface().print_message(
                            "The product was deleted successfully."
                        )
                        return admin_product_menu(logged_in_user)
                    else:
                        IOInterface().print_error_message(
                            ProductOperation().delete_product,
                            "\nThe product was not deleted. Please try again.",
                        )
                        return admin_product_menu(logged_in_user)
                if delete_input == "2":
                    ProductOperation().delete_all_products()
                    IOInterface().print_message("All products have been deleted.")
                    reload = IOInterface().get_user_input(
                        "Since you have deleted all the data, would you like to reload the product data? (y/n): ",
                        1,
                    )
                    if isinstance(reload, list):
                        reload = reload[0]
                    reload = reload.strip()
                    if reload == "y":
                        ProductOperation().extract_products_from_file()
                        IOInterface().print_message(
                            "The product database has been updated."
                        )
                        return admin_product_menu(logged_in_user)
                    else:
                        return admin_product_menu(logged_in_user)
            else:
                IOInterface().print_message("Invalid input. Please try again")
                return admin_product_menu(logged_in_user)
        if admin_prod_input == "3":
            load = IOInterface().get_user_input(
                "Please note that loading products will re-write the product database to default. Select 'y' to continue. (y/n): ",
                1,
            )
            if isinstance(load, list):
                load = load[0]
            load = load.strip()
            if load == "y":
                ProductOperation().extract_products_from_file()
                IOInterface().print_message("The product database has been updated.")
                return admin_product_menu(logged_in_user)
            else:
                return admin_product_menu(logged_in_user)
        if admin_prod_input == "4":
            IOInterface().print_message("Going back to the previous menu.")
            return admin_control(logged_in_user)
    else:
        IOInterface().print_message("Invalid input. Please try again")
        return admin_product_menu(logged_in_user)


def admin_customer_menu(logged_in_user):
    """


    Returns
    -------
    None.

    """
    print(
        """
Hello admin,
Please select your choice from the below
-------------------- Admin Profile Menu ------------------------
1. Search user
2. Add user
3. Delete user
4. Back to main menu
----------------------------------------------------------------
"""
    )
    ad_cust_input = IOInterface().get_user_input(
        "Please enter your choice here [1 - 4]: ", 1
    )
    ad_cust_list = [1, 2, 3, 4]
    if isinstance(ad_cust_input, list):
        ad_cust_input = ad_cust_input[0]
    ad_cust_input = ad_cust_input.strip()
    if ad_cust_input.isdigit() and int(ad_cust_input) in ad_cust_list:
        if ad_cust_input == "1":
            search_message = """
How would you like to search a user:
1. User ID
2. Page Number
Please enter your choice: """
            search_input = IOInterface().get_user_input(search_message, 1)
            search_list = [1, 2]
            if isinstance(search_input, list):
                search_input = search_input[0]
            search_input = search_input.strip()
            if search_input.isdigit() and int(search_input) in search_list:
                if search_input == "1":
                    input_search_data = IOInterface().get_user_input(
                        "Please input the User ID you would like to search for: ", 1
                    )
                    if isinstance(input_search_data, list):
                        input_search_data = input_search_data[0]
                    search_cust = AdminOperation().show_customer(
                        input_search_data, page_no=False, cust_id=True
                    )
                    if len(search_cust[0]) == 0:
                        IOInterface().print_error_message(
                            AdminOperation().show_customer,
                            "\nYou have entered an invalid input or the user does not exist. Redirecting you to the previous menu.",
                        )
                        return admin_customer_menu(logged_in_user)
                    else:
                        show_list = list(search_cust)
                        IOInterface().show_list(
                            show_list, user_role="admin", list_type="customer"
                        )
                        return admin_customer_menu(logged_in_user)
                if search_input == "2":
                    input_search_data = IOInterface().get_user_input(
                        "Please input the Page number you would like to search for: ", 1
                    )
                    if isinstance(input_search_data, list):
                        input_search_data = input_search_data[0]
                    input_search_data = input_search_data.strip()
                    search_cust = AdminOperation().show_customer(
                        input_search_data, page_no=True, cust_id=False
                    )
                    if len(search_cust[0]) == 0:
                        IOInterface().print_error_message(
                            AdminOperation().show_customer,
                            "\nYou have entered an invalid input or the page does not exist. Redirecting you to the previous menu.",
                        )
                        return admin_customer_menu(logged_in_user)
                    else:
                        show_list = list(search_cust)
                        IOInterface().show_list(
                            show_list, user_role="admin", list_type="customer"
                        )
                        return admin_customer_menu(logged_in_user)
            else:
                IOInterface().print_message("Invalid input. Please try again")
                return admin_customer_menu(logged_in_user)
        if ad_cust_input == "2":
            input_message = """
Who would you like to add:
    1. Admin
    2. Customer
Please input your choice here: """
            add_input = IOInterface().get_user_input(input_message, 1)
            add_list = [1, 2]
            if isinstance(add_input, list):
                add_input = add_input[0]
            add_input = add_input.strip()
            if add_input.isdigit() and int(add_input) in add_list:
                if add_input == "1":
                    user_prof = logged_in_user.__dict__
                    user_name = user_prof["user_name"]
                    if user_name == "primary_admin":
                        add_admin_message = """
Please provide the username to complete your registration:
Points to remember while registering:
* A default password "password123" has been set.
* The username should be atleast 5 characters long; 
    It should contain only letters or underscore.

Please enter the username here: """
                        det_input = IOInterface().get_user_input(add_admin_message, 1)
                        user_name = det_input[0]
                        register_ad = AdminOperation().add_admin(user_name)
                        if register_ad:
                            IOInterface().print_message(
                                "Admin has been successfully registered!"
                            )
                            return admin_customer_menu(logged_in_user)
                        else:
                            IOInterface().print_error_message(
                                AdminOperation().add_admin,
                                "\nAdmin was not registered. Please try again.\n",
                            )
                            return admin_customer_menu(logged_in_user)
                    else:
                        IOInterface().print_error_message(
                            AdminOperation().add_admin,
                            "\nYou are not authorised to register a new admin.\n",
                        )
                        return admin_customer_menu(logged_in_user)
                if add_input == "2":
                    add_message = """
Please provide the below details to complete your registration:
----------------------------------------------------------------
    1. Username
    2. Email ID
    3. Mobile
----------------------------------------------------------------
    Points to remember while registering:
    * A default password "password123" has been set.
    * The username should be atleast 5 characters long; 
        It should contain only letters or underscore.
    * The mobile number should start with 03 0r 04.
    
    Please enter your details with a single space between them: """
                    add_input = IOInterface().get_user_input(add_message, 3)
                    user_name = add_input[0]
                    user_email = add_input[1]
                    user_mobile = add_input[2]
                    # registering the new customer
                    register = AdminOperation().add_customer(
                        user_name, user_email, user_mobile
                    )
                    if register:
                        IOInterface().print_message(
                            "Customer has been successfully registered!"
                        )
                        return admin_customer_menu(logged_in_user)
                    else:
                        IOInterface().print_error_message(
                            AdminOperation().add_customer,
                            "\nCustomer was not registered. Please try again.",
                        )
                        return admin_customer_menu(logged_in_user)
                else:
                    IOInterface().print_message("Invalid input. Please try again")
                    return admin_customer_menu(logged_in_user)
        if ad_cust_input == "3":
            delete_message = """
How would you like to delete users?
1. One customer by customer ID
2. All customers
3. One admin
Select you option here [1, 2, 3]: """
            delete_input = IOInterface().get_user_input(delete_message, 1)
            delete_list = [1, 2, 3]
            if isinstance(delete_input, list):
                delete_input = delete_input[0]
            delete_input = delete_input.strip()
            if delete_input.isdigit() and int(delete_input) in delete_list:
                if delete_input == "1":
                    del_id_input = IOInterface().get_user_input(
                        "Please enter the customer ID you would like to delete: ", 1
                    )
                    if isinstance(del_id_input, list):
                        del_id_input = del_id_input[0]
                    del_id_input = del_id_input.strip()
                    delete = AdminOperation().delete_cust_admin(del_id_input)
                    if delete:
                        IOInterface().print_message(
                            "Customer has been successfully deleted!"
                        )
                        return admin_customer_menu(logged_in_user)
                    else:
                        IOInterface().print_error_message(
                            AdminOperation().delete_cust_admin,
                            "\nCustomer was not deleted. Please try again.",
                        )
                        return admin_customer_menu(logged_in_user)
                if delete_input == "2":
                    AdminOperation().delete_all_cust_admin()
                    IOInterface().print_message(
                        "All customers have been deleted. Returning to main menu."
                    )
                    return admin_customer_menu(logged_in_user)
                if delete_input == "3":
                    logged_in_user_dict = logged_in_user.__dict__
                    user_name = logged_in_user_dict["user_name"]
                    if user_name == "primary_admin":
                        del_id_input = IOInterface().get_user_input(
                            "Please enter the admin ID you would like to delete: ", 1
                        )
                        if isinstance(del_id_input, list):
                            del_id_input = del_id_input[0]
                        del_id_input = del_id_input.strip()
                        delete = AdminOperation().delete_admin(del_id_input)
                        if delete:
                            IOInterface().print_message(
                                "Admin has been successfully deleted!"
                            )
                            return admin_customer_menu(logged_in_user)
                        else:
                            IOInterface().print_error_message(
                                AdminOperation().delete_admin,
                                "\nUnsuccessful. Please try again.",
                            )
                            return admin_customer_menu(logged_in_user)
                    else:
                        IOInterface().print_message(
                            "You are not authorised to register a new admin."
                        )
                        return admin_customer_menu(logged_in_user)
            else:
                IOInterface().print_message("Invalid input. Please try again")
                return admin_customer_menu(logged_in_user)
        if ad_cust_input == "4":
            IOInterface().print_message("Going back to the Admin menu")
            return admin_control(logged_in_user)
    else:
        IOInterface().print_message("Invalid input. Please try again")
        return admin_customer_menu(logged_in_user)


def admin_order_menu(logged_in_user):
    """


    Returns
    -------
    None.

    """
    ord_message = """
Hello admin,
Please select your choice from the below
-------------------- Admin Product Menu ------------------------
1. Search orders
2. Delete orders
3. Back to main menu
----------------------------------------------------------------
Please input your choice: """
    ord_list = [1, 2, 3]
    ord_input = IOInterface().get_user_input(ord_message, 1)
    if isinstance(ord_input, list):
        ord_input = ord_input[0]
    ord_input = ord_input.strip()
    if ord_input.isdigit() and int(ord_input) in ord_list:
        if ord_input == "1":
            search_ord_message = """
Please input the below with a space to search for orders:
    Customer ID
    Page number
Please enter your choice in the order [customer_id page_number]: """
            search_ord_input = IOInterface().get_user_input(search_ord_message, 2)
            user_id = search_ord_input[0]
            page_no = search_ord_input[1]
            page_result = OrderOperation().get_order_list(user_id, page_no)
            if len(page_result[0]) == 0:
                IOInterface().print_error_message(
                    OrderOperation().get_order_list,
                    f"\nNo orders could be found for {page_result[0]} and {page_result[1]}",
                )
                return admin_order_menu(logged_in_user)
            else:
                page_list = list(page_result)
                IOInterface().show_list(page_list, user_role="admin", list_type="order")
                return admin_order_menu(logged_in_user)
        if ord_input == "2":
            del_ord_message = """
How would you like to delete orders?
1. Delete orders by order ID
2. Delete all orders
Please input your choice here: """
            del_ord_list = [1, 2]
            del_ord_input = IOInterface().get_user_input(del_ord_message, 1)
            if isinstance(del_ord_input, list):
                del_ord_input = del_ord_input[0]
            del_ord_input = del_ord_input.strip()
            if del_ord_input.isdigit() and int(del_ord_input) in del_ord_list:
                if del_ord_input == "1":
                    del_id_input = IOInterface().get_user_input(
                        "Please enter the order ID you would like to input: ", 1
                    )
                    if isinstance(del_id_input, list):
                        del_id_input = del_id_input[0]
                    del_id_input = del_id_input.strip()
                    delete_order = OrderOperation().delete_order(del_id_input)
                    if delete_order:
                        IOInterface().print_message("The order has been deleted.")
                        return admin_order_menu(logged_in_user)
                    else:
                        IOInterface().print_error_message(
                            OrderOperation().delete_order,
                            "\nYour order has not been deleted. Try again.",
                        )
                        return admin_order_menu(logged_in_user)
                if del_ord_input == "2":
                    OrderOperation().delete_all_orders()
                    IOInterface().print_message("All orders have been deleted.")
                    return admin_order_menu(logged_in_user)
            else:
                IOInterface().print_message("Invalid input. Please try again")
                return admin_order_menu(logged_in_user)
        if ord_input == "3":
            IOInterface().print_message("Going back to the Admin menu")
            return admin_control(logged_in_user)
    else:
        IOInterface().print_message("Invalid input. Please try again")
        return admin_order_menu(logged_in_user)


def logout():
    IOInterface().print_message("You have been logged out.")
    return main()


def main():
    while True:
        # Opening of a file and handling incase the file does noy exist
        open_file()
        # ensure products are loaded
        IOInterface().print_message(
            """
----------------------------------------------------------------
----------------------------------------------------------------
MONASH EasyBuy.com
An interactive e-commerce platform for retail convenience!
----------------------------------------------------------------
----------------------------------------------------------------
"""
        )
        # printing the main menu
        IOInterface().main_menu()
        # Seeking input from the user
        user_input = IOInterface().get_user_input(
            "Enter the number corresponding to your choice: ", 1
        )
        user_list = [1, 2, 3]
        if isinstance(user_input, list):
            user_input = user_input[0]
        user_input = user_input.strip()
        if user_input.isdigit() and int(user_input) in user_list:
            if user_input[0] == "1":
                login_control()
            if user_input[0] == "2":
                register_user()
            if user_input[0] == "3":
                IOInterface().print_message("You have chosen to exit. Thank you.")
                break
        else:
            IOInterface().print_message("Invalid input. Please try again")
        pass


if __name__ == "__main__":
    main()
