import sys, json
from kit import *
P = 'photos/'; S = SITE; W = SITE + 'realizacje/www/'; SK = SITE + 'realizacje/sklepy/'
CTA_FOOT = 'Piksel360 · <b>webowe systemy dla firm</b>'
POSTS = {}

def post(key, folder, base, slides):
    POSTS[key] = (folder, [(f'{base}-{k+1}', h) for k, h in enumerate(slides)])

# 06 Piksel – własny system
T = 'Wdrożenie · nasza pracownia'; F = 'Piksel pracownia reklamy · <b>Rypin</b>'; N = 5
post('2026-11-06', '06-piksel', 'piksel', [
    s_hero(S+'Piksel360.jpg', 'Szewc bez butów?', 'U nas nie <span class="lime">:)</span>', 'Zanim zrobiliśmy systemy dla innych, zrobiliśmy jeden dla siebie, dla naszej pracowni reklamy w Rypinie.', T, F, 1, N, pos='center 30%'),
    s_split(S+'Piksel_frezarka.jpg', 'Jak było', 'Zapytania w mailach, zlecenia w zeszycie', 'A produkcja i montaż na karteczkach. Każdy dzień zaczynał się od szukania.', T, F, 2, N, icon_name='file'),
    s_features(S+'kalendarz_piksel360.jpg', 'Jak jest dziś', 'Jedno miejsce na wszystko', [
        ('mail', 'Mail staje się zleceniem', 'jednym kliknięciem'),
        ('calendar', 'Kalendarz produkcji i montaży', 'cała ekipa widzi plan'),
        ('chart', 'Finanse i bilans na bieżąco', None),
        ('users', 'Historia klienta w jednym miejscu', None)], T, F, 3, N, pos='center 20%'),
    s_stat(S+'Bilans_firmy.jpg', 'Efekt', 'ok. 40%', 'szybciej przez pracownię', 'Zlecenia nie giną, a my wiemy, co dzieje się na produkcji.', T, F, 4, N, pos='center 20%'),
    s_cta(S+'Piksel360.jpg', 'Masz podobny <span class="lime">bałagan w firmie?</span>', 'Pogadajmy. Od tego zaczynamy każde wdrożenie.', T, CTA_FOOT, 5, N),
])

# 09 blog – historia z AI
T = 'Nowy wpis na blogu'; F = 'Blog · <b>piksel360.pl</b>'; N = 3
post('2026-11-09', '09-blog', 'blog', [
    s_hero(S+'programowanieAI.jpg', 'Nowy wpis na blogu', 'Jak zaczęła się moja historia z AI', 'Od pracowni reklamy do pierwszej rozmowy ze sztuczną inteligencją.', T, F, 1, N),
    s_split(S+'Leszek_Kaminski.jpg', 'We wpisie', 'Kiedy, do czego i co zaskoczyło', 'A także to, co nie wyszło. Bez technicznego języka, po ludzku.', T, F, 2, N, pos='center 25%', icon_name='pen'),
    s_cta(S+'programowanieAI.jpg', 'Przeczytaj <span class="lime">cały wpis</span>', 'Kilka minut lektury o tym, jak AI weszło do naszej pracowni.', T, CTA_FOOT, 3, N, btn='Czytaj na blogu', site='piksel360.pl/blog'),
])

# 11 Sensorek
T = 'Realizacja · Strona www'; F = 'Sensorek · <b>sensorek.eu</b>'; N = 5
post('2026-11-11', '11-sensorek', 'sensorek', [
    s_hero(P+'sens-hero.jpg', 'Nowa realizacja', 'Sensorek', 'Strona gabinetu terapii integracji sensorycznej dla dzieci', T, F, 1, N, pos='center 30%',
           extra=phone(W+'sensorek-mobile.webp', 770, 210, 470, 4)),
    s_features(P+'sens-terapia.jpg', 'Co jest na stronie', 'Spokój i zaufanie od pierwszego ekranu', [
        ('puzzle', 'Od razu widać, w czym pomagamy', None),
        ('users', 'Terapeutki z imienia i twarzy', None),
        ('image', 'Galeria prawdziwych zajęć', None),
        ('phone', 'Wygodna na telefonie', 'tam rodzice szukają najczęściej')], T, F, 2, N, pos='center 25%'),
    s_mockup(P+'sens-ksztalty.jpg', W+'sensorek-desktop.webp', W+'sensorek-mobile.webp', 'sensorek.eu', 'Komputer i telefon', 'Rodzic znajdzie wszystko<br>w kilka sekund', T, F, 3, N),
    s_collage([P+'sens-terapia.jpg', P+'sens-asia.jpg', P+'sens-ksztalty.jpg'], 'Prawdziwe zdjęcia', 'Prawdziwe zajęcia, prawdziwe twarze.<br><span class="lime">Tak buduje się zaufanie.</span>', T, F, 4, N),
    s_cta(P+'sens-hero.jpg', 'Prowadzisz gabinet albo <span class="lime">usługi lokalne?</span>', 'Chcesz, żeby klienci trafiali do Ciebie z Google? Napisz do nas.', T, CTA_FOOT, 5, N),
])

# 13 Prime Automotive
T = 'Wdrożenie · Komis'; F = 'Prime Automotive · <b>primeautomotive.com.pl</b>'; N = 5
post('2026-11-13', '13-prime', 'prime', [
    s_hero(P+'prime-landrover.jpg', 'Wdrożenie · Prime Automotive', 'Nowe auto na stronie w kilka minut', 'Strona komisu połączona z panelem sprzedaży', T, F, 1, N, pos='center 40%'),
    s_split(P+'prime-mazda.jpg', 'Jak było', 'Dodanie auta do oferty trwało długo', 'Przepisywanie danych, obróbka zdjęć, pilnowanie dokumentów.', T, F, 2, N, pos='center 40%', icon_name='clock'),
    s_features(P+'prime-audi.jpg', 'Co zrobiliśmy', 'Strona + panel sprzedaży', [
        ('car', 'Dane auta z dowodu rejestracyjnego', None),
        ('camera', 'Zdjęcia od razu gotowe pod Google', None),
        ('refresh', 'Import ogłoszeń z Allegro', None),
        ('file', 'Raporty PDF jednym kliknięciem', None)], T, F, 3, N, pos='center 40%'),
    s_screen(P+'prime-landrover.jpg', P+'prime-site.jpg', 'primeautomotive.com.pl', 'Efekt', 'Komplet danych i zdjęć,<br>bez przepisywania', T, F, 4, N),
    s_cta(P+'prime-audi.jpg', 'Robisz coś ręcznie <span class="lime">codziennie?</span>', 'To zwykle najlepsze miejsce na automatyzację. Napisz do nas.', T, CTA_FOOT, 5, N),
])

# 16 blog – czym jest AI
T = 'Nowy wpis na blogu'; F = 'Blog · <b>piksel360.pl</b>'; N = 3
post('2026-11-16', '16-blog', 'blog', [
    s_hero(S+'programowanieAI1.jpg', 'Nowy wpis na blogu', 'Czym właściwie jest AI?', 'Tłumaczymy bez technicznego języka, na przykładzie z naszej pracowni.', T, F, 1, N),
    s_split(S+'Piksel360.jpg', 'Frezarka kontra AI', 'Frezarka robi to, co zaprogramujesz. AI przewiduje odpowiedź.', 'Stąd jej siła i stąd pomyłki.', T, F, 2, N, pos='center 35%', icon_name='cpu'),
    s_cta(S+'programowanieAI1.jpg', 'Przeczytaj <span class="lime">cały wpis</span>', 'AI po ludzku, bez żargonu i bez straszenia.', T, CTA_FOOT, 3, N, btn='Czytaj na blogu', site='piksel360.pl/blog'),
])

# 18 kulisy
T = 'Kulisy'; F = 'Piksel360 · <b>Rypin</b>'; N = 4
post('2026-11-18', '18-kulisy', 'kulisy', [
    s_hero(S+'Piksel_frezarka.jpg', 'Zwykły dzień u nas', 'Rano frezarka i montaż reklamy', '...a po południu kod i AI.', T, F, 1, N),
    s_split(S+'programowanieAI.jpg', 'Po południu', 'Kod, systemy dla firm i AI', 'Piksel360 wyrósł z pracowni reklamy w Rypinie.', T, F, 2, N, icon_name='code'),
    s_split(S+'Piksel360.jpg', 'Dlaczego to ważne', 'Sami prowadzimy produkcję, ekipy i klientów', 'Wiemy, jak wygląda poniedziałek, kiedy wszystko się pali.', T, F, 3, N, pos='center 35%', icon_name='wrench'),
    s_cta(S+'Piksel_frezarka.jpg', 'Programy mają być <span class="lime">proste</span>, a nie „ładne w prezentacji”', 'Takie robimy dla siebie i takie robimy dla Ciebie.', T, CTA_FOOT, 4, N),
])

# 20 ALUS
T = 'Wdrożenie · Panel B2B'; F = 'ALUS · <b>alus.rypin.info</b>'; N = 5
post('2026-11-20', '20-alus', 'alus', [
    s_hero(P+'alus-pila.jpg', 'Wdrożenie · ALUS', 'Klienci sami liczą cenę i zamawiają', 'Panel B2B dla producenta systemów aluminiowych', T, F, 1, N),
    s_split(P+'alus-robot.jpg', 'Jak było', 'Każda wycena liczona ręcznie', 'A każde zamówienie przepisywane na produkcję.', T, F, 2, N, icon_name='calc'),
    s_features(P+'alus-profil.jpg', 'Co zrobiliśmy', 'Panel B2B', [
        ('calc', 'Kalkulator ceny dla klienta', 'klient sam liczy wycenę'),
        ('users', 'Konta klientów z historią', None),
        ('factory', 'Zamówienie prosto na produkcję', None)], T, F, 3, N),
    s_mockup(P+'alus-pila.jpg', SK+'alus-desktop.webp', SK+'alus-mobile.webp', 'alus.rypin.info', 'Efekt', 'Mniej telefonów,<br>mniej pomyłek', T, F, 4, N),
    s_cta(P+'alus-pila.jpg', 'Sprzedajesz <span class="lime">firmom?</span>', 'Tonie Ci skrzynka z zapytaniami o cenę? Napisz do nas.', T, CTA_FOOT, 5, N),
])

# 23 blog – AI na co dzień
T = 'Nowy wpis na blogu'; F = 'Blog · <b>piksel360.pl</b>'; N = 3
post('2026-11-23', '23-blog', 'blog', [
    s_hero(S+'kalendarz_piksel360.jpg', 'Nowy wpis na blogu', 'Jak AI pomaga nam w firmie na co dzień', 'Konkrety zamiast teorii.', T, F, 1, N, pos='center 30%'),
    s_features(S+'Bilans_firmy.jpg', 'We wpisie', 'Trzy rzeczy, które robimy z AI', [
        ('mail', 'Mail od klienta staje się zleceniem', None),
        ('calendar', 'Zadania same trafiają do kalendarza', None),
        ('code', 'Programowanie idzie szybciej', None)], T, F, 2, N, pos='center 20%'),
    s_cta(S+'kalendarz_piksel360.jpg', 'Przeczytaj <span class="lime">cały wpis</span>', 'Zobacz, jak to wygląda w prawdziwej firmie.', T, CTA_FOOT, 3, N, btn='Czytaj na blogu', site='piksel360.pl/blog'),
])

# 25 Kartoholik
T = 'Realizacja · Sklep'; F = 'Kartoholik · <b>kartoholik.pl</b>'; N = 5
post('2026-11-25', '25-kartoholik', 'kartoholik', [
    s_hero(P+'kart-banner.jpg', 'Nowa realizacja', 'Kartoholik', 'Sklep z kartami kolekcjonerskimi, ponad tysiąc produktów', T, F, 1, N,
           extra=phone(SK+'kartoholik-mobile.webp', 770, 210, 470, 4)),
    s_features(P+'kart-site.jpg', 'Co jest w sklepie', 'Klient szybko znajduje to, czego szuka', [
        ('search', 'Kategorie i wyszukiwarka', None),
        ('zap', 'Szybkie ładowanie', 'mimo tysięcy zdjęć'),
        ('phone', 'Zakupy wygodne na telefonie', None),
        ('cart', 'Prosty koszyk', 'bez zbędnych kroków')], T, F, 2, N),
    s_mockup(P+'kart-banner.jpg', SK+'kartoholik-desktop.webp', SK+'kartoholik-mobile.webp', 'kartoholik.pl', 'Komputer i telefon', 'Wygodnie na<br>każdym ekranie', T, F, 3, N),
    s_collage([P+'kart-c4.jpg', P+'kart-c1.jpg', P+'kart-c5.jpg'], 'Ponad 1000 produktów', 'Każda karta ma swoje miejsce.<br><span class="lime">I da się ją znaleźć.</span>', T, F, 4, N),
    s_cta(P+'kart-banner.jpg', 'Myślisz o <span class="lime">sklepie internetowym?</span>', 'Pomożemy dobrać rozwiązanie do Twojego asortymentu. Napisz do nas.', T, CTA_FOOT, 5, N),
])

# 27 HYDROSEVEN
T = 'Wdrożenie · Branża HVAC'; F = 'HYDROSEVEN · <b>hydroseven.pl</b>'; N = 5
post('2026-11-27', '27-hydroseven', 'hydroseven', [
    s_hero(P+'hydro-pompa.jpg', 'Wdrożenie · HYDROSEVEN', 'Czy na tym zleceniu zarabiamy?', 'System dla firmy HVAC: oferty, ekipy i finanse w jednym miejscu', T, F, 1, N),
    s_split(P+'hydro-podloga.jpg', 'Jak było', 'Dużo zleceń, terminów i ekip w terenie', 'Brakowało szybkiej odpowiedzi, który projekt przynosi zysk.', T, F, 2, N, icon_name='clock'),
    s_features(P+'hydro-pompa.jpg', 'Co zrobiliśmy', 'Jeden system zamiast kilku', [
        ('file', 'Ofertowanie', None),
        ('calendar', 'Kalendarz ekip', None),
        ('wallet', 'Finanse', None),
        ('chart', 'Statystyki rentowności', None)], T, F, 3, N, pos='85% center'),
    s_split(S+'Bilans_firmy.jpg', 'Efekt', 'Widać, która ekipa i który projekt zarabia', 'Na bieżąco, a nie po zamknięciu roku.', T, F, 4, N, pos='center 25%', icon_name='chart'),
    s_cta(P+'hydro-pompa.jpg', 'Masz ekipy <span class="lime">w terenie?</span>', 'Chcesz mieć nad tym kontrolę? Napisz do nas.', T, CTA_FOOT, 5, N),
])

# 30 blog – kiedy AI się myli
T = 'Nowy wpis na blogu'; F = 'Blog · <b>piksel360.pl</b>'; N = 3
post('2026-11-30', '30-blog', 'blog', [
    s_hero(S+'Leszek-krawat.jpg', 'Nowy wpis na blogu', 'Kiedy AI się myli', 'Prawdziwe sytuacje: odpowiedź brzmiała świetnie, a była błędna.', T, F, 1, N, pos='center 40%'),
    s_split(S+'programowanieAI1.jpg', 'Wniosek', 'AI to pomocnik, a nie wyrocznia', 'Piszemy, jak wyłapujemy takie błędy, zanim narobią szkód.', T, F, 2, N, icon_name='shield'),
    s_cta(S+'Leszek-krawat.jpg', 'Przeczytaj <span class="lime">cały wpis</span>', 'Zanim zaufasz AI w firmie, sprawdź, gdzie potrafi się pomylić.', T, CTA_FOOT, 3, N, btn='Czytaj na blogu', site='piksel360.pl/blog'),
])

if __name__ == '__main__':
    keys = sys.argv[1:] or list(POSTS)
    res = {}
    for k in keys:
        folder, jobs = POSTS[k]
        res[k] = render(jobs, 'out/' + folder)
    json.dump(res, open('res.json', 'w'), indent=1)
    from PIL import Image
    for k in keys:
        fs = res[k]; n = len(fs)
        sheet = Image.new('RGB', (360 * n, 360))
        for i, fn in enumerate(fs): sheet.paste(Image.open(fn).resize((360, 360)), (360 * i, 0))
        sheet.save(f'out/prev-{k}.jpg', quality=80)
