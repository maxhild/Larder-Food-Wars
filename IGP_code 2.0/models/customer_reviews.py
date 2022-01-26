from addons.functions import *
class CustomerReviews:

    review_id = None
    heading = None
    review_text = None

    def __init__(self, review_id, heading, review_text, product_id, product_name):

        self.review_id = review_id
        self.heading = heading
        self.review_text = review_text
        self.product_id = product_id
        self.product_name = product_name

    def print_review(self):

        print("Review ID:", self.review_id)
        print("Titel:", self.heading)
        print("Review Text:", self.review_text)

reviews = [[" Review 1:", "Great Keyboard!", "since i use the keyboard i finally enjoy programming! Simply Great!", id_one, name_one],
                    [" Review 2:", "What´s this???", "whenever i play on pc the keyboard rakes and i lose every level! extremly worse!", id_one, name_one],
                    [" Review 1:", "how needs Apple?", "Best phone nice to handle and taking pictures", id_two, name_two],
                    [" Review 2:", "I need Apple!", "Was not good idea to buy the phone :/", id_two, name_two],
                    ["Review 1", "Genius", "The book is simply said: genius", id_three, name_three],
                    ["Review 2", "No", "I didn´t like the book that much", id_three, name_three],
                    [" Review 1:", "The technic is very nice!", "I don´t knwo how they could created it that way but it´s hillarious", id_four, name_four],
                    ["Review 1:", "GPU for Mining", "Very nice GPU for mining", id_five, name_five],
                    [" Review 1:", "Taste = best", "what can i say the best beer in the world", id_six, name_six],
                    [" Review 2:", "WTF!", "I did not know that you can produce such a taste at all", id_six, name_six],
                    [" Review 1:", "Nike > Usain Bolt ", "When I use the shoe I am faster than Usain Bolt", id_seven, name_seven],
                    [" Review 2:", "Nike > Police", "The police will never catch up with me again", id_seven, name_seven],
                    ["Review 1", "The best movie", "Best movie i ever seen", id_eight, name_eight],
                    ["review 2", "Very Brutal", "too brutal", id_eight, name_eight],
                    ["Review 1", "So Fast", "The reminds me of Fast and Furious Movies", id_nine, name_nine],
                    ["Review2", "Slow", "I am happy when I am faster than 100 mph with it", id_nine, name_nine],
                    ["Review 1", "Not as big as the original", "I bought it for my son for christmas but it´s too small", id_ten, name_ten]]












