import requests 



def Getting_poke_info(Pokemon):

    print("Getting pokemon Information...", end=' ')
    Response = requests.get("https://pokeapi.co/api/v2/pokemon/"+Pokemon)

    if Response.status_code == 200:
        print("SUCCESS")
        dict_response = Response.json() 
        return(dict_response)
    else:
        print("Response failed")
        return

