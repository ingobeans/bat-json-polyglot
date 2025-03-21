import sys, json, os, random

def generate_polyglot(batch_data:str,json_data:dict)->str:
    rows = batch_data.split("\n")
    batch_json = {}

    for row in rows:
        if not row:
            continue
        key = '\" > nul 2> nul & ' + row + " & ::"
        # to avoid duplicate keys
        while key in batch_json:
            key = str(random.randint(0,999))+key
        
        batch_json[key] = 1
    
    batch_json[f'{random.randint(0,999)}\" > nul 2> nul & exit & ::'] = 1
    new = json.dumps({**batch_json, **json_data},indent=4)
    new = new.replace("{\n    ","{", 1)

    # validate that it still is valid json
    try:
        json.loads(new)
    except json.decoder.JSONDecodeError:
        print("polyglot generation failed: generated text is not valid json.")
        quit(1)

    return new

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("incorrect usage, do: python bat-json-polyglot.py <batch file> <json file> <output path>")
        quit(0)

    batch_path = sys.argv[1]
    json_path = sys.argv[2]
    output_path = sys.argv[3]

    should_quit = False
    if not os.path.isfile(batch_path):
        print("error: batch file doesn't exist")
        should_quit = True
    
    if not os.path.isfile(json_path):
        print("error: json file doesn't exist")
        should_quit = True
    
    if should_quit:
        quit(0)

    with open(batch_path,"r",encoding="utf-8") as f:
        batch_data = f.read()
    with open(json_path,"r",encoding="utf-8") as f:
        try:
            json_data = json.load(f)
        except json.decoder.JSONDecodeError:
            print("error: json file isnt valid json :(")
            quit(0)

    with open(output_path,"w",encoding="utf-8") as f:
        f.write(generate_polyglot(batch_data,json_data))
    
    print("success! :)")