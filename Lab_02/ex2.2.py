import re
import nltk

words = nltk.corpus.words.words("en")

only_vowel_words = [word for word in words if re.match("^[aeiouAEIOU]{3}$", word)]
print(only_vowel_words)
# ['iao', 'oii']

vcv = [
    word for word in words if re.match("^[aeiouAEIOU][b-df-hj-np-tv-z][aeiou]$", word)
]
print(vcv)
# ['aba', 'Abe', 'Abo', 'Abu', 'abu', 'ace', 'Ada', 'Ade', 'ade', 'ado', 'aga', 'age', 'ago', 'aha', 'aho', 'ahu', 'Aka', 'aka', 'ake', 'ako', 'aku', 'ala', 'ale', 'alo', 'ama', 'ame', 'Ami', 'ami', 'Ana', 'ana', 'ani', 'apa', 'ape', 'ara', 'are', 'Aro', 'aru', 'Asa', 'ase', 'Ata', 'ate', 'Ati', 'ava', 'Ave', 'ave', 'avo', 'awa', 'awe', 'axe', 'aye', 'ayu', 'azo', 'Edo', 'ego', 'eke', 'Eli', 'eme', 'emu', 'era', 'ere', 'eta', 'Eva', 'Eve', 'eve', 'Ewe', 'ewe', 'eye', 'iba', 'Ibo', 'ice', 'Ida', 'ide', 'Ido', 'ife', 'ihi', 'Ijo', 'Ike', 'Ila', 'Ima', 'imi', 'imu', 'Ino', 'Ira', 'ire', 'iso', 'Ita', 'Ito', 'iva', 'iwa', 'iyo', 'obe', 'obi', 'oda', 'ode', 'Ofo', 'oho', 'oka', 'oki', 'Ole', 'Ona', 'ona', 'one', 'ope', 'ora', 'ore', 'ose', 'Oto', 'Ova', 'ova', 'owe', 'ubi', 'Uca', 'Udi', 'udo', 'uji', 'uke', 'ula', 'ule', 'ulu', 'ume', 'umu', 'Una', 'upo', 'ura', 'ure', 'Uri', 'Uro', 'Uru', 'use', 'Uta', 'uta', 'Ute', 'utu', 'uva']

vcvv = [
    word
    for word in words
    if re.match("^[aeiouAEIOU][b-df-hj-np-tv-z][aeiou]{2}$", word)
]
print(vcvv)
# ['Abie', 'Adai', 'Agao', 'Agau', 'agee', 'agio', 'agua', 'ague', 'akee', 'akia', 'Alea', 'alee', 'aloe', 'Amia', 'anoa', 'apii', 'apio', 'aqua', 'aquo', 'area', 'aria', 'arui', 'awee', 'Eboe', 'eboe', 'edea', 'eheu', 'ejoo', 'Ekoi', 'Elia', 'epee', 'eria', 'Erie', 'etua', 'etui', 'Evea', 'evoe', 'idea', 'ilia', 'Inia', 'Itea', 'Ixia', 'oboe', 'ogee', 'ohia', 'Ohio', 'okee', 'okia', 'Okie', 'Olea', 'oleo', 'olio', 'omao', 'oxea', 'Ubii', 'Ulua', 'ulua', 'unau', 'unie', 'Unio', 'unio', 'urao', 'urea', 'Uria', 'usee', 'utai', 'uvea']


vcvvv = [
    word
    for word in words
    if re.match("^[aeiouAEIOU][b-df-hj-np-tv-z][aeiou]{3}$", word)
]
print(vcvvv)
# ['adieu', 'Araua', 'Arioi', 'iliau', 'Umaua']

len_7_adehins = [word for word in words if re.match(r"^[adehins]{7}$", word)]
print(len_7_adehins)
# ['addenda', 'adenase', 'adenine', 'ahaaina', 'anidian', 'aniseed', 'asinine', 'asshead', 'daisied', 'danaide', 'danaine', 'dasheen', 'deadish', 'deaness', 'deedeed', 'disdain', 'disease', 'enshade', 'hashish', 'hennish', 'insense', 'nandine', 'saddish', 'sadness', 'seaside', 'shadine', 'shedded']

textonyms = [word for word in words if re.match("^[defDEF][ghi][jkl][mno]$", word)]
print(textonyms)
# ['dilo', 'film', 'filo']
