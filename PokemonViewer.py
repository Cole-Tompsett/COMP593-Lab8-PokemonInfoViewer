from tkinter import *
from tkinter import ttk
from pokeApi import Getting_poke_info

def main():

#Creating frame
    root = Tk()

    root.title("Gotta Catch em all!!!")
    root.iconbitmap("Pokeball-1.ico")
    root.resizable(False,False)

#creating frames in the window
    frm_user_input= ttk.Frame(root)
    frm_user_input.grid(row=0, column=1, columnspan=2)

    frm_info= ttk.LabelFrame(root, text="Info")
    frm_info.grid(row=1, column=1,padx=10, pady=10, sticky=N)

    frm_stats= ttk.LabelFrame(root, text="Stats")
    frm_stats.grid(row=1, column=2,padx=10,pady=10,sticky=N)

#creating labels in the frames
    lbl_pokemon=ttk.Label(frm_user_input, text ="Pokemon name:")
    lbl_pokemon.grid(column=0, row=0,padx=3,pady=10)

#Creating place to enter text 
    ent_pokemon = ttk.Entry(frm_user_input)
    ent_pokemon.grid(column=1, row=0,pady=10)

#Creating a button to fetch the pokemon info
    def btn_get_info_click():
        
        pokemon_name = ent_pokemon.get()

        poke_dict = Getting_poke_info(pokemon_name)
        if poke_dict:
            lbl_height_result['text'] = str(poke_dict['height'])+'dm'
            lbl_weight_result['text'] = str(poke_dict['weight'])+'hg'
            lbl_name_result['text'] = poke_dict['name']

            types_list = [t['type']['name'] for t in poke_dict['types']]
            lbl_type_result['text'] = ", ".join(types_list)

#sets the value of the progress bars based off of the stats for each category
            prg_Hp['value'] = poke_dict['stats'][0]['base_stat']
            prg_Defense['value'] = poke_dict['stats'][1]['base_stat']
            prg_Attack['value'] = poke_dict['stats'][2]['base_stat']
            prg_Special_Attack['value'] = poke_dict['stats'][3]['base_stat']
            prg_Special_Defense['value'] = poke_dict['stats'][4]['base_stat']
            prg_Speed['value'] = poke_dict['stats'][5]['base_stat']
   
#Creating the button that collects the pokemon info
    btn_get_info = ttk.Button(frm_user_input,text="Get Info!",command=btn_get_info_click)
    btn_get_info.grid(column=3, row=0, padx=10,pady= 10)

#Widegets in the info column
    lbl_height= ttk.Label(frm_info,text="height:")
    lbl_height.grid(column= 100, row=100, padx=10, pady=10)
    lbl_height_result= ttk.Label(frm_info, text="TBD")
    lbl_height_result.grid(column=200,row=100)
    
    lbl_weight= ttk.Label(frm_info, text="weight:")
    lbl_weight.grid(column= 100, row=200, padx=10, pady=10)
    lbl_weight_result= ttk.Label(frm_info, text="TBD")
    lbl_weight_result.grid(column=200,row=200)
    
    lbl_type= ttk.Label(frm_info, text="type:")
    lbl_type.grid(column= 100, row=300, padx=10, pady=10)
    lbl_type_result= ttk.Label(frm_info, text="TBD")
    lbl_type_result.grid(column=200,row=300)

    lbl_name = ttk.Label(frm_info, text="Name:")
    lbl_name.grid(column=100,row=50)
    lbl_name_result = ttk.Label(frm_info, text='TBD')
    lbl_name_result.grid(column=200, row=50)

#Widgets in the stats column
    lbl_Hp= ttk.Label(frm_stats, text="HP")
    lbl_Hp.grid(column= 100,row=100)
    prg_Hp= ttk.Progressbar(frm_stats, length=200, maximum=255)
    prg_Hp.grid(column=200,row=100, padx=5, pady=5)

    lbl_Defense= ttk.Label(frm_stats, text="Defense")
    lbl_Defense.grid(column= 100,row=200)
    prg_Defense= ttk.Progressbar(frm_stats, length=200, maximum=255)
    prg_Defense.grid(column=200,row=200,padx=5, pady=5)


    lbl_Attack= ttk.Label(frm_stats, text="Attack")
    lbl_Attack.grid(column= 100,row=300)
    prg_Attack= ttk.Progressbar(frm_stats, length=200, maximum=255)
    prg_Attack.grid(column=200,row=300,padx=5, pady=5)

    lbl_Special_Attack= ttk.Label(frm_stats, text="Special Attack")
    lbl_Special_Attack.grid(column= 100,row=400)
    prg_Special_Attack= ttk.Progressbar(frm_stats, length=200, maximum=255)
    prg_Special_Attack.grid(column=200,row=400,padx=5,pady=5)

    lbl_Special_Defense= ttk.Label(frm_stats, text="Special Defense")
    lbl_Special_Defense.grid(column= 100,row=500)
    prg_Special_Defense= ttk.Progressbar(frm_stats, length=200, maximum=255)
    prg_Special_Defense.grid(column=200,row=500, padx=5, pady=5)

    lbl_Speed= ttk.Label(frm_stats, text="Speed")
    lbl_Speed.grid(column= 100,row=600)
    prg_Speed= ttk.Progressbar(frm_stats, length=200, maximum=255)
    prg_Speed.grid(column=200,row=600, padx=5, pady=5)
   
    root.mainloop()
    return

main()