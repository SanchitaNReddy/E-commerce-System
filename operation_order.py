# Name: Sanchita Reddy
# Student ID: 33483086
# Creation Date: May 29, 2023
# Last Modified: 
# Description: This program contains all the order related operations

import random
import string
import pandas as pd
from model_order import Order
from opreation_product import ProductOperation
from model_user import User
from model_product import Product
import matplotlib.pyplot as mp

class OrderOperation:
    
    def generate_unique_order_id(self) -> str:
        """


        Returns
        -------
        str
            DESCRIPTION.

        """
        # using the read_file_df function to get a data frame
        data_frame = Order().read_file_df()

        if(data_frame.empty):
            return "o_" + str(random.randint(10000, 99999))

        data_array = pd.Series(data_frame[Order.order_id])

        while True:
            new_order_id = "o_" + str(random.randint(10000, 99999))
            # ensuring the generated user_id does not exist
            if new_order_id not in data_array.values:
                return new_order_id
            
            
    def create_order(self, cust_id: str, pro_id: str, create_time=None) -> bool:
        """
        

        Parameters
        ----------
        cust_id : str
            DESCRIPTION.
        product_id : str
            DESCRIPTION.
        create_time : TYPE, optional
            DESCRIPTION. The default is None.

        Returns
        -------
        bool
            DESCRIPTION.

        """
        #checking if product exists
        product = ProductOperation().get_product_by_id(pro_id)
        if len(product[0]) == 0:
            return False
        else:
            if create_time is None:
                create_time = Order().current_order_time()
            order_id = self.generate_unique_order_id()
            order_obj = Order(order_id = order_id, user_id = cust_id, pro_id=pro_id, order_time_stamp=create_time)
            order_df = pd.DataFrame(order_obj.__dict__, index=[0])
            #writing to the order file
            existing_df = Order().read_file_df()
            updated_df = Order().append_df(existing_df, order_df)
            #writing to file
            order_obj.write_file_df(updated_df)
            return True
                            
    def delete_order(self, order_id: str) -> bool:
        """
        

        Parameters
        ----------
        order_id : str
            DESCRIPTION.

        Returns
        -------
        bool
            DESCRIPTION.

        """
        order_exists = Order().search_order(order_id, order_id=True, user_id=False)
        if order_exists.empty:
            return False
        else:
            old_df = Order().read_file_df()
            old_df = old_df[old_df[Order.order_id] != order_id].copy()
            Order().write_file_df(old_df)
            return True
          
    def get_order_list(self, user_id: str, page_no: str) -> tuple:
        """
        

        Parameters
        ----------
        user_id : str
            DESCRIPTION.
        page_no : str
            DESCRIPTION.

        Returns
        -------
        tuple
            DESCRIPTION.

        """
        #If page page number is blank or none
        try:
            page_no = int(page_no)
            
            #read the file
            order_df = Order().read_file_df()
            user_order = order_df[order_df['user_id'] == user_id]
            total_orders = len(user_order)
            total_pages = (total_orders // 10) + 1
            
            if page_no < 1 or page_no > total_pages:
                return ([], page_no, total_pages)
            
            s_index = (int(page_no) - 1) * 10
            e_index = min(s_index + 10, total_orders)
            order_list = []
            for _, row in user_order.iloc[s_index:e_index].iterrows():
                order_obj = Order(order_id=row["order_id"],user_id=row["user_id"],pro_id=row["pro_id"],order_time_stamp=row["order_time_stamp"])
                order_list.append(order_obj)
                #returning the list as a tuple with page number and total pages
            return order_list, page_no, total_pages
        except:
            return([], 0, 0)
    
    def delete_all_orders(self):
        """
        

        Returns
        -------
        None.

        """
        #creating a blank data frame
        data_frame = pd.DataFrame()
        #writing the black data frame
        updated_df = Order().write_file_df(data_frame)
        
    def generate_test_data(self) -> bool:
        #generating a random email id for users
        def gen_random_email() -> str:
            username = ''.join(random.choice(string.ascii_lowercase) for _ in range(random.randint(5, 10)))
            domain = ''.join(random.choice(string.ascii_lowercase) for _ in range(random.randint(5, 10)))
            domain_ext = random.choice(['com', 'edu'])
            return f"{username}@{domain}.{domain_ext}"

        #generating user_names at random
        def gen_usernames(ex_user_name: set) -> str:
            while True:
                user_name = ''.join(random.choice(string.ascii_lowercase + '_') for _ in range(random.randint(6, 10)))
                if user_name not in ex_user_name:
                    ex_user_name.add(user_name)
                    return user_name
        
        #generating mobile numbers at random
        def gen_mobile() -> str:
            start = random.choice(["03", "04"])
            nums = [start] + [str(random.randint(0, 9)) for _ in range(8)]
            final = ''.join(nums)
            return final
            
        def random_time() -> str:
            day = random.randint(1, 30)
            month = random.randint(1, 12)
            year = random.randint(2022, 2022)
            hour = random.randint(0, 23)
            minute = random.randint(0, 59)
            sec = random.randint(0, 59)
            return f"{day:02d}-{month:02d}-{year:02d}_{hour:02d}:{minute:02d}:{sec:02d}"
        
        #test users
        ex_user_names = set(User().read_file_df()["user_name"])
        set_user = []
        for _ in range(10):
            user_name = gen_usernames(ex_user_names)
            ex_user_names.add(user_name)
            mail = gen_random_email()
            phone = gen_mobile()
            password = "jungle123"
            #tuple format
            set_user.append((user_name, password, mail, phone))
            
        #registering these users
        from operation_customer import CustomerOperation
        for user_name, password, mail, phone in set_user:
            CustomerOperation().register_customer(user_name=user_name, user_password=password, user_email=mail, user_mobile=phone)
        
        new_data_frame = User().read_file_df()
        final_df = new_data_frame[new_data_frame["user_name"].isin([user_name for user_name, _, _, _ in set_user])]
        
        #get the product data
        product = Product().read_file_df()
        
        #test orders
        for _, user_row in final_df.iterrows():
            cust_id = user_row["user_id"]
            orders = random.randint(50, 200)
            
            for _ in range(orders):
                pro_id = random.choice(product["pro_id"])
                order_time = random_time()
                OrderOperation().create_order(cust_id=cust_id, pro_id=pro_id, create_time=order_time)

    
    def generate_single_customer_consumption_figure(self, cust_id: str):
        #get orders for specified customers
        read_product = Product().read_file_df()
        read_product['pro_current_price'] = read_product['pro_current_price'].astype(float)
        read_product['pro_discount'] = read_product['pro_discount'].astype(float)
        
        read_orders = Order().read_file_df()
        if cust_id in read_orders['user_id'].values:
            merge_df = pd.merge(read_orders, read_product, on='pro_id')
            merge_df['order_time_stamp'] = pd.to_datetime(merge_df['order_time_stamp'],format='%d-%m-%Y_%H:%M:%S')
            merge_df['month'] = merge_df['order_time_stamp'].dt.month
            
            filter_df = merge_df[merge_df['user_id'] == cust_id]
            filter_df.loc[:,'discounted_price'] = filter_df['pro_current_price'] - (filter_df['pro_current_price'] * filter_df['pro_discount'] / 100)
            consumption_month = filter_df.groupby('month')['discounted_price'].sum()
            
            #visualisation with modifications and formatting
            fig, ax = mp.subplots()
            mp.bar(consumption_month.index, consumption_month.values, color='red')
            mp.xlabel('Month')
            mp.ylabel('Total Consumption')
            mp.title('Monthly consumption for Customer {}'.format(cust_id))
            
            ax.set_xticks(consumption_month.index)
            ax.set_xticklabels(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
            mp.savefig('data/figure/generate_single_customer_consumption_figure.png', bbox_inches='tight')
            mp.show()
            return True
        else:
            return False
        
    def generate_all_customers_consumption_figure(self):
        read_product = Product().read_file_df()
        read_orders = Order().read_file_df()
        merge_data = pd.merge(read_orders, read_product, on='pro_id')
        merge_data['order_time_stamp'] = pd.to_datetime(merge_data['order_time_stamp'], format='%d-%m-%Y_%H:%M:%S')
        merge_data['month'] = merge_data['order_time_stamp'].dt.month
        merge_data['order_price'] = merge_data['pro_current_price'].astype(float) - (merge_data['pro_current_price'].astype(float) * merge_data['pro_discount'].astype(float) / 100)
        total_consum = merge_data.groupby('month')['order_price'].sum()
        mp.bar(total_consum.index, total_consum.values, color='red')
        mp.xlabel('Month')
        mp.ylabel('Total Consumption')
        mp.title('Total consumption for Customer')
        months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
        mp.xticks(total_consum.index, months)
        mp.savefig('data/figure/generate_all_customers_consumption_figure.png', bbox_inches='tight')
        mp.show()
        
    def generate_all_top_10_best_sellers_figure(self):
        read_product = Product().read_file_df()
        read_orders = Order().read_file_df()
        merge_data = pd.merge(read_orders, read_product, on='pro_id')
        #no of orders per product
        order_count = merge_data['pro_id'].value_counts()
        
        #sorting in descending order
        top_sellers = order_count.sort_values(ascending=False).head(10)
        
        mp.bar(top_sellers.index, top_sellers.values, color='red')
        mp.xlabel('Product ID')
        mp.ylabel('Order Count')
        mp.title('Top 10 Best Sel')
        mp.savefig('data/figure/generate_all_top_10_best_sellers_figure.png', bbox_inches='tight')
        mp.show()
    
    
    