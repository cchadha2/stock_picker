from tkinter import END, Entry, Tk


class StockTable:

    def __init__(self, root, stock_infos):
        # Fill in all the tkinter stuff we need here.
        self.root = root

        for idx, header in enumerate(stock_infos[0]):
            entry = Entry(root, width=20, fg='blue',
                          font=('Arial',24,'bold'))
                
            entry.grid(row=0, column=idx)
            entry.insert(END, header)

        for row, elem in enumerate(stock_infos, start=1):
            for col, key in enumerate(elem):
                entry = Entry(root, width=20, fg='blue',
                              font=('Arial',16,'bold'))
                
                entry.grid(row=row, column=col)
                entry.insert(END, elem[key])

    def display(self):
        """Display given list of StockInfo objects"""
        self.root.mainloop()


if __name__ == '__main__':
    import os
    from stock_info import QuoteGetter
    
    params = {"region": "US", "symbols": "AMD,IBM,AAPL"}

    getter = QuoteGetter(api_key=os.environ.get("API_KEY"), params=params)
    quotes = getter.get_info()

    print(quotes)
    
    root = Tk()
    table = StockTable(root, quotes)
    table.display()
