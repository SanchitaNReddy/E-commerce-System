# Name: Sanchita Reddy
# Student ID: 33483086
# Creation Date: May 29, 2023
# Last Modified:
# Description: This program contains all the product related operations

from model_product import Product
import os
import pandas as pd
import matplotlib.pyplot as mp
import numpy as np


class ProductOperation:

    product_path = "data/product/"
    data = os.listdir(product_path)
    # variable to capture the data from the csv files
    csv_data = [file for file in data if file.endswith(".csv")]
    # reading and saving columns in the file
    final_column = Product().df_file_save_columns
    read_columns = Product().df_file_read_columns
    final_csv = []

    for file in csv_data:
        the_file = os.path.join(product_path, file)
        final_csv.append(the_file)

    def extract_products_from_file(self):
        """


        Returns
        -------
        None.

        """
        product_list = []
        for file in ProductOperation.final_csv:
            # reading the csv file and saving it as a data frame
            data_frame = pd.read_csv(file)
            # appending the final data frame
            product_list.append(data_frame)

        product_df = pd.concat(product_list, ignore_index=True)
        product_df = product_df.loc[
            :, product_df.columns.isin(ProductOperation.read_columns)
        ]
        product_df_final = product_df.drop_duplicates(subset="id")
        prod = product_df_final.copy()
        # prod_df_dinal = prod.copy()
        product_df_final = product_df_final[ProductOperation.read_columns]
        product_df_final.columns = ProductOperation.final_column

        # ensuring that everything is saved as a string
        write_file = product_df_final.astype(str)
        write_file_final = Product().write_file_df(write_file)

    def get_product_list(self, page_number: str):
        """


        Parameters
        ----------
        page_number : str
            DESCRIPTION.

        Returns
        -------
        obj
            DESCRIPTION.

        """
        products_per_page = 10

        # reading the data
        data = Product().read_file_df()

        # adding a column to the data frame for page_no
        total_prod = len(data)
        max_pages = (total_prod + products_per_page - 1) // products_per_page
        data["page_number"] = (data.index // products_per_page) + 1

        # match the data_frame
        product_page = data[data["page_number"] == int(page_number)]
        if product_page.empty:
            return ([], "0", "0")
        # converting to a product object
        product_list = []
        for _, row in product_page.iterrows():
            data_list = row.tolist()
            products = Product(
                data_list[0],
                data_list[1],
                data_list[2],
                data_list[3],
                data_list[4],
                data_list[5],
                data_list[6],
                data_list[7],
            )
            product_list.append(products)
        return (product_list, page_number, max_pages)

    def delete_product(self, product_id: str) -> bool:
        # reading the file
        data_frame = Product().read_file_df()
        if data_frame is None or data_frame.empty:
            return False

        # find the row matching the product_id
        delete_row = data_frame[data_frame[Product.product_id] == product_id]

        if delete_row.empty:
            return False

        data_frame = data_frame.drop(delete_row.index)
        Product().write_file_df(data_frame)
        return True

    def get_product_list_by_keyword(self, keyword: str):
        """


        Parameters
        ----------
        keyword : str
            DESCRIPTION.

        Returns
        -------
        prod_list : TYPE
            DESCRIPTION.

        """
        try:
            prod_list = []
            # reading the data
            data_frame = Product().read_file_df()
            # getting the row matching the keyword
            get_product_row = data_frame[Product.product_name].str.contains(
                keyword, case=False, regex=True
            )
            matched_row = data_frame[get_product_row]

            if matched_row.empty:
                return ([], "0", "0")
            else:
                matched_list = matched_row.values.tolist()
                for each in matched_list:
                    prod_list.append(
                        Product(
                            each[0],
                            each[1],
                            each[2],
                            each[3],
                            each[4],
                            each[5],
                            each[6],
                            each[7],
                        )
                    )
                return (prod_list, "0", "0")
        except:
            return ([], "0", "0")

    def get_product_by_id(self, product_id: str):
        """


        Parameters
        ----------
        product_id : str
            DESCRIPTION.

        Returns
        -------
        product_list : TYPE
            DESCRIPTION.

        """
        try:
            product_list = []
            # reading the file
            data_frame = Product().read_file_df()

            # find the row matching the product_id
            get_row = data_frame[data_frame[Product.product_id] == product_id]

            if get_row.empty:
                return ([], "0", "0")
            else:
                matched_row_list = get_row.values.tolist()
                for each in matched_row_list:
                    product_list.append(
                        Product(
                            each[0],
                            each[1],
                            each[2],
                            each[3],
                            each[4],
                            each[5],
                            each[6],
                            each[7],
                        )
                    )
                return (product_list, "0", "0")
        except:
            return ([], "0", "0")

    def delete_all_products(self):
        # creating a blank data frame
        data_frame = pd.DataFrame()
        # writing the black data frame
        updated_df = Product().write_file_df(data_frame)

    def generate_category_figure(self):
        product = Product().read_file_df()
        count_category = product["pro_category"].value_counts()
        sort_cat = count_category.sort_values(ascending=False)

        mp.bar(sort_cat.index, sort_cat.values, color="red")
        mp.xlabel("Category")
        mp.ylabel("Number of Products")
        mp.title("Total products by Category")
        mp.savefig("data/figure/enerate_category_figure.png", bbox_inches="tight")
        mp.show()

    def convert_data_type(self, df):
        df["pro_id"] = df["pro_id"].astype(str)
        df["pro_model"] = df["pro_model"].astype(str)
        df["pro_category"] = df["pro_category"].astype(str)
        df["pro_name"] = df["pro_name"].astype(str)
        df["pro_current_price"] = df["pro_current_price"].astype(float)
        df["pro_raw_price"] = df["pro_raw_price"].astype(float)
        df["pro_discount"] = df["pro_discount"].astype(float)
        df["pro_likes_count"] = df["pro_likes_count"].astype(int)
        return df

    def generate_discount_figure(self):
        product = Product().read_file_df()
        product = self.convert_data_type(product)

        discount = pd.cut(
            product["pro_discount"],
            bins=[0, 30, 60, np.inf],
            labels=["<30", "30-60", ">60"],
        ).value_counts()
        mp.pie(discount, labels=discount.index, autopct="%1.1f%%", startangle=90)
        mp.title("Products by Discount Range")
        mp.savefig("data/figure/generate_discount_figure.png", bbox_inches="tight")
        mp.show()

    def generate_likes_count_figure(self):
        product = Product().read_file_df()
        product = self.convert_data_type(product)
        likes_count = (
            product.groupby("pro_category")["pro_likes_count"]
            .sum()
            .sort_values(ascending=True)
        )
        bars = mp.barh(likes_count.index, likes_count.values, color="red")
        mp.xlabel("Total Likes Count")
        mp.ylabel("Category")
        mp.title("Total likes by Category")
        mp.savefig("data/figure/generate_likes_count_figure.png", bbox_inches="tight")
        mp.show()

    def generate_discount_likes_count_figure(self):
        product = Product().read_file_df()
        product = self.convert_data_type(product)
        mp.scatter(
            product["pro_discount"], product["pro_likes_count"], alpha=0.5, color="red"
        )
        mp.xlabel("Discount")
        mp.ylabel("Likes Count")
        mp.title("Relationship between Likes and Discount")
        mp.savefig(
            "data/figure/generate_discount_likes_count_figure", bbox_inches="tight"
        )
        mp.show()
