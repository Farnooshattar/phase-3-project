from prettycli import red, blue


class Banner:
    def welcome(self):
        print(red("Check your"))
        print(
            red(
                """             
--      __   ____  _        ___  ____   ___     ____  ____  
--     /  ] /    || |      /  _]|    \ |   \   /    ||    \ 
--    /  / |  o  || |     /  [_ |  _  ||    \ |  o  ||  D  )
--   /  /  |     || |___ |    _]|  |  ||  D  ||     ||    / 
--  /   \_ |  _  ||     ||   [_ |  |  ||     ||  _  ||    \ 
--   \____||__|__||_____||_____||__|__||_____||__|__||__|\_|      
"""
            ).bold()
        )
