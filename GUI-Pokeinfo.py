from ntpath import join
from tkinter import *
from tkinter import ttk
from pokeapii import get_pokemon_info  

def main():
    root = Tk()
    root.title("PokeInfo")
    #root.iconbitmap("Poke-Ball.ico")
    
    frm_user_input = ttk.Frame(root)
    frm_user_input.grid(row=0, column=0, columnspan=2, padx=20, pady=20)

    frm_Info = ttk.LabelFrame(root, text="Info")
    frm_Info.grid(row=1, column=0, padx= 15 , pady= 15, sticky =N)
    
    frm_Stats = ttk.LabelFrame(root, text="Stats")
    frm_Stats.grid(row=1, column=1, padx= 15 , pady= 15, sticky =N)

    lbl_name = ttk.Label(frm_user_input, text = "Pokemon Name:")
    lbl_name.grid(row=0, column=0, padx=10, pady=10)
    
    ent_name = ttk.Entry(frm_user_input)
    ent_name.grid(row=0, column=1, pady =10)

    def btnn_get_info_click():
        pokemon_name = ent_name.get()
        poke_dict = get_pokemon_info(pokemon_name)
        if poke_dict:
            lbl_height_val['text']= str(poke_dict['height']) + ' dm'
            lbl_weight_val['text']= str(poke_dict['weight']) + ' hg'
            types_list = (t['type']['name'] for t in poke_dict['types'])
            lbl_type_val['text']= ', '.join(types_list)
            pgp_hp['value']=poke_dict['stats'][0]['base_stat']
            pgp_attack['value']=poke_dict['stats'][1]['base_stat']
            pgp_defense['value']=poke_dict['stats'][2]['base_stat']
            pgp_spcl_attack['value']=poke_dict['stats'][3]['base_stat']
            pgp_spcl_defense['value']=poke_dict['stats'][4]['base_stat']
            pgp_speed['value']=poke_dict['stats'][5]['base_stat']

    btnn_getinfo = ttk.Button(frm_user_input, text = "Get Info", command = btnn_get_info_click)
    btnn_getinfo.grid(column=2, row=0,padx=10, pady=10)

    lbl_height = ttk.Label(frm_Info, text ="Height:")
    lbl_height.grid(row=100, column=100)
    lbl_height_val = ttk.Label(frm_Info, text = "TBD")
    lbl_height_val.grid(row=100, column=200,  padx= 15, pady= 7)

    lbl_Weight = ttk.Label(frm_Info, text ="Weight:")
    lbl_Weight.grid(row=300, column=100)
    lbl_weight_val = ttk.Label(frm_Info, text = "TBD")
    lbl_weight_val.grid(row=300, column=200, padx= 15, pady= 7)

    lbl_type = ttk.Label(frm_Info, text ="Type:")
    lbl_type.grid(row=500, column=100)
    lbl_type_val = ttk.Label(frm_Info, text = "TBD")
    lbl_type_val.grid(row=500, column=200, padx= 15,  pady= 7)
 
    lbl_hp = ttk.Label(frm_Stats, text = 'HP:')
    lbl_hp.grid(row= 100, column=100, sticky = E)
    pgp_hp = ttk.Progressbar(frm_Stats, length=200 , maximum=225)
    pgp_hp.grid(row=100, column=200,  padx= 10, pady= 10)

    lbl_attack = ttk.Label(frm_Stats, text = 'Attack:')
    lbl_attack.grid(row= 200, column=100, sticky = E)
    pgp_attack = ttk.Progressbar(frm_Stats, length=200 , maximum=225)
    pgp_attack.grid(row=200, column=200)

    lbl_defense = ttk.Label(frm_Stats, text = 'Defense:')
    lbl_defense.grid(row= 300, column=100, sticky = E)
    pgp_defense = ttk.Progressbar(frm_Stats, length=200 , maximum=225)
    pgp_defense.grid(row=300, column=200, padx= 10, pady= 10)

    lbl_spcl_attack = ttk.Label(frm_Stats, text = 'Special Attack:')
    lbl_spcl_attack.grid(row= 400, column=100, sticky = E)
    pgp_spcl_attack = ttk.Progressbar(frm_Stats, length=200 , maximum=225)
    pgp_spcl_attack.grid(row=400, column=200)

    lbl_spcl_defense = ttk.Label(frm_Stats, text = 'Special Defense')
    lbl_spcl_defense.grid(row= 500, column=100, sticky = E)
    pgp_spcl_defense = ttk.Progressbar(frm_Stats, length=200 , maximum=225)
    pgp_spcl_defense.grid(row=500, column=200,  padx= 10, pady= 10)

    lbl_speed = ttk.Label(frm_Stats, text = 'Speed:')
    lbl_speed.grid(row= 600, column=100, sticky = E)
    pgp_speed = ttk.Progressbar(frm_Stats, length=200 , maximum=225)
    pgp_speed.grid(row=600, column=200)

    root.mainloop()

main()