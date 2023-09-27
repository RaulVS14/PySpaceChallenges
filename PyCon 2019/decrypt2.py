import re
LETTERS = [ "A", "B", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "R", "S", "Z", "T", "U", "V", "Õ", "Ä", "Ö", "Ü"]
FREQUENCY_LIST = "AEISTLUNKDOMRVGHJPÄÕBÜÖFZ"
# https://inventwithpython.com/hacking/chapter18.html
def get_pattern(word):
    word = word.upper()
    position = 0
    letter_positions = {}
    pattern = []
    for char in word:
        if char not in letter_positions:
            letter_positions[char] = str(position)
            position += 1
        pattern.append(letter_positions[char])
    return '.'.join(pattern)

# 1. frequency directly not working
# 2. pattern based not working, because always new letter
def decrypt(text, words):
    text_patterns = []
    text_list = text.split(" ")
    for word in text_list:
        cleaned_word = re.sub(r'[^\w\s]','',word)
        text_patterns.append(get_pattern(word))
    matches = {}
    for word in words:
        word_pattern = get_pattern(word)
        if word_pattern in text_patterns:
            text_pattern_index = text_patterns.index(word_pattern)
            if word not in matches:
                matches[word] = text_list[text_pattern_index]
    print(matches)
    cypher = {}
    for key, value in matches.items():
        for i in range(len(key)):
            key_char = key[i]
            val_char = value[i]
            if key_char not in cypher:
                cypher[key_char] = val_char
    return "True"
if __name__ == "__main__":
   text = """AFFG HTVV
Allgpõll Rmobvlup

Õfbahapv ljlv pvla Allgpõllv rtbõla rmobvlup Affg Htvv. Zlarfvh svb hl hsäfhf affg: ulof hlõõ öttalahp zpazpv rtb
 äbbovlzffaz zldlzlhp ztgrlv.

Äbbfõllvp rtb hpbahpvp allghpvp pb atbhufd hl zfulob vlprlol, rlbd alõõfa jlvoab vmüb õpgp. Abba hpzzbabd hpõl jlvop ppa
 õljlztgofapd vlbupd. Zlvld ötopupabd hl alõõfdp õidbulah zlfopvp õpggp.

Ömglah bal afgõl alb Htvvfah allgvlahp rlupõ jl rlvbhapjl. Hl lafa sõl zsdfzsähl Htvvfahpvp jl zsaba ulbapza Öbgphb.
 App svb sõl affgp zlarf jl jtfol Htvvfvp bolhb rmmgbvbup pvfzllavlup.

Ztbz hnnd hpob Htvv zsdfa bap: ziudba jl zivrla rbvjl, ubbhba äpbul jl ölub rbvjl zszzf, päbhla ubuo zsäpudla ässupbd. 
Gfäuf allgpv svb Htvvfv zlöallpd. Zfb Öbgph öljl hfvpvp ölub, allhba hl Htvvf zlöalbd hssõl. Htvv rthhba apbhaõpaivvlap
 ölvob zpöbza zmhhp jl vmza hppvp. Öbgphb öldl lol svb ubb affg ulof rlpap õpäp alfu. Hpgrp hbbobhmba rphh õlähfa abuul 
 abaap.

Affg Htvv lgõlahla rmol ömäzvpbd. Bolv aiobapv zmba hl Lügfzl allgpv jl zsgjla hlazfd ömäzvpbd hmba. Upbd svb abba zsdfa
 Htvvfahpv zssa Öbgphb jl ösjlol õtufa ulzafhldl.

Iäpv hsgõbapv aiobaömprlv hfvb Affg Htvv Lügfzlvh ömäzvpbd zsgjlõlah. Aplv õmgzla hl mzzb sõl jlvop ppa õpgpa iäh Atgrp
zlvfgbhp vlprl, õbvvp vlbupd svbd iõüpg ölbalufd. Gfhhf hthhla Htvv lööb. Hl rthhba vlprl, zlvvla apvvp rppah hiäjlza.
Hpbap zmpol usööba hl õpäpd izaällrlv õpgpah jl laphla uld vlprl. Abba zsgjla hl rppah rmvjl zl õppahp rtgofd, lpgfd,
bahpöbuobd, vpbrlzshbd ubuo õff rlgl. Rbbõlza htahba hl vlprl ztbopol zssa tvlvp jl zludba gludl."""
   words = [
        'suur',
        'tõll',
        'saaremaa',
        'vägilane',
        'piret',
        'ruhnu',
        'abruka',
    ]
   print(decrypt(text, words))
   
