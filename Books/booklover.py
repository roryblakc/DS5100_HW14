import numpy as np
import pandas as pd

class BookLover():
    num_books = 0
    book_list = pd.DataFrame({'book_name':[], 'book_rating':[]})
    
    def __init__(self, name, email, fav_genre):
        self.name = name
        self.email = email
        self.fav_genre = fav_genre
        
    def add_book(self, book_name, book_rating):
        '''This method adds a book to a person's book list'''
        if book_name not in set(self.book_list['book_name']):
            new_book = pd.DataFrame({'book_name':[book_name], 'book_rating':[book_rating]})
            self.book_list = pd.concat([self.book_list, new_book], ignore_index=True)
            self.num_books += 1
        else:
            print("This book is already in the list.")
            
    def has_read(self, book_name):
        '''This method checks if a person has read a book'''
        if book_name in set(self.book_list['book_name']):
            return True
        else:
            return False
        
    def num_books_read(self):
        '''This method returns the number of books a person has read'''
        num = len(self.book_list)
        print(f"This person has read {num} book(s).")
        
    def fav_books(self):
        '''This method makes a df of a person's favorite books'''
        fav_book_df = pd.DataFrame({
                'book_name':[],
                'book_rating':[]})
        for i in range(len(self.book_list)):
            if self.book_list.loc[i, 'book_rating'] > 3:
                fav_book_df = fav_book_df.append(self.book_list.iloc[i], ignore_index=True)
            else:
                pass
            
        return fav_book_df