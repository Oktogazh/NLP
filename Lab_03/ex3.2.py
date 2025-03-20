import re

frequent_types = {
    "cy": ["yn", "yr", "yng", "i", "a", "yw", "'n", "'r", "mae", "o"],
    "en": ["the", "a", "and", "of", "be", "that", "is", "it", "for", "not", "in"],
    "br": ["an", "ar", "eo", "e", "o", "a", "ez", "ha", "da", "en"],
    "fr": ["le", "la", "de", "ne", "n'", "et", "un", "pas", "se", "les", "et"],
}

texts = [
    "Ret eo din [boulc'hañ hag echuiñ] skrivañ ar brezegenn-mañ a-raok embannadur statistikoù an niveridigezh a voe warlene war stad ar C'hembraeg e Kembre. Rakwelet a ran e vo ar sifroù a embannor a-benn nebeut ur feuk hag ur vezh evit ar re ac'hanomp a gav dezho ne c'hall ket Kembre bezañ Kembre hep ar C'hembraeg. Diouganiñ a ran ivez e vo diwezh d'ar C'hembraeg evel yezh vev, ha padout a rafe an tuadur a-vremañ, dre zeroù ar c'hentañ kantved warn-ugent, bezet e vo tud c'hoazh war Enez Vreizh da neuze.",
    "Rhaid imi [gychwyn a gorffen] sgrifennu'r ddarlith hon cyn cyhoeddi ystadegau'r cyfrifiad a fu y llynedd ar y Cymry Cymraeg yng Nghymru. Mi ragdybiaf y bydd y ffigurau a gyhoeddir cyn hir yn sioc ac yn siom i'r rheini ohonom sy'n ystyried nad Cymru fydd Cymru heb y Gymraeg. Mi ragdybiaf hefyd y bydd terfyn ar y Gymraeg yn iaith fyw, ond parhau'r tueddiad presennol, tua dechrau'r unfed ganrif ar hugain, a rhoi bod dynion ar gael yn Ynys Prydain y pryd hynny.",
    "A dra sur n'en doa ket gellet Doue faziañ ha kuzhet e oa ster an istor-se tu bennak met ne oa ket en addisplegoù.",
    "Certainement Dieu n'avait pu se tromper et le sens de cette histoire se cachait quelque part, mais non dans les commentaires.",
    "The big difference between a physical and a digital Zettelkasten is that in a digital one, one does not need to store the notes in different boxes, this is because the indexation and link system are core features of the app the app.",
]

for text in texts:
    counter = {}
    most_likely_language = {"name": "", "value": 0}
    for key, list in frequent_types.items():
        counter[key] = 0
        for type in list:
            counter[key] += len(re.findall(rf"{type}\b", text.lower()))
        if most_likely_language["value"] < counter[key]:
            most_likely_language = {"name": key, "value": counter[key]}
    print(
        "Found",
        most_likely_language["name"],
        "with a confidence of",
        f'{most_likely_language["value"] * 100 // sum(counter.values())}%,',
        " details: ",
        counter,
    )

"""
Found br with a confidence of 55%,  details:  {'cy': 16, 'en': 13, 'br': 48, 'fr': 10}
Found cy with a confidence of 62%,  details:  {'cy': 28, 'en': 7, 'br': 10, 'fr': 0}
Found br with a confidence of 35%,  details:  {'cy': 6, 'en': 6, 'br': 14, 'fr': 13}
Found fr with a confidence of 44%,  details:  {'cy': 0, 'en': 3, 'br': 7, 'fr': 8}
Found en with a confidence of 41%,  details:  {'cy': 4, 'en': 18, 'br': 18, 'fr': 3}
"""
