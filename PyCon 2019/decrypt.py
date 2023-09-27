LETTERS = ["A", "B", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "R", "S", "Z", "T", "U", "V", "Õ", "Ä", "Ö", "Ü"]

def analyze_text(text):
    text_map = {}
    for i in text:
        if i.upper() in LETTERS:
            if i not in text_map:
                text_map[i] = {
                    "count": 0,
                    "decoded": ""
                    }
            else:
                text_map[i]["count"] += 1
    return text_map

def find_max_letter_index(text_map):
    max_letter = ""
    max_count = 0
    for letter in text_map:
        if text_map[letter]["count"] >= max_count:
            max_letter = letter
            max_count = text_map[letter]["count"]
    return LETTERS.index(max_letter.upper())

def decode_letters(text_map, max_letter_index):
    for letter in text_map:
        text_map[letter]["decoded"] = LETTERS[(LETTERS.index(letter.upper()) - max_letter_index + len(LETTERS)) % len(LETTERS)]
    return text_map

def decode_text(text, decoded_text_map):
    solve_text = ""
    for char in text:
        decoded_char = char
        if char in decoded_text_map:
            decoded_char = decoded_text_map[char]["decoded"]
            if char.islower():
                decoded_char = decoded_char.lower()
        solve_text += decoded_char
    return solve_text

def decrypt(text):
    text_map = analyze_text(text)
    max_letter_index = find_max_letter_index(text_map)
    decoded_text_map = decode_letters(text_map, max_letter_index)
    return decode_text(text, decoded_text_map)

if __name__ == "__main__":
    text = """ZVVS UÄMM

Nvjzuzfm bkbm fmbz Zbbsfnbbm õäjnbz õöhjmbof Zvvs Uämm. Lbzõvmu pmj ub upivuv zvvs: obhv ubnn rääzbzuf lfzlfm õäj
ijjhmblvvzl lbeblbuf läsõbm.

Ijjvnbbmf õäj ufjzufmf zbbsufmf fj zäjuove ub lvobhj mbfõbhb, õbje zbnnvz kbmhzj mödj nfsf. Zjjz uflljzje ufnb kbmhf
ffz nbkbläshvzfe mbjofe. Lbmbe rähfofzje ub zbnnvef naejobzu lbvhfmf nfssf.

Rösbzu jzb zvsnb zbj Uämmvzu zbbsmbzuf õbofn kb õbmjuzfkb. Ub bzvz pnb lpevlpiub Uämmvzufmf kb lpzjz objzflz Rjsfuj. 
Zff pmj pnb zvvsf lbzõv kb kävhb Uämmvmf jhbuj õöösjmjof fmvlbbzmbof.

Läjl uüüe ufhj Uämm lpevz jzf: laoejz kb lamõbz õjmkb, ojjujz ifjob kb rboj õjmkb lpllv, fijubz ojoh lpifoebz ippofje. 
Sviov zbbsfm pmj Uämmvm lbrzbbfe. Lvj Rjsfu rbkb uvmfmf rboj, zbbujz ub Uämmv lbrzbje uppnb. Uämm õäuujz zfjuznfzammbzf 
rbmhj lfrjlz löuuf kb mölz uffmf. Rjsfuj rbeb bhb pmj ojj zvvs obhv õbfzf nfif zbvo. Ufsõf ujjhjuöjz õfuu nbiuvz zjoob 
zjzzf.

Zvvm Uämm bsnbzubz õöhb röilmfje. Jhbm zahjzfm löjz ub Bdsvlb zbbsfm kb lpskbz ubzlve röilmfje uöjz. Ofje pmj zjjz lpevz
Uämmvzufm lppz Rjsfuj kb rpkbhb näovz oblzvubeb.

Aifm upsnjzfm zahjzröfõbm uvmj Zvvs Uämm Bdsvlbmu röilmfje lpskbnbzu. Zfbm nöslbz ub öllj pnb kbmhf ffz nfsfz aiu Zäsõf 
lbmvsjuf mbfõb, njmmf mbjofe pmje andfs rbjzbove. Svuuv uäuubz Uämm brrj. Ub õäuujz mbfõb, lbmmbz zfmmf õffzu uaikblz. 
Ufjzf löfhb oprrjz ub nfife alzibbõbm nfsfzu kb bzfubz obe mbfõb. Zjjz lpskbz ub õffzu õömkb lb nffzuf õäshve, bfsve, 
jzufrjohje, mfjõblpuje ojoh nvv õbsb. Õjjnblz uäzujz ub mbfõb läjhfhb lppz ämbmf kb lboejz sboeb."""
    print(decrypt(text))
