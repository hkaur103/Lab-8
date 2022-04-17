from ntpath import join
from tkinter import *
from tkinter import ttk
from pokeapi import get_pokemon_info

def main():
    root = Tk()
    root.title("PokeInfo")
    #root.iconbitmap("Poke-Ball.ico")
    
    frm_user_input = ttk.Frame(root)
    frm_user_input.grid(row=0, column=0, columnspan=2)

    frm_Info = ttk.LabelFrame(root, text="Info")
    frm_Info.grid(row=1, column=0)
    
    frm_Stats = ttk.LabelFrame(root, text="Stats")
    frm_Stats.grid(row=1, column=1)

    lbl_name = ttk.Label(frm_user_input, text = "Pokemon Name:")
    lbl_name.grid(row=0, column=0, padx=10, pady=10)
    
    ent_name = ttk.Entry(frm_user_input)
    ent_name.grid(row=0, column=1, padx=10, pady =10)

    def btnn_get_info_click():
        pokemon_name = ent_name.get()
        poke_dict = get_pokemon_info(pokemon_name)
        if poke_dict:
            lbl_height_val['text']= str(poke_dict['height']) + ' dm'
            types_list = (t["type"]['name'] for t in poke_dict['type'])
            lbl_type_val['text']= ', '.join(types_list)


        print("Button Clicked")

    btnn_getinfo = ttk.Button(frm_user_input, text = "Get Info", command = btnn_get_info_click)
    btnn_getinfo.grid(column=2, row=0,padx=10, pady=10)

    lbl_height = ttk.Label(frm_Info, text ="Height:")
    lbl_height.grid(row=100, column=100)
    lbl_height_val = ttk.Label(frm_Info, text = "TBD")
    lbl_height_val.grid(row=100, column=200)

    lbl_Weight = ttk.Label(frm_Info, text ="Weight:")
    lbl_Weight.grid(row=300, column=100)
    lbl_weight_val = ttk.Label(frm_Info, text = "TBD")
    lbl_weight_val.grid(row=300, column=200)

    lbl_type = ttk.Label(frm_Info, text ="Type:")
    lbl_type.grid(row=500, column=100)
    lbl_type_val = ttk.Label(frm_Info, text = "TBD")
    lbl_type_val.grid(row=500, column=200)



    
    root.mainloop()

main()