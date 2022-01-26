from controllers.ProductController import ProductController
from models.customer_reviews import *

pc = ProductController

class CustomerReviewController:

    customer_review_list = []

    def add_reviews(self, review_id, heading, review_text, product_id, product_name):
        review = CustomerReviews(review_id, heading, review_text, product_id, product_name)
        self.customer_review_list.append(review)

    def find_product(self, product_id):
        for product in self.customer_review_list:
            if product.product_id == product_id:
                return product.product_name

    def add_all_reviews(self):
        review = 0
        while review < len(reviews):
            crc.add_reviews(reviews[review][0], reviews[review][1], reviews[review][2], reviews[review][3], reviews[review][4])
            review += 1

    def ViewCustomerReview(self, product_id):

        review = self.find_product(product_id)
        customer_review_list = self.customer_review_list
        for reviews in customer_review_list:
            if reviews.product_name == review:
                reviews.print_review()

    def new_customer_review(self, product_id, review_titel, review_text):
        review_id = "New Customer Review"
        product_name = self.find_product(product_id)

        def find_index_position(name):
            rev = 0
            index_list = []
            while rev < len(reviews):

                if name in reviews[rev]:
                    if reviews[rev].index(name):
                        index_list.append(rev)
                    else:
                        continue
                rev += 1

            last_element = index_list[-1]

            return last_element + 1

        reviews.insert(find_index_position(product_name), self.add_reviews(review_id, review_titel, review_text, product_id, product_name))

crc = CustomerReviewController()
crc.add_all_reviews()


