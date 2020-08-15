from tkinter import *
from recommendations import generate_recomm

# Recommendations window
def show_recomm_window(recomms):
    recomm_window = Tk()
    recomm_window.title('Item Recommendations')
    recomm_window.geometry('300x600')

    Label(recomm_window, text='Recommendations').pack()

    if(type(recomms) is not str):
        for v in recomms:
            Label(recomm_window, text=v).pack()
    else:
        Label(recomm_window, text=recomms).pack()

    recomm_window.mainloop()

def recommend():
    recomms = generate_recomm(country_name.get(), item_name.get())
    show_recomm_window(recomms)

# Main window
main_window = Tk()
main_window.title('Market Basket Item recommender')
main_window.geometry('200x200')

# Get country name from user
lbl_country_input= Label(main_window, text='Enter a country name')
lbl_country_input.pack()

country_name = Entry(main_window, width=30)
country_name.pack()

# Get item name from user
lbl_item_input= Label(main_window, text='Enter an item name')
lbl_item_input.pack()

item_name = Entry(main_window, width=30)
item_name.pack()

# Submit the country name and item name to the generate_recomm function
btn_get_recom = Button(main_window, text='Generate Recommendation', command=recommend)
btn_get_recom.pack()

main_window.mainloop()