from tkinter import END, Entry, Tk


class StockTable:

    def __init__(self, stock_getter, refresh_time):
        # Fill in all the tkinter stuff we need here.
        self.root = Tk()
        self.refresh_time = refresh_time
        self.info_getter = stock_getter
        self._info = stock_getter.get_info()
        self._create_table()

    @property
    def info(self):
        return self.info_getter.update_info(self._info)

    def _create_table(self):
        info = self.info

        for idx, header in enumerate(info[0]):
            entry = Entry(self.root, width=20, fg='blue',
                          font=('Arial',24,'bold'))

            entry.grid(row=0, column=idx)
            entry.insert(END, header)

        for row, elem in enumerate(info, start=1):
            for col, key in enumerate(elem):
                entry = Entry(self.root, width=20, fg='blue',
                              font=('Arial',16,'bold'))

                entry.grid(row=row, column=col)
                entry.insert(END, elem[key])
        self.root.after(self.refresh_time, self._create_table)

    def display(self):
        """Display given list of StockInfo objects"""
        self.root.mainloop()

